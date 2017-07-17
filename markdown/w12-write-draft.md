
## Shared Intro

There are several ways to keep information on a disk drive so you can store information between runs of a program.  For example, you can

-   Have a "save" action that writes the values of all important variables to a file in disk and a "load" action that reads those same values from disk.
-   Use a database, which is a program optimized for reading and writing small parts of large amounts of information to a disk.
-   Use an action log.
-   Re-write the entire file every time anything changes.

This assignment will have you implement one of these.

# Repeated re-write files

The idea of re-writing the file on a change occurs because files don't readily change length.
removing some characters from the middle leaves a gap, which can mess up most file parsing algorithms.
Thus, to record a change we can

1.  Open the old file for reading, the new file for writing
2.  For each old entry, decide if it should be copied into the new file or not
3.  Add any new entries we might need to the new file
4.  Close both files, delete the old one, and re-name the new one to replace the old one.

This lets us "update" files frequently, avoiding data loss, and leads to straghtforward file reading, but it also means we spend a lot of time writing and re-writing files on the disk.


## Task

Have a set of functions that record and update a product inventory in a file.
Any change to the inventory should also update the file, using the re-write outline described above.

Your file should be a CSV file with three columns: product name, quantity, price.
Each product should have at most one row, and no quantity should be zero or negative.

An example inventory CSV file might be

````
eggplant,8,2.35
cannonball,2,14.20
stuffed red panda (toy),1503,16.50
````

Loading this file would give the `dict` `{'eggplant': [8, 2.35], 'cannonball': [2, 14.2], 'stuffed red panda (toy)': [1503, 16.50]}`{.python}

## Functions

Write the following functions.

-   `load(filename)` should read the product list from a file and return it as a dict of products with product names as keys and `[quantity, price]` lists as values.

-   `stock(filename, product, quantity)` should 
    
    1.  increase the quantity of the given product by the given ammount.
    2.  if the product is not found, it should use `input` to ask the user for a price, re-asking until a valid positive float is entered.
    3.  Return the new quantity in stock.

-   `sell(filename, product, quantity)` should 
    
    1.  If there are not enough of this item, leave the number of items unchanged and return `None`
    2.  decrease the quantity of the given product by the given ammount.
    3.  If this results in zero items in stock, remove the entire row from the inventory.
    4.  return the new quantity.

-   `save(filename, product_list)` where `product_list` is a dict of products with product names as keys and `[quantity, price]` lists as values; should write this product list to the file, omitting any entries with zero quantities.


# Action-log files

The idea of an action log is that every time you change a value, you also write down that that change occured in a file.
When restarting the program you read the log and "replay" the actions, ending up with the same set of values you had when last you stopped running the program.
Action logs can use a bit more disk space than other ways of writing files, and they can take a bit longer to load, but they have various advantages too, including:

-   You can't forget to save: changing a variable changes the log.
-   They include an edit history and "un-do" information: every previous state of the program is represented by a prefix of the log.
-   Various accounting, sequentiality, and robustness properties we won't go into here.

You'll implement an action log in this assignment.

## Task

Have a set of functions that interact with a `dict` and a file.
Those that update the `dict` also write a history of that update to the file.
Those that read the file re-play those updates and return the resulting `dict`.

Your file should be a CSV file with three columns: action, key, and value.
Valid **action**s are `put` (corresponding to `d[key] = value`{.python})
and `del` (corresponding to `del d[key]`{.python}).
Valid **key**s are strings, but they should not contain commas `,` or newlines `\n` or `\r`.
Valid **values**s are strings, but they should not contain commas `,` or newlines `\n` or `\r`;
the **value** should be omitted for a `del` action.

An example action log CSV file might be

````
put,3,three
put,three,3
put,fvie,5
put,5,five
del,fvie
````

Replaying this log would give the `dict` `{'3': 'three', 'three': '3', '5': 'five'}`{.python}.

## Functions

Write the following functions.

-   `load(filename)` should
    
    1.  if the filename corresponds to a file on disk, read and replay the contents of the file to generate a `dict`; otherwise the `dict` should be `{}`.
    2.  open the given file in append-only mode.
    3.  return the `dict` and the opened file in a tuple.

-   `put(pair, key, value)`, where `pair` is a (dict, opened_file) tuple, should
    
    1.  check that `key` and `value` are legal (no commas or new-lines) and return `False` if they are not.
    2.  update the `dict` in `pair` to contain the given key:value pair.
    3.  write a `put` action line to the file in `pair`.  Use `print` with the option `flush=True` to ensure the write is committed to disk immediately.
    4.  return `True` if all actions succeeded.

-   `remove(pair, key)`, where `pair` is a (dict, opened_file) tuple, should

    1.  check that `key` is a key in the `dict` in `pair`
    2.  update the `dict` in `pair` to contain the given key:value mapping; and
    3.  write a `del` action line to the file in `pair`.  Use `print` with the option `flush=True` to ensure the write is committed to disk immediately.
    4.  return `True` if all actions succeeded.

-   `save(dict, filename)` should open the file, write a single `put` line for each key:value pair in the dict, then close the file.
    It should only print the keys and values that follow the rules (strings, no commas or newlines)
    and should return a list of the keys it was not able to write.

----
