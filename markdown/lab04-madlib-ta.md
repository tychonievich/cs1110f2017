---
title: "Lab 4: Madlibs - TA guide"
...


# Logic Groups (15--20 min)

1.  Announce "Get in the logic groups you had last lab"
    -   "You may leave your stuff where it is"
    -   "But bring a pen or pencil and paper"
1.  Bring up on the screen this: [money boat problem](https://docs.google.com/a/virginia.edu/presentation/d/1yVfHnOsGcXM1z2rr5-o7eubKbPA3A1kVmEdx4Rb4zQQ/edit?usp=sharing)
1.  Announce "Work with your group to solve this problem"
1.  Wander the room, but respond to all questions with "I'm not a part of your group. What does your group think?" No matter what they say, nod and move on.
1.  After a few people appear to have a solution,
    -   stop them
    -   ask someone to share their solution
    -   "Judging by the thunderous applause" (pause of applause if necessary), "we like this answer!"
1.  Announce "Return to your seats and let's begin the main lab activity"

Reminder: do not offer hints, solutions, or clarifying explanations.
During sharing, don't say "that's a bad solution"---instead ask a question that helps them see it is bad


# Background

The students have had three lectures since the add deadline:

-   one that introduced `print`, `input`, comments, literals, and whitespace
-   one that introduced `type`, values, `=`, variables, operators, and math
-   one that introduced `def`, parameters, `return`, and docstrings

# Review

Start with a review, more to see if there are questions than to teach.
For example, you might display a piece of code like the following:

````python
def line(m, x, b):
    '''determines the value of y = m x + b'''
    print(m * x + b)

y = line(2, 3, 4)
y = line(1, 0, 2)
print(y)
````

and ask what it prints; run it and show them they are wrong; remind them of the difference between `print` and `return` and fix that; run it again; remind them how a second `=` overwrites the first.

Also review pairing and discuss the need for switching who drives.

# New material

Summarize the task for this lab, which is to make a program that 

- has a template phrase
- asks for user-supplied words
- prints the phrase with the user-supplied words

Ask them to think about how they might get the user-supplied words into a phrase.
Prompt them with the following if they don't come up with them on their own:

- they could define the entire phrase as a big string with place-holder words and replace the place-holders with the user-typed words.
- they could define the parts of the phase separating the words each as its own string and append the user-supplied words in between with the `+` operator.

Explain that the replacement model makes for more readable code,
but it depends on parts of Python that we have not yet learned.
Thus, we suggest they do the second model in this lab.

Remind them about spaces, commas in `print`, and string `+`:

- `print("I'm a", profession, "!")`{.python} produces `I'm a juggler !` (extra space)
- `print("I'm a" +  profession + "!")`{.python} produces `I'm ajuggler!` (missing space)
- `print("I'm a " +  profession + "!")`{.python} produces `I'm a juggler!` (correct)
- `print("I'm a",  profession + "!")`{.python} produces `I'm a juggler!` (correct)
- `print("I'm a ", profession + "!")`{.python} produces `I'm a  juggler!` (extra space)

# Guidance

Remind them to start by

-   trying it by hand
-   writing some pseudo-code
-   identifying what functions make sense

They should each have at least one function that does not contain all of the code.

# Help

## Supervise pairing

Keep an eye out for pairs dominated by one partner or the other.
Suggest these partnerships switch driver.
You could also do something like announce "Everyone now switch so the person on the left is driving!" periodically, helping you know which person should drive at any given time.

When asked a question by one partner, your first response should always be to turn to the other partner and say something like "What do you think?"

## `replace` and `format`

There are more elegant solutions that the plus-and-print, using the string method `.replace`, the string method `.format`, and the built-in function `format`.
If you see these, ask both partners if they know what the parts they are using mean.
If so, let them do it, but otherwise remind them that part of pairing is moving at the same pace and ask the one who does to go back to the simpler method you suggested in the recitation.

## Suggested design

One way to organize the code is

1.  A function with parameters for the user-supplied words that prints or returns the phrase
1.  Non-function code that asks for the words and calls the function

More modular designs make sense, but if students have no modularization suggest "if you had to break the program into two pieces, what would they be?" and then "maybe you should make one of those into a function."

Don't force functions; if they are confused and you don't have time to explain, let them write straight-line code, but let the instructors know how many students were in that situation so we can review in lecture if needed.

