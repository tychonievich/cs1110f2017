---
title: Assignments
...


<div style="display:table; font-size:200%; margin: 1em auto; padding:1ex; box-shadow: 0 1px 10px rgba(0,0,0,.1); border: thin solid #eee; border-radius:1ex; background-image: linear-gradient(to bottom, #ffffff, #f2f2f2);">[Submit assignments here](https://archimedes.cs.virginia.edu/cs1110/)</div>

<!--
The submission page for programming assignments is not quite ready yet, but will appear here soon.
-->
# Programming Assignments

Assignments are generally due at 10am.
If the submission site states a different due time, it supersedes this general rule.

<style type="text/css">
dl dd {
  display: inline;
  margin: 0;
}
dl dd:after{
  display: block;
  content: '';
}
dl dt{
  display: inline-block;
  min-width: 6em;
  font-weight:normal;
}
</style>



Mon 11 Sep 
:    [PA 01: greeting.py](pa01-greeting.html) 

Mon 11 Sep 
:    [PA 02: nonsense.py](pa02-nonsense.html) 

Wed 13 Sep 
:    [PA 03: dating.py](pa03-dating.html) 

Wed 13 Sep 
:    [PA 04: c2f.py](pa04-c2f.html) 

Fri 15 Sep 
:    [PA 05: maydate.py](pa05-maydate.html) 

Mon 18 Sep 
:    [PA 06: conversion.py](pa06-conversion.html) 

Wed 20 Sep 
:    [PA 07: quadratic.py](pa07-quadratic.html) 

Fri 22 Sep 
:    [PA 08: bmr.py](pa08-bmr.html) 

Mon 25 Sep 
:    [PA 09: averages.py](pa09-averages.html) 

Fri 06 Oct 
:    [PA 10: calculator.py](pa10-calculator.html) 

Mon 09 Oct 
:    [PA 11: rumple.py](pa11-rumple.html) 

Fri 13 Oct 
:    [PA 12: higher_lower.py](pa12-higher-lower.html) 

Mon 16 Oct 
:    [PA 13: higher_lower_player.py](pa13-higher-lower2.html) 

Wed 18 Oct 
:    [PA 14: roman.py](pa14-roman.html) 

Mon 23 Oct 
:    [PA 15: credit_card.py](pa15-credit.html) 

Wed 25 Oct 
:    [PA 16: matchmaker.py](pa16-matchmaker.html) 

Mon 30 Oct 
:    [PA 17: lous_list.py](pa17-louslist.html) 

Mon 06 Nov 
:    [PA 18: spellcheck.py](pa18-spellcheck.html) 

Wed 15 Nov 
:    [PA 19: flappybird.py](pa19-flappy.html) 


<script>
var dts = document.getElementsByTagName('dt');
for(var i=0; i<dts.length; i+=1) {
    if (new Date(dts[i].innerHTML+' 2017 10:00') < new Date()) {
        dts[i].style.color = '#999999';
    } else {
        console.log(new Date(dts[i].innerHTML+' 2017 10:00') + ' is in the future')
    }
}
</script>

# 1110 Labs

Labs are listed in order. See the [schedule](schedule.html) for the specific date of each lab.


-   [installing Python and PyCharm](lab01-installing.html)
-   [pseudocode counting squares](lab02-counting.html)
-   [turtle art contest](lab03-turtle.html)
-   [madlibs](lab04-madlib.html)
-   [exam prep](lab05-paper.html)
-   [strings](lab06-strpuz.html)
-   [hangman](lab07-hangman.html)
-   [old cryptography](lab08-crypto.html)
-   [debugging](lab09-debug.html)
-   [point-of-interest location](lab10-wendys.html)
-   [gamebox installation](lab11-gamebox.html)
-   [pong](lab12-pong.html)
-   [email hunt](lab13-email.html)
