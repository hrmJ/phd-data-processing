import re

def FormUrl(url):
    if 'http://' in url:
        url = re.sub(r'http://.*lex1=','&lex1=', url)
    urlprefix = 'http://search2.ruscorpora.ru/search.xml?sort=random&out=normal&dpp=100&spd=10&seed=21964&env=alpha&mydocsize=&text=lexgramm&lang=ru&nodia=1&parent1=0&level1=0'
    urlpostfix = '&mode=paper'
    return '{}{}{}'.format(urlprefix,url,urlpostfix)

def GiveName(string):
    return 'ru_nkrja_{}'.format(string)

urlprefix = 'http://search2.ruscorpora.ru/search.xml?sort=random&out=normal&dpp=100&spd=10&seed=21964&env=alpha&mydocsize=&text=lexgramm&lang=ru&nodia=1&parent1=0&level1=0'
urlpostfix = '&mode=paper'

lc0a = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E2%F7%E5%F0%E0%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2='),
        'query': '"вчера"','filename':GiveName('lc0a')}

lc0b = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%F1%E5%E3%EE%E4%ED%FF%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2='),
        'query': '"сегодня"','filename':GiveName('lc0b')}

lc0c = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E7%E0%E2%F2%F0%E0%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2='),
        'query': '"завтра"','filename':GiveName('lc0c')}

lc1 = {'url': urlprefix + '&lex1=%E2%7C%ED%E0&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%EF%F0%EE%F8%EB%FB%E9&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%E3%EE%E4%7C%ED%E5%E4%E5%EB%FF&gramm3=%28loc%7Cloc2%29&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=' + urlpostfix,
       'query': ''}

lc2 = {'url': urlprefix + '&lex1=%22%F3%F2%F0%EE%EC%22%7C%22%E2%E5%F7%E5%F0%EE%EC%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=' + urlpostfix,
       'query': '"утром"|"вечером"'}

lc3 = {'url': FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%EF%EE%F1%EB%E5&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%E2%EE%E9%ED%FB%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&mode=paper'),
        'query': 'после + "войны"','filename':GiveName('lc3')}

lc4 = {'url': urlprefix + '&lex1=%22%F1%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%F2%E5%F5%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%EF%EE%F0%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=' + urlpostfix,
        'query': 'с тех пор'}
              
lc5 = {'url': urlprefix + '&lex1=%22%F7%E5%F0%E5%E7%22%7C%22%F1%EF%F3%F1%F2%FF%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=NUM&sem2=&sem-mod3=sem&sem-mod3=sem2&flags2=&m3=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%EB%E5%F2%22%7C%22%E4%ED%E5%E9%22%7C%22%F1%F3%F2%EE%EA%22%7C%22%F7%E0%F1%EE%E2%22&gramm3=&sem3=&sem-mod2=sem&sem-mod2=sem2&flags3=&m2=' + urlpostfix,
        'query': '"через"|"спустя" NUM "лет"|"дней"|"суток"|"часов"'}

lc6 = {'url': urlprefix + '&lex1=%E2&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=NUM%2C%28nom%7Cacc%29&sem2=&sem-mod3=sem&sem-mod3=sem2&flags2=&m3=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%F7%E0%F1%EE%E2%22%7C%22%F7%E0%F1%E0%22&gramm3=&sem3=&sem-mod2=sem&sem-mod2=sem2&flags3=&m2=' + urlpostfix,
       'query': 'в + NUM + "часов"|"часа"'}

lc7a = {'url': urlprefix + '&lex1=%E2&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%F2%EE%22&gramm2=&sem2=&sem-mod3=sem&sem-mod3=sem2&flags2=&m3=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%E2%F0%E5%EC%FF%22&gramm3=&sem3=&sem-mod2=sem&sem-mod2=sem2&flags3=&m2=&parent4=0&level4=0&min4=1&max4=1&lex4=*+-%EA%E0%EA+-%E3%EE%E4+-%EA%EE%E3%E4%E0&gramm4=&sem4=&sem-mod5=sem&sem-mod5=sem2&flags4=&m5=' + urlpostfix,
   'query': 'в то время + * -как -когда -год'}


