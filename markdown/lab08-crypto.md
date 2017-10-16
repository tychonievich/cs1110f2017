---
title: "Lab 8: Cryptography"
...


# Overview

We'll have a logic group activity and pairing, like usual.  We'll also have TAs pulling students aside to explain code, like we did two weeks ago.

Cryptography is the art of hiding the meaning of a message in a way that the intended recipient can understand, but not anyone else.
Fully secure cryptography requires a a lot of detail-oriented nuance of implementation and some abstract algebra, but we can get some casual-level cryptography using what we know so far.

You'll write several functions in `crypto.py` you can use to perform casual encryption.
Feel free to use them to make messages harder for people who don't know the encryption to figure out,
but don't use them for truly sensitive information...

## Vocabulary

Cipher
:   A particular set of rules used to encrypt and decrypt.

Cipher text
:   The encrypted message.

Decrypt
:   To convert from cipher text to plain text.

Encrypt
:   To convert from plain text to cipher text.

Key
:   Extra information used to customize an encryption algorithm.

Plain text
:   The not-encrypted message.

## Guidelines

Most (though not all) of the functions will have a format similar to the following:

````python
def func(text, key):
    ans = ''
    for letter in text:
        ans += do_something_with(letter, key)
    return ans
````

Sometimes, however, you'll need to know the position of each letter; for that you do instead

def func(text, key):
    ans = ''
    for i in range(len(text)):
        letter = text[i]
        ans += do_something_with(letter, i, key)
    return ans
````

Notably, you'll usually start with some empty string and add one letter to it at a time.

# Algorithms

You'll write a series of function pairs.
Each will accept a string (either the plain text to encrypt, or the cipher text to decrypt) and possibly a key,
and each will return a string.

You'll almost certainly want to write a few helper functions;
some examples are given in the section [Possoible Helper Functions] below.


## Shift

One of the first documented ciphers was the Caesar Cipher, which adds 3 to each letter ("a" becomes "d", "b" becomes "e", etc.)
We'll generalize that to add an arbitrary integer *key*, not just 3.

The encryption function, `shift(text, key)`, should add `key` to every letter in `text`, using `letter_to_index` and `index_to_letter` to do so.
Don't change non-letters.
Perserve case (the string methods `isupper()` and `islower()` can help; if the pre-shift letter `isupper` then then post-shift letter should be `upper` as well).

The decryption function, `unshift(text, key)`, should subtract `key` to every letter in `text`, which can be implemented in two lines:

````python
def unshift(text, key):
    return shift(text, -key)
````

Example: `shift("Caesar cipher", 3)`{.python} returns `"Fdhvdu flskhu"`{.python}


## Vigenère

Giovan Battista Bellaso modified the shift cipher by shifting different letters different amounts,
a method later misattributed to Blaise de Vigenère.
This cipher much like the shift cipher, but the key is a string instead of a single number
and the shift for each letter is the `letter_to_index` of the corresponding letter in the key.

Generally, the key is quite a bit shorter than the text being encrypted.
Thus, when we reach the end of the key we start over with the first letter again.
Wrapping indices in this way is easily accomplished using the `%` operator: `key[i % len(key)]`{.python}.


For example, `vignere("secret", "hi")`{.python} is going to be `"zmjzlb"`{.python}:

-----------------
                 
- - - - - - - - -
s + h = s + 7 = z
e + i = e + 8 = m
c + h = c + 7 = j
r + i = r + 8 = z
e + h = e + 7 = l
t + i = t + 8 = b
-----------------

The decryption function `unvignere(text, key)` is almost exactly like the encryption function `vignere(text, key)` except that it subtracts the key from text instead of adding it to the text.  Unlike `unshift`, it cannot be a two-liner because `-key` does not work for string `key`s.


## (de)Interleave

The encryption function, `interleave`, should split the string in half and return a string alternating letters from the first and second half. For example, `interleave('ABCDEFG')`{.python} should return `'AEBFCGD'`{.python}

The decryption function, `deinterleave`, should return a string made up of every other letter starting with the first letter, then every other letter starting with the second letter. For example, `deinterleave('AeBfCgD')`{.python} should return `'ABCDefg'`{.python}


# Application

Once you have a working encryption method or two, try communicating with someone else in class using an encrypted message.

# Code Breaking

If you have extra time, try writing code to break encryption without knowing the key.

`interleave` doesn't have a key, so nothing to do there.

For `ceasar`, you might try a simple loop over possible keys and print them all; you can likely pick out the correct one pretty easily.  You can also use the observation that English texts generally have about 16% spaces and 13% `e`s to filter out some highly-unlikely keys that do not result in enough of these characters.

Vigenère is a lot harder (people were claiming it was unbreakable as late as the 1917), but if you want to give it a stab [wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Cryptanalysis) has a reasonable overview of the main tactics

# Real security

Current encryption relies on several things we haven't discussed here:

-   Encrypting large blocks of text at once, instead of letter-by-letter.
-   Using methods of encryption based on abstract algebra and number theory which computer scientists are reasonably confident cannot be easily reversed.
-   Implementations that ensure each encryption of a block takes *exactly* the same amount of time, so that you can't infer things about the message from the timing.
-   The use of techniques beyond encryption, such as hashing (a topic you'll learn in our third programming course, CS 2150), to establish other kinds of trust.

However, one lesson learned from the Union's breaking of the Confederacy's use of Vignère ciphers in the US Civil War still holds today:
the Union didn't know how to break the cipher quickly in general, but once it discovered that the Confederacy used three keys for almost all of its communications ("ManchesterBluff", "CompleteVictory", and "ComeRetribution") they were able to break the codes with ease.
This remains true today: if you re-use passwords, or use passwords others might guess, good encryption doesn't help.

# Possible Helper Functions

You might find that implementing the following will make some of your tasks easier.

````python
def index_to_letter(index):
    """Converts an integer into its corresponding letter, wrapping as needed
    
    ...
    index_to_letter(-2) gives 'y'
    index_to_letter(-1) gives 'z'
    index_to_letter(0) gives 'a'
    index_to_letter(1) gives 'b'
    ...
    index_to_letter(25) gives 'z'
    index_to_letter(26) gives 'a'
    ...
    
    :returns: a one-character string
    """
    implement me!

def letter_to_index(letter):
    """Converts a letter into its corresponding index, between 0 and 25
    
    index_to_letter('a') gives 0
    index_to_letter('b') gives 1
    ...
    index_to_letter('z') gives 25
    
    :returns: an integer between 0 and 25, inclusive
    """
    implement me!

def is_letter(letter):
    """tells if the given string is a letter (as opposed to a space, period, etc)"""
    implement me!
````


## Submission

**At least one partner** should submit one .py file named `crypto.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **all partners' ids** in comments at the top of the file.
