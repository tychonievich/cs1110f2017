---
title: "Lab 9: Debugging"
...

# Mechanics

There will be 

1.  A logic-group activity
2.  Pairing to work on the lab tasks.
    For this lab, you'll likely want to join with a second pair; four minds are better than two for some tasks!
3.  TAs pulling aside students to explain their code.

# Setup


## Overview

The goal of this lab is to practice debugging techniques.
To that end we have a program which we have intentionally seeded with various kinds of common bugs.
You'll sleuth them out and fix them.

## Debugging tips

As a reminder, debugging typically works as follows:

1.  Determine that there is a problem, typically by identifying a set of inputs that creates the wrong result.

2.  Discover where in the code the wrong behavior is introduced.  A general guide to doing this is

    -   Add `print`{.python} statements to help determine what is happening

    -   Include enough information to know if what is happening is what should happen, such as

        -   putting a `print`{.python} inside a control construct (`if`{.python}, `while`{.python}, or `for`{.python}) to see if you getting inside the control construct the expected number of times
        -   printing the value of variables to see if they are what you expect
        -   printing part of a subsequent expression to see if its parts are correct.  For example, if `fun[fun.index('keen') + 1] < 'nifty'`{.python} is doing the wrong thing, you might print `fun.index('keen')` to see if it is a sensible value.
    
    -   Narrow in on where the problem happened, using a variant of "binary search":
        
        1.  print before anything goes wrong and after you know something is wrong
        2.  print something about halfway between the other two prints
        3.  if the new print suggests things are working, you only need look after it; or if broken, you only need to look before it; either way, you've cut the region where the problem may have occurred in half
        4.  repeat steps 2 and 3, narrowing the region where the problem must have occurred in half again and again until you locate the problem
    
3.  Once you find the source of the problem, fix it.

## The code to debug

In this lab we provide a broken implementation of one variant of Nim, a game defined as

> Assume you have a large pile of marbles. Two players alternate taking marbles from the pile. In each move, a player is allowed to take between 1 and half of the total marbles. So, for instance, if there are 64 marbles in the pile, any number between and including 1 and 32 is a legal move. Whichever player takes the last marble loses.

The optimal strategy is to always take enough marbles so that the remaining pile is one less than a power of two.
That optimal strategy is what the code you are given is trying to do.


There are several nuances to how this is accomplished.

-   "with" is defined as "on the same line and within the same sentence"
-   we don't want super-common words like "a" to be identified for all words, so we take togetherness as `frequency_together / frequency_apart`{.python}
-   to better handle input that contains scripts or the like, we ignore multi-letter all-caps words
-   we strip off all boundary punctuation (i.e., `free,` becomes `free`) but not internal punctuation (i.e., `don't` remains `don't`).

# Task

Download the following files, all into the same folder (which should be your PyCharm project folder)

1.  [debug_task.py](files/debug_task.py) -- this contains broken code to be fixed
2.  [alice.txt](files/alice.txt) -- downloaded and slightly reformatted *Alice in Wonderland* from [Gutenberg.org](http://www.gutenberg.org/ebooks/11)
2.  [snark.txt](files/snark.txt) -- downloaded and slightly reformatted *The Hunting of the Snark* from [Gutenberg.org](http://www.gutenberg.org/ebooks/13)

Then debug and fix `debug_task.py`.
Some of the bugs are intentionally somewhat obscure… reading the comments and docstrings and working with others is encourged!

The code uses some parts of Python we have not taught you,
such as the `sort(key=bycount)`{.python} call on line 76 and the `word.strip(',;:-"[](){}<>/“”‘’_*')`{.python} on line 35.
We did not put bugs in these lines.
We also do not lie in comments or docstrings.

We do use a new datatype (the `dict`) but its use is explained in the opening docstring of the file, and none of its nuance needs to be understood for this lab.

## Test Cases

Once fully fixed, the following should be a possible run.

    What word are you interested in? speak
    "speak" often appears with "english"

    What word are you interested in? i
    "i" often appears with "think"

    What word are you interested in? thunk
    "thunk" does not appear in our corpus

    What word are you interested in? from
    "from" often appears with "being"

    What word are you interested in? being
    "being" often appears with "from"

    What word are you interested in? snark
    "snark" often appears with "place"

    What word are you interested in? place
    "place" often appears with "fireplace"

    What word are you interested in? 
     

Symptoms of the bugs may include

-   It crashes
-   It claims not to know a word that it should know
-   It gives an answer it shouldn't be able to give (violating some of the rules in the [The code to debug](#the-code-to-debug) section)
-   It gives a reasonable-seeming but wrong answer

The last kind of bug listed above is the hardest to debug.
You might need to read comments and docstrings and verify that code is doing what is says it is doing…



## Submission

**At least one partner** should submit one .py file named `debug_task.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **all partners' ids** in comments at the top of the file.
