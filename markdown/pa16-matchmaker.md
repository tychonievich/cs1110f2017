---
title: "PA 16: matchmaker.py"
...

# Task

Write a file named `matchmaker.py` that contains a collection of functions
that will help you find the compatibility between various things.

The main idea used in these functions will be finding the overlap between lists of elements.
These will be done as follows:

## `agreement(i1, i2)`

Given two lists of interests, return a list of the shared interests between the two.
Do not modify the provided lists.
The order of elements in the returned list does not matter.
You may assume that both `i1` and `i2` are lists or tuples and that neither lists contains a duplicate element.

For example, `agreement(['games', 'museums', 'food'], ['art', 'food', 'hiking', 'games'])`{.python} should return either `['games', 'food']`{.python} or `['food', 'games']`{.python}

## `disagreement(i1, i2)`

Given two lists of interests, return a list of interests in only one list.
Do not modify the provided lists.
The order of elements in the returned list does not matter.
You may assume that both `i1` and `i2` are lists or tuples and that neither lists contains a duplicate element.

For example, `disagreement(['games', 'museums', 'food'], ['art', 'food', 'hiking', 'games'])`{.python} should return some permutation of `['museums', 'art', 'hiking']`{.python}

## `compatibility(i1, i2)`

Given two lists of interests, return a "compatibility score" for the two.
This is computed as the number of shared interests divided by the total number of interests:
$\frac{shared}{shared + notshared}$
Do not modify the provided lists.
You may assume that both `i1` and `i2` are lists or tuples and that neither lists contains a duplicate element.

For example, `compatibility(['games', 'museums', 'food'], ['art', 'food', 'hiking', 'games'])`{.python} should return `0.4`{.python} because there are five interests listed in total, of which only 2 are shared.

## `bestmatch(me, others)`

If `compatibility` is working correctly, the following function:

````python
def bestmatch(me, others):
    """Returns a most-compatible person.
    
    Parameters:
        me:     a list of things I like
        
        others: a list of pairs, where each pair is a name 
                and a list of things that person likes; for example,
                [ ["Scrooge", ["money", "food"]], 
                  ["Cratchit", ["family", "heat", "food"]]
                ]
    """
    whom = 'no one'
    comp = -1
    for person in others:
        name, likes = person
        match = compatibility(me, likes)
        if match > comp:
            comp = match
            whom = name
    return whom

````

... will return the name of the most compatible person.

Functions like `bestmatch` are widely used in online "personality tests" and the like:
several questions are asked to establish your lists of interests,
and then those are compared to a set of options to create the "you are" response.

# Example Invocations

When you run `matchmaker.py` nothing should happen.
It defines functions, it does not run them.

If in a separate file you write

````python
import matchmaker

me = ['coding', 'homework', 'money', 'reciting poetry']

k = ['homework']
m = ['coding', 'homework', 'sleep']
d = ['money', 'cruises', 'reciting poetry', 'gardening']

match = matchmaker.bestmatch(me, [['K.', k], ['M.', m], ['D.', d]])

if match == 'K.':
    them = k
elif match == 'M.':
    them = m
else:
    them = d

print('You should go out with', match)
print('Topics to discuss include', ' and '.join(matchmaker.agreement(me, them)))
print('Topics to avoid include', ' and '.join(matchmaker.disagreement(me, them)))
````

you should get the following output:

````
You should go out with M.
Topics to discuss include coding and homework
Topics to avoid include money and reciting poetry and sleep
````

(the words may be in a different order for you; that's fine).

# Thought Question

You might try making something more like the usual online personality test.
To do this, create a list of final options, all with the same number of interests.
Then ask a set of multiple-choice questions to populate the user's interests based on those options.

For example, if you have three interest sets: `['money', 'swimming']`{.python}, `['food', 'sleep']`{.python}, and `['jokes', 'running']`{.python}, you might want the interaction to be

````
Do you prefer
  1. money
  2. food
  3. jokes
Enter a number, 1-3: 1

Do you prefer
  1. swimming
  2. sleep
  3. running
Enter a number, 1-3: 2

Congratulations: you're Scrooge McDuck!
````

You could also try implementing variations of these functions that have *weighted* interest:
`me = [['coding', 2], ['homework', 1], ['money', 10]]`;
there are several possible interpretations of each function given this starting point.


# Troubleshooting

The simplest implementation of `compatibility` invokes both `agreement` and `disagreement` to find out their `len`gths.

You can implement `agreement` by looping over one list, but `disagreement` will probably require two loops, one over each.

We only gave a few examples; you'll also want to test other cases, such as

-   tuple arguments instead of lists
-   empty lists
-   two copies of the same list
-   two lists with no overlap

If your code is not working for a few numbers, try adding `print`{.python} statements inside your loops and checking that what is printed is what should be printed according to how you did it on paper.

