import datetime
from yaml import load
from glob import glob
from sys import stderr
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

def debug(*args, **kargs):
    kargs['file'] = stderr
    print(*args, **kargs)

with open('cal-shared.yaml') as stream:
    data = load(stream, Loader=Loader)
with open('cal-1110.yaml') as stream:
    tmp = load(stream, Loader=Loader)
    luther = tmp['1110']
    lkey = tmp.get('key', ['topic'])
with open('cal-1111.yaml') as stream:
    tmp = load(stream, Loader=Loader)
    craig = tmp['1111']
    ckey = tmp.get('key', ['topic'])
with open('media.list') as stream:
    lmedia = stream.read().split()

day = datetime.timedelta(days=1)

now = data['Special Dates']['Courses begin']
end = data['Special Dates']['Courses end']
lab = data['1110-lab']

print('''---
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

''')

cal1110 = '''<table id="cal1110" class="calendar">
<thead><tr><th>Monday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th></tr></thead>
<tbody><tr><td/>
'''
age1110 = '''<table id="age1110" class="agenda">
<thead><tr><th>Date</th><th>'''+'</th><th>'.join(s.title() for s in lkey)+'''</th></tr></thead>
<tbody>'''


cal1111 = '''<table id="cal1111" class="calendar">
<thead><tr><th>Monday</th><th>Wednesday</th></tr></thead>
<tbody><tr><td/>
'''
age1111 = '''<table id="age1111" class="agenda">
<thead><tr><th>Date</th><th>'''+'</th><th>'.join(s.title() for s in ckey)+'''</th></tr></thead>
<tbody>'''

classes = {}
content = {}
def record(date, kind):
    global classes, content
    if kind.endswith('eadline'): 
        content.setdefault(date, []).append('<span class="special">'+kind+'</span>')
    elif kind.endswith('ecess') or kind.endswith('reak') or 'eading' in kind:
        classes.setdefault(date, []).append('noclass')
        content.setdefault(date, []).append('<span class="reason">'+kind+'</span>')
    elif 'xam' in kind:
        classes.setdefault(date, []).append('exam')

for d in data['Special Dates']:
    date = data['Special Dates'][d]
    if not isinstance(date, datetime.date):
        date2 = date['start']
        while date2 <= date['end']:
            record(date2, d)
            date2 += day
    else:
        record(date, d)
    
def pretty(s):
    if s.startswith('1000-'):
        s = '10am ' + s[5:]
    if s.startswith('1000'):
        s = '10am' + s[4:]
    if s.startswith('1400-'):
        s = '2pm ' + s[5:]
    if s.startswith('1400'):
        s = '2pm' + s[4:]
    if s.endswith('.webm'):
        s = s[:-5] + ' video'
    if s.endswith('.mp3'):
        s = s[:-4] + ' audio'
    return s

def mwf(date, index, ilab, section, key, friday=True, media=[], fpath=None):
    special = '<br/>'+'<br/>'.join(content.get(date, [])) if date not in classes else ''
    caldate = '<td class="day {2} {3}" id="{0}"><span class="date">{1}</span>'.format(
        date, 
        date.strftime('%d ').strip('0')+ date.strftime('%B')[:3], 
        date.strftime('%A'),
        ' '.join(classes.get(date, []))+(' lab' if date.weekday() == 3 else ''),
    )
    agedate = '\n<tr id="{0}" class="{2}"><th>{1} {3}</th><td>'.format(
        date, 
        date.strftime('%d ').strip('0')+ date.strftime('%B')[:3], 
        ' '.join(classes.get(date, []))+(' lab' if date.weekday() == 3 else ''),
        special
    )
    cal = ''
    age = ''
    if date.weekday() in ([0,2,4] if friday else [0,2]):
        if 'noclass' in classes.get(date, []):
            text = '\n'.join(content.get(date, []))
        else:
            if index < len(section) and section[index] is not None: text = section[index]
            else: text = ''
            index += 1
        if type(text) is not dict: text = {key[0]:text}
        if fpath is not None:
            for img in sorted(glob('files/{}/{}*'.format(fpath, date.strftime('%Y%m%d')))+glob('files/{}/{}*'.format(fpath, date.strftime('%Y-%m-%d')))):
                # print(img, file=stderr)
                text['notes'] = text.get('notes', '') + ' [{}]({})'.format(pretty(img.split('/')[-1][8:].split('-',1)[-1]), img)
        for m in media:
            # debug(m, '{}'.format(date), '{}'.format(date) in m)
            ds = '{}'.format(date)
            if ds in m:
                text['notes'] = text.get('notes', '') + ' [{1}]({0})'.format(m, pretty(m[m.find(ds)+len(ds)+1:]))
        cal = caldate + '<br/>'.join(text[k] for k in key if k in text) + special + '</td>\n'
        age = agedate + '</td><td>'.join(text.get(k,'') for k in key)
    elif date.weekday() == 3 and friday:
        if 'noclass' in classes.get(date, []):
            text = '\n'.join(content.get(date, []))
        else:
            if ilab < len(lab) and lab[ilab] is not None: text = lab[ilab]
            else: text = ''
            ilab += 1
        if type(text) is not dict: text = {key[0]:text}
        cal = caldate + '<br/>'.join(text[k] for k in key if k in text) + special + '</td>\n'
        age = agedate + '</td><td>'.join(text.get(k,'') for k in key)+'</td></tr>\n'
    elif date.weekday() == 6:
        cal = '</tr><tr>\n'
    return cal, age, index, ilab