lc7a_loppu = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%E2&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%F2%EE%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%E2%F0%E5%EC%FF%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=bdot%7Cbcolon%7Cbsemicolon%7Cbexcl%7Cbques&m3=&mode=paper'),'filename':GiveName('lc7a_loppu')}

lc7b = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%F2%EE%E3%E4%E0%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1='),
        'query': '"тогда"','filename':GiveName('lc7b')}

lc8 = {'url': urlprefix + '&lex1=%22%F1%EA%EE%F0%EE%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=' + urlpostfix,
   'query': '"скоро"'}

lc9a = {'url': urlprefix + '&lex1=%22%F2%E5%EF%E5%F0%FC%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=' + urlpostfix,
   'query': 'теперь'}

lc9b = {'url': urlprefix + '&lex1=%22%F1%E5%E9%F7%E0%F1%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=' + urlpostfix,
    'query': 'сейчас'}

fr1 = {'url': urlprefix + '&lex1=%EA%E0%E6%E4%FB%E9&gramm1=%28nom%7Cacc%29&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%E4%E5%ED%FC%7C%ED%E5%E4%E5%EB%FF%7C%E3%EE%E4%7C%EC%E5%F1%FF%F6&gramm2=%28nom%7Cacc%29&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=' + urlpostfix,
   'query': 'каждый [день|неделя|год|месяц]'}

fr2 = {'url': urlprefix + '&lex1=%EF%EE&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%EF%EE%ED%E5%E4%E5%EB%FC%ED%E8%EA%E0%EC%22%7C%22%E2%F2%EE%F0%ED%E8%EA%E0%EC%22%7C%22%F1%F0%E5%E4%E0%EC%22%7C%22%F7%E5%F2%E2%E5%F0%E3%E0%EC%22%7C%22%EF%FF%F2%ED%E8%F6%E0%EC%22%7C%22%F1%F3%E1%E1%EE%F2%E0%EC%22%7C%22%E2%EE%EA%F0%E5%F1%E5%ED%FC%FF%EC%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=' + urlpostfix,
   'query': 'по "понедельникам"|"вторникам"|"средам"|"четвергам"|"пятницам"|"субботам"|"вокресеньям"'}

fr3a = {'url': FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E4%E2%E0%22%7C%22%F2%F0%E8%22%7C%22%F7%E5%F2%FB%F0%E5%22%7C%22%EF%FF%F2%FC%22%7C%22%F8%E5%F1%F2%FC%22%7C%22%F1%E5%EC%FC%22%7C%22%E2%EE%F1%E5%EC%FC%22%7C%22%E4%E5%E2%FF%F2%FC%22%7C%22%E4%E5%F1%FF%F2%FC%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%20%22%F0%E0%E7%E0%22%7C%22%F0%E0%E7%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&mode=paper'),
        'query': '"два"|"три"|"четыре"|"пять"|"шесть"|"семь"|"восемь"|"девять"|"десять" "раза"|"раз"', 'filename':GiveName('fr3a')}


fr3b = {'url': urlprefix + '&lex1=%E4%E2%E0%E6%E4%FB%7C%F2%F0%E8%E6%E4%FB&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=' + urlpostfix,
    'query': 'дважды|трижды'}

fr4a = {'url': urlprefix + '&lex1=%F7%E0%F1%F2%EE&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=' + urlpostfix,
        'query': 'часто', 'filename':GiveName('fr4a')}

fr4b = {'url': urlprefix + '&lex1=%22%E2%F1%E5%E3%E4%E0%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=' + urlpostfix,
        'query': 'всегда','filename':GiveName('fr4b')}

fr5a = {'url': FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&dpp=&spp=&spd=&text=lexgramm&mode=paper&sort=gr_tagging&lang=ru&parent1=0&level1=0&lex1=%F0%E5%E4%EA%EE&gramm1=&sem1=&flags1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&flags2='),
        'query': 'редко', 'filename':GiveName('fr5a')}

fr5b = {'url': FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E8%ED%EE%E3%E4%E0%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2='),
        'query': 'иногда', 'filename':GiveName('fr5b')}

fr6 = {'url': FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%EE%E1%FB%F7%ED%EE%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2='),
        'query': 'обычно', 'filename':GiveName('fr6')}

