---
title: "PA 09: averages.py"
...

# Task

Write a file named `averages.py` with several functions in it for computing averages of three values:

- `mean(a, b, c)`{.python} should compute the [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of `a`, `b`, and `c`.
- `median(a, b, c)`{.python} should compute the [median](https://en.wikipedia.org/wiki/Median) of `a`, `b`, and `c`.
- `rms(a, b, c)`{.python} should compute the [root-mean-square](https://en.wikipedia.org/wiki/Root_mean_square) of `a`, `b`, and `c`.
- `middle_average(a, b, c)`{.python} should compute the mean, median, and rms of `a`, `b`, `c`; and then return the median of those three averages.

Additionally, you should implement your solution such that

- `rms` invokes `mean` once.
- `middle_average` invokes `mean` and `rms` once each and `median` twice.
- use only features of Python we've learned in class (e.g., do not use `list`s, `sort`, `sorted`, etc.)


# Example Invocations

When you run `averages.py`, nothing should happen.
It defines functions, it does not run them.

If in another file (which you do not submit) you write the following:

````python
import averages

print(averages.mean(1, 5, 1))
print(averages.median(1, 5, 1))
print(averages.rms(1, 5, 1))
print(averages.middle_average(1, 5, 1))
````

you should get the following output:

````
1110
22
18.207964601769913
842
````


# Thought Questions

How hard would it be to

-   Return the number if all there is is one number?
-   Deal with negative numbers too, like `"-123 - -456"`
-   Deal with a string with two operators, like `"1 + 23 * 456"`?


# Troubleshooting

There are four operators that could be `in` the string, so you probably want four cases in a big `if`-`elif`-type statement.

Those string methods you learned about in lab will come in handy (1111 students or others that missed the lab: see [lab 06](lab06-strpuz.html), especially the "Tools to Use" section).

Since you can't rely on the number of spaces, it probably makes sense to find the operator and slice off the part before and after that to turn into `int`s.

`int` can deal with spaces just fine (`int(" 12  ")`{.python} works) but not non-number-space bits very well (`int("12+")`{.python} raises a `ValueError`).