labdates = []
i1110 = 0
i1111 = 0
ilab = 0
while now < end:
        cx, ax, i1111, _ = mwf(now, i1111, ilab, craig, ckey, friday=False)
        c1, a1, i1110, ilab = mwf(now, i1110, ilab, luther, lkey, media=lmedia, fpath='1110')
        cal1110 += c1
        age1110 += a1
        cal1111 += cx
        age1111 += ax
        if '(lab' in c1:
            i1 = c1.find('(lab')
            i2 = c1.find('.html)', i1)
            labdates.append({'due':now, 'links':[c1[i1+1:i2]]})
        now += day

cal1110 += '</tr></tbody></table>'
age1110 += '</tbody></table>'
cal1111 += '</tr></tbody></table>'
age1111 += '</tbody></table>'

print(cal1110)
print(age1110)
print(cal1111)
print(age1111)

print('<script>rehide()</script>')
print('''
<hr/>

Per <a href="http://www.virginia.edu/registrar/exams.html#1178">the registrar</a>, all sections of 1110 and 1111 will have their final exam at **7--10 pm on Thursday, 7 Dec 2017**. Locations are given below:

| Section | Instructor | Exam Location |
|---------|------------|---------------|
| 1110-001|Tychonievich| Chemistry 402 |
| 1110-002| Dill       | Maury 209     |
| 1110-003|Tychonievich| Chemistry 402 |
| 1111-001| Dill       | Maury 209     |


7pm exams in large rooms tend to have **heating** problems: the rooms tend to start too cold, then get too hot, then cool off again. Dress in layers.

<!--
Conflicts with that time will be resolved the preceding day (Wednesday 6 Dec) at 7 pm, location sent via email.
No permission to take the exam on a different day or from off of UVA grounds will be granted without Deans' office request.

You may report conflicts and request accommodations via [this form](https://docs.google.com/forms/d/e/1FAIpQLSfDcGGIYdkK0a9ZXnMagAF1L39zL8dYyRNVCvXmYEBS7dfrGA/viewform?usp=sf_link).
-->

The deadline for reporting conflicts with the final has passed. If you have not been informed of an alternative arrangement, it is probably too late to get one now as the makeup exam room we were given is not large enough to add more people.

A **TA-led review session** will be held in Chem 402 on Wednesday, 6 December at 2pm.
''')




import csv, re
filename = re.compile(r'`([^`]*\.py)`')
with open('../assignments.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow('slug,files,duedate,late,opendate,fbdelay,support,unittests'.split(','))
    for asgn in sorted(data['assignments'] + labdates, key=lambda x:x['due']):
        date = asgn['due']
        for task in asgn['links']:
            extra = ''
            if ' (' in task:
                task, extra = task.split(' (',1)
                extra = ' ('+extra
            if task.startswith('pa'):
                slug = task[0:4].upper()
            else:
                slug = task
            if 'checkpoint' in extra:
                continue
            if (task == 'project' or 'project' in slug) and 'checkpoint' not in extra:
                #w.writerow([
                    #'game partner selection',
                    #'partner.txt',
                    #'2017-04-13 23:59',
                    #'0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0','','0','',''
                #])
                w.writerow([
                    'flappybird images (optional)',
                    '*.*',
                    '2017-11-13 11:00',
                    '0 0 ','','0','',''
                ])
                w.writerow([
                    'game checkpoint 1',
                    'game.py|*.*',
                    '2017-11-15 23:59',
                    '','','0','',''
                ])
                w.writerow([
                    'game checkpoint 2',
                    'game.py|*.*',
                    '2017-11-29 23:59',
                    '','','0','',''
                ])
                w.writerow([
                    'game project',
                    'game.py|*.*',
                    '2017-12-05 23:59',
                    '','','0','',''
                ])
                continue
            try:
                with open(task+'.md') as t:
                    fnames = set(_ for _ in filename.findall(t.read()) if _ not in ['gamebox.py', 'get-pip.py','.py'])
                if not fnames: continue
                testnames = sorted('test_'+x for x in fnames if '*' not in x and x != 'flappybird.py')
                if task.startswith('lab'): testnames = '' 
                w.writerow([
                    slug,
                    '|'.join(sorted(fnames)),
                    str(date) + (' 23:00' if task.startswith('lab') else ' 10:00'),
                    '1 2' if slug not in 'PA01 PA02 PA05' else '0 0','','2','timeout.py|timeout2.py|gradetools.py|cacheurls.py',
                    '|'.join(testnames)
                ])
                if slug.endswith('turtle'):
                    w.writerow([
                        slug+' art contest',
                        '*.png|*.ps',
                        str(date) + (' 23:00' if task.startswith('lab') else ' 10:00'),
                        '1 2','','','',
                        ''
                    ])
                        
            except BaseException as ex:
                print('exception', task, ex, file=stderr)
                pass
