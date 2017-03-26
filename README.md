# adventure:bit

Members of the CodeGuild have been hard at work, creating new, complex, and exciting packages for the BBC micro:bit. This repo contains their work.

You'll find the contents of the [website](http://pxt-packages.codeguild.co) as well as the source code for each of the packages. There's also a list of possible improvements to be made, so if you'd like to contribute you can get cracking straight away!

## Making your own Game

You can use any micro:bit editor you like, all you need to do is be able to output downloadable `.hex` files for the micro:bit.

Build your game and test it out. Once you've got something that works you'll need to make changes to this repository to add your game to the website. Here's how:

You'll need to make sure you've got [git](https://git-scm.com/), [VirtualBox](https://www.virtualbox.org/), and [Vagrant](https://www.vagrantup.com/) installed. They're all free and pretty easy to install.

Then you'll need to fork this repo (so you'll need a GitHub account, if you don't already have one). This is easy, just click the "Fork" button in the top right of this page.

You'll now have your own copy of the repository stored in your own account. You can make whatever changes you'd like to this copy; it's yours.

To make changes you'll need to clone your fork. This might require running something like this on the command line:

    $ git clone https://github.com/YOUR_USERNAME/adventure-bit

This will have downloaded the repo to your computer. Let's now get vagrant up and running by doing:

    $ cd adventure-bit
    $ vagrant up

This one might take a while, but when it's done there will be a virtual machine running on your computer with all the code inside. We can connect to the virtual machine like this:

    $ vagrant ssh

And now we can serve the website locally:

    $ cd /vagrant
    $ jekyll serve

If you now open this link: http://192.168.33.10:4000 you should see the adventure:bit website. Except this one is running on your machine, so changes we make here will be seen on the website.

To reload the website with any new changes, you might have to restart the jekyll server by pressing `Ctrl-c` and then running `jekyll serve` again.

To add your game you'll need to:

1) Create a new directory inside the `games` directory
2) Inside this directory put another directory called `src`. Inside this, put all of your source code files
3) Create another directory called `dist`, here you should put your `.hex` files for downloading
4) Add a `README.md` file to the directory, giving instructions for developers on how to develop your game
5) Add an `index.md` file to the directory giving instructions on how to download and play your game
6) Add a link to your directory in the `list.md` file

The `index.md` file is used to create the webpage for the game. It should contain a links to download the game files, as well as instructions on what to do, and a diary of the work that went into creating the game. This file should contain enough information for people to start playing the game for themselves. Make sure to include a diary of the work you've done. What problems are you solving? How did you go about it? What was hard? What was fun?

The `README.md` file contains any information that the game developer thought might be useful for future developers of the game (or other games). This file is for developers of games (not normally for people wanting to play the game). Make sure to include a list of improvements, things that could be worked on to make the game better.

Take a look at the existing projects for clues on how to format the files and what information to put in them.

When you're done making changes you'll want to have them included in the official website (not just your own). So first push your changes up to your fork:

    $ git add CHANGED_FILE CHANGED_FILE
    $ git commit -m 'DESCRIPTION_OF_CHANGES'
    $ git push origin master

If you don't know what the `git add` or `git commit` instructions are doing, ask around!

Now your fork will have the changes, let's make a pull request to the main repo to have them included in the main site. You'll need to open your fork on the GitHub website and click the "New Pull Request" button. Hopefully you'll see a green bit of text that says "Able to merge", if so, click the "Create pull request" button, provide a description of the work you've done and alick "Create pull request" again. If instead you see a red error message, you'll have to fix the problems it talks about before your work can be merged.

## Improvements

Here's a list of things that could be done to make this repo/website better.

- Improve the existing games. Each game has a `README.md` that will list some possible improvements to be made, why not tackle one?
- Create your own game. We haven't got that many at the moment. Why not build one from scratch? Here are some ideas:
    - Zombie chase game
        - Detect proximity using the bluetooth radio
        - Have the humans try to escape the zombies
        - Maybe the zombies aren't allowed to move very fast?
        - Maybe the humans all have to stick close together
    - Bomb defusing game
        - There's one bomb micro:bit
        - and a team of bomb squad micro:bits
        - Each player has a speciality that they have to use on the bomb to defuse it
            - Keep it cold
            - Flip it over
            - Press the right buttons
            - Cut the right wire?
        - If you fail you can run away from everyone else to explode it and keep them (but not you) safe
    - Dungeon Crawler game
        - You have to walk around the building collecting items and solving puzzles
- Make the website nicer. Currently it's using a standard jekyll theme and doesn't have that much content. Why not make it gorgeous?
- Improve the instructions. Did you find the instructions hard to follow? Why not make them better?
