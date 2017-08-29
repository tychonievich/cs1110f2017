import datetime
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

with open('cal-shared.yaml') as stream:
    data = load(stream, Loader=Loader)

day = datetime.timedelta(days=1)

now = data['Special Dates']['Courses begin']
end = data['Special Dates']['Courses end']
lab = data['1110-lab']

print('''---
title: Assignments
...

<!--
<div style="display:table; font-size:200%; margin: 1em auto; padding:1ex; box-shadow: 0 1px 10px rgba(0,0,0,.1); border: thin solid #eee; border-radius:1ex; background-image: linear-gradient(to bottom, #ffffff, #f2f2f2);">[Submit assignments here](https://archimedes.cs.virginia.edu/cs1110/)</div>
-->

The submission page for programming assignments is not quite ready yet, but will appear here soon.

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

''')

for asgn in data['assignments']:
    due = asgn['due']
    due = due.strftime('\n%a %d %b')# \n'+str(due)
    links = asgn['links']
    if len(links) == 0:
        print(due,'\n:    TBA')
        break
    else:
        #print(due,'\n:    ')
        for link in links:
            try:
                if ' (' in link:
                    link, extra = link.split(' (',1)
                    extra = ' ('+extra
                else: extra = ''
                with open(link+'.md') as f:
                    for line in f:
                        if line.startswith('title: '): break
                print(due,'\n:    ['+line[7:].strip()+']('+link.strip()+'.html)', extra)
                #print('    1.  ['+line[7:].strip()+']('+link.strip()+'.html)')
            except:
                print(due,'\n:    assignment not yet released')
                #print('    1.  assignment not yet released')
print('''

<script>
var dts = document.getElementsByTagName('dt');
for(var i=0; i<dts.length; i+=1) {
    if (new Date(dts[i].innerHTML+' 10:00') < new Date()) {
        dts[i].style.color = '#999999';
    }
}
</script>

# 1110 Labs

Labs are listed in order. See the [schedule](schedule.html) for the specific date of each lab.

''')

for asgn in data['1110-lab']:
    print('-   '+asgn)
