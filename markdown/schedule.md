---
title: Schedule
...


<style>
.calendar { border-collapse: collapse; }
.calendar td { padding:0.5ex; }
.day { width:25%; border:thin solid black; vertical-align:top; }
.date { color:#777; font-size:80%; float:right; padding-left:1ex; margin-top:-0.8ex; }
.Monday { }
.Wednesday { }
.Thursday { }
.Thursday.day { border:none; }
.Friday { }
.noclass { background-color: #eee; color:#777; border:none; }
.exam, .special { background-color: #fda; }
span.special { white-space:pre; }
td span.special { display:block; margin:0ex -0.5ex; padding: 0ex 0.5ex;}
.agenda th+td { padding-left:1em; }
tr.lab { background-color: #fff7f0; }
.button { padding:1ex; margin:1ex; border-radius:0.5ex; background-color:#fda; display:inline-block;}
.button.visited { background-color:#eee; color:#777; }
thead { background-color: #fda; }
#age1111 tbody tr:nth-child(2n+1) { background-color: #fff7f0; }
#age1111 tbody tr.noclass { background-color: #eee; }
</style>
<script>
function rehide(e) {
        var hash=window.location.hash;
        if (e) hash = e;
        if (typeof(hash) != "string") return;
        console.log("hash = " + hash);
        var elems = ['cal001', 'cal002', 'cal1111', 'age001', 'age002', 'age1111'];
        for(var i in elems) {
                var id = elems[i];
                if (hash == id || hash == '#'+id)
                        document.getElementById(id).setAttribute('style', '');
                else
                        document.getElementById(id).setAttribute('style', 'display:none;');
                if (hash == id || hash == '#'+id)
                        document.getElementById('a'+id).setAttribute('class', 'button visited');
                else
                        document.getElementById('a'+id).setAttribute('class', 'button');
                
        }
        return true;
}
</script>

<a id="acal001" class="button" href="#cal001" onclick="rehide('cal001')">1110-001 Calendar</a>
<a id="aage001" class="button" href="#age001" onclick="rehide('age001')">1110-001 Agenda</a>
<a id="acal002" class="button" href="#cal002" onclick="rehide('cal002')">1110-002 Calendar</a>
<a id="aage002" class="button" href="#age002" onclick="rehide('age002')">1110-002 Agenda</a>
<a id="acal1111" class="button" href="#cal1111" onclick="rehide('cal1111')">1111 Calendar</a>
<a id="aage1111" class="button" href="#age1111" onclick="rehide('age1111')">1111 Agenda</a>

<hr/>

Note: assignments and their due dates are listed on the [assignments page](assignments.html), not on this page.


<table id="cal001" class="calendar">
<thead><tr><th>Monday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th></tr></thead>
<tbody><tr><td/>
<td class="day Wednesday " id="2017-01-18"><span class="date">18 Jan</span>welcome<br/>§[1.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.6), §[1.9](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.9)<br/> [sketch.png](files/001/20170118a-sketch.png) [sketch.png](files/001/20170118b-sketch.png) [sketch.png](files/001/20170118c-sketch.png) [video](screencasts/2017-01-18-lecture.webm)<br/></td>
<td class="day Thursday  lab" id="2017-01-19"><span class="date">19 Jan</span>[installing Python and PyCharm](lab01-installing.html)<br/></td>
<td class="day Friday " id="2017-01-20"><span class="date">20 Jan</span>from requirements to software<br/>§[1.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.5)<br/> [sketch.png](files/001/20170120a-sketch.png) [computing.png](files/001/20170120b-computing.png) [computer.png](files/001/20170120c-computer.png) [development-lifecycle.png](files/001/20170120d-development-lifecycle.png) [design.png](files/001/20170120e-design.png) [compilation.png](files/001/20170120f-compilation.png) [kinds-of-errors.png](files/001/20170120g-kinds-of-errors.png) [algorithm.png](files/001/20170120j-algorithm.png) [video](screencasts/2017-01-20-lecture.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-23"><span class="date">23 Jan</span>ambiguity<br/>Exercises 1.1 and 1.2 from textbook<br/> [sketch.png](files/001/20170123a-sketch.png) [activity.png](files/001/20170123c-activity.png) [short-examples.png](files/001/20170123d-short-examples.png) [sketch.png](files/001/20170123e-sketch.png) [language-by-elimination.png](files/001/20170123f-language-by-elimination.png) [language-by-construction.png](files/001/20170123g-language-by-construction.png) [video](screencasts/2017-01-23-lecture.webm)<br/></td>
<td class="day Wednesday " id="2017-01-25"><span class="date">25 Jan</span>pseudocode<br/>[wikihow](http://www.wikihow.com/Write-Pseudocode)<br/> [notes.txt](files/001/2017-01-25-notes.txt) [sketch.png](files/001/20170125b-sketch.png) [pseudocode.png](files/001/20170125d-pseudocode.png) [video](screencasts/2017-01-25-lecture.webm)<br/></td>
<td class="day Thursday  lab" id="2017-01-26"><span class="date">26 Jan</span>[pseudocode counting squares](lab02-counting.html)<br/></td>
<td class="day Friday " id="2017-01-27"><span class="date">27 Jan</span>PyCharm<br/>§[1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.4), §[1.7](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.7)<br/>[demo.py](files/001/demo.py) [demo1.py](files/001/2017-01-27-demo1.py) [turtle_1.py](files/001/2017-01-27-turtle_1.py) [sketch.png](files/001/20170127a-sketch.png) [turtle.png](files/001/20170127b-turtle.png) [box.png](files/001/20170127c-box.png) [video](screencasts/2017-01-27-lecture.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-30"><span class="date">30 Jan</span>course overview with `turtle`{.python}, part 1<br/> [turtle_2.py](files/001/2017-01-30-turtle_2.py) [video](screencasts/2017-01-30-lecture.webm)<br/></td>
<td class="day Wednesday " id="2017-02-01"><span class="date">1 Feb</span>course overview with `turtle`{.python}, part 2<br/>video didn't work right -- [audio](podcasts/2017-02-01-audio.mp3) [turtle_3.py](files/001/2017-02-01-turtle_3.py) [sketch.png](files/001/20170201a-sketch.png) [sketch.png](files/001/20170201b-sketch.png) [stars.png](files/001/20170201c-stars.png) [sunflowers.png](files/001/20170201d-sunflowers.png) [video](screencasts/2017-02-01-lecture.webm)<br/><span class="special">Add deadline</span></td>
<td class="day Thursday  lab" id="2017-02-02"><span class="date">2 Feb</span>[turtle art contest](lab03-turtle.html)<br/></td>
<td class="day Friday " id="2017-02-03"><span class="date">3 Feb</span>hello, world!<br/>[revised chapter 2](revised2.2.html); §[5.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.5.2.4)--5.2.5; §[4.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.4.1)<br/>[PythonTutor](http://pythontutor.com/) [example1.py](files/001/2017-02-03-example1.py) [example2.py](files/001/2017-02-03-example2.py) [example3.py](files/001/2017-02-03-example3.py) [recipe.png](files/001/20170203a-recipe.png) [workspace.png](files/001/20170203b-workspace.png) [program-components.png](files/001/20170203c-program-components.png) [video](screencasts/2017-02-03-lecture.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-06"><span class="date">6 Feb</span>variables, values, and operators<br/>§[3](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.3) and §[4](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.4)<br/> [complimenter.py](files/001/2017-02-06-complimenter.py) [complimenter2.py](files/001/2017-02-06-complimenter2.py) [polynomial.py](files/001/2017-02-06-polynomial.py) [polynomial2.py](files/001/2017-02-06-polynomial2.py) [video](screencasts/2017-02-06-lecture.webm)<br/></td>
<td class="day Wednesday " id="2017-02-08"><span class="date">8 Feb</span>functions -- basics, `def`{.python}<br/>§[5](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.5)--5.2 and §[8](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.8)--8.2.1<br/>guest instructor; recordings will not be made or posted, [functions](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-functions.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/functions/)<br/></td>
<td class="day Thursday  lab" id="2017-02-09"><span class="date">9 Feb</span>[madlibs](lab04-madlib.html)<br/></td>
<td class="day Friday " id="2017-02-10"><span class="date">10 Feb</span>functions -- flow of control<br/>§[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6<br/>guest instructor; recordings will not be made or posted<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-13"><span class="date">13 Feb</span>functions -- scope, `global`{.python}<br/>§[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)<br/> [func_test.py](files/001/2017-02-13-func_test.py) [functions_calling_functions.py](files/001/2017-02-13-functions_calling_functions.py) [video](screencasts/2017-02-13-lecture.webm)<br/></td>
<td class="day Wednesday " id="2017-02-15"><span class="date">15 Feb</span>decisions -- `if`{.python}, `elif`{.python}, and `else`{.python}<br/>§[6.1.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.6.1.2) and §[6.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.2)--6.2.3<br/> [guessing_game.py](files/001/2017-02-15-guessing_game.py) [if_in_func.py](files/001/2017-02-15-if_in_func.py) [if_intro.py](files/001/2017-02-15-if_intro.py) [ordianal.py](files/001/2017-02-15-ordianal.py) [video](screencasts/2017-02-15-lecture.webm)<br/></td>
<td class="day Thursday  lab" id="2017-02-16"><span class="date">16 Feb</span>[exam prep](lab05-paper.html)<br/></td>
<td class="day Friday " id="2017-02-17"><span class="date">17 Feb</span>decisions -- logical operators (not on exam 1)<br/>rest of §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2<br/>**never** use §[6.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.3)'s `exit()`{.python} function [bool_type.py](files/001/2017-02-17-bool_type.py) [fundamental_truthiness.py](files/001/2017-02-17-fundamental_truthiness.py) [types.png](files/001/20170217a-types.png) [operators.png](files/001/20170217b-operators.png) [boolean_operators.png](files/001/20170217c-boolean_operators.png) [video](screencasts/2017-02-17-lecture.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-20"><span class="date">20 Feb</span>review<br/>§[2](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.2)--5.2, §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2.3, §[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6, §[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)<br/> [qa.txt](files/001/2017-02-20-qa.txt) [test1review.py](files/001/2017-02-20-test1review.py) [sketch.png](files/001/20170220a-sketch.png) [video](screencasts/2017-02-20-lecture.webm)<br/></td>
<td class="day Wednesday exam" id="2017-02-22"><span class="date">22 Feb</span>exam 1<br/>see [lab 5](lab05-paper.html)</td>
<td class="day Thursday  lab" id="2017-02-23"><span class="date">23 Feb</span>[oracle](lab06-magic.html)<br/></td>
<td class="day Friday " id="2017-02-24"><span class="date">24 Feb</span>code readability, elegance<br/>§[3.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.3.4), §[8.2.9](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.9)--8.2.10; skim [PEP 8](https://www.python.org/dev/peps/pep-0008/)<br/> [cruft.py](files/001/2017-02-24-cruft.py) [more_true_stuff.py](files/001/2017-02-24-more_true_stuff.py) [style.py](files/001/2017-02-24-style.py) [zen.py](files/001/2017-02-24-zen.py) [sketch.png](files/001/20170224a-sketch.png) [video](screencasts/2017-02-24-lecture.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-27"><span class="date">27 Feb</span>testing<br/>our own [testing writeup](testing.html)<br/> [tester_qa.py](files/001/2017-02-27-tester_qa.py) [sketch.png](files/001/20170227a-sketch.png) [proof.png](files/001/20170227b-proof.png) [black-box.png](files/001/20170227c-black-box.png) [test-cases.png](files/001/20170227d-test-cases.png) [is-even.png](files/001/20170227e-is-even.png) [code-tracing.png](files/001/20170227f-code-tracing.png) [video](screencasts/2017-02-27-lecture.webm)<br/></td>
<td class="day Wednesday " id="2017-03-01"><span class="date">1 Mar</span>repeating with `while`{.python}<br/>§[7.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.1)<br/> [annoy.py](files/001/2017-03-01-annoy.py) [while_funcs.py](files/001/2017-03-01-while_funcs.py) [while_intro.py](files/001/2017-03-01-while_intro.py) [sketch.png](files/001/20170301a-sketch.png) [if-vs-while.png](files/001/20170301b-if-vs-while.png) [video](screencasts/2017-03-01-lecture.webm)<br/></td>
<td class="day Thursday  lab" id="2017-03-02"><span class="date">2 Mar</span>[nim](lab07-nim.html)<br/></td>
<td class="day Friday " id="2017-03-03"><span class="date">3 Mar</span>composite datatypes -- strings, ranges, lists, tuples<br/>§[10.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.4), §[11](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.11), §[12.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.1), §[12.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.3)<br/> [change_element.py](files/001/2017-03-03-change_element.py) [intro_range.py](files/001/2017-03-03-intro_range.py) [str_index.py](files/001/2017-03-03-str_index.py) [sketch.png](files/001/20170303a-sketch.png) [collections.png](files/001/20170303b-collections.png) [video](screencasts/2017-03-03-lecture.webm)<br/><span class="special">Drop deadline</span></td>
</tr><tr>
<td class="day Monday noclass" id="2017-03-06"><span class="date">6 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Wednesday noclass" id="2017-03-08"><span class="date">8 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Thursday noclass lab" id="2017-03-09"><span class="date">9 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Friday noclass" id="2017-03-10"><span class="date">10 Mar</span><span class="reason">Spring recess</span></td>
</tr><tr>
<td class="day Monday " id="2017-03-13"><span class="date">13 Mar</span>methods and mutability -- why `list`{.python} is special<br/>§[12.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.2), §[12.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.5),<br/> [favorite_words.py](files/001/2017-03-13-favorite_words.py) [for_intro.py](files/001/2017-03-13-for_intro.py) [string-indices.py](files/001/2017-03-13-string-indices.py) [string-split.py](files/001/2017-03-13-string-split.py) [value-identity.png](files/001/20170313b-value-identity.png) [methods.png](files/001/20170313c-methods.png) [in-and-find.png](files/001/20170313d-in-and-find.png) [video](screencasts/2017-03-13-lecture.webm)<br/></td>
<td class="day Wednesday " id="2017-03-15"><span class="date">15 Mar</span>iteration -- the `for`{.python} loop<br/>§[7.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.2)<br/> [for_append.py](files/001/2017-03-15-for_append.py) [for_functions.py](files/001/2017-03-15-for_functions.py) [for_intro.py](files/001/2017-03-15-for_intro.py) [for_numbers.py](files/001/2017-03-15-for_numbers.py) [more_on_ranges.py](files/001/2017-03-15-more_on_ranges.py) [sort_by_length.py](files/001/2017-03-15-sort_by_length.py) [video](screencasts/2017-03-15-lecture.webm)<br/><span class="special">Withdraw deadline</span></td>
<td class="day Thursday  lab" id="2017-03-16"><span class="date">16 Mar</span>[wahoo spoon](lab08-spoon.html)<br/></td>
<td class="day Friday " id="2017-03-17"><span class="date">17 Mar</span>applications of lists and strings<br/>§[10.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.6), §[12.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.4)<br/> [part_of_spoon.py](files/001/2017-03-17-part_of_spoon.py) [scramble.py](files/001/2017-03-17-scramble.py) [sort_by_length.py](files/001/2017-03-17-sort_by_length.py) [sketch.png](files/001/20170317a-sketch.png) [video](screencasts/2017-03-17-lecture.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-03-20"><span class="date">20 Mar</span>debugging techniques<br/>[buggy code](files/001/spoon.py) [sketch.png](files/001/20170320a-sketch.png) [know_this.png](files/001/20170320b-know_this.png) [print_bedugging.png](files/001/20170320c-print_bedugging.png) [video](screencasts/2017-03-20-lecture.webm)<br/></td>
<td class="day Wednesday " id="2017-03-22"><span class="date">22 Mar</span>flexible indices -- `dict`{.python}<br/>§[13](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.13)<br/> [dict_intro.py](files/001/2017-03-22-dict_intro.py) [function.png](files/001/20170322a-function.png) [sketch.png](files/001/20170322b-sketch.png) [mappings.png](files/001/20170322c-mappings.png) [dict-literals.png](files/001/20170322d-dict-literals.png) [dict-vs-list.png](files/001/20170322e-dict-vs-list.png) [dict-methods.png](files/001/20170322f-dict-methods.png) [video](screencasts/2017-03-22-lecture.webm)<br/></td>
<td class="day Thursday  lab" id="2017-03-23"><span class="date">23 Mar</span>[debugging practice](lab09-debug.html)<br/></td>
<td class="day Friday " id="2017-03-24"><span class="date">24 Mar</span>reading data -- `open`{.python} and `urllib`{.python}<br/>§[16.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.16.2), §[27.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.27.3)<br/> [debug_task.py](files/001/2017-03-24-debug_task.py) [file_intro_1.py](files/001/2017-03-24-file_intro_1.py) [file_intro_2.py](files/001/2017-03-24-file_intro_2.py) [url_intro_1.py](files/001/2017-03-24-url_intro_1.py) [url_intro_2.py](files/001/2017-03-24-url_intro_2.py) [postoffice.png](files/001/20170324a-postoffice.png) [disk.png](files/001/20170324b-disk.png) [video](screencasts/2017-03-24-lecture.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-03-27"><span class="date">27 Mar</span>understanding data<br/>Wikpedia on [delimiter-separated values](https://en.wikipedia.org/wiki/Delimiter-separated_values)<br/>[vastats.csv](files/vastats.csv) [url_intro_2.py](files/001/2017-03-27-url_intro_2.py) [va_stat_parse.py](files/001/2017-03-27-va_stat_parse.py) [video](screencasts/2017-03-27-lecture.webm)<br/></td>
<td class="day Wednesday " id="2017-03-29"><span class="date">29 Mar</span>more on the data theme<br/>[fake-queue.csv](files/fake-queue.csv) [csv_queue_examples.py](files/001/2017-03-29-csv_queue_examples.py) [sketch.png](files/001/20170329a-sketch.png) [dict_example.png](files/001/20170329b-dict_example.png) [video](screencasts/2017-03-29-lecture.webm)<br/></td>
<td class="day Thursday  lab" id="2017-03-30"><span class="date">30 Mar</span>[location finder](lab10-wendys.html)<br/></td>
<td class="day Friday " id="2017-03-31"><span class="date">31 Mar</span>polite code -- using `try`{.python} and `except`{.python} (not on exam 2)<br/>§[17.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.17.2)<br/> [exceptions_1.py](files/001/2017-03-31-exceptions_1.py) [exceptions_2.py](files/001/2017-03-31-exceptions_2.py) [exceptions_3.py](files/001/2017-03-31-exceptions_3.py) [exceptions_4.py](files/001/2017-03-31-exceptions_4.py) [new_csv_file.py](files/001/2017-03-31-new_csv_file.py) [url_intro_1.py](files/001/2017-03-31-url_intro_1.py) [footnotes.png](files/001/20170331a-footnotes.png) [video](screencasts/2017-03-31-lecture.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-03"><span class="date">3 Apr</span>review<br/>[things to know](know.html) [e2questions.py](files/001/2017-04-03-e2questions.py) [cs-prereq.png](files/001/20170403a-cs-prereq.png) [strip-split-order.png](files/001/20170403b-strip-split-order.png) [video](screencasts/2017-04-03-lecture.webm)<br/></td>
<td class="day Wednesday exam" id="2017-04-05"><span class="date">5 Apr</span>exam 2</td>
<td class="day Thursday  lab" id="2017-04-06"><span class="date">6 Apr</span>[gamebox installation](lab11-gamebox.html)<br/></td>
<td class="day Friday " id="2017-04-07"><span class="date">7 Apr</span>game design with `gamebox`{.python}<br/>[gamebox documentation](code/gamebox/gamebox.pdf)<br/> [blankgame.py](files/001/2017-04-07-blankgame.py) [game1.py](files/001/2017-04-07-game1.py) [game2.py](files/001/2017-04-07-game2.py) [game3.py](files/001/2017-04-07-game3.py) [game4.py](files/001/2017-04-07-game4.py) [game5.py](files/001/2017-04-07-game5.py) [gamebox.png](files/001/20170407a-gamebox.png) [momentum.png](files/001/20170407b-momentum.png) [video](screencasts/2017-04-07-lecture.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-10"><span class="date">10 Apr</span>game design with `gamebox`{.python}<br/> [jumper1.py](files/001/2017-04-10-jumper1.py) [jumper2.py](files/001/2017-04-10-jumper2.py) [jumper3.py](files/001/2017-04-10-jumper3.py) [jumper4.py](files/001/2017-04-10-jumper4.py) [jumper.png](files/001/20170410a-jumper.png) [bounce-speed.png](files/001/20170410b-bounce-speed.png) [frames.png](files/001/20170410c-frames.png) [video](screencasts/2017-04-10-lecture.webm)<br/></td>
<td class="day Wednesday " id="2017-04-12"><span class="date">12 Apr</span>game design with `gamebox`{.python}<br/> [game_over.py](files/001/2017-04-12-game_over.py) [game_wish_list.py](files/001/2017-04-12-game_wish_list.py) [sprite_example.py](files/001/2017-04-12-sprite_example.py) [sprites.png](files/001/20170412a-sprites.png) [sprite-sheets.png](files/001/20170412c-sprite-sheets.png) [video](screencasts/2017-04-12-lecture.webm)<br/></td>
<td class="day Thursday  lab" id="2017-04-13"><span class="date">13 Apr</span>[pong](lab12-pong.html)<br/></td>
<td class="day Friday " id="2017-04-14"><span class="date">14 Apr</span>regular expressions<br/>§[25.1.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.1), §[25.1.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.3), §[25.1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.4), §[25.2.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.1), [regexr.com](http://regexr.com/)<br/> [re_intro.py](files/001/2017-04-14-re_intro.py) [regex.png](files/001/20170414a-regex.png) [compile.png](files/001/20170414b-compile.png) [regex-guide.png](files/001/20170414c-regex-guide.png) [character-class.png](files/001/20170414d-character-class.png) [video](screencasts/2017-04-14-lecture.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-17"><span class="date">17 Apr</span>re repetition and groups<br/>§[25.2.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.3), §[25.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.4)<br/> [re_intro.py](files/001/2017-04-17-re_intro.py) [charclass-review.png](files/001/20170417a-charclass-review.png) [groups.png](files/001/20170417b-groups.png) [regex-overview.png](files/001/20170417c-regex-overview.png) [matching-examples.png](files/001/20170417d-matching-examples.png) [vertical-bar.png](files/001/20170417e-vertical-bar.png) [video](screencasts/2017-04-17-lecture.webm)<br/></td>
<td class="day Wednesday " id="2017-04-19"><span class="date">19 Apr</span>re building<br/>our [building guide and example](re-tips.html)<br/> [re_practice.py](files/001/2017-04-19-re_practice.py) [sketch.png](files/001/20170419a-sketch.png) [re-trace.png](files/001/20170419b-re-trace.png) [video](screencasts/2017-04-19-lecture.webm)<br/></td>
<td class="day Thursday  lab" id="2017-04-20"><span class="date">20 Apr</span>[email hunt](lab13-email.html)<br/></td>
<td class="day Friday " id="2017-04-21"><span class="date">21 Apr</span>re replacing<br/>§[25.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.25.4)<br/> [re_sub.py](files/001/2017-04-21-re_sub.py) [sketch.png](files/001/20170421a-sketch.png) [elegance.png](files/001/20170421b-elegance.png) [character-classes.png](files/001/20170421c-character-classes.png) [video](screencasts/2017-04-21-lecture.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-24"><span class="date">24 Apr</span>file writing<br/>§[16](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.16)–[16.5.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.16.5.1), especially §[16.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.16.3); also [our writeup](16-addendum.html)<br/> [selfdelete.py](files/001/2017-04-24-selfdelete.py) [user_info.py](files/001/2017-04-24-user_info.py) [writing_1.py](files/001/2017-04-24-writing_1.py) [writing_problem.py](files/001/2017-04-24-writing_problem.py) [sketch.png](files/001/20170424a-sketch.png) [buckets.png](files/001/20170424b-buckets.png) [buffering.png](files/001/20170424c-buffering.png) [video](screencasts/2017-04-24-lecture.webm)<br/></td>
<td class="day Wednesday " id="2017-04-26"><span class="date">26 Apr</span>file writing<br/> [read_write_csv.py](files/001/2017-04-26-read_write_csv.py) [user_info.py](files/001/2017-04-26-user_info.py) [user_info_2.py](files/001/2017-04-26-user_info_2.py) [sketch.png](files/001/20170426a-sketch.png) [modify-file-by-temporary.png](files/001/20170426b-modify-file-by-temporary.png) [video](screencasts/2017-04-26-lecture.webm)<br/></td>
<td class="day Thursday  lab" id="2017-04-27"><span class="date">27 Apr</span>[review](lab14-review.html)<br/></td>
<td class="day Friday " id="2017-04-28"><span class="date">28 Apr</span>file writing wrapup, and Q&A<br/>submit questions [here](https://docs.google.com/a/virginia.edu/forms/d/e/1FAIpQLSfUZeCfOpr04FMG9d1QdbBivgGtnpjx5Rq2wXHUAsp1huLo3g/viewform?usp=sf_link)<br/>No recording available (my audio recorder's battery died 48 seconds into lecture)<br/> [read_write_csv.py](files/001/2017-04-28-read_write_csv.py) [salary.py](files/001/2017-04-28-salary.py)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-05-01"><span class="date">1 May</span>review<br/>[review topics](know.html)<br/>the final exam is cumulative [salary.py](files/001/2017-05-01-salary.py) [video](screencasts/2017-05-01-lecture.webm)<br/></td>
</tr></tbody></table>
<table id="age001" class="agenda">
<thead><tr><th>Date</th><th>Topic</th><th>Reading</th><th>Notes</th></tr></thead>
<tbody>
<tr id="2017-01-18" class=""><th>18 Jan <br/></th><td>welcome</td><td>§[1.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.6), §[1.9](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.9)</td><td> [sketch.png](files/001/20170118a-sketch.png) [sketch.png](files/001/20170118b-sketch.png) [sketch.png](files/001/20170118c-sketch.png) [video](screencasts/2017-01-18-lecture.webm)
<tr id="2017-01-19" class=" lab"><th>19 Jan <br/></th><td>[installing Python and PyCharm](lab01-installing.html)</td><td></td><td></td></tr>

<tr id="2017-01-20" class=""><th>20 Jan <br/></th><td>from requirements to software</td><td>§[1.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.5)</td><td> [sketch.png](files/001/20170120a-sketch.png) [computing.png](files/001/20170120b-computing.png) [computer.png](files/001/20170120c-computer.png) [development-lifecycle.png](files/001/20170120d-development-lifecycle.png) [design.png](files/001/20170120e-design.png) [compilation.png](files/001/20170120f-compilation.png) [kinds-of-errors.png](files/001/20170120g-kinds-of-errors.png) [algorithm.png](files/001/20170120j-algorithm.png) [video](screencasts/2017-01-20-lecture.webm)
<tr id="2017-01-23" class=""><th>23 Jan <br/></th><td>ambiguity</td><td>Exercises 1.1 and 1.2 from textbook</td><td> [sketch.png](files/001/20170123a-sketch.png) [activity.png](files/001/20170123c-activity.png) [short-examples.png](files/001/20170123d-short-examples.png) [sketch.png](files/001/20170123e-sketch.png) [language-by-elimination.png](files/001/20170123f-language-by-elimination.png) [language-by-construction.png](files/001/20170123g-language-by-construction.png) [video](screencasts/2017-01-23-lecture.webm)
<tr id="2017-01-25" class=""><th>25 Jan <br/></th><td>pseudocode</td><td>[wikihow](http://www.wikihow.com/Write-Pseudocode)</td><td> [notes.txt](files/001/2017-01-25-notes.txt) [sketch.png](files/001/20170125b-sketch.png) [pseudocode.png](files/001/20170125d-pseudocode.png) [video](screencasts/2017-01-25-lecture.webm)
<tr id="2017-01-26" class=" lab"><th>26 Jan <br/></th><td>[pseudocode counting squares](lab02-counting.html)</td><td></td><td></td></tr>

<tr id="2017-01-27" class=""><th>27 Jan <br/></th><td>PyCharm</td><td>§[1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.4), §[1.7](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.7)</td><td>[demo.py](files/001/demo.py) [demo1.py](files/001/2017-01-27-demo1.py) [turtle_1.py](files/001/2017-01-27-turtle_1.py) [sketch.png](files/001/20170127a-sketch.png) [turtle.png](files/001/20170127b-turtle.png) [box.png](files/001/20170127c-box.png) [video](screencasts/2017-01-27-lecture.webm)
<tr id="2017-01-30" class=""><th>30 Jan <br/></th><td>course overview with `turtle`{.python}, part 1</td><td></td><td> [turtle_2.py](files/001/2017-01-30-turtle_2.py) [video](screencasts/2017-01-30-lecture.webm)
<tr id="2017-02-01" class=""><th>1 Feb <br/><span class="special">Add deadline</span></th><td>course overview with `turtle`{.python}, part 2</td><td></td><td>video didn't work right -- [audio](podcasts/2017-02-01-audio.mp3) [turtle_3.py](files/001/2017-02-01-turtle_3.py) [sketch.png](files/001/20170201a-sketch.png) [sketch.png](files/001/20170201b-sketch.png) [stars.png](files/001/20170201c-stars.png) [sunflowers.png](files/001/20170201d-sunflowers.png) [video](screencasts/2017-02-01-lecture.webm)
<tr id="2017-02-02" class=" lab"><th>2 Feb <br/></th><td>[turtle art contest](lab03-turtle.html)</td><td></td><td></td></tr>

<tr id="2017-02-03" class=""><th>3 Feb <br/></th><td>hello, world!</td><td>[revised chapter 2](revised2.2.html); §[5.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.5.2.4)--5.2.5; §[4.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.4.1)</td><td>[PythonTutor](http://pythontutor.com/) [example1.py](files/001/2017-02-03-example1.py) [example2.py](files/001/2017-02-03-example2.py) [example3.py](files/001/2017-02-03-example3.py) [recipe.png](files/001/20170203a-recipe.png) [workspace.png](files/001/20170203b-workspace.png) [program-components.png](files/001/20170203c-program-components.png) [video](screencasts/2017-02-03-lecture.webm)
<tr id="2017-02-06" class=""><th>6 Feb <br/></th><td>variables, values, and operators</td><td>§[3](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.3) and §[4](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.4)</td><td> [complimenter.py](files/001/2017-02-06-complimenter.py) [complimenter2.py](files/001/2017-02-06-complimenter2.py) [polynomial.py](files/001/2017-02-06-polynomial.py) [polynomial2.py](files/001/2017-02-06-polynomial2.py) [video](screencasts/2017-02-06-lecture.webm)
<tr id="2017-02-08" class=""><th>8 Feb <br/></th><td>functions -- basics, `def`{.python}</td><td>§[5](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.5)--5.2 and §[8](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.8)--8.2.1</td><td>guest instructor; recordings will not be made or posted, [functions](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-functions.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/functions/)
<tr id="2017-02-09" class=" lab"><th>9 Feb <br/></th><td>[madlibs](lab04-madlib.html)</td><td></td><td></td></tr>

<tr id="2017-02-10" class=""><th>10 Feb <br/></th><td>functions -- flow of control</td><td>§[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6</td><td>guest instructor; recordings will not be made or posted
<tr id="2017-02-13" class=""><th>13 Feb <br/></th><td>functions -- scope, `global`{.python}</td><td>§[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)</td><td> [func_test.py](files/001/2017-02-13-func_test.py) [functions_calling_functions.py](files/001/2017-02-13-functions_calling_functions.py) [video](screencasts/2017-02-13-lecture.webm)
<tr id="2017-02-15" class=""><th>15 Feb <br/></th><td>decisions -- `if`{.python}, `elif`{.python}, and `else`{.python}</td><td>§[6.1.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.6.1.2) and §[6.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.2)--6.2.3</td><td> [guessing_game.py](files/001/2017-02-15-guessing_game.py) [if_in_func.py](files/001/2017-02-15-if_in_func.py) [if_intro.py](files/001/2017-02-15-if_intro.py) [ordianal.py](files/001/2017-02-15-ordianal.py) [video](screencasts/2017-02-15-lecture.webm)
<tr id="2017-02-16" class=" lab"><th>16 Feb <br/></th><td>[exam prep](lab05-paper.html)</td><td></td><td></td></tr>

<tr id="2017-02-17" class=""><th>17 Feb <br/></th><td>decisions -- logical operators (not on exam 1)</td><td>rest of §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2</td><td>**never** use §[6.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.3)'s `exit()`{.python} function [bool_type.py](files/001/2017-02-17-bool_type.py) [fundamental_truthiness.py](files/001/2017-02-17-fundamental_truthiness.py) [types.png](files/001/20170217a-types.png) [operators.png](files/001/20170217b-operators.png) [boolean_operators.png](files/001/20170217c-boolean_operators.png) [video](screencasts/2017-02-17-lecture.webm)
<tr id="2017-02-20" class=""><th>20 Feb <br/></th><td>review</td><td>§[2](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.2)--5.2, §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2.3, §[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6, §[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)</td><td> [qa.txt](files/001/2017-02-20-qa.txt) [test1review.py](files/001/2017-02-20-test1review.py) [sketch.png](files/001/20170220a-sketch.png) [video](screencasts/2017-02-20-lecture.webm)
<tr id="2017-02-22" class="exam"><th>22 Feb </th><td>exam 1</td><td>see [lab 5](lab05-paper.html)</td><td>
<tr id="2017-02-23" class=" lab"><th>23 Feb <br/></th><td>[oracle](lab06-magic.html)</td><td></td><td></td></tr>

<tr id="2017-02-24" class=""><th>24 Feb <br/></th><td>code readability, elegance</td><td>§[3.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.3.4), §[8.2.9](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.9)--8.2.10; skim [PEP 8](https://www.python.org/dev/peps/pep-0008/)</td><td> [cruft.py](files/001/2017-02-24-cruft.py) [more_true_stuff.py](files/001/2017-02-24-more_true_stuff.py) [style.py](files/001/2017-02-24-style.py) [zen.py](files/001/2017-02-24-zen.py) [sketch.png](files/001/20170224a-sketch.png) [video](screencasts/2017-02-24-lecture.webm)
<tr id="2017-02-27" class=""><th>27 Feb <br/></th><td>testing</td><td>our own [testing writeup](testing.html)</td><td> [tester_qa.py](files/001/2017-02-27-tester_qa.py) [sketch.png](files/001/20170227a-sketch.png) [proof.png](files/001/20170227b-proof.png) [black-box.png](files/001/20170227c-black-box.png) [test-cases.png](files/001/20170227d-test-cases.png) [is-even.png](files/001/20170227e-is-even.png) [code-tracing.png](files/001/20170227f-code-tracing.png) [video](screencasts/2017-02-27-lecture.webm)
<tr id="2017-03-01" class=""><th>1 Mar <br/></th><td>repeating with `while`{.python}</td><td>§[7.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.1)</td><td> [annoy.py](files/001/2017-03-01-annoy.py) [while_funcs.py](files/001/2017-03-01-while_funcs.py) [while_intro.py](files/001/2017-03-01-while_intro.py) [sketch.png](files/001/20170301a-sketch.png) [if-vs-while.png](files/001/20170301b-if-vs-while.png) [video](screencasts/2017-03-01-lecture.webm)
<tr id="2017-03-02" class=" lab"><th>2 Mar <br/></th><td>[nim](lab07-nim.html)</td><td></td><td></td></tr>

<tr id="2017-03-03" class=""><th>3 Mar <br/><span class="special">Drop deadline</span></th><td>composite datatypes -- strings, ranges, lists, tuples</td><td>§[10.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.4), §[11](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.11), §[12.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.1), §[12.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.3)</td><td> [change_element.py](files/001/2017-03-03-change_element.py) [intro_range.py](files/001/2017-03-03-intro_range.py) [str_index.py](files/001/2017-03-03-str_index.py) [sketch.png](files/001/20170303a-sketch.png) [collections.png](files/001/20170303b-collections.png) [video](screencasts/2017-03-03-lecture.webm)
<tr id="2017-03-06" class="noclass"><th>6 Mar </th><td><span class="reason">Spring recess</span></td><td></td><td>
<tr id="2017-03-08" class="noclass"><th>8 Mar </th><td><span class="reason">Spring recess</span></td><td></td><td>
<tr id="2017-03-09" class="noclass lab"><th>9 Mar </th><td><span class="reason">Spring recess</span></td><td></td><td></td></tr>

<tr id="2017-03-10" class="noclass"><th>10 Mar </th><td><span class="reason">Spring recess</span></td><td></td><td>
<tr id="2017-03-13" class=""><th>13 Mar <br/></th><td>methods and mutability -- why `list`{.python} is special</td><td>§[12.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.2), §[12.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.5),</td><td> [favorite_words.py](files/001/2017-03-13-favorite_words.py) [for_intro.py](files/001/2017-03-13-for_intro.py) [string-indices.py](files/001/2017-03-13-string-indices.py) [string-split.py](files/001/2017-03-13-string-split.py) [value-identity.png](files/001/20170313b-value-identity.png) [methods.png](files/001/20170313c-methods.png) [in-and-find.png](files/001/20170313d-in-and-find.png) [video](screencasts/2017-03-13-lecture.webm)
<tr id="2017-03-15" class=""><th>15 Mar <br/><span class="special">Withdraw deadline</span></th><td>iteration -- the `for`{.python} loop</td><td>§[7.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.2)</td><td> [for_append.py](files/001/2017-03-15-for_append.py) [for_functions.py](files/001/2017-03-15-for_functions.py) [for_intro.py](files/001/2017-03-15-for_intro.py) [for_numbers.py](files/001/2017-03-15-for_numbers.py) [more_on_ranges.py](files/001/2017-03-15-more_on_ranges.py) [sort_by_length.py](files/001/2017-03-15-sort_by_length.py) [video](screencasts/2017-03-15-lecture.webm)
<tr id="2017-03-16" class=" lab"><th>16 Mar <br/></th><td>[wahoo spoon](lab08-spoon.html)</td><td></td><td></td></tr>

<tr id="2017-03-17" class=""><th>17 Mar <br/></th><td>applications of lists and strings</td><td>§[10.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.6), §[12.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.4)</td><td> [part_of_spoon.py](files/001/2017-03-17-part_of_spoon.py) [scramble.py](files/001/2017-03-17-scramble.py) [sort_by_length.py](files/001/2017-03-17-sort_by_length.py) [sketch.png](files/001/20170317a-sketch.png) [video](screencasts/2017-03-17-lecture.webm)
<tr id="2017-03-20" class=""><th>20 Mar <br/></th><td>debugging techniques</td><td></td><td>[buggy code](files/001/spoon.py) [sketch.png](files/001/20170320a-sketch.png) [know_this.png](files/001/20170320b-know_this.png) [print_bedugging.png](files/001/20170320c-print_bedugging.png) [video](screencasts/2017-03-20-lecture.webm)
<tr id="2017-03-22" class=""><th>22 Mar <br/></th><td>flexible indices -- `dict`{.python}</td><td>§[13](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.13)</td><td> [dict_intro.py](files/001/2017-03-22-dict_intro.py) [function.png](files/001/20170322a-function.png) [sketch.png](files/001/20170322b-sketch.png) [mappings.png](files/001/20170322c-mappings.png) [dict-literals.png](files/001/20170322d-dict-literals.png) [dict-vs-list.png](files/001/20170322e-dict-vs-list.png) [dict-methods.png](files/001/20170322f-dict-methods.png) [video](screencasts/2017-03-22-lecture.webm)
<tr id="2017-03-23" class=" lab"><th>23 Mar <br/></th><td>[debugging practice](lab09-debug.html)</td><td></td><td></td></tr>

<tr id="2017-03-24" class=""><th>24 Mar <br/></th><td>reading data -- `open`{.python} and `urllib`{.python}</td><td>§[16.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.16.2), §[27.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.27.3)</td><td> [debug_task.py](files/001/2017-03-24-debug_task.py) [file_intro_1.py](files/001/2017-03-24-file_intro_1.py) [file_intro_2.py](files/001/2017-03-24-file_intro_2.py) [url_intro_1.py](files/001/2017-03-24-url_intro_1.py) [url_intro_2.py](files/001/2017-03-24-url_intro_2.py) [postoffice.png](files/001/20170324a-postoffice.png) [disk.png](files/001/20170324b-disk.png) [video](screencasts/2017-03-24-lecture.webm)
<tr id="2017-03-27" class=""><th>27 Mar <br/></th><td>understanding data</td><td>Wikpedia on [delimiter-separated values](https://en.wikipedia.org/wiki/Delimiter-separated_values)</td><td>[vastats.csv](files/vastats.csv) [url_intro_2.py](files/001/2017-03-27-url_intro_2.py) [va_stat_parse.py](files/001/2017-03-27-va_stat_parse.py) [video](screencasts/2017-03-27-lecture.webm)
<tr id="2017-03-29" class=""><th>29 Mar <br/></th><td>more on the data theme</td><td></td><td>[fake-queue.csv](files/fake-queue.csv) [csv_queue_examples.py](files/001/2017-03-29-csv_queue_examples.py) [sketch.png](files/001/20170329a-sketch.png) [dict_example.png](files/001/20170329b-dict_example.png) [video](screencasts/2017-03-29-lecture.webm)
<tr id="2017-03-30" class=" lab"><th>30 Mar <br/></th><td>[location finder](lab10-wendys.html)</td><td></td><td></td></tr>

<tr id="2017-03-31" class=""><th>31 Mar <br/></th><td>polite code -- using `try`{.python} and `except`{.python} (not on exam 2)</td><td>§[17.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.17.2)</td><td> [exceptions_1.py](files/001/2017-03-31-exceptions_1.py) [exceptions_2.py](files/001/2017-03-31-exceptions_2.py) [exceptions_3.py](files/001/2017-03-31-exceptions_3.py) [exceptions_4.py](files/001/2017-03-31-exceptions_4.py) [new_csv_file.py](files/001/2017-03-31-new_csv_file.py) [url_intro_1.py](files/001/2017-03-31-url_intro_1.py) [footnotes.png](files/001/20170331a-footnotes.png) [video](screencasts/2017-03-31-lecture.webm)
<tr id="2017-04-03" class=""><th>3 Apr <br/></th><td>review</td><td></td><td>[things to know](know.html) [e2questions.py](files/001/2017-04-03-e2questions.py) [cs-prereq.png](files/001/20170403a-cs-prereq.png) [strip-split-order.png](files/001/20170403b-strip-split-order.png) [video](screencasts/2017-04-03-lecture.webm)
<tr id="2017-04-05" class="exam"><th>5 Apr </th><td>exam 2</td><td></td><td>
<tr id="2017-04-06" class=" lab"><th>6 Apr <br/></th><td>[gamebox installation](lab11-gamebox.html)</td><td></td><td></td></tr>

<tr id="2017-04-07" class=""><th>7 Apr <br/></th><td>game design with `gamebox`{.python}</td><td>[gamebox documentation](code/gamebox/gamebox.pdf)</td><td> [blankgame.py](files/001/2017-04-07-blankgame.py) [game1.py](files/001/2017-04-07-game1.py) [game2.py](files/001/2017-04-07-game2.py) [game3.py](files/001/2017-04-07-game3.py) [game4.py](files/001/2017-04-07-game4.py) [game5.py](files/001/2017-04-07-game5.py) [gamebox.png](files/001/20170407a-gamebox.png) [momentum.png](files/001/20170407b-momentum.png) [video](screencasts/2017-04-07-lecture.webm)
<tr id="2017-04-10" class=""><th>10 Apr <br/></th><td>game design with `gamebox`{.python}</td><td></td><td> [jumper1.py](files/001/2017-04-10-jumper1.py) [jumper2.py](files/001/2017-04-10-jumper2.py) [jumper3.py](files/001/2017-04-10-jumper3.py) [jumper4.py](files/001/2017-04-10-jumper4.py) [jumper.png](files/001/20170410a-jumper.png) [bounce-speed.png](files/001/20170410b-bounce-speed.png) [frames.png](files/001/20170410c-frames.png) [video](screencasts/2017-04-10-lecture.webm)
<tr id="2017-04-12" class=""><th>12 Apr <br/></th><td>game design with `gamebox`{.python}</td><td></td><td> [game_over.py](files/001/2017-04-12-game_over.py) [game_wish_list.py](files/001/2017-04-12-game_wish_list.py) [sprite_example.py](files/001/2017-04-12-sprite_example.py) [sprites.png](files/001/20170412a-sprites.png) [sprite-sheets.png](files/001/20170412c-sprite-sheets.png) [video](screencasts/2017-04-12-lecture.webm)
<tr id="2017-04-13" class=" lab"><th>13 Apr <br/></th><td>[pong](lab12-pong.html)</td><td></td><td></td></tr>

<tr id="2017-04-14" class=""><th>14 Apr <br/></th><td>regular expressions</td><td>§[25.1.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.1), §[25.1.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.3), §[25.1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.4), §[25.2.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.1), [regexr.com](http://regexr.com/)</td><td> [re_intro.py](files/001/2017-04-14-re_intro.py) [regex.png](files/001/20170414a-regex.png) [compile.png](files/001/20170414b-compile.png) [regex-guide.png](files/001/20170414c-regex-guide.png) [character-class.png](files/001/20170414d-character-class.png) [video](screencasts/2017-04-14-lecture.webm)
<tr id="2017-04-17" class=""><th>17 Apr <br/></th><td>re repetition and groups</td><td>§[25.2.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.3), §[25.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.4)</td><td> [re_intro.py](files/001/2017-04-17-re_intro.py) [charclass-review.png](files/001/20170417a-charclass-review.png) [groups.png](files/001/20170417b-groups.png) [regex-overview.png](files/001/20170417c-regex-overview.png) [matching-examples.png](files/001/20170417d-matching-examples.png) [vertical-bar.png](files/001/20170417e-vertical-bar.png) [video](screencasts/2017-04-17-lecture.webm)
<tr id="2017-04-19" class=""><th>19 Apr <br/></th><td>re building</td><td>our [building guide and example](re-tips.html)</td><td> [re_practice.py](files/001/2017-04-19-re_practice.py) [sketch.png](files/001/20170419a-sketch.png) [re-trace.png](files/001/20170419b-re-trace.png) [video](screencasts/2017-04-19-lecture.webm)
<tr id="2017-04-20" class=" lab"><th>20 Apr <br/></th><td>[email hunt](lab13-email.html)</td><td></td><td></td></tr>

<tr id="2017-04-21" class=""><th>21 Apr <br/></th><td>re replacing</td><td>§[25.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.25.4)</td><td> [re_sub.py](files/001/2017-04-21-re_sub.py) [sketch.png](files/001/20170421a-sketch.png) [elegance.png](files/001/20170421b-elegance.png) [character-classes.png](files/001/20170421c-character-classes.png) [video](screencasts/2017-04-21-lecture.webm)
<tr id="2017-04-24" class=""><th>24 Apr <br/></th><td>file writing</td><td>§[16](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.16)–[16.5.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.16.5.1), especially §[16.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.16.3); also [our writeup](16-addendum.html)</td><td> [selfdelete.py](files/001/2017-04-24-selfdelete.py) [user_info.py](files/001/2017-04-24-user_info.py) [writing_1.py](files/001/2017-04-24-writing_1.py) [writing_problem.py](files/001/2017-04-24-writing_problem.py) [sketch.png](files/001/20170424a-sketch.png) [buckets.png](files/001/20170424b-buckets.png) [buffering.png](files/001/20170424c-buffering.png) [video](screencasts/2017-04-24-lecture.webm)
<tr id="2017-04-26" class=""><th>26 Apr <br/></th><td>file writing</td><td></td><td> [read_write_csv.py](files/001/2017-04-26-read_write_csv.py) [user_info.py](files/001/2017-04-26-user_info.py) [user_info_2.py](files/001/2017-04-26-user_info_2.py) [sketch.png](files/001/20170426a-sketch.png) [modify-file-by-temporary.png](files/001/20170426b-modify-file-by-temporary.png) [video](screencasts/2017-04-26-lecture.webm)
<tr id="2017-04-27" class=" lab"><th>27 Apr <br/></th><td>[review](lab14-review.html)</td><td></td><td></td></tr>

<tr id="2017-04-28" class=""><th>28 Apr <br/></th><td>file writing wrapup, and Q&A</td><td></td><td>submit questions [here](https://docs.google.com/a/virginia.edu/forms/d/e/1FAIpQLSfUZeCfOpr04FMG9d1QdbBivgGtnpjx5Rq2wXHUAsp1huLo3g/viewform?usp=sf_link)<br/>No recording available (my audio recorder's battery died 48 seconds into lecture)<br/> [read_write_csv.py](files/001/2017-04-28-read_write_csv.py) [salary.py](files/001/2017-04-28-salary.py)
<tr id="2017-05-01" class=""><th>1 May <br/></th><td>review</td><td>[review topics](know.html)</td><td>the final exam is cumulative [salary.py](files/001/2017-05-01-salary.py) [video](screencasts/2017-05-01-lecture.webm)</tbody></table>
<table id="cal002" class="calendar">
<thead><tr><th>Monday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th></tr></thead>
<tbody><tr><td/>
<td class="day Wednesday " id="2017-01-18"><span class="date">18 Jan</span>welcome<br/>§[1.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.6), §[1.9](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.9)<br/></td>
<td class="day Thursday  lab" id="2017-01-19"><span class="date">19 Jan</span>[installing Python and PyCharm](lab01-installing.html)<br/></td>
<td class="day Friday " id="2017-01-20"><span class="date">20 Jan</span>from requirements to software<br/>§[1.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.5)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-23"><span class="date">23 Jan</span>[algorithm and ambiguity](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-algorithm.pptx)<br/>Exercises 1.1 and 1.2 from textbook<br/>inclass: [ambiguity](http://www.cs.virginia.edu/~up3f/cs1110/inclass/inclass-algorithm.html)<br/></td>
<td class="day Wednesday " id="2017-01-25"><span class="date">25 Jan</span>[pseudocode](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-pseudocode.pptx)<br/>[wikihow](http://www.wikihow.com/Write-Pseudocode)<br/>inclass: [pseudocode](http://www.cs.virginia.edu/~up3f/cs1110/inclass/inclass-algorithm-2.html)<br/></td>
<td class="day Thursday  lab" id="2017-01-26"><span class="date">26 Jan</span>[pseudocode counting squares](lab02-counting.html)<br/></td>
<td class="day Friday " id="2017-01-27"><span class="date">27 Jan</span>PyCharm<br/>§[1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.4), §[1.7](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.7)<br/>[Transition to code](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-transition-to-code.pptx), [PyCharm Quickstart](http://www.cs.virginia.edu/~up3f/cs1110/supplement/getting-start-pycharm.html)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-30"><span class="date">30 Jan</span>course overview with `turtle`{.python}, part 1<br/>[reference](https://docs.python.org/3.6/library/turtle.html), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/turtle_examples/)<br/></td>
<td class="day Wednesday " id="2017-02-01"><span class="date">1 Feb</span>course overview with `turtle`{.python}, part 2<br/>[examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/turtle_examples/)<br/><span class="special">Add deadline</span></td>
<td class="day Thursday  lab" id="2017-02-02"><span class="date">2 Feb</span>[turtle art contest](lab03-turtle.html)<br/></td>
<td class="day Friday " id="2017-02-03"><span class="date">3 Feb</span>hello, world!<br/>[revised chapter 2](revised2.2.html); §[5.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.5.2.4)--5.2.5; §[4.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.4.1)<br/>[input and output](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-input-output.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/input_output/)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-06"><span class="date">6 Feb</span>variables, values, and operators<br/>§[3](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.3) and §[4](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.4)<br/>[PythonTutor](http://pythontutor.com/visualize.html#mode=edit), [Data type overview](http://www.cs.virginia.edu/~up3f/cs1110/supplement/Data-type.html), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/variable/)<br/></td>
<td class="day Wednesday " id="2017-02-08"><span class="date">8 Feb</span>functions -- basics, `def`{.python}<br/>§[5](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.5)--5.2 and §[8](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.8)--8.2.1,<br/>[functions](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-functions.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/functions/)<br/></td>
<td class="day Thursday  lab" id="2017-02-09"><span class="date">9 Feb</span>[madlibs](lab04-madlib.html)<br/></td>
<td class="day Friday " id="2017-02-10"><span class="date">10 Feb</span>functions -- flow of control<br/>§[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-13"><span class="date">13 Feb</span>functions -- scope, `global`{.python}<br/>§[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)<br/>[functions (2)](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-functions-2.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/functions/)<br/></td>
<td class="day Wednesday " id="2017-02-15"><span class="date">15 Feb</span>decisions -- `if`{.python}, `else`{.python}, and `elif`{.python}<br/>§[6.1.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.6.1.2) and §[6.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.2)--6.2.3<br/>[decisions](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-decisions.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/decisions/)<br/></td>
<td class="day Thursday  lab" id="2017-02-16"><span class="date">16 Feb</span>[exam prep](lab05-paper.html)<br/></td>
<td class="day Friday " id="2017-02-17"><span class="date">17 Feb</span>logical operators (not on exam 1)<br/>rest of §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2<br/>**never** use §[6.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.3)'s `exit()`{.python} function; guest instructor's [lecture recording](screencasts/2017-02-17-guest-lecture.webm), [bool_type.py](files/002/bool_type.py), and [fundamental_truthiness.py](files/002/fundamental_truthiness.py)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-20"><span class="date">20 Feb</span>review<br/>§[2](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.2)--5.2, §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2.3, §[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6, §[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)<br/></td>
<td class="day Wednesday exam" id="2017-02-22"><span class="date">22 Feb</span>exam 1<br/>see [lab 5](lab05-paper.html)</td>
<td class="day Thursday  lab" id="2017-02-23"><span class="date">23 Feb</span>[oracle](lab06-magic.html)<br/></td>
<td class="day Friday " id="2017-02-24"><span class="date">24 Feb</span>code readability, elegance<br/>§[3.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.3.4), §[8.2.9](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.9)--8.2.10; skim [PEP 8](https://www.python.org/dev/peps/pep-0008/)<br/>[exercise](http://www.cs.virginia.edu/~up3f/cs1110/inclass/inclass-decisions.html), [sample solution](http://www.cs.virginia.edu/~up3f/cs1110/examples/decisions/simple_grid.txt), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-27"><span class="date">27 Feb</span>testing<br/>our own [testing writeup](testing.html)<br/>[writing test cases](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-ISP.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/testing/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Wednesday " id="2017-03-01"><span class="date">1 Mar</span>repeating with `while`{.python}<br/>§[7.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.1), §[11](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.11), §[12.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.1), §[12.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.3)<br/>[loops](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-loops.pptx), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Thursday  lab" id="2017-03-02"><span class="date">2 Mar</span>[nim](lab07-nim.html)<br/></td>
<td class="day Friday " id="2017-03-03"><span class="date">3 Mar</span>composite datatypes -- strings, ranges, lists, tuples<br/>§[10.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.4), §[11](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.11), §[12.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.1), §[12.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.3)<br/>[lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/><span class="special">Drop deadline</span></td>
</tr><tr>
<td class="day Monday noclass" id="2017-03-06"><span class="date">6 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Wednesday noclass" id="2017-03-08"><span class="date">8 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Thursday noclass lab" id="2017-03-09"><span class="date">9 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Friday noclass" id="2017-03-10"><span class="date">10 Mar</span><span class="reason">Spring recess</span></td>
</tr><tr>
<td class="day Monday " id="2017-03-13"><span class="date">13 Mar</span>iteration -- the `for`{.python} loop<br/>§[7.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.2)<br/>[loops (from slide 13)](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-loops.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/loops/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Wednesday " id="2017-03-15"><span class="date">15 Mar</span>methods and mutability -- why `list`{.python} is special<br/>§[12.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.2), §[12.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.5),<br/>[lists](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-list.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/datatype/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/><span class="special">Withdraw deadline</span></td>
<td class="day Thursday  lab" id="2017-03-16"><span class="date">16 Mar</span>[wahoo spoon](lab08-spoon.html)<br/></td>
<td class="day Friday " id="2017-03-17"><span class="date">17 Mar</span>applications of lists and strings<br/>§[10.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.6), §[12.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.4)<br/>[strings](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-string-processing.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/datatype/), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-03-20"><span class="date">20 Mar</span>debugging techniques<br/>[examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/testing/), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Wednesday " id="2017-03-22"><span class="date">22 Mar</span>flexible indices -- `dict`{.python}<br/>§[13](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.13)<br/>[dict](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-dictionaries.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/datatype/), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Thursday  lab" id="2017-03-23"><span class="date">23 Mar</span>[debugging practice](lab09-debug.html)<br/></td>
<td class="day Friday " id="2017-03-24"><span class="date">24 Mar</span>reading data -- `open`{.python} and `urllib`{.python}<br/>§[16.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.16.2), §[27.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.27.3)<br/>[file and urllib](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-file-urllib.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/file/), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-03-27"><span class="date">27 Mar</span>understanding data<br/>Wikpedia on [delimiter-separated values](https://en.wikipedia.org/wiki/Delimiter-separated_values)<br/>[file and urllib](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-file-urllib.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/file/), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Wednesday " id="2017-03-29"><span class="date">29 Mar</span>more on the data theme<br/>guest instructor; [questions.py](files/002/questions.py), [fake-queue.csv](files/fake-queue.csv), [csv_example1.py](files/002/csv_example1.py).<br/>No recording of lecture was made, but see the other section's lectures on [files and urls](screencasts/2017-03-24-lecture.webm) and [CSV](screencasts/2017-03-27-lecture.webm), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Thursday  lab" id="2017-03-30"><span class="date">30 Mar</span>[location finder](lab10-wendys.html)<br/></td>
<td class="day Friday " id="2017-03-31"><span class="date">31 Mar</span>polite code -- using `try`{.python} and `except`{.python} (not on exam 2)<br/>§[17.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.17.2)<br/>[practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-03"><span class="date">3 Apr</span>review<br/>[things to know](http://cs1110.cs.virginia.edu/know.html), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Wednesday exam" id="2017-04-05"><span class="date">5 Apr</span>exam 2</td>
<td class="day Thursday  lab" id="2017-04-06"><span class="date">6 Apr</span>[gamebox installation](lab11-gamebox.html)<br/></td>
<td class="day Friday " id="2017-04-07"><span class="date">7 Apr</span>game design with `gamebox`{.python}<br/>[gamebox documentation](code/gamebox/gamebox.pdf)<br/>[Gamebox overview](http://www.cs.virginia.edu/~up3f/cs1110/supplement/gamebox-overview.html), [examples](http://cs1110.cs.virginia.edu/code/gamebox/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-10"><span class="date">10 Apr</span>game design with `gamebox`{.python}<br/>[lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Wednesday " id="2017-04-12"><span class="date">12 Apr</span>game design with `gamebox`{.python}<br/>[animation.py](files/002/animation.py), [scrap.py](files/002/scrap.py), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Thursday  lab" id="2017-04-13"><span class="date">13 Apr</span>[pong](lab12-pong.html)<br/></td>
<td class="day Friday " id="2017-04-14"><span class="date">14 Apr</span>regular expressions<br/>§[25.1.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.1), §[25.1.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.3), §[25.1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.4), §[25.2.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.1), [regexr.com](http://regexr.com/)<br/>[regex](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-regex.pptx), [regex_example1.py](files/002/regex_example1.py), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-17"><span class="date">17 Apr</span>re repetition and groups<br/>§[25.2.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.3), §[25.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.4)<br/>[practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [regex_example2.py](files/002/regex_example2.py), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Wednesday " id="2017-04-19"><span class="date">19 Apr</span>re building<br/>our [building guide and example](re-tips.html)<br/>[practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Thursday  lab" id="2017-04-20"><span class="date">20 Apr</span>[email hunt](lab13-email.html)<br/></td>
<td class="day Friday " id="2017-04-21"><span class="date">21 Apr</span>re replacing<br/>§[25.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.25.4)<br/>[replace.py](files/002/replace_example.py), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-24"><span class="date">24 Apr</span>file writing<br/>§[16](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.16)–[16.5.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.16.5.1), especially §[16.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.16.3); also [our writeup](16-addendum.html)<br/>[file writing](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-files-2.pptx), [with_open_example.py](files/002/with_open_example.py), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Wednesday " id="2017-04-26"><span class="date">26 Apr</span>file writing<br/>[write_ex1.py](files/002/write_ex1.py), [check_file.py](files/002/check_file.py), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)<br/></td>
<td class="day Thursday  lab" id="2017-04-27"><span class="date">27 Apr</span>[review](lab14-review.html)<br/></td>
<td class="day Friday " id="2017-04-28"><span class="date">28 Apr</span>file writing<br/>[practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/) <font color='green'><i>Thanks to Layne for providing us resourceful lecture notes</i></font><br/></td>
</tr><tr>
<td class="day Monday " id="2017-05-01"><span class="date">1 May</span>review<br/>[review topics](know.html)<br/>the final exam is cumulative<br/></td>
</tr></tbody></table>
<table id="age002" class="agenda">
<thead><tr><th>Date</th><th>Topic</th><th>Reading</th><th>Notes</th></tr></thead>
<tbody>
<tr id="2017-01-18" class=""><th>18 Jan <br/></th><td>welcome</td><td>§[1.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.6), §[1.9](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.9)</td><td>
<tr id="2017-01-19" class=" lab"><th>19 Jan <br/></th><td>[installing Python and PyCharm](lab01-installing.html)</td><td></td><td></td></tr>

<tr id="2017-01-20" class=""><th>20 Jan <br/></th><td>from requirements to software</td><td>§[1.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.5)</td><td>
<tr id="2017-01-23" class=""><th>23 Jan <br/></th><td>[algorithm and ambiguity](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-algorithm.pptx)</td><td>Exercises 1.1 and 1.2 from textbook</td><td>inclass: [ambiguity](http://www.cs.virginia.edu/~up3f/cs1110/inclass/inclass-algorithm.html)
<tr id="2017-01-25" class=""><th>25 Jan <br/></th><td>[pseudocode](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-pseudocode.pptx)</td><td>[wikihow](http://www.wikihow.com/Write-Pseudocode)</td><td>inclass: [pseudocode](http://www.cs.virginia.edu/~up3f/cs1110/inclass/inclass-algorithm-2.html)
<tr id="2017-01-26" class=" lab"><th>26 Jan <br/></th><td>[pseudocode counting squares](lab02-counting.html)</td><td></td><td></td></tr>

<tr id="2017-01-27" class=""><th>27 Jan <br/></th><td>PyCharm</td><td>§[1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.4), §[1.7](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.7)</td><td>[Transition to code](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-transition-to-code.pptx), [PyCharm Quickstart](http://www.cs.virginia.edu/~up3f/cs1110/supplement/getting-start-pycharm.html)
<tr id="2017-01-30" class=""><th>30 Jan <br/></th><td>course overview with `turtle`{.python}, part 1</td><td></td><td>[reference](https://docs.python.org/3.6/library/turtle.html), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/turtle_examples/)
<tr id="2017-02-01" class=""><th>1 Feb <br/><span class="special">Add deadline</span></th><td>course overview with `turtle`{.python}, part 2</td><td></td><td>[examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/turtle_examples/)
<tr id="2017-02-02" class=" lab"><th>2 Feb <br/></th><td>[turtle art contest](lab03-turtle.html)</td><td></td><td></td></tr>

<tr id="2017-02-03" class=""><th>3 Feb <br/></th><td>hello, world!</td><td>[revised chapter 2](revised2.2.html); §[5.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.5.2.4)--5.2.5; §[4.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.4.1)</td><td>[input and output](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-input-output.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/input_output/)
<tr id="2017-02-06" class=""><th>6 Feb <br/></th><td>variables, values, and operators</td><td>§[3](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.3) and §[4](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.4)</td><td>[PythonTutor](http://pythontutor.com/visualize.html#mode=edit), [Data type overview](http://www.cs.virginia.edu/~up3f/cs1110/supplement/Data-type.html), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/variable/)
<tr id="2017-02-08" class=""><th>8 Feb <br/></th><td>functions -- basics, `def`{.python}</td><td>§[5](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.5)--5.2 and §[8](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.8)--8.2.1,</td><td>[functions](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-functions.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/functions/)
<tr id="2017-02-09" class=" lab"><th>9 Feb <br/></th><td>[madlibs](lab04-madlib.html)</td><td></td><td></td></tr>

<tr id="2017-02-10" class=""><th>10 Feb <br/></th><td>functions -- flow of control</td><td>§[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6</td><td>
<tr id="2017-02-13" class=""><th>13 Feb <br/></th><td>functions -- scope, `global`{.python}</td><td>§[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)</td><td>[functions (2)](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-functions-2.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/functions/)
<tr id="2017-02-15" class=""><th>15 Feb <br/></th><td>decisions -- `if`{.python}, `else`{.python}, and `elif`{.python}</td><td>§[6.1.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.6.1.2) and §[6.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.2)--6.2.3</td><td>[decisions](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-decisions.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/decisions/)
<tr id="2017-02-16" class=" lab"><th>16 Feb <br/></th><td>[exam prep](lab05-paper.html)</td><td></td><td></td></tr>

<tr id="2017-02-17" class=""><th>17 Feb <br/></th><td>logical operators (not on exam 1)</td><td>rest of §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2</td><td>**never** use §[6.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.3)'s `exit()`{.python} function; guest instructor's [lecture recording](screencasts/2017-02-17-guest-lecture.webm), [bool_type.py](files/002/bool_type.py), and [fundamental_truthiness.py](files/002/fundamental_truthiness.py)
<tr id="2017-02-20" class=""><th>20 Feb <br/></th><td>review</td><td>§[2](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.2)--5.2, §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2.3, §[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6, §[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)</td><td>
<tr id="2017-02-22" class="exam"><th>22 Feb </th><td>exam 1</td><td>see [lab 5](lab05-paper.html)</td><td>
<tr id="2017-02-23" class=" lab"><th>23 Feb <br/></th><td>[oracle](lab06-magic.html)</td><td></td><td></td></tr>

<tr id="2017-02-24" class=""><th>24 Feb <br/></th><td>code readability, elegance</td><td>§[3.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.3.4), §[8.2.9](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.9)--8.2.10; skim [PEP 8](https://www.python.org/dev/peps/pep-0008/)</td><td>[exercise](http://www.cs.virginia.edu/~up3f/cs1110/inclass/inclass-decisions.html), [sample solution](http://www.cs.virginia.edu/~up3f/cs1110/examples/decisions/simple_grid.txt), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-02-27" class=""><th>27 Feb <br/></th><td>testing</td><td>our own [testing writeup](testing.html)</td><td>[writing test cases](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-ISP.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/testing/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-03-01" class=""><th>1 Mar <br/></th><td>repeating with `while`{.python}</td><td>§[7.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.1), §[11](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.11), §[12.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.1), §[12.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.3)</td><td>[loops](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-loops.pptx), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-03-02" class=" lab"><th>2 Mar <br/></th><td>[nim](lab07-nim.html)</td><td></td><td></td></tr>

<tr id="2017-03-03" class=""><th>3 Mar <br/><span class="special">Drop deadline</span></th><td>composite datatypes -- strings, ranges, lists, tuples</td><td>§[10.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.4), §[11](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.11), §[12.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.1), §[12.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.3)</td><td>[lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-03-06" class="noclass"><th>6 Mar </th><td><span class="reason">Spring recess</span></td><td></td><td>
<tr id="2017-03-08" class="noclass"><th>8 Mar </th><td><span class="reason">Spring recess</span></td><td></td><td>
<tr id="2017-03-09" class="noclass lab"><th>9 Mar </th><td><span class="reason">Spring recess</span></td><td></td><td></td></tr>

<tr id="2017-03-10" class="noclass"><th>10 Mar </th><td><span class="reason">Spring recess</span></td><td></td><td>
<tr id="2017-03-13" class=""><th>13 Mar <br/></th><td>iteration -- the `for`{.python} loop</td><td>§[7.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.2)</td><td>[loops (from slide 13)](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-loops.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/loops/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-03-15" class=""><th>15 Mar <br/><span class="special">Withdraw deadline</span></th><td>methods and mutability -- why `list`{.python} is special</td><td>§[12.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.2), §[12.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.5),</td><td>[lists](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-list.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/datatype/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-03-16" class=" lab"><th>16 Mar <br/></th><td>[wahoo spoon](lab08-spoon.html)</td><td></td><td></td></tr>

<tr id="2017-03-17" class=""><th>17 Mar <br/></th><td>applications of lists and strings</td><td>§[10.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.6), §[12.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.4)</td><td>[strings](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-string-processing.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/datatype/), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-03-20" class=""><th>20 Mar <br/></th><td>debugging techniques</td><td></td><td>[examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/testing/), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-03-22" class=""><th>22 Mar <br/></th><td>flexible indices -- `dict`{.python}</td><td>§[13](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.13)</td><td>[dict](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-dictionaries.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/datatype/), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-03-23" class=" lab"><th>23 Mar <br/></th><td>[debugging practice](lab09-debug.html)</td><td></td><td></td></tr>

<tr id="2017-03-24" class=""><th>24 Mar <br/></th><td>reading data -- `open`{.python} and `urllib`{.python}</td><td>§[16.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.16.2), §[27.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.27.3)</td><td>[file and urllib](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-file-urllib.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/file/), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-03-27" class=""><th>27 Mar <br/></th><td>understanding data</td><td>Wikpedia on [delimiter-separated values](https://en.wikipedia.org/wiki/Delimiter-separated_values)</td><td>[file and urllib](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-file-urllib.pptx), [examples](http://www.cs.virginia.edu/~up3f/cs1110/examples/file/), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-03-29" class=""><th>29 Mar <br/></th><td>more on the data theme</td><td></td><td>guest instructor; [questions.py](files/002/questions.py), [fake-queue.csv](files/fake-queue.csv), [csv_example1.py](files/002/csv_example1.py).<br/>No recording of lecture was made, but see the other section's lectures on [files and urls](screencasts/2017-03-24-lecture.webm) and [CSV](screencasts/2017-03-27-lecture.webm), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-03-30" class=" lab"><th>30 Mar <br/></th><td>[location finder](lab10-wendys.html)</td><td></td><td></td></tr>

<tr id="2017-03-31" class=""><th>31 Mar <br/></th><td>polite code -- using `try`{.python} and `except`{.python} (not on exam 2)</td><td>§[17.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.17.2)</td><td>[practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-04-03" class=""><th>3 Apr <br/></th><td>review</td><td></td><td>[things to know](http://cs1110.cs.virginia.edu/know.html), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-04-05" class="exam"><th>5 Apr </th><td>exam 2</td><td></td><td>
<tr id="2017-04-06" class=" lab"><th>6 Apr <br/></th><td>[gamebox installation](lab11-gamebox.html)</td><td></td><td></td></tr>

<tr id="2017-04-07" class=""><th>7 Apr <br/></th><td>game design with `gamebox`{.python}</td><td>[gamebox documentation](code/gamebox/gamebox.pdf)</td><td>[Gamebox overview](http://www.cs.virginia.edu/~up3f/cs1110/supplement/gamebox-overview.html), [examples](http://cs1110.cs.virginia.edu/code/gamebox/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-04-10" class=""><th>10 Apr <br/></th><td>game design with `gamebox`{.python}</td><td></td><td>[lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-04-12" class=""><th>12 Apr <br/></th><td>game design with `gamebox`{.python}</td><td></td><td>[animation.py](files/002/animation.py), [scrap.py](files/002/scrap.py), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-04-13" class=" lab"><th>13 Apr <br/></th><td>[pong](lab12-pong.html)</td><td></td><td></td></tr>

<tr id="2017-04-14" class=""><th>14 Apr <br/></th><td>regular expressions</td><td>§[25.1.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.1), §[25.1.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.3), §[25.1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.4), §[25.2.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.1), [regexr.com](http://regexr.com/)</td><td>[regex](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-regex.pptx), [regex_example1.py](files/002/regex_example1.py), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-04-17" class=""><th>17 Apr <br/></th><td>re repetition and groups</td><td>§[25.2.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.3), §[25.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.4)</td><td>[practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [regex_example2.py](files/002/regex_example2.py), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-04-19" class=""><th>19 Apr <br/></th><td>re building</td><td>our [building guide and example](re-tips.html)</td><td>[practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-04-20" class=" lab"><th>20 Apr <br/></th><td>[email hunt](lab13-email.html)</td><td></td><td></td></tr>

<tr id="2017-04-21" class=""><th>21 Apr <br/></th><td>re replacing</td><td>§[25.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.25.4)</td><td>[replace.py](files/002/replace_example.py), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-04-24" class=""><th>24 Apr <br/></th><td>file writing</td><td>§[16](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.16)–[16.5.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.16.5.1), especially §[16.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.16.3); also [our writeup](16-addendum.html)</td><td>[file writing](http://www.cs.virginia.edu/~up3f/cs1110/slides/1110-files-2.pptx), [with_open_example.py](files/002/with_open_example.py), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-04-26" class=""><th>26 Apr <br/></th><td>file writing</td><td></td><td>[write_ex1.py](files/002/write_ex1.py), [check_file.py](files/002/check_file.py), [practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/)
<tr id="2017-04-27" class=" lab"><th>27 Apr <br/></th><td>[review](lab14-review.html)</td><td></td><td></td></tr>

<tr id="2017-04-28" class=""><th>28 Apr <br/></th><td>file writing</td><td></td><td>[practice-of-the-day](http://www.cs.virginia.edu/~up3f/cs1110/practice-of-the-day/), [lecture-note by Virginia Layne Berry](http://www.cs.virginia.edu/~up3f/cs1110/lecture-note/) <font color='green'><i>Thanks to Layne for providing us resourceful lecture notes</i></font>
<tr id="2017-05-01" class=""><th>1 May <br/></th><td>review</td><td>[review topics](know.html)</td><td>the final exam is cumulative</tbody></table>
<table id="cal1111" class="calendar">
<thead><tr><th>Monday</th><th>Wednesday</th></tr></thead>
<tbody><tr><td/>
<td class="day Wednesday " id="2017-01-18"><span class="date">18 Jan</span>welcome<br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-23"><span class="date">23 Jan</span>Algorithms & pseudocode<br/></td>
<td class="day Wednesday " id="2017-01-25"><span class="date">25 Jan</span>Algorithms & pseudocode<br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-30"><span class="date">30 Jan</span>Turtle & number conversion<br/></td>
<td class="day Wednesday " id="2017-02-01"><span class="date">1 Feb</span>Computer system architecture<br/><span class="special">Add deadline</span></td>
</tr><tr>
<td class="day Monday " id="2017-02-06"><span class="date">6 Feb</span>Basic functions<br/></td>
<td class="day Wednesday " id="2017-02-08"><span class="date">8 Feb</span>Functions<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-13"><span class="date">13 Feb</span>Variable scope<br/></td>
<td class="day Wednesday " id="2017-02-15"><span class="date">15 Feb</span>Decisions if elif<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-20"><span class="date">20 Feb</span>Review<br/></td>
<td class="day Wednesday exam" id="2017-02-22"><span class="date">22 Feb</span>Exam 1</td>
</tr><tr>
<td class="day Monday " id="2017-02-27"><span class="date">27 Feb</span>Testing<br/></td>
<td class="day Wednesday " id="2017-03-01"><span class="date">1 Mar</span>Repetition<br/></td>
</tr><tr>
<td class="day Monday noclass" id="2017-03-06"><span class="date">6 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Wednesday noclass" id="2017-03-08"><span class="date">8 Mar</span><span class="reason">Spring recess</span></td>
</tr><tr>
<td class="day Monday " id="2017-03-13"><span class="date">13 Mar</span>String operations<br/></td>
<td class="day Wednesday " id="2017-03-15"><span class="date">15 Mar</span>String methods/Lists<br/><span class="special">Withdraw deadline</span></td>
</tr><tr>
<td class="day Monday " id="2017-03-20"><span class="date">20 Mar</span>Lists<br/></td>
<td class="day Wednesday " id="2017-03-22"><span class="date">22 Mar</span>Dicts<br/></td>
</tr><tr>
<td class="day Monday " id="2017-03-27"><span class="date">27 Mar</span>Files<br/></td>
<td class="day Wednesday " id="2017-03-29"><span class="date">29 Mar</span>Urllib<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-03"><span class="date">3 Apr</span>Exceptions/review<br/></td>
<td class="day Wednesday exam" id="2017-04-05"><span class="date">5 Apr</span>Exam 2</td>
</tr><tr>
<td class="day Monday " id="2017-04-10"><span class="date">10 Apr</span>Regular expressions<br/></td>
<td class="day Wednesday " id="2017-04-12"><span class="date">12 Apr</span>Regular expressions<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-17"><span class="date">17 Apr</span>game design with `gamebox`{.python}<br/></td>
<td class="day Wednesday " id="2017-04-19"><span class="date">19 Apr</span>game design with `gamebox`{.python}<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-24"><span class="date">24 Apr</span>image manipulation with `pillow`{.python}<br/></td>
<td class="day Wednesday " id="2017-04-26"><span class="date">26 Apr</span>image manipulation with `pillow`{.python}<br/></td>
</tr><tr>
<td class="day Monday " id="2017-05-01"><span class="date">1 May</span>review<br/></td>
</tr></tbody></table>
<table id="age1111" class="agenda">
<thead><tr><th>Date</th><th>Topic</th></tr></thead>
<tbody>
<tr id="2017-01-18" class=""><th>18 Jan <br/></th><td>welcome
<tr id="2017-01-23" class=""><th>23 Jan <br/></th><td>Algorithms & pseudocode
<tr id="2017-01-25" class=""><th>25 Jan <br/></th><td>Algorithms & pseudocode
<tr id="2017-01-30" class=""><th>30 Jan <br/></th><td>Turtle & number conversion
<tr id="2017-02-01" class=""><th>1 Feb <br/><span class="special">Add deadline</span></th><td>Computer system architecture
<tr id="2017-02-06" class=""><th>6 Feb <br/></th><td>Basic functions
<tr id="2017-02-08" class=""><th>8 Feb <br/></th><td>Functions
<tr id="2017-02-13" class=""><th>13 Feb <br/></th><td>Variable scope
<tr id="2017-02-15" class=""><th>15 Feb <br/></th><td>Decisions if elif
<tr id="2017-02-20" class=""><th>20 Feb <br/></th><td>Review
<tr id="2017-02-22" class="exam"><th>22 Feb </th><td>Exam 1
<tr id="2017-02-27" class=""><th>27 Feb <br/></th><td>Testing
<tr id="2017-03-01" class=""><th>1 Mar <br/></th><td>Repetition
<tr id="2017-03-06" class="noclass"><th>6 Mar </th><td><span class="reason">Spring recess</span>
<tr id="2017-03-08" class="noclass"><th>8 Mar </th><td><span class="reason">Spring recess</span>
<tr id="2017-03-13" class=""><th>13 Mar <br/></th><td>String operations
<tr id="2017-03-15" class=""><th>15 Mar <br/><span class="special">Withdraw deadline</span></th><td>String methods/Lists
<tr id="2017-03-20" class=""><th>20 Mar <br/></th><td>Lists
<tr id="2017-03-22" class=""><th>22 Mar <br/></th><td>Dicts
<tr id="2017-03-27" class=""><th>27 Mar <br/></th><td>Files
<tr id="2017-03-29" class=""><th>29 Mar <br/></th><td>Urllib
<tr id="2017-04-03" class=""><th>3 Apr <br/></th><td>Exceptions/review
<tr id="2017-04-05" class="exam"><th>5 Apr </th><td>Exam 2
<tr id="2017-04-10" class=""><th>10 Apr <br/></th><td>Regular expressions
<tr id="2017-04-12" class=""><th>12 Apr <br/></th><td>Regular expressions
<tr id="2017-04-17" class=""><th>17 Apr <br/></th><td>game design with `gamebox`{.python}
<tr id="2017-04-19" class=""><th>19 Apr <br/></th><td>game design with `gamebox`{.python}
<tr id="2017-04-24" class=""><th>24 Apr <br/></th><td>image manipulation with `pillow`{.python}
<tr id="2017-04-26" class=""><th>26 Apr <br/></th><td>image manipulation with `pillow`{.python}
<tr id="2017-05-01" class=""><th>1 May <br/></th><td>review</tbody></table>
<script>rehide()</script>

<hr/>

Per <a href="http://www.virginia.edu/registrar/exams.html#1172">the registrar</a>, all sections of 1110 and 1111 will have their final exam at 7--10 pm on Thursday, 11 May 2017.

1110-001
:   Gilmer 130

1110-002
:   Phys 203

1111-001
:   Rice 130

Conflicts with that time will be resolved the following day (Friday 12 May) at 10 am, location sent via email.
No permission to take the exam earlier than 11 May or from off of UVA grounds will be granted without Deans' office request.

<!-- You may report conflicts and request accomodations at <https://goo.gl/forms/hC5oRY2zJoVfQz023>. -->

TA-led review sessions will be held in Chem 402 on Sunday, 7 May at 7pm and on Wednesday, 10 May at 1pm.

