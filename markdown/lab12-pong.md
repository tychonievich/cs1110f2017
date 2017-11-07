---
title: "Lab 12: Pong"
...

# Mechanics

There will be 

1.  A brief logic-group activity
1.  Pairing up for the coming game project (and for this lab)
1.  Working on filling in missing code of a Pong game.
1.  TAs pulling aside students to explain their code.

# Activities

## Pairing

It is time to get ready for your [game project](project.html).
Things to note.

-   This is a paired assignment.  Pick someone you can work with and who has a schedule similar to yours.  The TAs may help match you up.

    -   Each partner should report their pair at [the partner status page](https://archimedes.cs.virginia.edu/cs1110/partners.php).
    -   If for some reason you need to work alone or in a group of three, see a TA or professor.

-   You'll have to decide on your own game.  It will be a 2D game using gamebox, as we have a few other requirements in the project description, but you can make many different games within these rules.
-   You will be submitting weekly checkpoints.  We won't tell you exactly what you need in each, but we do expect to see steady progress.
-   There will still be other individual assignments during the project time.  Plan your time accordingly!

# Activity

Today we are doing an example game in gamebox; specifically the classic game *Pong*.
If you are unfamiliar with Pong, head over to [http://www.ponggame.org/](http://www.ponggame.org/) to see what it's all about.
You can also try out [a one-player web version](pong.html)

We'll play by a basic version of the rules:

-   There is a ball that bounces back and forth.
-   Move your paddle on your side of the screen to prevent it from getting past you.
-   If it gets past you, your opponent earns a point.
-   First player to 10 points wins.

After you've figured out how the game plays, copy the following files and code into a new Python file in the same directory as your `gamebox.py` file:

-   [gamebox.py](http://cs1110.cs.virginia.edu/code/gamebox/gamebox.py)
-   [pong.py](http://cs1110.cs.virginia.edu/code/gamebox/pong.py)
-   [paddle.wav](http://cs1110.cs.virginia.edu/code/gamebox/paddle.wav)
-   [wall.wav](http://cs1110.cs.virginia.edu/code/gamebox/wall.wav)

## Finish `pong.py`

If you run the game as is, you should see what the game will look like, but nothing actually works.
We have left comments in the `pong.py` file that describes the code you need to add to make the game work.
Add some code, try it out, and keep going until you have a working Pong game!


## Submission

**At least one partner** should submit one .py file named `pong.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **all partners' ids** in comments at the top of the file.