fr7 = {'url': FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=-%F1&gramm1=%28nom%7Cvoc%7Cgen%7Cgen2%7Cdat%7Cacc%7Cacc2%7Cloc%7Cloc2%7Cadnum%29&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%E2%F0%E5%EC%E5%ED%E0%EC%E8%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&mode=paper'),
        'query': 'временами', 'filename':GiveName('fr7')}

fr8 = {'url': FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&dpp=&spp=&spd=&text=lexgramm&mode=paper&sort=gr_tagging&lang=ru&parent1=0&level1=0&lex1=%22%ED%E8%EA%EE%E3%E4%E0%22&gramm1=&sem1=&flags1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&flags2='),
        'query': 'никогда', 'filename':GiveName('fr8')}

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

ex1 = {'url': FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&dpp=&spp=&spd=&text=lexgramm&mode=paper&sort=gr_tagging&lang=ru&parent1=0&level1=0&lex1=%22%ED%E5%F1%EA%EE%EB%FC%EA%EE%22%7C%22%EF%E0%F0%F3%22%7C%22%E4%E2%E0%22%7C%22%F2%F0%E8%22%7C%22%F7%E5%F2%FB%F0%E5%22%7C%22%EF%FF%F2%FC%22%7C%22%F8%E5%F1%F2%FC%22%7C%22%F1%E5%EC%FC%22%7C%22%E2%EE%F1%E5%EC%FC%22%7C%22%E4%E5%E2%FF%F2%FC%22%7C%22%E4%E5%F1%FF%F2%FC%22&gramm1=&sem1=&flags1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%E4%ED%E5%E9%22%7C%22%EB%E5%F2%22%7C%22%ED%E5%E4%E5%EB%FC%22%7C%22%F7%E0%F1%EE%E2%22%7C%22%EC%E8%ED%F3%F2%22&gramm2=&sem2=&flags2='),
        'filename':GiveName('ex1'), 'query': '"несколько"|"пару"|"два"|"три"|"четыре"|"пять"|"шесть"|"семь"|"восемь"|"девять"|"десять"][word="дней"|"лет"|"недель"|"часов"|"минут"]'}


#[lc="несколько|пару|два|три|четыре|пять|шесть|семь|восемь|девять|десять"][word="дней|лет|недель|часов|минут"][word!="назад|после|до|от|за|тому|спустя"]
#* -"назад" -"после" -"до" -"от" -"за" -"тому" -"спустя"

ex2a = {'url': urlprefix + '&lex1=%E8%E0&gramm1=&sem1=&sem-mod1=sem&sem-mod2=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=NUM%2C%28nom%7Cacc%29&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%E4%ED%E5%E9%22%7C%22%EB%E5%F2%22%7C%22%ED%E5%E4%E5%EB%FC%22%7C%22%F7%E0%F1%EE%E2%22%7C%22%EC%E8%ED%F3%F2%22%7C%22%F1%E5%EA%F3%ED%E4%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=' + urlpostfix,
        'query': 'за "дней"|"лет"|"недель"|"часов"|"минут"', 'filename':GiveName('ex2a')}

ex2b = {'url': FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E7%E0%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%FD%F2%EE%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%E2%F0%E5%EC%FF%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3='),
        'query': 'за это время', 'filename':GiveName('ex2b')}

ex3a = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E2%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%F2%E5%F7%E5%ED%E8%E5%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%FD%F2%EE%E9%22%7C%22%F2%EE%E9%22%7C%22%EF%F0%EE%F8%EB%EE%E3%EE%22%7C%22%F2%EE%E3%EE%22%7C%22%FD%F2%EE%E3%EE%22%7C%22%EF%F0%EE%F8%EB%EE%E9%22%7C%22%EF%EE%F1%EB%E5%E4%ED%E5%E3%EE%22%7C%22%EF%EE%F1%EB%E5%E4%ED%E5%E9%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=&parent4=0&level4=0&min4=1&max4=1&lex4=%22%E3%EE%E4%E0%22%7C%22%EC%E5%F1%FF%F6%E0%22%7C%22%ED%E5%E4%E5%EB%E8%22%7C%22%EB%E5%F2%E0%22%7C%22%EE%F1%E5%ED%E8%22%7C%22%E2%E5%F1%ED%FB%22&gramm4=&sem4=&sem-mod4=sem&sem-mod4=sem2&flags4=&m4='),
        'query': '"в" "течение" "этой"|"той"|"прошлого"|"того"|"этого"|"прошлой"|"последнего"|"последней" "года"|"месяца"|"недели"|"лета"|"осени"|"весны"','filename':GiveName('ex3a')}

