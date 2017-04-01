/* Declare variables */
const MAX_ROUNDS = 10
let roundsCompleted = 0

let verification: boolean[] = [false, false]
let inputted: boolean[] = [false, false]

let localPlayer: Player
let foreignBetray: boolean
let foreignScore = 0

let test = 0;

/* STATE enumeration */
enum STATE {
    INIT = 1,
    VER_PLAYER,
    VER_COMPLETE,
    GAME,
    POST_ROUND,
    POST_ROUND_WAIT,
    POST_GAME
}
let state = STATE.INIT

/* Player class */
class Player {
    private isHuman: boolean
    private years: number
    private moves: boolean[]
    private ai: Ai

    constructor(isHuman: boolean) {
        this.isHuman = isHuman
        this.years = 0
        this.moves = []

        if (!this.isHuman) {
            this.ai = new Ai(this)
        }
    }

    public getAi(): Ai {
        return this.ai;
    }

    public getMoves(): boolean[] {
        return this.moves
    }

    public getNextMove(): boolean {
        return this.moves[this.moves.length - 1]
    }

    public addMove(move: boolean): void {
        this.moves.push(move)
    }

    public addYears(years: number): void {
        this.years += years
    }

    public getYears(): number {
        return this.years
    }

    public isHumanPlayer(): boolean {
        return this.isHuman
    }

    public respond(): void {
        if (this.isHuman)
            return;

        radio.sendString(this.ai.getDecision() ? "cB" : "cA")
    }
}

/* Ai Class */
class Ai {
    private player: Player
    private aiMoves: boolean[]
    private enemyMoves: boolean[]
    private strategies: Strategy[]
    private currentStratIndex: number

    //this function is called to create the AI    
    constructor(player: Player) {
        this.player = player
        this.aiMoves = player.getMoves()
        this.enemyMoves = []
        this.strategies = []

        this.currentStratIndex = Math.random(5)

        this.strategies.push(new Strategy1(this))
        this.strategies.push(new Strategy2(this))
        this.strategies.push(new Strategy3(this))
        this.strategies.push(new Strategy4(this))
        this.strategies.push(new Strategy5(this))

    }

    public setStrat(stratIndex: number): void {
        this.currentStratIndex = stratIndex
    }

    public getAiMoves(): boolean[] {
        return this.aiMoves
    }

    public getEnemyMoves(): boolean[] {
        let moves: boolean[] = []
        for (let i = 0; i < this.enemyMoves.length - 1; i++) {
            moves.push(this.enemyMoves[i])
        }
        return moves
    }

    public registerEnemyMove(enemyMove: boolean): void {
        this.enemyMoves.push(enemyMove)
    }

    public getDecision(): boolean {
        let decision = this.strategies[this.currentStratIndex].getNextMove()
        this.aiMoves.push(decision)
        return decision
    }
}

/* Strategy class */
class Strategy {
    protected parentAi: Ai

    constructor(ai: Ai) {
        this.parentAi = ai
    }

    getNextMove(): boolean {
        return true
    }
}

/* Strategy 1
    Tit for tat: copies the last move of the opponent
*/
class Strategy1 extends Strategy {

    constructor(ai: Ai) {
        super(ai)
    }

    getNextMove(): boolean {
        let enemyMoves = this.parentAi.getEnemyMoves()
        return enemyMoves.length > 0 ? enemyMoves[enemyMoves.length - 1] : true
    }

}

/* Unforgiving
    If the opponent has betrayed before, the AI will
    always betray.
*/
class Strategy2 extends Strategy {

    constructor(ai: Ai) {
        super(ai)
    }

    getNextMove(): boolean {
        let enemyMoves = this.parentAi.getEnemyMoves()
        for (let i = 0; i < enemyMoves.length; i++) {
            if (enemyMoves[i]) {
                return true
            }
        }
        return false
    }
}

/* Champion


*/
class Strategy3 extends Strategy {

    constructor(ai: Ai) {
        super(ai)
    }

    getNextMove(): boolean {
        let enemyMoves = this.parentAi.getEnemyMoves()
        let percent = 0
        let currentRound = enemyMoves.length + 1;

        if (currentRound < 6) {
            return false
        } else if (currentRound < 11) {
            return enemyMoves[enemyMoves.length - 1]
        }

        for (let i = 0; i < 11; i++) {
            if (enemyMoves[i]) {
                percent += 1
            }
        }

        if (enemyMoves[enemyMoves.length - 1] || percent > 5) {
            return enemyMoves[enemyMoves.length - 1]
        }

        return true
    }
}

/*
Resurrection
The AI will play 'silent' in the first 5 turns.
After 5 turns, the AI will play 'betray' if the
player had 'betray'ed the previous 5 turns. 
Otherwise, it follows "Tit for Tat".
*/
class Strategy4 extends Strategy {

    constructor(ai: Ai) {
        super(ai)
    }

