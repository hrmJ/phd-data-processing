from utils import Group

testgroups= {'lc4' : Group('lc4','ru',{'token':('с',)},depcond=['token',('пор',)],lengthmeter=[0,2])}

subgroups= {'lc0a' : Group('lc0a','ru',{'lemma':('вчера',)}, nextcond=[['!token'],[['утром','вечером','днем','днём','ночью','около','часов']]],secondnextcond=[['!token', '!lemma'],[['утра','полудня','вечера','ночи','обеда'],['два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','половина']]],lengthmeter=[0,0]),
            'lc0b' : Group('lc0b','ru',{'lemma':('сегодня',)}, nextcond=[['!token'],[['утром','вечером','днем','днём','ночью','около','часов']]],secondnextcond=[['!token', '!lemma'],[['утра','полудня','вечера','ночи','обеда'],['два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','половина']]],lengthmeter=[0,0]),
            'lc0c' : Group('lc0c','ru',{'lemma':('завтра',)}, nextcond=[['!token'],[['утром','вечером','днем','днём','ночью','около','часов']]],secondnextcond=[['!token', '!lemma'],[['утра','полудня','вечера','ночи','обеда'],['два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','половина']]],lengthmeter=[0,0]),
            'lc1' : Group('lc1','ru',{'token':('в', 'на')},nextcond=['token',('прошлом','прошлой')], depcond=['token',('году','неделе')],lengthmeter=[0,2]),
            'lc2' : Group('lc2','ru',{'token':('утром', 'вечером')},prevcond=['!token',('вчера','сегодня','завтра')],secondnextcond=[['!token'],[['два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','половина']]],lengthmeter=[0,0]),
            'lc3' : Group('lc3','ru',{'token':('после',)},depcond=['token',('войны',)],lengthmeter=[0,1]),
            'lc4' : Group('lc4','ru',{'token':('с',)},depcond=['token',('пор',)],lengthmeter=[0,2]),
            'lc5' : Group('lc5','ru',{'token':('через','спустя')},depcond=['token',('лет', 'дней', 'суток', 'часов')],lengthmeter=[0,2]),
            'lc6' : Group('lc6','ru',{'token':('в',)},depcond=['token',('часа', 'часов')],prevcond=['!token',('сегодня','завтра','вчера','позавчера')],lengthmeter=[0,2]),
            'lc7a' : Group('lc7a','ru',{'token':('в',)}, nextcond=['token','то'], depcond=['token','время'], thirdnextcond=['!token',('как','когда')], countcomma=False,lengthmeter=[0,2]),
            'lc7b' : Group('lc7b','ru',{'token':('тогда',)},nextcond=['!token',('как','когда','если')], countcomma=False,lengthmeter=[0,0]),
            'lc8' : Group('lc8','ru',{'token':('скоро',)},nextcond=['!token',('после',)],lengthmeter=[0,0]),
            'lc9a' : Group('lc9a','ru',{'token':('теперь',)},nextcond=['!token',('как','когда')], countcomma=False,lengthmeter=[0,0]),
            'lc9b' : Group('lc9b','ru',{'token':('сейчас',)},nextcond=['!token',('как','когда')], countcomma=False,lengthmeter=[0,0]),
            'lc10' : Group('lc10','ru',{'token':('с',)},secondnextcond=['token',('прошлого','этого')],nextcond=['lemma',('январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')],lengthmeter=[0,2]),
            'lc11' : Group('lc11','ru',{'token':('в',)},nextcond=['#token','199.'],secondnextcond=['token',('году',)],lengthmeter=[0,2]),
            'lc12' : Group('lc12','ru',{'token':('в',)},nextcond=['token',('одно','один')],secondnextcond=['token',('день','утро','вечер')],prevcond=['!token',('раз','раза')],lengthmeter=[0,2]),
            'lc13' : Group('lc13','ru',{'token':('с',)},nextcond=['#token','19..',],secondnextcond=['token',('года',)],thirdnextcond=['!token',('до','по')],lengthmeter=[0,2]),
            'lc15' : Group('lc15','ru',{'token':('в',)},nextcond=['lemma',('такой',)],secondnextcond=['token',('момент','моменты')],lengthmeter=[0,2]),
            'lc16' : Group('lc16','ru',{'token':('в','во')},nextcond=['token',('вторник','среду','четверг')],lengthmeter=[0,1]),
            'lc17' : Group('lc17','ru',{'token':('в','во')},nextcond=['token',('марте','октябре')],secondnextcond=['¤feat','M.*'],lengthmeter=[0,1]),
            'fr1' : Group('fr1','ru',{'token':('день', 'неделю', 'год', 'месяц')},depcond=['token',('каждый', 'каждую')],secondpreviouscond=['!token',('на',)],lengthmeter=[1,0]),
            'fr2' : Group('fr2','ru',{'token':('по',)},nextcond=['token',('понедельникам', 'вторникам', 'средам', 'четвергам', 'пятницам', 'субботам', 'вокресеньям')],lengthmeter=[0,1]),
            'fr3a' : Group('fr3a','ru',{'token':('раза', 'раз')},secondpreviouscond=['!token',('в',)],nextcond=[['!token','¤feat'],[['больше','меньше','лучше','дальше'],'.*cm.*']], secondnextcond=['!token',('чем',)], depcond=['token',('два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')],lengthmeter=[1,0]),
            'fr3b' : Group('fr3b','ru',{'token':('дважды', 'трижды')},lengthmeter=[0,0]),
            'fr4a' : Group('fr4a','ru',{'token':('часто',)},lengthmeter=[0,0]),
            'fr4b' : Group('fr4b','ru',{'token':('всегда',)},lengthmeter=[0,0]),
            'fr5a' : Group('fr5a','ru',{'token':('редко',)},lengthmeter=[0,0]),
            'fr5b' : Group('fr5b','ru',{'token':('иногда',)},lengthmeter=[0,0]),
            'fr6' : Group('fr6','ru',{'token':('обычно',)},lengthmeter=[0,0]),
            'fr7' : Group('fr7','ru',{'token':('временами',)},prevcond=[['!token','¤feat'],[['с'],'.*i.']],lengthmeter=[0,0]),
            'fr8' : Group('fr8','ru',{'token':('никогда',)}, nextcond=['!token',('раньше',)], prevcond=['!token',('чем',)], countcomma=False,lengthmeter=[0,0]),
            'ex1' : Group('ex1','ru',{'token':('дней', 'лет', 'недель', 'часов', 'минут')}, prevcond=['token',('несколько', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')],nextcond=['!token',('назад', 'после', 'до', 'от', 'за', 'тому', 'спустя','заключения')], secondnextcond=['!token',('назад', 'после', 'до', 'от', 'за', 'тому', 'спустя')], secondpreviouscond=['!token',('от', 'в', 'за', 'от', 'c', 'после', 'до', 'через', 'спустя', 'после', 'на','исполнится','исполнилось')],lengthmeter=[1,0]),
            'ex1b' : Group('ex1b','ru',{'token':('пару',)},nextcond=['token',('дней', 'лет', 'недель', 'часов', 'минут')], secondnextcond=['!token',('назад', 'после', 'до', 'от', 'за', 'тому', 'спустя')], prevcond=['!token',('от', 'в', 'за', 'от', 'c', 'после', 'до', 'через', 'спустя', 'после', 'на','исполнится','исполнилось')],lengthmeter=[0,1]),
            'ex2a' : Group('ex2a','ru',{'token':('за',)}, depcond=['token',('дней', 'лет', 'недель', 'часов', 'минут')],lengthmeter=[0,2]),
            'ex2b' : Group('ex2b','ru',{'token':('за',)}, depcond=['token',('время',)],lengthmeter=[0,2]),
            'ex3a' : Group('ex3a','ru',{'token':('в',)}, depcond=['token',('течение',)], secondnextcond=['token',('этой', 'той', 'прошлого', 'того', 'этого', 'прошлой', 'последнего', 'последней')],lengthmeter=[0,3]),
            'ex3b' : Group('ex3b','ru',{'token':('в',)}, depcond=['token',('течение',)], secondnextcond=['token',('года', 'месяца', 'недели', 'лета', 'осени', 'весны')],lengthmeter=[0,2]),
            'ex4' : Group('ex4','ru',{'token':('на',)}, secondnextcond=['token',('дней', 'лет', 'недель', 'часов', 'минут', 'месяцев')],lengthmeter=[0,2]),
            'ex5a' : Group('ex5a','ru',{'token':('в', 'во', 'за')}, nextcond=['token',('мгновенье','мгновение')],lengthmeter=[0,1]),
            'ex5b' : Group('ex5b','ru',{'token':('вдруг',)},lengthmeter=[0,0]),
            'ex6' : Group('ex6','ru',{'token':('долго',)},lengthmeter=[0,0]),
            'ex7' : Group('ex7','ru',{'token':('давно',)},lengthmeter=[0,0]),
            'ex8' : Group('ex8','ru',{'token':('время',)},secondpreviouscond=['!token',('в', 'на', 'через', 'спустя')],prevcond=['token',('какое-то','некоторое')],nextcond=['!token',('назад','тому','после','спустя','через')],lengthmeter=[1,0]),
            'ex9' : Group('ex9','ru',{'token':('неделю',)},prevcond=['!token',('в', 'на', 'через', 'спустя','ту','прошлую','семисуточную', 'масленичную', 'страстную', 'предпоследнюю', 'рабочую', 'другую', 'минувшую', 'последующую', 'оставшуюся', 'предстоящую', 'следующую', 'прошедшую', 'предшествующую', 'остальную', 'каждую', 'в', 'через', 'спустя', 'такую', 'на', 'ту', 'за', 'целую', 'всю', 'эту', 'прошлую', 'предыдущую', 'последнюю')],nextcond=['!token',('назад','тому','после','спустя','через')],lengthmeter=[0,0]),
            'ex10' : Group('ex10','ru',{'token':('неделю',)},prevcond=['token',('всю',)],nextcond=['!token',('после', 'назад', 'спустя', 'тому')],lengthmeter=[1,0]),
            'ex11' : Group('ex11','ru',{'token':('быстро',)},lengthmeter=[0,0]),
            'pr1' : Group('pr1','ru',{'token':('уже',)},lengthmeter=[0,0]),
            'pr2' : Group('pr2','ru',{'token':('еще','ещё')},lengthmeter=[0,0]),
            'pr3' : Group('pr3','ru',{'token':('больше',)}, nextcond=['!token',('чем',)], countcomma=False,lengthmeter=[0,0]),
            'lm1a' : Group('lm1a','ru',{'token':('около',)}, nextcond=['token',('часа','двух','трёх','трех','четырёх','четырех','пяти','шести','восьми','девяти','десяти','одиннадцати','дведандцати')],secondnextcond=['¤feat','.*pg.'], name_in_db = 'lm1',lengthmeter=[0,1]),
            'lm1b' : Group('lm1b','ru',{'token':('около',)}, nextcond=['token',('двух','трёх','трех','четырёх','четырех','пяти','шести','восьми','девяти','десяти','одиннадцати','дведандцати')],secondnextcond=['token',('часов','часа')], name_in_db = 'lm1', lengthmeter=[0,2]),
            }


# Kun lisäät muita alaryhmiä, käytä tietokantojen osalta simple_insert.py-skriptiä.