ex3b = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E2%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%F2%E5%F7%E5%ED%E8%E5%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%E3%EE%E4%E0%22%7C%22%EC%E5%F1%FF%F6%E0%22%7C%22%ED%E5%E4%E5%EB%E8%22%7C%22%EB%E5%F2%E0%22%7C%22%EE%F1%E5%ED%E8%22%7C%22%E2%E5%F1%ED%FB%22&gramm3=&sem3=&sem-mod4=sem&sem-mod4=sem2&flags3=&m4='),
        'query': '"в" "течение" "года"|"месяца"|"недели"|"лета"|"осени"|"весны"','filename':GiveName('ex3b')}

ex4 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%ED%E0%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=NUM&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%EC%E5%F1%FF%F6%E5%E2%22%7C%22%E4%ED%E5%E9%22%7C%22%ED%E5%E4%E5%EB%FC%22%7C%22%EB%E5%F2%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3='),
        'query': '"на" ЧИСЛ "дней"|"недель"|"месяцев"|"лет"','filename':GiveName('ex4')}

ex5a = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E2%22%7C%22%E7%E0%22%7C%22%E2%EE%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%EC%E3%ED%EE%E2%E5%ED%E8%E5%22%7C%22%EC%E3%ED%EE%E2%E5%ED%FC%E5%22%7C%22%EC%E8%E3%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2='),
        'query': 'в мгновение|миг','filename':GiveName('ex5a')}

ex5b = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E2%E4%F0%F3%E3%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1='),
        'query': 'вдруг','filename':GiveName('ex5b')}

ex6 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E4%EE%EB%E3%EE%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1='),
        'query': 'долго','filename':GiveName('ex6')}

ex7 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E4%E0%E2%ED%EE%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&mode=paper'),
        'query': 'давно','filename':GiveName('ex7')}

#UUDET

lc10 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%F1&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%FF%ED%E2%E0%F0%FC%7C%F4%E5%E2%F0%E0%EB%FC%7C%EC%E0%F0%F2%7C%E0%EF%F0%E5%EB%FC%7C%EC%E0%E9%7C%E8%FE%ED%FC%7C%E8%FE%EB%FC%7C%E0%E2%E3%F3%F1%F2%7C%F1%E5%ED%F2%FF%E1%F0%FC%7C%EE%EA%F2%FF%E1%F0%FC%7C%ED%EE%FF%E1%F0%FC%7C%E4%E5%EA%E0%E1%F0%FC&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%EF%F0%EE%F8%EB%EE%E3%EE%22%7C%22%FD%F2%EE%E3%EE%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=&parent4=0&level4=0&min4=1&max4=1&lex4=%22%E3%EE%E4%E0%22&gramm4=&sem4=&sem-mod4=sem&sem-mod4=sem2&flags4=&m4=&mode=paper'),
        'query': 'с января прошлого года','filename':GiveName('lc10')}


lc11 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%E2&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=199*&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%E3%EE%E4%F3%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=&mode=paper'),
        'query': '','filename':GiveName('lc11')}

lc12 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%E2&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%EE%E4%E8%ED%22%7C%22%EE%E4%ED%EE%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%F3%F2%F0%EE%7C%E2%E5%F7%E5%F0%7C%E4%E5%ED%FC&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=&mode=paper'),
        'query': '','filename':GiveName('lc12')}

lc13 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%F1&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=19*&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%E3%EE%E4%E0%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=&parent4=0&level4=0&min4=1&max4=1&lex4=-%E4%EE%7C-%EF%EE&gramm4=&sem4=&sem-mod4=sem&sem-mod4=sem2&flags4=&m4=&mode=paper'),
        'query': '','filename':GiveName('lc13')}

