---
title: "PA 21: salary.py"
...

# Background

A lot of information is freely available on the web, but not a lot of it is in forms that computers find useful to read.
A common use of regular expressions is to understand or **parse** data from a human-centric view like a webpage into a computer-centric view like CSV.

One source of data is [the Richmond Times-Dispatch's summary of Virginia state salaries](http://data.richmond.com/salaries/)'s, obtained using the state's [Freedom of Information statute](http://foiacouncil.dls.virginia.gov/).
To avoid overloading the newpaper's website with hundreds students testing their code, we have a mirror of the 2015--2016 UVA salary data you can have your code access on our servers for this assignment.

> <http://cs1110.cs.virginia.edu/files/uva2015/>

When you visit a page, you see a rendering of the content, but under the hood most web pages are written in a language called HTML.
Like Python, this is a text-based representation that describes what the computer is supposed to do.
Unlike Python, it is a *markup language*, not a *programming language*, meaning it is interested primarily in describing data rather than specifying processes.
The nuances of HTML are not important for our task; all you need to do is write regular expressions to find specific information within it.

You can view the HTML of any web page using the "view source" option of your web browser (typically either via the keyboard shortcut Ctrl+U or Cmd+Opt+U).
The source is what `urllib.request` will retrieve, what your regular expressions will need to look at, and what we discuss below.

# Task

The following writeup describes elements of the task you are to do, mostly with examples taken from the ["view source" of Teresa Sullivan's page](view-source:http://cs1110.cs.virginia.edu/files/uva2015/teresa-sullivan).
Your job is to generalize the pattern and put it in a regular expression.
Some information has multiple locations; you only need to find one of the options.

## Name normalization

The URLs use full names, family name last, lower-case, with hyphens between name parts.

If given                    Create
--------------------------- ------------------------------
`Teresa Sullivan`           `teresa-sullivan`
`Sullivan, Teresa`          `teresa-sullivan`
`teresa-sullivan`           `teresa-sullivan`
`151028368`                 `151028368`
`Polanowska-Grabow, Renata` `renata-polanowska-grabow`

## Find job title

Job title, e.g. the `President - University of Virginia`, which can be found in multiple locations in the website:

    <meta property="og:description" content="Job title: President - University of Virginia<br /> 2015 total gross pay: $733,800" />

and

    <span class="small text-muted" id="personjob">President - University of Virginia</span>

(the `<title>` line also has a job title, but with the wrong case; use one of the two above)

You'll need a regular expression that (a) finds one of those lines and (b) has a group (parentheses) around the portion that is the job title (`President - University of Virginia`).

After you get the group, if the job title contains `&amp;`, replace it with just `&`; likewise replace `&lt;` with `<` and `&gt;` with `>`.


## Find total compensation

Total compensation appears in multiple locations:

    <meta property="og:description" content="Job title: President - University of Virginia<br /> 2015 total gross pay: $733,800" />

and
    
    <h2 class="pay" id="paytotal">$733,800</h2>

and
    
    <div style="margin:0; float:left; background:#337ab7; height:100%; width:<%= getPct(paytype.amount, 733800.00) %>%;"></div>

Make a regular expression that finds one of these lines and has a group for the salary, and convert it to a `float` (`733800.0`{.python} in this case).


## Find rank, if given

Some (but not all) pages have a pay rank compared to other UVA employees; for example, the `1` in

    <tr><td>University of Virginia rank</td><td>1 of 7,474</td></tr>

If it is present, you'll want to turn it into an `int`{.python}.
If not, use the dummy-rank of `0`.
    

## Combine into a function

Write a function named `report` in a file `salary.py` that takes a name and returns three values:

-   The job title of that person.
-   That person's total salary.
-   That person's salary rank within UVA, or 0 if not provided.

If the person is not in the salary site, return `None, 0, 0`{.python}


# Example Runs

If you run `salary.py` it should not do anything.
It defines functions, it does not run them.

If in a separate file you write

````
import salary

for name in (
        'Teresa Sullivan', 
        'Sullivan, Teresa', 
        '151028368', 
        'Ali Reza Forghani Esfahani', 
        'pamela-neff',
        'Thomas Jefferson'
        ):
    job, money, rank = salary.report(name)
    print(name, 'is a', job, 'and makes', money, '(rank', str(rank)+')')
````


# Thought Question

    -   Compensation breakdown as a `dict`{.python} with `str`{.python} keys and `float`{.python} values;
        e.g. 
        
        ````python
        {'Base salary': 188617.0, 'Additional compensation': 4100.0, 'Non-state salary': 346083.0, 'Deferred compensation', 180000.0}
        ````
        
        based on
    
            var pay = [ {'name': 'Base salary', 'amount': 188617 }, {'name': 'Additional compensation', 'amount': 4100 }, {'name': 'Non-state salary', 'amount': 346083 }, {'name': 'Deferred compensation', 'amount': 180000 } ];
        
        Note that the set of keys in the breakdown `dict` will depend on the employee; for example, `151028368`'s line looks like just
        
            var pay = [ {'name': 'Base salary', 'amount': 41000 } ];
        
        and would create the `dict`
        
        ````python
        {'Base salary': 41000.0}
        ````
    
-   Return the results in a `dict`{.python}, like so:

    ````python
    {'title': 'President - University of Virginia', 'pay': 733800.0, 'rank': 1, 'breakdown': {'Base salary': 188617.0, 'Additional compensation': 4100.0, 'Non-state salary': 346083.0, 'Deferred compensation': 180000.0}}
    ````
    
    If the name does not map into a URL we have, instead return an empty `dict`{.python}, `{}`{.python}

# Example runs

In addition to `"Teresa Sullivan"`, noted above,
you should try out 

-   an unranked anonymous employee like `"151028368"`,
-   a hyphenated surname like `"Polanowska-Grabow, Renata"`,
-   a multiple-spaces name like `"Ali Reza Forghani Esfahani"`,
-   a job title with a special character like `"pamela-neff"`, and
-   a person not listed like `"thomas-jefferson"`.

In each case, your results should match what you find on the Richmond Times-Dispatch website and our mirror copy of it (except the missing person who should return `{}`).


# Troubleshooting

You will probably find it easier to create an empty `dict` first and add new key/value pairs to it as you find them.
This will help particularly with the optional keys like `rank` and set of the keys in the `breakdown` `dict`.

---

There are a lot of things going on in this function.
Good coding practice would be to make a few extra functions to help out;
for example it might make sense to have a `name_to_URL(name)` function, etc.

Incidentally, the `name_to_url` proceess does not need regular expressions; it is enough to 

1.  find a comma (using `in`{.python}) and reorder the text if there is one (move what was before the comma to be after it)
2.  make it lower-case
3.  change spaces to hyphens

---

The easiest way to tell if the URL does not exist is to open it in a `try:`{.python} and handle failure in an `except:`{.python}

---

Since the values are identifiable by their surrounding context, try making regular expressions that match that context and keep the answer in a group, such as `<td>([0-9]+) of` for finding rank (which does not quite work as written...).

---

When `search` fails to find something, it returns `None`{.python}.

For most of the elements of the answer, `search` is the regular expression method you're most likely to want.
However, the compensation breakdown will probably benefit from a `finditer`, with a regular expression that matches the key in one group and the value in another group.

---

Case matters. If the website describes a person's `Base salary` report their `Base salary` not their `Base Salary`.

---

For the compensation breakdown, try looking for all generic `'name': '...', 'ammount': ...` strings and adding each one to an initially-empty `dict`.
Using groups and the `match.group(number)` method will make this much easier than not using those tools.