    //return true if betray, return false if silent
    getNextMove(): boolean {
        let enemyMoves = this.parentAi.getEnemyMoves()
        let currentRound = enemyMoves.length + 1;

        if (currentRound <= 5) {
            return false
        } else {
            for (let i = enemyMoves.length - 1; i >= enemyMoves.length - 5; i--) {
                if (!enemyMoves[i]) {
                    return enemyMoves[enemyMoves.length - 1];
                }
            }
            return true
        }
    }

}

/* Grumpy Strategy:
The AI always plays 'silent', unless
they are "grumpy", in which they will
play 'betray'. */
class Strategy5 extends Strategy {
    private happiness: number

    constructor(ai: Ai) {
        super(ai)
        this.happiness = 7
    }

    //return true if betray, return false if silent
    getNextMove(): boolean {
        let enemyMoves = this.parentAi.getEnemyMoves()
        let currentRound = enemyMoves.length + 1;

        if (enemyMoves[enemyMoves.length - 1]) {
            this.happiness -= 1
        } else {
            this.happiness += 1
        }

        return this.happiness < 6
    }
}

/* Event handler for receiving the opponent's choice */
// cA - Silent
// cB - Betray
radio.onDataPacketReceived(({receivedString}) => {

    if (state == STATE.VER_PLAYER) {

        verification[1] = true

    } else if (state == STATE.GAME) {

        if (receivedString[0] == "c") {
            foreignBetray = receivedString[1] === "B"

            if (!localPlayer.isHumanPlayer()) {
                localPlayer.getAi().registerEnemyMove(foreignBetray)
            }

            inputted[1] = true
        }

    }

})

/* function that handles button presses */
function handleInput(buttonName: string) {
    let stringToSend = buttonName === "A" ? "cA" : "cB"

    if (state == STATE.VER_PLAYER) {
        if (!verification[0]) {
            verification[0] = true
            localPlayer = new Player(buttonName === "A")

            if (!localPlayer.isHumanPlayer()) {
                // **** // 
                //localPlayer.getAi().setStrat(4)
                // **** //
            }

            radio.sendString(stringToSend)
        }
    } else if (state == STATE.GAME && !inputted[0] && localPlayer.isHumanPlayer()) {
        localPlayer.addMove(buttonName === "B")
        inputted[0] = true
        radio.sendString(stringToSend)
    }
}

/* Button A (Left) event handler */
input.onButtonPressed(Button.A, () => {
    if (state == STATE.POST_ROUND) {
        return;
    }

    handleInput("A")
})

/* Button B (Right) event handler */
input.onButtonPressed(Button.B, () => {
    if (state == STATE.POST_ROUND) {
        return;
    }

    handleInput("B")
})

/* Begins the player verification process */
function startVerification() {
    state = STATE.VER_PLAYER
    basic.showString("V")
}

/* Checks if the verification has finished */
function checkVerification() {
    if (verification[0] && verification[1]) {
        state = STATE.VER_COMPLETE
    }
}

/* Game loop */
function startGameLoop() {
    state = STATE.GAME
    let roundInitialised = false

    basic.forever(() => {

        if (state == STATE.GAME) {
            if (!roundInitialised) {
                basic.showNumber((roundsCompleted + 1))

                if (!localPlayer.isHumanPlayer()) {
                    localPlayer.respond()
                    inputted[0] = true
                }

            }

            if (inputted[0] && inputted[1]) {
                state = STATE.POST_ROUND;

                let localBetray = localPlayer.getNextMove()

                if (localBetray && foreignBetray) {
                    localPlayer.addYears(2)
                    foreignScore += 2
                } else if (!(localBetray) && !(foreignBetray)) {
                    localPlayer.addYears(1)
                    foreignScore += 1
                } else if (!(localBetray) && foreignBetray) {
                    localPlayer.addYears(3)
                } else {
                    foreignScore += 3
                }

                inputted = [false, false]
                roundsCompleted++
                roundInitialised = false

                basic.showString(" " + localPlayer.getYears() + ":" + foreignScore);
                returnToGame();
            }
        }

        if (roundsCompleted >= MAX_ROUNDS) {
            state = STATE.POST_GAME
        }
    })
}

/* Concludes the game */
function endGame() {
    basic.pause(500)
    let conclusion: string
    let localScore = localPlayer.getYears()

    if (localScore < foreignScore) {
        conclusion = "W"
    } else if (localScore > foreignScore) {
        conclusion = "L"
    } else {
        conclusion = "D"
    }
    basic.showString("" + conclusion + " " + localScore + ":" + foreignScore)
}

/* Waits 3 seconds, returns to game */
function returnToGame() {
    state = STATE.POST_ROUND_WAIT
    game.startStopwatch()

    while (true) {
        if (game.currentTime() >= 2000) {
            state = STATE.GAME;
            break;
        }
    }
}

/* Main function */
function main() {
    basic.forever(() => {

        switch (state) {
            case STATE.INIT:
                startVerification()
                break
            case STATE.VER_PLAYER:
                checkVerification()
                break
            case STATE.VER_COMPLETE:
                startGameLoop()
                break
            case STATE.POST_GAME:
                endGame()
        }

    })
}

main()
