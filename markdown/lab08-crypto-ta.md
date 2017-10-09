---
title: "Lab 8: Crypto"
...


# Purpose of this lab

This lab has three goals

1.	Help them see cases where both `for element in thing:`{.python} and `for i in range(len(thing)):`{.python} are useful
2.	Have them write simple loops
3.	Provide an introduction to an important topic that we won't get to in lecture


# Logic Groups

The logic problem for today is [a self-referential quiz](https://docs.google.com/presentation/d/1ODu2fJHhPRvXswms1bvVk5_NaYet_XbU-XfOFMu7pFw/edit?usp=sharing).
There are two such quizzes in that slide deck; feel free to use either one.


# Overview

Provide a brief review of the two main ways of making a for loop: with and without `range`.  For example, you might show something like the following

````python
text = 'an example'
two = ''
for c in text:
    two += c*2
print(two)

many = ''
for i in range(len(text)):
    c = text[i]
    many += c*i
print(many)
````

and discuss how both give you access to each letter, but the second also gives access to which letter it is you have.

# Spot Check

Each TA should go to

> [The Code Explainer](https://archimedes.cs.virginia.edu/cs1110/explain.php)

and have four of their students explain the produced code sometime during lab.
Have them do this away from other students (i.e., ask them to come to you).
Example questions to ask include

-	Explain to me how your code works.
-	How would your code work differently if we did $Z$ to line $n$?
-	How would you describe the value inside variable $X$ after line $n$? Is that the same as its meaning on line $m$?
-	If I ran it with input/argument $X$, what would it do/return/print?  What value would variable $Y$ have on line $n$?

Answer guidelines:

Clear
:	They seem to both understand their code and understand how to articulate it.

Adequate
:	They seem to basically understand their code, but struggle to explain it.
	Help them out by modeling how you would answer your own questions.

Confused
:	They did not seem to understand their own code.

	Note: if the code doesn't work and they don't know why, that's adequate, not confused;
	confused is when they don't know why/if it will work.

> TAs with 2 labs: sorry, right now Archimedes doesn't know the difference between your two lab groups, so you'll have to skip a lot of students to get to the right ones...


# Example solution

I don't usually do this, but this code is so strange-looking I suspect many TAs will think the correct code looks wrong:
[my reference solution to this lab](https://archimedes.cs.virginia.edu/cs1110/download.php?unittest=unittest&filename=noloop_hangman.py).