lc14 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%EA%E0%EA-%F2%EE&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%F0%E0%E7%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&mode=paper'),'filename':GiveName('lc14')}

lc15 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%E2&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%F2%E0%EA%EE%E9%22%7C%22%F2%E0%EA%E8%E5%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%EC%EE%EC%E5%ED%F2%22%7C%22%EC%EE%EC%E5%ED%F2%FB%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=&mode=paper'),'filename':GiveName('lc15')}

lc16 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%E2%7C%E2%EE&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%E2%F2%EE%F0%ED%E8%EA%22%7C%22%F1%F0%E5%E4%F3%22%7C%22%F7%E5%F2%E2%E5%F0%E3%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&mode=paper'),'filename':GiveName('lc16')}

lc17 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%E2&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%EC%E0%F0%F2%E5%22%7C%22%EE%EA%F2%FF%E1%F0%E5%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=&gramm3=(S%7CA%7CV%7CADV%7CPRAEDIC%7CPARENTH%7CSPRO%7CAPRO%7CPRAEDICPRO%7CADVPRO%7CPR%7CCONJ%7CPART%7CINTJ)&sem3=&sem-mod4=sem&sem-mod4=sem2&flags3=&m4=&parent4=0&level4=0&min4=1&max4=1&lex4=-%22%E3%EE%E4%E0%22&gramm4=&sem4=&sem-mod3=sem&sem-mod3=sem2&flags4=&m3=&mode=paper'),'filename':GiveName('lc17')}

ex8 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=-%E2+-%ED%E0+-%F7%E5%F0%E5%E7+-%F1%EF%F3%F1%F2%FF&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%EA%E0%EA%EE%E5-%F2%EE%22%7C%22%ED%E5%EA%EE%F2%EE%F0%EE%E5%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=%E2%F0%E5%EC%FF&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=&parent4=0&level4=0&min4=1&max4=1&lex4=-%ED%E0%E7%E0%E4+-%22%F2%EE%EC%F3%22&gramm4=&sem4=&sem-mod4=sem&sem-mod4=sem2&flags4=&m4='),'filename':GiveName('ex8')}

ex9 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=-%22%EF%E5%F0%E2%F3%FE%22%20-%22%E2%F2%EE%F0%F3%FE%22%20-%22%F2%F0%E5%F2%FC%FE%22%20-%22%F1%E5%EC%E8%F1%F3%F2%EE%F7%ED%F3%FE%22%20-%22%EC%E0%F1%EB%E5%ED%E8%F7%ED%F3%FE%22%20-%22%F1%F2%F0%E0%F1%F2%ED%F3%FE%22%20-%22%EF%F0%E5%E4%EF%EE%F1%EB%E5%E4%ED%FE%FE%22%20-%22%F0%E0%E1%EE%F7%F3%FE%22%20-%22%E4%F0%F3%E3%F3%FE%22%20-%22%EC%E8%ED%F3%E2%F8%F3%FE%22%20-%22%EF%EE%F1%EB%E5%E4%F3%FE%F9%F3%FE%22%20-%22%EE%F1%F2%E0%E2%F8%F3%FE%F1%FF%22%20-%22%EF%F0%E5%E4%F1%F2%EE%FF%F9%F3%FE%22%20-%22%F1%EB%E5%E4%F3%FE%F9%F3%FE%22%20-%22%EF%F0%EE%F8%E5%E4%F8%F3%FE%22%20-%22%EF%F0%E5%E4%F8%E5%F1%F2%E2%F3%FE%F9%F3%FE%22%20-%22%EE%F1%F2%E0%EB%FC%ED%F3%FE%22%20-%22%EA%E0%E6%E4%F3%FE%22%20-%22%E2%22%20-%22%F7%E5%F0%E5%E7%22%20-%22%F1%EF%F3%F1%F2%FF%22%20-%22%F2%E0%EA%F3%FE%22%20-%22%ED%E0%22%20-%22%F2%F3%22%20-%22%E7%E0%22%20-%22%F6%E5%EB%F3%FE%22%20-%22%E2%F1%FE%22%20-%22%FD%F2%F3%22%20-%22%EF%F0%EE%F8%EB%F3%FE%22%20-%22%EF%F0%E5%E4%FB%E4%F3%F9%F3%FE%22%20-%22%EF%EE%F1%EB%E5%E4%ED%FE%FE%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%ED%E5%E4%E5%EB%FE%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=-%EF%EE%F1%EB%E5%20-%ED%E0%E7%E0%E4%20-%F1%EF%F3%F1%F2%FF%20-%22%F2%EE%EC%F3%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=&mode=paper'),'filename':GiveName('ex9')}

