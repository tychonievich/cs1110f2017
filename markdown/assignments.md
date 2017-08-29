---
title: Assignments
...

<!--
<div style="display:table; font-size:200%; margin: 1em auto; padding:1ex; box-shadow: 0 1px 10px rgba(0,0,0,.1); border: thin solid #eee; border-radius:1ex; background-image: linear-gradient(to bottom, #ffffff, #f2f2f2);">[Submit assignments here](https://archimedes.cs.virginia.edu/cs1110/)</div>
-->

The submission page for programming assignments is not quite ready yet, but will appear here soon.

# Programming Assignments

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
}
</style>



2017-09-06 
:    [greeting.py](w01-greeting.html) 

2017-09-06 
:    [nonsense.py](w01-nonsense.html) 

2017-09-08 
:    [c2f.py](w01-c2f.html) 

2017-09-08 
:    [dating.py](w01-dating.html) 

2017-09-10 
:    [maydate.py](w02-maydate.html) 

2017-09-13 
:    [conversion.py](w02-conversion.html) 

2017-09-15 
:    [quadratic.py](w02-quadratic.html) 


<script>
var dts = document.getElementsByTagName('dt');
for(var i=0; i<dts.length; i+=1) {
    if (new Date(dts[i].innerHTML+' 10:00') < Date('2017-09-10 09:56')) {
        dts[i].style.backgroundColor = '#e3e3e3';
        dts[i].nextElementSibling.style.backgroundColor = '#e3e3e3';
    }
}
</script>

# 1110 Labs

Labs are listed in order. See the [schedule](schedule.html) for the specific date of each lab.


-   [installing Python and PyCharm](lab01-installing.html)
-   [pseudocode counting squares](lab02-counting.html)
-   [turtle art contest](lab03-turtle.html)
