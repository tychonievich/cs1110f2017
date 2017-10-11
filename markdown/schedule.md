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
.day a, .agenda tbody tr td a { border: thin solid #f5f5f5; }
</style>
<script>
function rehide(e) {
        var hash=window.location.hash;
        if (e) hash = e;
        if (typeof(hash) != "string") return;
        console.log("hash = " + hash);
        var elems = ['cal1110', 'cal1111', 'age1110', 'age1111'];
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

<a id="acal1110" class="button" href="#cal1110" onclick="rehide('cal1110')">1110 Calendar</a>
<a id="aage1110" class="button" href="#age1110" onclick="rehide('age1110')">1110 Agenda</a>
<a id="acal1111" class="button" href="#cal1111" onclick="rehide('cal1111')">1111 Calendar</a>
<a id="aage1111" class="button" href="#age1111" onclick="rehide('age1111')">1111 Agenda</a>

<hr/>

Note: assignments and their due dates are listed on the [assignments page](assignments.html), not on this page.


<table id="cal1110" class="calendar">
<thead><tr><th>Monday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th></tr></thead>
<tbody><tr><td/>
<td class="day Wednesday " id="2017-08-23"><span class="date">23 Aug</span>welcome<br/>§[1.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.6), §[1.9](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.9)<br/> [10am qa.txt](files/1110/2017-08-23-1000-qa.txt) [2pm qa.txt](files/1110/2017-08-23-1400-qa.txt) [10am video](screencasts/2017-08-23-1000.webm) [2pm audio](screencasts/2017-08-23-1400.mp3)<br/></td>
<td class="day Thursday  lab" id="2017-08-24"><span class="date">24 Aug</span>[installing Python and PyCharm](lab01-installing.html)<br/></td>
<td class="day Friday " id="2017-08-25"><span class="date">25 Aug</span>from requirements to software<br/>§[1.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.5)<br/> [10am slides.pdf](files/1110/2017-08-25-1000-slides.pdf) [2pm slides.pdf](files/1110/2017-08-25-1400-slides.pdf) [10am video](screencasts/2017-08-25-1000.webm) [2pm video](screencasts/2017-08-25-1400.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-08-28"><span class="date">28 Aug</span>ambiguity<br/>Exercises 1.1 and 1.2 from textbook<br/> [10am slides.pdf](files/1110/2017-08-28-1000-slides.pdf) [2pm slides.pdf](files/1110/2017-08-28-1400-slides.pdf) [10am video](screencasts/2017-08-28-1000.webm) [2pm video](screencasts/2017-08-28-1400.webm)<br/></td>
<td class="day Wednesday " id="2017-08-30"><span class="date">30 Aug</span>pseudocode<br/>[wikihow](http://www.wikihow.com/Write-Pseudocode)<br/>the 10am lecture wasn't recorded; use 2pm instead [10am 01-sequence.txt](files/1110/2017-08-30-1000-01-sequence.txt) [10am 02-selection.txt](files/1110/2017-08-30-1000-02-selection.txt) [10am 03-iteration.txt](files/1110/2017-08-30-1000-03-iteration.txt) [10am 04-declaration.txt](files/1110/2017-08-30-1000-04-declaration.txt) [10am 05-update.txt](files/1110/2017-08-30-1000-05-update.txt) [2pm 01-sequence.txt](files/1110/2017-08-30-1400-01-sequence.txt) [2pm 02-selection.txt](files/1110/2017-08-30-1400-02-selection.txt) [2pm 03-iteration.txt](files/1110/2017-08-30-1400-03-iteration.txt) [2pm 04-declaration.txt](files/1110/2017-08-30-1400-04-declaration.txt) [2pm 05-update.txt](files/1110/2017-08-30-1400-05-update.txt) [2pm slides.pdf](files/1110/2017-08-30-1400-slides.pdf) [2pm video](screencasts/2017-08-30-1400.webm)<br/></td>
<td class="day Thursday  lab" id="2017-08-31"><span class="date">31 Aug</span>[pseudocode counting squares](lab02-counting.html)<br/></td>
<td class="day Friday " id="2017-09-01"><span class="date">1 Sep</span>PyCharm<br/>§[1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.4), §[1.7](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.7)<br/>[demo.py](files/001/demo.py) [10am demo.py](files/1110/2017-09-01-1000-demo.py) [10am slides.pdf](files/1110/2017-09-01-1000-slides.pdf) [2pm demo.py](files/1110/2017-09-01-1400-demo.py) [2pm example.py](files/1110/2017-09-01-1400-example.py) [2pm my_math_rules.py](files/1110/2017-09-01-1400-my_math_rules.py) [2pm slides.pdf](files/1110/2017-09-01-1400-slides.pdf) [10am video](screencasts/2017-09-01-1000.webm) [2pm video](screencasts/2017-09-01-1400.webm) [2pm video](screencasts/2017-09-01-1400.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-09-04"><span class="date">4 Sep</span>course overview with `turtle`{.python}, part 1<br/> [10am about_for.py](files/1110/2017-09-04-1000-about_for.py) [10am slides.pdf](files/1110/2017-09-04-1000-slides.pdf) [10am turtle_square.py](files/1110/2017-09-04-1000-turtle_square.py) [10am turtle_with_brush.py](files/1110/2017-09-04-1000-turtle_with_brush.py) [2pm for_explainer.py](files/1110/2017-09-04-1400-for_explainer.py) [2pm slides.pdf](files/1110/2017-09-04-1400-slides.pdf) [2pm turtle_paint.py](files/1110/2017-09-04-1400-turtle_paint.py) [2pm turtle_square.py](files/1110/2017-09-04-1400-turtle_square.py) [10am video](screencasts/2017-09-04-1000.webm) [2pm video](screencasts/2017-09-04-1400.webm)<br/></td>
<td class="day Wednesday " id="2017-09-06"><span class="date">6 Sep</span>course overview with `turtle`{.python}, part 2<br/> [10am big_turtle_race.py](files/1110/2017-09-06-1000-big_turtle_race.py) [10am sierpinski_tri.py](files/1110/2017-09-06-1000-sierpinski_tri.py) [10am slides.pdf](files/1110/2017-09-06-1000-slides.pdf) [10am turtle_race.py](files/1110/2017-09-06-1000-turtle_race.py) [10am turtle_square.py](files/1110/2017-09-06-1000-turtle_square.py) [2pm big_turtle_race.py](files/1110/2017-09-06-1400-big_turtle_race.py) [2pm for_explainer.py](files/1110/2017-09-06-1400-for_explainer.py) [2pm sierpinski.py](files/1110/2017-09-06-1400-sierpinski.py) [2pm slides.pdf](files/1110/2017-09-06-1400-slides.pdf) [2pm turtle_race.py](files/1110/2017-09-06-1400-turtle_race.py) [10am video](screencasts/2017-09-06-1000.webm) [2pm video](screencasts/2017-09-06-1400.webm)<br/><span class="special">Add deadline</span></td>
<td class="day Thursday  lab" id="2017-09-07"><span class="date">7 Sep</span>[turtle art contest](lab03-turtle.html)<br/></td>
<td class="day Friday " id="2017-09-08"><span class="date">8 Sep</span>hello, world!<br/>[revised chapter 2](revised2.2.html); §[5.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.5.2.4)--5.2.5; §[4.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.4.1)<br/>[PythonTutor](http://pythontutor.com/) [10am get_input.py](files/1110/2017-09-08-1000-get_input.py) [10am print_test.py](files/1110/2017-09-08-1000-print_test.py) [10am python_variable.py](files/1110/2017-09-08-1000-python_variable.py) [10am slides.pdf](files/1110/2017-09-08-1000-slides.pdf) [2pm math_string.py](files/1110/2017-09-08-1400-math_string.py) [2pm python_variable.py](files/1110/2017-09-08-1400-python_variable.py) [2pm slides.pdf](files/1110/2017-09-08-1400-slides.pdf) [2pm using_print.py](files/1110/2017-09-08-1400-using_print.py) [10am video](screencasts/2017-09-08-1000.webm) [2pm video](screencasts/2017-09-08-1400.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-09-11"><span class="date">11 Sep</span>variables, values, and operators<br/>§[3](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.3) and §[4](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.4)<br/> [10am assign_test.py](files/1110/2017-09-11-1000-assign_test.py) [10am float_is_strange.py](files/1110/2017-09-11-1000-float_is_strange.py) [10am function_type.py](files/1110/2017-09-11-1000-function_type.py) [10am get_input.py](files/1110/2017-09-11-1000-get_input.py) [10am print_test.py](files/1110/2017-09-11-1000-print_test.py) [10am python_variable.py](files/1110/2017-09-11-1000-python_variable.py) [10am slides.pdf](files/1110/2017-09-11-1000-slides.pdf) [10am you_are_young.py](files/1110/2017-09-11-1000-you_are_young.py) [2pm age_liar.py](files/1110/2017-09-11-1400-age_liar.py) [2pm float_is_strange.py](files/1110/2017-09-11-1400-float_is_strange.py) [2pm func_intro.py](files/1110/2017-09-11-1400-func_intro.py) [2pm slides.pdf](files/1110/2017-09-11-1400-slides.pdf) [2pm variable_test.py](files/1110/2017-09-11-1400-variable_test.py) [10am video](screencasts/2017-09-11-1000.webm) [2pm video](screencasts/2017-09-11-1400.webm)<br/></td>
<td class="day Wednesday " id="2017-09-13"><span class="date">13 Sep</span>functions -- basics, `def`{.python}<br/>§[5](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.5)--5.2 and §[8](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.8)--8.2.1<br/>Typo in 10am slides: `'hi' < 'bye'`{.python} is `False`{.python}, not `True`{.python} [10am first_functions.py](files/1110/2017-09-13-1000-first_functions.py) [10am len_and_raound.py](files/1110/2017-09-13-1000-len_and_raound.py) [10am slides.pdf](files/1110/2017-09-13-1000-slides.pdf) [10am testing_functions.py](files/1110/2017-09-13-1000-testing_functions.py) [10am use_first_functions.py](files/1110/2017-09-13-1000-use_first_functions.py) [10am you_are_young.py](files/1110/2017-09-13-1000-you_are_young.py) [2pm first_functions.py](files/1110/2017-09-13-1400-first_functions.py) [2pm len_and_round.py](files/1110/2017-09-13-1400-len_and_round.py) [2pm slides.pdf](files/1110/2017-09-13-1400-slides.pdf) [2pm use_first_functions.py](files/1110/2017-09-13-1400-use_first_functions.py) [10am video](screencasts/2017-09-13-1000.webm) [2pm video](screencasts/2017-09-13-1400.webm)<br/></td>
<td class="day Thursday  lab" id="2017-09-14"><span class="date">14 Sep</span>[madlibs](lab04-madlib.html)<br/></td>
<td class="day Friday " id="2017-09-15"><span class="date">15 Sep</span>functions -- flow of control<br/>§[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6<br/> [10am func_tangle.py](files/1110/2017-09-15-1000-func_tangle.py) [10am get.py](files/1110/2017-09-15-1000-get.py) [10am page_to_read.py](files/1110/2017-09-15-1000-page_to_read.py) [10am poly_func.py](files/1110/2017-09-15-1000-poly_func.py) [10am slides.pdf](files/1110/2017-09-15-1000-slides.pdf) [2pm following_functions.py](files/1110/2017-09-15-1400-following_functions.py) [2pm func_puzzle.py](files/1110/2017-09-15-1400-func_puzzle.py) [2pm get.py](files/1110/2017-09-15-1400-get.py) [2pm read_pages.py](files/1110/2017-09-15-1400-read_pages.py) [2pm slides.pdf](files/1110/2017-09-15-1400-slides.pdf) [10am video](screencasts/2017-09-15-1000.webm) [2pm video](screencasts/2017-09-15-1400.webm) [2pm video](screencasts/2017-09-15-1400.webm) [2pm video](screencasts/2017-09-15-1400.webm) [2pm video](screencasts/2017-09-15-1400.webm) [2pm video](screencasts/2017-09-15-1400.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-09-18"><span class="date">18 Sep</span>functions -- scope, `global`{.python}<br/>§[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)<br/> [10am following_functions.py](files/1110/2017-09-18-1000-following_functions.py) [10am func_swap.py](files/1110/2017-09-18-1000-func_swap.py) [10am play_with_scope.py](files/1110/2017-09-18-1000-play_with_scope.py) [10am slides.pdf](files/1110/2017-09-18-1000-slides.pdf) [2pm following_functions.py](files/1110/2017-09-18-1400-following_functions.py) [2pm get.py](files/1110/2017-09-18-1400-get.py) [2pm scope_quiz.py](files/1110/2017-09-18-1400-scope_quiz.py) [2pm slides.pdf](files/1110/2017-09-18-1400-slides.pdf) [10am video](screencasts/2017-09-18-1000.webm) [2pm video](screencasts/2017-09-18-1400.webm)<br/></td>
<td class="day Wednesday " id="2017-09-20"><span class="date">20 Sep</span>decisions -- `if`{.python}, `elif`{.python}, and `else`{.python}<br/>§[6.1.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.6.1.2) and §[6.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.2)--6.2.3<br/> [10am age_classifier.py](files/1110/2017-09-20-1000-age_classifier.py) [10am if_func.py](files/1110/2017-09-20-1000-if_func.py) [10am if_intro.py](files/1110/2017-09-20-1000-if_intro.py) [10am slides.pdf](files/1110/2017-09-20-1000-slides.pdf) [2pm if_func.py](files/1110/2017-09-20-1400-if_func.py) [2pm if_intro.py](files/1110/2017-09-20-1400-if_intro.py) [2pm slides.pdf](files/1110/2017-09-20-1400-slides.pdf) [10am video](screencasts/2017-09-20-1000.webm) [2pm video](screencasts/2017-09-20-1400.webm)<br/></td>
<td class="day Thursday  lab" id="2017-09-21"><span class="date">21 Sep</span>[exam prep](lab05-paper.html)<br/></td>
<td class="day Friday " id="2017-09-22"><span class="date">22 Sep</span>decisions -- logical operators<br/>rest of §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2<br/>**never** use §[6.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.3)'s `exit()`{.python} function [10am if_and_things.py](files/1110/2017-09-22-1000-if_and_things.py) [10am if_func.py](files/1110/2017-09-22-1000-if_func.py) [10am slides.pdf](files/1110/2017-09-22-1000-slides.pdf) [10am truthiness.py](files/1110/2017-09-22-1000-truthiness.py) [2pm bad_booleans.py](files/1110/2017-09-22-1400-bad_booleans.py) [2pm if_func.py](files/1110/2017-09-22-1400-if_func.py) [2pm if_things.py](files/1110/2017-09-22-1400-if_things.py) [2pm slides.pdf](files/1110/2017-09-22-1400-slides.pdf) [10am video](screencasts/2017-09-22-1000.webm) [2pm video](screencasts/2017-09-22-1400.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-09-25"><span class="date">25 Sep</span>review<br/>§[2](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.2)--5.2, §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2.3, §[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6, §[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)<br/> [10am exam1-prep.py](files/1110/2017-09-25-1000-exam1-prep.py) [10am slides.pdf](files/1110/2017-09-25-1000-slides.pdf) [2pm exam1_review.py](files/1110/2017-09-25-1400-exam1_review.py) [2pm slides.pdf](files/1110/2017-09-25-1400-slides.pdf) [10am video](screencasts/2017-09-25-1000.webm) [2pm video](screencasts/2017-09-25-1400.webm)<br/></td>
<td class="day Wednesday exam" id="2017-09-27"><span class="date">27 Sep</span>exam 1<br/>the [exam](files/f2017e1.pdf), [key](https://piazza.com/class/j6m7hyps7tx66x?cid=135), and [TPEGS](https://tpegs.cs.virginia.edu/)</td>
<td class="day Thursday  lab" id="2017-09-28"><span class="date">28 Sep</span>[strings](lab06-strpuz.html)<br/></td>
<td class="day Friday " id="2017-09-29"><span class="date">29 Sep</span>code readability, elegance<br/>§[3.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.3.4), §[8.2.9](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.9)--8.2.10; skim [PEP 8](https://www.python.org/dev/peps/pep-0008/)<br/> [10am input_print_return.py](files/1110/2017-09-29-1000-input_print_return.py) [10am on_naming.py](files/1110/2017-09-29-1000-on_naming.py) [10am play_with_scope.py](files/1110/2017-09-29-1000-play_with_scope.py) [10am slides.pdf](files/1110/2017-09-29-1000-slides.pdf) [10am stylish_functions.py](files/1110/2017-09-29-1000-stylish_functions.py) [2pm func_style.py](files/1110/2017-09-29-1400-func_style.py) [2pm koan.py](files/1110/2017-09-29-1400-koan.py) [2pm readability.py](files/1110/2017-09-29-1400-readability.py) [2pm scope_quiz.py](files/1110/2017-09-29-1400-scope_quiz.py) [2pm slides.pdf](files/1110/2017-09-29-1400-slides.pdf) [10am video](screencasts/2017-09-29-1000.webm) [2pm video](screencasts/2017-09-29-1400.webm) [2pm video](screencasts/2017-09-29-1400.webm)<br/></td>
</tr><tr>
<td class="day Monday noclass" id="2017-10-02"><span class="date">2 Oct</span><span class="reason">Reading Days</span></td>
<td class="day Wednesday " id="2017-10-04"><span class="date">4 Oct</span>testing<br/>our own [testing writeup](testing.html)<br/> [10am pow_test_func.py](files/1110/2017-10-04-1000-pow_test_func.py) [10am slides.pdf](files/1110/2017-10-04-1000-slides.pdf) [10am test_pow.py](files/1110/2017-10-04-1000-test_pow.py) [2pm func_test_funcs.py](files/1110/2017-10-04-1400-func_test_funcs.py) [2pm slides.pdf](files/1110/2017-10-04-1400-slides.pdf) [2pm test_pow.py](files/1110/2017-10-04-1400-test_pow.py) [10am video](screencasts/2017-10-04-1000.webm) [2pm video](screencasts/2017-10-04-1400.webm)<br/></td>
<td class="day Thursday  lab" id="2017-10-05"><span class="date">5 Oct</span>[hangman](lab07-hangman.html)<br/></td>
<td class="day Friday " id="2017-10-06"><span class="date">6 Oct</span>repeating with `while`{.python}<br/>§[7.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.1)<br/> [10am hangman.py](files/1110/2017-10-06-1000-hangman.py) [10am hangman2.py](files/1110/2017-10-06-1000-hangman2.py) [10am input_validation.py](files/1110/2017-10-06-1000-input_validation.py) [10am making_a_while.py](files/1110/2017-10-06-1000-making_a_while.py) [10am slides.pdf](files/1110/2017-10-06-1000-slides.pdf) [10am while_examples.py](files/1110/2017-10-06-1000-while_examples.py) [2pm about_while.py](files/1110/2017-10-06-1400-about_while.py) [2pm func_test_funcs.py](files/1110/2017-10-06-1400-func_test_funcs.py) [2pm hangman.py](files/1110/2017-10-06-1400-hangman.py) [2pm hangman2.py](files/1110/2017-10-06-1400-hangman2.py) [2pm how_to_write_loops.py](files/1110/2017-10-06-1400-how_to_write_loops.py) [2pm slides.pdf](files/1110/2017-10-06-1400-slides.pdf) [2pm validate_input.py](files/1110/2017-10-06-1400-validate_input.py) [10am video](screencasts/2017-10-06-1000.webm) [10am video](screencasts/2017-10-06-1000.webm) [2pm video](screencasts/2017-10-06-1400.webm)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-10-09"><span class="date">9 Oct</span>composite datatypes -- strings, ranges, lists, tuples<br/>§[10.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.4), §[11](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.11), §[12.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.1), §[12.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.3)<br/> [10am collections_intro.py](files/1110/2017-10-09-1000-collections_intro.py) [10am loop_over_collections.py](files/1110/2017-10-09-1000-loop_over_collections.py) [10am slides.pdf](files/1110/2017-10-09-1000-slides.pdf) [2pm collections_intro.py](files/1110/2017-10-09-1400-collections_intro.py) [2pm hangman2.py](files/1110/2017-10-09-1400-hangman2.py) [2pm slides.pdf](files/1110/2017-10-09-1400-slides.pdf) [10am video](screencasts/2017-10-09-1000.webm) [2pm video](screencasts/2017-10-09-1400.webm)<br/><span class="special">Drop deadline</span></td>
<td class="day Wednesday " id="2017-10-11"><span class="date">11 Oct</span>iteration -- the `for`{.python} loop<br/>§[7.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.2)<br/> [10am basic_iteration.py](files/1110/2017-10-11-1000-basic_iteration.py) [10am in_range.py](files/1110/2017-10-11-1000-in_range.py) [10am lists_1.py](files/1110/2017-10-11-1000-lists_1.py) [10am nested_loops.py](files/1110/2017-10-11-1000-nested_loops.py) [10am slides.pdf](files/1110/2017-10-11-1000-slides.pdf) [2pm basic_iteration.py](files/1110/2017-10-11-1400-basic_iteration.py) [2pm following_functions.py](files/1110/2017-10-11-1400-following_functions.py) [2pm func_style.py](files/1110/2017-10-11-1400-func_style.py) [2pm loop_index.py](files/1110/2017-10-11-1400-loop_index.py) [2pm more_iterations.py](files/1110/2017-10-11-1400-more_iterations.py) [2pm nest_loops.py](files/1110/2017-10-11-1400-nest_loops.py) [2pm slides.pdf](files/1110/2017-10-11-1400-slides.pdf) [10am video](screencasts/2017-10-11-1000.webm)<br/></td>
<td class="day Thursday  lab" id="2017-10-12"><span class="date">12 Oct</span>[old cryptography](lab08-crypto.html)<br/></td>
<td class="day Friday " id="2017-10-13"><span class="date">13 Oct</span>methods and mutability -- why `list`{.python} is special<br/>§[12.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.2), §[12.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.5),<br/></td>
</tr><tr>
<td class="day Monday " id="2017-10-16"><span class="date">16 Oct</span>applications of lists and strings<br/>§[10.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.6), §[12.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.4)<br/><span class="special">Withdraw deadline</span></td>
<td class="day Wednesday " id="2017-10-18"><span class="date">18 Oct</span>debugging techniques<br/>[buggy code](files/001/spoon.py)<br/></td>
<td class="day Thursday  lab" id="2017-10-19"><span class="date">19 Oct</span>[debugging](lab09-debug.html)<br/></td>
<td class="day Friday " id="2017-10-20"><span class="date">20 Oct</span>flexible indices -- `dict`{.python}<br/>§[13](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.13)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-10-23"><span class="date">23 Oct</span>reading data -- `open`{.python} and `urllib`{.python}<br/>§[16.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.16.2), §[27.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.27.3)<br/></td>
<td class="day Wednesday " id="2017-10-25"><span class="date">25 Oct</span>understanding data<br/>Wikpedia on [delimiter-separated values](https://en.wikipedia.org/wiki/Delimiter-separated_values)<br/>[vastats.csv](files/vastats.csv)<br/></td>
<td class="day Thursday  lab" id="2017-10-26"><span class="date">26 Oct</span>[point-of-interest location](lab10-wendys.html)<br/></td>
<td class="day Friday " id="2017-10-27"><span class="date">27 Oct</span>more on the data theme<br/></td>
</tr><tr>
<td class="day Monday " id="2017-10-30"><span class="date">30 Oct</span>review<br/></td>
<td class="day Wednesday exam" id="2017-11-01"><span class="date">1 Nov</span>exam 2</td>
<td class="day Thursday  lab" id="2017-11-02"><span class="date">2 Nov</span>[gamebox installation](lab11-gamebox.html)<br/></td>
<td class="day Friday " id="2017-11-03"><span class="date">3 Nov</span>polite code -- using `try`{.python} and `except`{.python} (not on exam 2)<br/>§[17.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.17.2)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-11-06"><span class="date">6 Nov</span>game design with `gamebox`{.python}<br/>[gamebox documentation](code/gamebox/gamebox.pdf)<br/></td>
<td class="day Wednesday " id="2017-11-08"><span class="date">8 Nov</span>game design with `gamebox`{.python}<br/></td>
<td class="day Thursday  lab" id="2017-11-09"><span class="date">9 Nov</span><br/></td>
<td class="day Friday " id="2017-11-10"><span class="date">10 Nov</span>game design with `gamebox`{.python}<br/></td>
</tr><tr>
<td class="day Monday " id="2017-11-13"><span class="date">13 Nov</span>regular expressions<br/>§[25.1.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.1), §[25.1.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.3), §[25.1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.4), §[25.2.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.1), [pythex.org](//https://pythex.org/)<br/></td>
<td class="day Wednesday " id="2017-11-15"><span class="date">15 Nov</span>re repetition and groups<br/>§[25.2.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.3), §[25.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.4)<br/></td>
<td class="day Thursday  lab" id="2017-11-16"><span class="date">16 Nov</span><br/></td>
<td class="day Friday " id="2017-11-17"><span class="date">17 Nov</span>re building<br/>our [building guide and example](re-tips.html)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-11-20"><span class="date">20 Nov</span>re replacing<br/>§[25.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.25.4)<br/></td>
<td class="day Wednesday noclass" id="2017-11-22"><span class="date">22 Nov</span><span class="reason">Thanksgiving break</span></td>
<td class="day Thursday noclass lab" id="2017-11-23"><span class="date">23 Nov</span><span class="reason">Thanksgiving break</span></td>
<td class="day Friday noclass" id="2017-11-24"><span class="date">24 Nov</span><span class="reason">Thanksgiving break</span></td>
</tr><tr>
<td class="day Monday " id="2017-11-27"><span class="date">27 Nov</span>varies by section<br/></td>
<td class="day Wednesday " id="2017-11-29"><span class="date">29 Nov</span>varies by section<br/></td>
<td class="day Thursday  lab" id="2017-11-30"><span class="date">30 Nov</span><br/></td>
<td class="day Friday " id="2017-12-01"><span class="date">1 Dec</span>varies by section<br/></td>
</tr><tr>
<td class="day Monday " id="2017-12-04"><span class="date">4 Dec</span>review<br/>[review topics](know.html)<br/>the final exam is cumulative<br/></td>
</tr></tbody></table>
<table id="age1110" class="agenda">
<thead><tr><th>Date</th><th>Topic</th><th>Reading</th><th>Notes</th></tr></thead>
<tbody>
<tr id="2017-08-23" class=""><th>23 Aug <br/></th><td>welcome</td><td>§[1.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.6), §[1.9](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.9)</td><td> [10am qa.txt](files/1110/2017-08-23-1000-qa.txt) [2pm qa.txt](files/1110/2017-08-23-1400-qa.txt) [10am video](screencasts/2017-08-23-1000.webm) [2pm audio](screencasts/2017-08-23-1400.mp3)
<tr id="2017-08-24" class=" lab"><th>24 Aug <br/></th><td>[installing Python and PyCharm](lab01-installing.html)</td><td></td><td></td></tr>

<tr id="2017-08-25" class=""><th>25 Aug <br/></th><td>from requirements to software</td><td>§[1.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.5)</td><td> [10am slides.pdf](files/1110/2017-08-25-1000-slides.pdf) [2pm slides.pdf](files/1110/2017-08-25-1400-slides.pdf) [10am video](screencasts/2017-08-25-1000.webm) [2pm video](screencasts/2017-08-25-1400.webm)
<tr id="2017-08-28" class=""><th>28 Aug <br/></th><td>ambiguity</td><td>Exercises 1.1 and 1.2 from textbook</td><td> [10am slides.pdf](files/1110/2017-08-28-1000-slides.pdf) [2pm slides.pdf](files/1110/2017-08-28-1400-slides.pdf) [10am video](screencasts/2017-08-28-1000.webm) [2pm video](screencasts/2017-08-28-1400.webm)
<tr id="2017-08-30" class=""><th>30 Aug <br/></th><td>pseudocode</td><td>[wikihow](http://www.wikihow.com/Write-Pseudocode)</td><td>the 10am lecture wasn't recorded; use 2pm instead [10am 01-sequence.txt](files/1110/2017-08-30-1000-01-sequence.txt) [10am 02-selection.txt](files/1110/2017-08-30-1000-02-selection.txt) [10am 03-iteration.txt](files/1110/2017-08-30-1000-03-iteration.txt) [10am 04-declaration.txt](files/1110/2017-08-30-1000-04-declaration.txt) [10am 05-update.txt](files/1110/2017-08-30-1000-05-update.txt) [2pm 01-sequence.txt](files/1110/2017-08-30-1400-01-sequence.txt) [2pm 02-selection.txt](files/1110/2017-08-30-1400-02-selection.txt) [2pm 03-iteration.txt](files/1110/2017-08-30-1400-03-iteration.txt) [2pm 04-declaration.txt](files/1110/2017-08-30-1400-04-declaration.txt) [2pm 05-update.txt](files/1110/2017-08-30-1400-05-update.txt) [2pm slides.pdf](files/1110/2017-08-30-1400-slides.pdf) [2pm video](screencasts/2017-08-30-1400.webm)
<tr id="2017-08-31" class=" lab"><th>31 Aug <br/></th><td>[pseudocode counting squares](lab02-counting.html)</td><td></td><td></td></tr>

<tr id="2017-09-01" class=""><th>1 Sep <br/></th><td>PyCharm</td><td>§[1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.4), §[1.7](http://www.spronck.net/pythonbook/pythonbook.pdf#section.1.7)</td><td>[demo.py](files/001/demo.py) [10am demo.py](files/1110/2017-09-01-1000-demo.py) [10am slides.pdf](files/1110/2017-09-01-1000-slides.pdf) [2pm demo.py](files/1110/2017-09-01-1400-demo.py) [2pm example.py](files/1110/2017-09-01-1400-example.py) [2pm my_math_rules.py](files/1110/2017-09-01-1400-my_math_rules.py) [2pm slides.pdf](files/1110/2017-09-01-1400-slides.pdf) [10am video](screencasts/2017-09-01-1000.webm) [2pm video](screencasts/2017-09-01-1400.webm) [2pm video](screencasts/2017-09-01-1400.webm)
<tr id="2017-09-04" class=""><th>4 Sep <br/></th><td>course overview with `turtle`{.python}, part 1</td><td></td><td> [10am about_for.py](files/1110/2017-09-04-1000-about_for.py) [10am slides.pdf](files/1110/2017-09-04-1000-slides.pdf) [10am turtle_square.py](files/1110/2017-09-04-1000-turtle_square.py) [10am turtle_with_brush.py](files/1110/2017-09-04-1000-turtle_with_brush.py) [2pm for_explainer.py](files/1110/2017-09-04-1400-for_explainer.py) [2pm slides.pdf](files/1110/2017-09-04-1400-slides.pdf) [2pm turtle_paint.py](files/1110/2017-09-04-1400-turtle_paint.py) [2pm turtle_square.py](files/1110/2017-09-04-1400-turtle_square.py) [10am video](screencasts/2017-09-04-1000.webm) [2pm video](screencasts/2017-09-04-1400.webm)
<tr id="2017-09-06" class=""><th>6 Sep <br/><span class="special">Add deadline</span></th><td>course overview with `turtle`{.python}, part 2</td><td></td><td> [10am big_turtle_race.py](files/1110/2017-09-06-1000-big_turtle_race.py) [10am sierpinski_tri.py](files/1110/2017-09-06-1000-sierpinski_tri.py) [10am slides.pdf](files/1110/2017-09-06-1000-slides.pdf) [10am turtle_race.py](files/1110/2017-09-06-1000-turtle_race.py) [10am turtle_square.py](files/1110/2017-09-06-1000-turtle_square.py) [2pm big_turtle_race.py](files/1110/2017-09-06-1400-big_turtle_race.py) [2pm for_explainer.py](files/1110/2017-09-06-1400-for_explainer.py) [2pm sierpinski.py](files/1110/2017-09-06-1400-sierpinski.py) [2pm slides.pdf](files/1110/2017-09-06-1400-slides.pdf) [2pm turtle_race.py](files/1110/2017-09-06-1400-turtle_race.py) [10am video](screencasts/2017-09-06-1000.webm) [2pm video](screencasts/2017-09-06-1400.webm)
<tr id="2017-09-07" class=" lab"><th>7 Sep <br/></th><td>[turtle art contest](lab03-turtle.html)</td><td></td><td></td></tr>

<tr id="2017-09-08" class=""><th>8 Sep <br/></th><td>hello, world!</td><td>[revised chapter 2](revised2.2.html); §[5.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.5.2.4)--5.2.5; §[4.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.4.1)</td><td>[PythonTutor](http://pythontutor.com/) [10am get_input.py](files/1110/2017-09-08-1000-get_input.py) [10am print_test.py](files/1110/2017-09-08-1000-print_test.py) [10am python_variable.py](files/1110/2017-09-08-1000-python_variable.py) [10am slides.pdf](files/1110/2017-09-08-1000-slides.pdf) [2pm math_string.py](files/1110/2017-09-08-1400-math_string.py) [2pm python_variable.py](files/1110/2017-09-08-1400-python_variable.py) [2pm slides.pdf](files/1110/2017-09-08-1400-slides.pdf) [2pm using_print.py](files/1110/2017-09-08-1400-using_print.py) [10am video](screencasts/2017-09-08-1000.webm) [2pm video](screencasts/2017-09-08-1400.webm)
<tr id="2017-09-11" class=""><th>11 Sep <br/></th><td>variables, values, and operators</td><td>§[3](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.3) and §[4](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.4)</td><td> [10am assign_test.py](files/1110/2017-09-11-1000-assign_test.py) [10am float_is_strange.py](files/1110/2017-09-11-1000-float_is_strange.py) [10am function_type.py](files/1110/2017-09-11-1000-function_type.py) [10am get_input.py](files/1110/2017-09-11-1000-get_input.py) [10am print_test.py](files/1110/2017-09-11-1000-print_test.py) [10am python_variable.py](files/1110/2017-09-11-1000-python_variable.py) [10am slides.pdf](files/1110/2017-09-11-1000-slides.pdf) [10am you_are_young.py](files/1110/2017-09-11-1000-you_are_young.py) [2pm age_liar.py](files/1110/2017-09-11-1400-age_liar.py) [2pm float_is_strange.py](files/1110/2017-09-11-1400-float_is_strange.py) [2pm func_intro.py](files/1110/2017-09-11-1400-func_intro.py) [2pm slides.pdf](files/1110/2017-09-11-1400-slides.pdf) [2pm variable_test.py](files/1110/2017-09-11-1400-variable_test.py) [10am video](screencasts/2017-09-11-1000.webm) [2pm video](screencasts/2017-09-11-1400.webm)
<tr id="2017-09-13" class=""><th>13 Sep <br/></th><td>functions -- basics, `def`{.python}</td><td>§[5](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.5)--5.2 and §[8](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.8)--8.2.1</td><td>Typo in 10am slides: `'hi' < 'bye'`{.python} is `False`{.python}, not `True`{.python} [10am first_functions.py](files/1110/2017-09-13-1000-first_functions.py) [10am len_and_raound.py](files/1110/2017-09-13-1000-len_and_raound.py) [10am slides.pdf](files/1110/2017-09-13-1000-slides.pdf) [10am testing_functions.py](files/1110/2017-09-13-1000-testing_functions.py) [10am use_first_functions.py](files/1110/2017-09-13-1000-use_first_functions.py) [10am you_are_young.py](files/1110/2017-09-13-1000-you_are_young.py) [2pm first_functions.py](files/1110/2017-09-13-1400-first_functions.py) [2pm len_and_round.py](files/1110/2017-09-13-1400-len_and_round.py) [2pm slides.pdf](files/1110/2017-09-13-1400-slides.pdf) [2pm use_first_functions.py](files/1110/2017-09-13-1400-use_first_functions.py) [10am video](screencasts/2017-09-13-1000.webm) [2pm video](screencasts/2017-09-13-1400.webm)
<tr id="2017-09-14" class=" lab"><th>14 Sep <br/></th><td>[madlibs](lab04-madlib.html)</td><td></td><td></td></tr>

<tr id="2017-09-15" class=""><th>15 Sep <br/></th><td>functions -- flow of control</td><td>§[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6</td><td> [10am func_tangle.py](files/1110/2017-09-15-1000-func_tangle.py) [10am get.py](files/1110/2017-09-15-1000-get.py) [10am page_to_read.py](files/1110/2017-09-15-1000-page_to_read.py) [10am poly_func.py](files/1110/2017-09-15-1000-poly_func.py) [10am slides.pdf](files/1110/2017-09-15-1000-slides.pdf) [2pm following_functions.py](files/1110/2017-09-15-1400-following_functions.py) [2pm func_puzzle.py](files/1110/2017-09-15-1400-func_puzzle.py) [2pm get.py](files/1110/2017-09-15-1400-get.py) [2pm read_pages.py](files/1110/2017-09-15-1400-read_pages.py) [2pm slides.pdf](files/1110/2017-09-15-1400-slides.pdf) [10am video](screencasts/2017-09-15-1000.webm) [2pm video](screencasts/2017-09-15-1400.webm) [2pm video](screencasts/2017-09-15-1400.webm) [2pm video](screencasts/2017-09-15-1400.webm) [2pm video](screencasts/2017-09-15-1400.webm) [2pm video](screencasts/2017-09-15-1400.webm)
<tr id="2017-09-18" class=""><th>18 Sep <br/></th><td>functions -- scope, `global`{.python}</td><td>§[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)</td><td> [10am following_functions.py](files/1110/2017-09-18-1000-following_functions.py) [10am func_swap.py](files/1110/2017-09-18-1000-func_swap.py) [10am play_with_scope.py](files/1110/2017-09-18-1000-play_with_scope.py) [10am slides.pdf](files/1110/2017-09-18-1000-slides.pdf) [2pm following_functions.py](files/1110/2017-09-18-1400-following_functions.py) [2pm get.py](files/1110/2017-09-18-1400-get.py) [2pm scope_quiz.py](files/1110/2017-09-18-1400-scope_quiz.py) [2pm slides.pdf](files/1110/2017-09-18-1400-slides.pdf) [10am video](screencasts/2017-09-18-1000.webm) [2pm video](screencasts/2017-09-18-1400.webm)
<tr id="2017-09-20" class=""><th>20 Sep <br/></th><td>decisions -- `if`{.python}, `elif`{.python}, and `else`{.python}</td><td>§[6.1.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.6.1.2) and §[6.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.2)--6.2.3</td><td> [10am age_classifier.py](files/1110/2017-09-20-1000-age_classifier.py) [10am if_func.py](files/1110/2017-09-20-1000-if_func.py) [10am if_intro.py](files/1110/2017-09-20-1000-if_intro.py) [10am slides.pdf](files/1110/2017-09-20-1000-slides.pdf) [2pm if_func.py](files/1110/2017-09-20-1400-if_func.py) [2pm if_intro.py](files/1110/2017-09-20-1400-if_intro.py) [2pm slides.pdf](files/1110/2017-09-20-1400-slides.pdf) [10am video](screencasts/2017-09-20-1000.webm) [2pm video](screencasts/2017-09-20-1400.webm)
<tr id="2017-09-21" class=" lab"><th>21 Sep <br/></th><td>[exam prep](lab05-paper.html)</td><td></td><td></td></tr>

<tr id="2017-09-22" class=""><th>22 Sep <br/></th><td>decisions -- logical operators</td><td>rest of §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2</td><td>**never** use §[6.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.3)'s `exit()`{.python} function [10am if_and_things.py](files/1110/2017-09-22-1000-if_and_things.py) [10am if_func.py](files/1110/2017-09-22-1000-if_func.py) [10am slides.pdf](files/1110/2017-09-22-1000-slides.pdf) [10am truthiness.py](files/1110/2017-09-22-1000-truthiness.py) [2pm bad_booleans.py](files/1110/2017-09-22-1400-bad_booleans.py) [2pm if_func.py](files/1110/2017-09-22-1400-if_func.py) [2pm if_things.py](files/1110/2017-09-22-1400-if_things.py) [2pm slides.pdf](files/1110/2017-09-22-1400-slides.pdf) [10am video](screencasts/2017-09-22-1000.webm) [2pm video](screencasts/2017-09-22-1400.webm)
<tr id="2017-09-25" class=""><th>25 Sep <br/></th><td>review</td><td>§[2](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.2)--5.2, §[6.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.6.1)--6.2.3, §[8.2.2](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.2)--8.2.6, §[8.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.8.3)</td><td> [10am exam1-prep.py](files/1110/2017-09-25-1000-exam1-prep.py) [10am slides.pdf](files/1110/2017-09-25-1000-slides.pdf) [2pm exam1_review.py](files/1110/2017-09-25-1400-exam1_review.py) [2pm slides.pdf](files/1110/2017-09-25-1400-slides.pdf) [10am video](screencasts/2017-09-25-1000.webm) [2pm video](screencasts/2017-09-25-1400.webm)
<tr id="2017-09-27" class="exam"><th>27 Sep </th><td>exam 1</td><td></td><td>the [exam](files/f2017e1.pdf), [key](https://piazza.com/class/j6m7hyps7tx66x?cid=135), and [TPEGS](https://tpegs.cs.virginia.edu/)
<tr id="2017-09-28" class=" lab"><th>28 Sep <br/></th><td>[strings](lab06-strpuz.html)</td><td></td><td></td></tr>

<tr id="2017-09-29" class=""><th>29 Sep <br/></th><td>code readability, elegance</td><td>§[3.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.3.4), §[8.2.9](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.8.2.9)--8.2.10; skim [PEP 8](https://www.python.org/dev/peps/pep-0008/)</td><td> [10am input_print_return.py](files/1110/2017-09-29-1000-input_print_return.py) [10am on_naming.py](files/1110/2017-09-29-1000-on_naming.py) [10am play_with_scope.py](files/1110/2017-09-29-1000-play_with_scope.py) [10am slides.pdf](files/1110/2017-09-29-1000-slides.pdf) [10am stylish_functions.py](files/1110/2017-09-29-1000-stylish_functions.py) [2pm func_style.py](files/1110/2017-09-29-1400-func_style.py) [2pm koan.py](files/1110/2017-09-29-1400-koan.py) [2pm readability.py](files/1110/2017-09-29-1400-readability.py) [2pm scope_quiz.py](files/1110/2017-09-29-1400-scope_quiz.py) [2pm slides.pdf](files/1110/2017-09-29-1400-slides.pdf) [10am video](screencasts/2017-09-29-1000.webm) [2pm video](screencasts/2017-09-29-1400.webm) [2pm video](screencasts/2017-09-29-1400.webm)
<tr id="2017-10-02" class="noclass"><th>2 Oct </th><td><span class="reason">Reading Days</span></td><td></td><td>
<tr id="2017-10-04" class=""><th>4 Oct <br/></th><td>testing</td><td>our own [testing writeup](testing.html)</td><td> [10am pow_test_func.py](files/1110/2017-10-04-1000-pow_test_func.py) [10am slides.pdf](files/1110/2017-10-04-1000-slides.pdf) [10am test_pow.py](files/1110/2017-10-04-1000-test_pow.py) [2pm func_test_funcs.py](files/1110/2017-10-04-1400-func_test_funcs.py) [2pm slides.pdf](files/1110/2017-10-04-1400-slides.pdf) [2pm test_pow.py](files/1110/2017-10-04-1400-test_pow.py) [10am video](screencasts/2017-10-04-1000.webm) [2pm video](screencasts/2017-10-04-1400.webm)
<tr id="2017-10-05" class=" lab"><th>5 Oct <br/></th><td>[hangman](lab07-hangman.html)</td><td></td><td></td></tr>

<tr id="2017-10-06" class=""><th>6 Oct <br/></th><td>repeating with `while`{.python}</td><td>§[7.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.1)</td><td> [10am hangman.py](files/1110/2017-10-06-1000-hangman.py) [10am hangman2.py](files/1110/2017-10-06-1000-hangman2.py) [10am input_validation.py](files/1110/2017-10-06-1000-input_validation.py) [10am making_a_while.py](files/1110/2017-10-06-1000-making_a_while.py) [10am slides.pdf](files/1110/2017-10-06-1000-slides.pdf) [10am while_examples.py](files/1110/2017-10-06-1000-while_examples.py) [2pm about_while.py](files/1110/2017-10-06-1400-about_while.py) [2pm func_test_funcs.py](files/1110/2017-10-06-1400-func_test_funcs.py) [2pm hangman.py](files/1110/2017-10-06-1400-hangman.py) [2pm hangman2.py](files/1110/2017-10-06-1400-hangman2.py) [2pm how_to_write_loops.py](files/1110/2017-10-06-1400-how_to_write_loops.py) [2pm slides.pdf](files/1110/2017-10-06-1400-slides.pdf) [2pm validate_input.py](files/1110/2017-10-06-1400-validate_input.py) [10am video](screencasts/2017-10-06-1000.webm) [10am video](screencasts/2017-10-06-1000.webm) [2pm video](screencasts/2017-10-06-1400.webm)
<tr id="2017-10-09" class=""><th>9 Oct <br/><span class="special">Drop deadline</span></th><td>composite datatypes -- strings, ranges, lists, tuples</td><td>§[10.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.4), §[11](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.11), §[12.1](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.1), §[12.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.3)</td><td> [10am collections_intro.py](files/1110/2017-10-09-1000-collections_intro.py) [10am loop_over_collections.py](files/1110/2017-10-09-1000-loop_over_collections.py) [10am slides.pdf](files/1110/2017-10-09-1000-slides.pdf) [2pm collections_intro.py](files/1110/2017-10-09-1400-collections_intro.py) [2pm hangman2.py](files/1110/2017-10-09-1400-hangman2.py) [2pm slides.pdf](files/1110/2017-10-09-1400-slides.pdf) [10am video](screencasts/2017-10-09-1000.webm) [2pm video](screencasts/2017-10-09-1400.webm)
<tr id="2017-10-11" class=""><th>11 Oct <br/></th><td>iteration -- the `for`{.python} loop</td><td>§[7.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.7.2)</td><td> [10am basic_iteration.py](files/1110/2017-10-11-1000-basic_iteration.py) [10am in_range.py](files/1110/2017-10-11-1000-in_range.py) [10am lists_1.py](files/1110/2017-10-11-1000-lists_1.py) [10am nested_loops.py](files/1110/2017-10-11-1000-nested_loops.py) [10am slides.pdf](files/1110/2017-10-11-1000-slides.pdf) [2pm basic_iteration.py](files/1110/2017-10-11-1400-basic_iteration.py) [2pm following_functions.py](files/1110/2017-10-11-1400-following_functions.py) [2pm func_style.py](files/1110/2017-10-11-1400-func_style.py) [2pm loop_index.py](files/1110/2017-10-11-1400-loop_index.py) [2pm more_iterations.py](files/1110/2017-10-11-1400-more_iterations.py) [2pm nest_loops.py](files/1110/2017-10-11-1400-nest_loops.py) [2pm slides.pdf](files/1110/2017-10-11-1400-slides.pdf) [10am video](screencasts/2017-10-11-1000.webm)
<tr id="2017-10-12" class=" lab"><th>12 Oct <br/></th><td>[old cryptography](lab08-crypto.html)</td><td></td><td></td></tr>

<tr id="2017-10-13" class=""><th>13 Oct <br/></th><td>methods and mutability -- why `list`{.python} is special</td><td>§[12.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.2), §[12.5](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.5),</td><td>
<tr id="2017-10-16" class=""><th>16 Oct <br/><span class="special">Withdraw deadline</span></th><td>applications of lists and strings</td><td>§[10.6](http://www.spronck.net/pythonbook/pythonbook.pdf#section.10.6), §[12.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.12.4)</td><td>
<tr id="2017-10-18" class=""><th>18 Oct <br/></th><td>debugging techniques</td><td></td><td>[buggy code](files/001/spoon.py)
<tr id="2017-10-19" class=" lab"><th>19 Oct <br/></th><td>[debugging](lab09-debug.html)</td><td></td><td></td></tr>

<tr id="2017-10-20" class=""><th>20 Oct <br/></th><td>flexible indices -- `dict`{.python}</td><td>§[13](http://www.spronck.net/pythonbook/pythonbook.pdf#chapter.13)</td><td>
<tr id="2017-10-23" class=""><th>23 Oct <br/></th><td>reading data -- `open`{.python} and `urllib`{.python}</td><td>§[16.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.16.2), §[27.3](http://www.spronck.net/pythonbook/pythonbook.pdf#section.27.3)</td><td>
<tr id="2017-10-25" class=""><th>25 Oct <br/></th><td>understanding data</td><td>Wikpedia on [delimiter-separated values](https://en.wikipedia.org/wiki/Delimiter-separated_values)</td><td>[vastats.csv](files/vastats.csv)
<tr id="2017-10-26" class=" lab"><th>26 Oct <br/></th><td>[point-of-interest location](lab10-wendys.html)</td><td></td><td></td></tr>

<tr id="2017-10-27" class=""><th>27 Oct <br/></th><td>more on the data theme</td><td></td><td>
<tr id="2017-10-30" class=""><th>30 Oct <br/></th><td>review</td><td></td><td>
<tr id="2017-11-01" class="exam"><th>1 Nov </th><td>exam 2</td><td></td><td>
<tr id="2017-11-02" class=" lab"><th>2 Nov <br/></th><td>[gamebox installation](lab11-gamebox.html)</td><td></td><td></td></tr>

<tr id="2017-11-03" class=""><th>3 Nov <br/></th><td>polite code -- using `try`{.python} and `except`{.python} (not on exam 2)</td><td>§[17.2](http://www.spronck.net/pythonbook/pythonbook.pdf#section.17.2)</td><td>
<tr id="2017-11-06" class=""><th>6 Nov <br/></th><td>game design with `gamebox`{.python}</td><td>[gamebox documentation](code/gamebox/gamebox.pdf)</td><td>
<tr id="2017-11-08" class=""><th>8 Nov <br/></th><td>game design with `gamebox`{.python}</td><td></td><td>
<tr id="2017-11-09" class=" lab"><th>9 Nov <br/></th><td></td><td></td><td></td></tr>

<tr id="2017-11-10" class=""><th>10 Nov <br/></th><td>game design with `gamebox`{.python}</td><td></td><td>
<tr id="2017-11-13" class=""><th>13 Nov <br/></th><td>regular expressions</td><td>§[25.1.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.1), §[25.1.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.3), §[25.1.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.1.4), §[25.2.1](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.1), [pythex.org](//https://pythex.org/)</td><td>
<tr id="2017-11-15" class=""><th>15 Nov <br/></th><td>re repetition and groups</td><td>§[25.2.3](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.3), §[25.2.4](http://www.spronck.net/pythonbook/pythonbook.pdf#subsection.25.2.4)</td><td>
<tr id="2017-11-16" class=" lab"><th>16 Nov <br/></th><td></td><td></td><td></td></tr>

<tr id="2017-11-17" class=""><th>17 Nov <br/></th><td>re building</td><td>our [building guide and example](re-tips.html)</td><td>
<tr id="2017-11-20" class=""><th>20 Nov <br/></th><td>re replacing</td><td>§[25.4](http://www.spronck.net/pythonbook/pythonbook.pdf#section.25.4)</td><td>
<tr id="2017-11-22" class="noclass"><th>22 Nov </th><td><span class="reason">Thanksgiving break</span></td><td></td><td>
<tr id="2017-11-23" class="noclass lab"><th>23 Nov </th><td><span class="reason">Thanksgiving break</span></td><td></td><td></td></tr>

<tr id="2017-11-24" class="noclass"><th>24 Nov </th><td><span class="reason">Thanksgiving break</span></td><td></td><td>
<tr id="2017-11-27" class=""><th>27 Nov <br/></th><td>varies by section</td><td></td><td>
<tr id="2017-11-29" class=""><th>29 Nov <br/></th><td>varies by section</td><td></td><td>
<tr id="2017-11-30" class=" lab"><th>30 Nov <br/></th><td></td><td></td><td></td></tr>

<tr id="2017-12-01" class=""><th>1 Dec <br/></th><td>varies by section</td><td></td><td>
<tr id="2017-12-04" class=""><th>4 Dec <br/></th><td>review</td><td>[review topics](know.html)</td><td>the final exam is cumulative</tbody></table>
<table id="cal1111" class="calendar">
<thead><tr><th>Monday</th><th>Wednesday</th></tr></thead>
<tbody><tr><td/>
<td class="day Wednesday " id="2017-08-23"><span class="date">23 Aug</span>welcome<br/></td>
</tr><tr>
<td class="day Monday " id="2017-08-28"><span class="date">28 Aug</span>Algorithms & pseudocode<br/></td>
<td class="day Wednesday " id="2017-08-30"><span class="date">30 Aug</span>Algorithms & pseudocode<br/></td>
</tr><tr>
<td class="day Monday " id="2017-09-04"><span class="date">4 Sep</span>Turtle & number conversion<br/></td>
<td class="day Wednesday " id="2017-09-06"><span class="date">6 Sep</span>Computer system architecture<br/><span class="special">Add deadline</span></td>
</tr><tr>
<td class="day Monday " id="2017-09-11"><span class="date">11 Sep</span>Basic functions<br/></td>
<td class="day Wednesday " id="2017-09-13"><span class="date">13 Sep</span>Functions<br/></td>
</tr><tr>
<td class="day Monday " id="2017-09-18"><span class="date">18 Sep</span>Variable scope<br/></td>
<td class="day Wednesday " id="2017-09-20"><span class="date">20 Sep</span>Decisions if elif<br/></td>
</tr><tr>
<td class="day Monday " id="2017-09-25"><span class="date">25 Sep</span>Review<br/></td>
<td class="day Wednesday exam" id="2017-09-27"><span class="date">27 Sep</span>Exam 1</td>
</tr><tr>
<td class="day Monday noclass" id="2017-10-02"><span class="date">2 Oct</span><span class="reason">Reading Days</span></td>
<td class="day Wednesday " id="2017-10-04"><span class="date">4 Oct</span>Testing<br/></td>
</tr><tr>
<td class="day Monday " id="2017-10-09"><span class="date">9 Oct</span>Repetition<br/><span class="special">Drop deadline</span></td>
<td class="day Wednesday " id="2017-10-11"><span class="date">11 Oct</span>String operations<br/></td>
</tr><tr>
<td class="day Monday " id="2017-10-16"><span class="date">16 Oct</span>String methods/Lists<br/><span class="special">Withdraw deadline</span></td>
<td class="day Wednesday " id="2017-10-18"><span class="date">18 Oct</span>Lists<br/></td>
</tr><tr>
<td class="day Monday " id="2017-10-23"><span class="date">23 Oct</span>Dicts<br/></td>
<td class="day Wednesday " id="2017-10-25"><span class="date">25 Oct</span>Files<br/></td>
</tr><tr>
<td class="day Monday " id="2017-10-30"><span class="date">30 Oct</span>Urllib/review<br/></td>
<td class="day Wednesday exam" id="2017-11-01"><span class="date">1 Nov</span>Exam 2</td>
</tr><tr>
<td class="day Monday " id="2017-11-06"><span class="date">6 Nov</span>Exceptions<br/></td>
<td class="day Wednesday " id="2017-11-08"><span class="date">8 Nov</span>Regular expressions<br/></td>
</tr><tr>
<td class="day Monday " id="2017-11-13"><span class="date">13 Nov</span>Regular expressions<br/></td>
<td class="day Wednesday " id="2017-11-15"><span class="date">15 Nov</span>game design with `gamebox`{.python}<br/></td>
</tr><tr>
<td class="day Monday " id="2017-11-20"><span class="date">20 Nov</span>game design with `gamebox`{.python}<br/></td>
<td class="day Wednesday noclass" id="2017-11-22"><span class="date">22 Nov</span><span class="reason">Thanksgiving break</span></td>
</tr><tr>
<td class="day Monday " id="2017-11-27"><span class="date">27 Nov</span>file writing<br/></td>
<td class="day Wednesday " id="2017-11-29"><span class="date">29 Nov</span>file writing<br/></td>
</tr><tr>
<td class="day Monday " id="2017-12-04"><span class="date">4 Dec</span>review<br/></td>
</tr></tbody></table>
<table id="age1111" class="agenda">
<thead><tr><th>Date</th><th>Topic</th></tr></thead>
<tbody>
<tr id="2017-08-23" class=""><th>23 Aug <br/></th><td>welcome
<tr id="2017-08-28" class=""><th>28 Aug <br/></th><td>Algorithms & pseudocode
<tr id="2017-08-30" class=""><th>30 Aug <br/></th><td>Algorithms & pseudocode
<tr id="2017-09-04" class=""><th>4 Sep <br/></th><td>Turtle & number conversion
<tr id="2017-09-06" class=""><th>6 Sep <br/><span class="special">Add deadline</span></th><td>Computer system architecture
<tr id="2017-09-11" class=""><th>11 Sep <br/></th><td>Basic functions
<tr id="2017-09-13" class=""><th>13 Sep <br/></th><td>Functions
<tr id="2017-09-18" class=""><th>18 Sep <br/></th><td>Variable scope
<tr id="2017-09-20" class=""><th>20 Sep <br/></th><td>Decisions if elif
<tr id="2017-09-25" class=""><th>25 Sep <br/></th><td>Review
<tr id="2017-09-27" class="exam"><th>27 Sep </th><td>Exam 1
<tr id="2017-10-02" class="noclass"><th>2 Oct </th><td><span class="reason">Reading Days</span>
<tr id="2017-10-04" class=""><th>4 Oct <br/></th><td>Testing
<tr id="2017-10-09" class=""><th>9 Oct <br/><span class="special">Drop deadline</span></th><td>Repetition
<tr id="2017-10-11" class=""><th>11 Oct <br/></th><td>String operations
<tr id="2017-10-16" class=""><th>16 Oct <br/><span class="special">Withdraw deadline</span></th><td>String methods/Lists
<tr id="2017-10-18" class=""><th>18 Oct <br/></th><td>Lists
<tr id="2017-10-23" class=""><th>23 Oct <br/></th><td>Dicts
<tr id="2017-10-25" class=""><th>25 Oct <br/></th><td>Files
<tr id="2017-10-30" class=""><th>30 Oct <br/></th><td>Urllib/review
<tr id="2017-11-01" class="exam"><th>1 Nov </th><td>Exam 2
<tr id="2017-11-06" class=""><th>6 Nov <br/></th><td>Exceptions
<tr id="2017-11-08" class=""><th>8 Nov <br/></th><td>Regular expressions
<tr id="2017-11-13" class=""><th>13 Nov <br/></th><td>Regular expressions
<tr id="2017-11-15" class=""><th>15 Nov <br/></th><td>game design with `gamebox`{.python}
<tr id="2017-11-20" class=""><th>20 Nov <br/></th><td>game design with `gamebox`{.python}
<tr id="2017-11-22" class="noclass"><th>22 Nov </th><td><span class="reason">Thanksgiving break</span>
<tr id="2017-11-27" class=""><th>27 Nov <br/></th><td>file writing
<tr id="2017-11-29" class=""><th>29 Nov <br/></th><td>file writing
<tr id="2017-12-04" class=""><th>4 Dec <br/></th><td>review</tbody></table>
<script>rehide()</script>

<hr/>

Per <a href="http://www.virginia.edu/registrar/exams.html#1178">the registrar</a>, all sections of 1110 and 1111 will have their final exam at 7--10 pm on Thursday, 7 Dec 2017.  Rooms will be announced later.

Conflicts with that time will be resolved the preceding day (Wednesday 6 Dec) at 2 pm, location sent via email.
No permission to take the exam on a different day or from off of UVA grounds will be granted without Deans' office request.
A form for reporting conflicts and requesting accommodations will be provided after exam 2.

<!-- You may report conflicts and request accomodations at <https://goo.gl/forms/hC5oRY2zJoVfQz023>. -->

<!-- TA-led review sessions will be held in Chem 402 on Sunday, 7 May at 7pm and on Wednesday, 10 May at 1pm. -->