ex10 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E2%F1%FE%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%ED%E5%E4%E5%EB%FE%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=-%EF%EE%F1%EB%E5%20-%ED%E0%E7%E0%E4%20-%F1%EF%F3%F1%F2%FF%20-%22%F2%EE%EC%F3%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=&mode=paperhttp://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%22%E2%F1%FE%22&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%ED%E5%E4%E5%EB%FE%22&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&parent3=0&level3=0&min3=1&max3=1&lex3=-%EF%EE%F1%EB%E5%20-%ED%E0%E7%E0%E4%20-%F1%EF%F3%F1%F2%FF%20-%22%F2%EE%EC%F3%22&gramm3=&sem3=&sem-mod3=sem&sem-mod3=sem2&flags3=&m3=&mode=paper'),'filename':GiveName('ex10')}

ex11 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&dpp=&spp=&spd=&text=lexgramm&mode=paper&sort=gr_tagging&lang=ru&parent1=0&level1=0&lex1=%22%E1%FB%F1%F2%F0%EE%22&gramm1=&sem1=&flags1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&flags2='),'filename':GiveName('ex11')}

pr1 = {'url':FormUrl('http://search2.ruscorpora.ru/search.xml?env=alpha&mydocsize=&spd=&text=lexgramm&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1=%F3%E6%E5&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&mode=paper'),'filename':GiveName('pr1')}

lm1 = {'url':'http://search1.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&dpp=100&spp=&spd=&text=lexgramm&mode=paper&sort=gr_tagging&lang=ru&parent1=0&level1=0&lex1=%EE%EA%EE%EB%EE&gramm1=&sem1=&flags1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%F7%E0%F1%E0%22%7C%22%E4%E2%F3%F5%22%7C%22%F2%F0%B8%F5%22%7C%22%F2%F0%E5%F5%22%7C%22%F7%E5%F2%FB%F0%E5%F5%22%7C%22%F7%E5%F2%FB%F0%B8%F5%22%7C%22%EF%FF%F2%E8%22%7C%22%F8%E5%F1%F2%E8%22%7C%22%F1%E5%EC%E8%22%7C%22%E2%EE%F1%FC%EC%E8%22%7C%22%E4%E5%E2%FF%F2%E8%22%7C%22%E4%E5%F1%FF%F2%E8%22%7C%22%EE%E4%E8%ED%ED%E0%E4%F6%E0%F2%E8%22%7C%22%E4%E2%E5%ED%E0%E4%F6%E0%F2%E8%22&gramm2=&sem2=&flags2=', 'filename':GiveName('lm1')}

jp1 = {'url':'http://search1.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&dpp=100&spp=&spd=&text=lexgramm&mode=paper&sort=gr_tagging&lang=ru&parent1=0&level1=0&lex1=%EF%EE%F1%EB%E5&gramm1=&sem1=&flags1=&parent2=0&level2=0&min2=1&max2=1&lex2=%22%ED%EE%E2%EE%E3%EE%22&gramm2=&sem2=&flags2=&parent3=0&level3=0&min3=1&max3=1&lex3=%22%E3%EE%E4%E0%22&gramm3=&sem3=&flags3=','query':'"после нового года"', 'filename':GiveName('jp1')}

#-"первую" -"вторую" -"третью" -"семисуточную" -"масленичную" -"страстную" -"предпоследнюю" -"рабочую" -"другую" -"минувшую" -"последующую" -"оставшуюся" -"предстоящую" -"следующую" -"прошедшую" -"предшествующую" -"остальную" -"каждую" -"в" -"через" -"спустя" -"такую" -"на" -"ту" -"за" -"целую" -"всю" -"эту" -"прошлую" -"предыдущую" -"последнюю"
#-после -назад -спустя -"тому"
