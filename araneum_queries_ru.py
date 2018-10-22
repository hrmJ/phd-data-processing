def GiveName(string):
    return 'ru_araneum_{}'.format(string)

lc0a = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/viewattrsx?q=aword%2C[lc%3D%22%D0%B2%D1%87%D0%B5%D1%80%D0%B0%22]&corpname=AranRusj_b&viewmode=sen&refs=%3Ddoc.urldomain&fromp=1&setattrs=word&allpos=kw&attr_tooltip=nott&setstructs=doc&setstructs=p&setstructs=g&setrefs=%3Ddoc.urldomain&refs_up=0&pagesize=1000&newctxsize=40&gdex_enabled=0&show_gdex_scores=0&gdexcnt=100&copy_icon=0&multiple_copy=0&use_noflash=0&select_lines=0&line_numbers=0&shorten_refs=0',
        'query': '[lc="вчера"]', 'filename':GiveName('lc0a')}

lc0b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="сегодня"]', 'filename':GiveName('lc0b')}

lc0c = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="завтра"]', 'filename':GiveName('lc0c')}

lc1 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranRusj_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%B2%7C%D0%BD%D0%B0%22][word%3D%22%D0%BF%D1%80%D0%BE%D1%88%D0%BB%D0%BE%D0%BC%7C%D0%BF%D1%80%D0%BE%D1%88%D0%BB%D0%BE%D0%B9%22][word%3D%22%D0%B3%D0%BE%D0%B4%D1%83%7C%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="в|на"][word="прошлом|прошлой"][word="году|неделе"]','filename':GiveName('lc1')}

#ru2 link broken>>
lc2 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D1%83%D1%82%D1%80%D0%BE%D0%BC%7C%D0%B2%D0%B5%D1%87%D0%B5%D1%80%D0%BE%D0%BC%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="утром|вечером"]','filename':GiveName('lc2')}

lc3 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranRusj_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%22][word%3D%22%D0%B2%D0%BE%D0%B9%D0%BD%D1%8B%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="после"][word="войны"]', 'filename':GiveName('lc3')}

lc4 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D1%81%22][word%3D%22%D1%82%D0%B5%D1%85%22][word%3D%22%D0%BF%D0%BE%D1%80%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="с"][word="тех"][word="пор"]', 'filename':GiveName('lc4')}

lc5 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D1%87%D0%B5%D1%80%D0%B5%D0%B7%7C%D1%81%D0%BF%D1%83%D1%81%D1%82%D1%8F%22][][word%3D%22%D0%BB%D0%B5%D1%82%7C%D0%B4%D0%BD%D0%B5%D0%B9%7C%D1%81%D1%83%D1%82%D0%BE%D0%BA%7C%D1%87%D0%B0%D1%81%D0%BE%D0%B2%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="через|спустя"][][word="лет|дней|суток|часов"]', 'filename':GiveName('lc5')}

lc6 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranRusj_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%B2%22][][word%3D%22%D1%87%D0%B0%D1%81%D0%B0%7C%D1%87%D0%B0%D1%81%D0%BE%D0%B2%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="в"][][word="часа|часов"]', 'filename':GiveName('lc6')}

lc7a = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B2%22][word%3D%22%D1%82%D0%BE%22][word%3D%22%D0%B2%D1%80%D0%B5%D0%BC%D1%8F%22][word!%3D%22%D0%BA%D0%B0%D0%BA%7C%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0%7C%D0%B3%D0%BE%D0%B4%D0%B0%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="в"][word="то"][word="время"][word!="как|когда|года"]', 'filename':GiveName('lc7a')}

lc7b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D1%82%D0%BE%D0%B3%D0%B4%D0%B0%22][lc!%3D%22%D0%BA%D0%B0%D0%BA%7C%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="тогда"][lc!="как|когда"]','filename':GiveName('lc7b')}

lc8 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D1%81%D0%BA%D0%BE%D1%80%D0%BE%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="скоро"]', 'filename':GiveName('lc8')}

lc9a = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D1%82%D0%B5%D0%BF%D0%B5%D1%80%D1%8C%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="теперь"]','filename':GiveName('lc9a')}

lc9b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D1%81%D0%B5%D0%B9%D1%87%D0%B0%D1%81%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="сейчас"]','filename':GiveName('lc9b')}

# FREQ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><

fr1 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%BA%D0%B0%D0%B6%D0%B4%D1%8B%D0%B9%7C%D0%BA%D0%B0%D0%B6%D0%B4%D1%83%D1%8E%22][word%3D%22%D0%B4%D0%B5%D0%BD%D1%8C%7C%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8E%7C%D0%B3%D0%BE%D0%B4%7C%D0%BC%D0%B5%D1%81%D1%8F%D1%86%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="каждый|каждую"][word="день|неделю|год|месяц"]', 'filename':GiveName('fr1')}

fr2 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranRusj_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%BF%D0%BE%22][word%3D%22%D0%BF%D0%BE%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%B0%D0%BC%7C%D0%B2%D1%82%D0%BE%D1%80%D0%BD%D0%B8%D0%BA%D0%B0%D0%BC%7C%D1%81%D1%80%D0%B5%D0%B4%D0%B0%D0%BC%7C%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D0%B3%D0%B0%D0%BC%7C%D0%BF%D1%8F%D1%82%D0%BD%D0%B8%D1%86%D0%B0%D0%BC%7C%D1%81%D1%83%D0%B1%D0%B1%D0%BE%D1%82%D0%B0%D0%BC%7C%D0%B2%D0%BE%D0%BA%D1%80%D0%B5%D1%81%D0%B5%D0%BD%D1%8C%D1%8F%D0%BC%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="по"][word="понедельникам|вторникам|средам|четвергам|пятницам|субботам|вокресеньям"]', 'filename':GiveName('fr2')}

fr3a = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B4%D0%B2%D0%B0%7C%D1%82%D1%80%D0%B8%7C%D1%87%D0%B5%D1%82%D1%8B%D1%80%D0%B5%7C%D0%BF%D1%8F%D1%82%D1%8C%7C%D1%88%D0%B5%D1%81%D1%82%D1%8C%7C%D1%81%D0%B5%D0%BC%D1%8C%7C%D0%B2%D0%BE%D1%81%D0%B5%D0%BC%D1%8C%7C%D0%B4%D0%B5%D0%B2%D1%8F%D1%82%D1%8C%7C%D0%B4%D0%B5%D1%81%D1%8F%D1%82%D1%8C%22][word%3D%22%D1%80%D0%B0%D0%B7%D0%B0%7C%D1%80%D0%B0%D0%B7%22][word!%3D%22%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5%7C%D0%BC%D0%B5%D0%BD%D1%8C%D1%88%D0%B5%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="два|три|четыре|пять|шесть|семь|восемь|девять|десять"][word="раза|раз"][word!="больше|меньше"]', 'filename': GiveName('fr3a')}

fr3b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B4%D0%B2%D0%B0%D0%B6%D0%B4%D1%8B%7C%D1%82%D1%80%D0%B8%D0%B6%D0%B4%D1%8B%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="дважды|трижды"]', 'filename':GiveName('fr3b')}

fr4a = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D1%87%D0%B0%D1%81%D1%82%D0%BE%22];q=f;corpname=AranRusj_b&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000',
        'query': '[lc="часто"]', 'filename':GiveName('fr4a')}

fr4b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B2%D1%81%D0%B5%D0%B3%D0%B4%D0%B0%22]&q=f;corpname=AranRusj_b&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000;viewmode=sen;fromp=1',
        'query': '[lc="всегда"]','filename':GiveName('fr4b')}

fr5a = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D1%80%D0%B5%D0%B4%D0%BA%D0%BE%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="редко"]','filename' : GiveName('fr5a')}

fr5b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B8%D0%BD%D0%BE%D0%B3%D0%B4%D0%B0%22]&q=f;q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="иногда"]','filename' : GiveName('fr5b')}

fr6 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%BE%D0%B1%D1%8B%D1%87%D0%BD%D0%BE%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="обычно"]','filename' : GiveName('fr6')}

fr7 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B0%D0%BC%D0%B8%22];q=f;corpname=AranRusi_a&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="временами"]','filename' : GiveName('fr7')}

# EXT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><

ex1 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%7C%D0%BF%D0%B0%D1%80%D1%83%7C%D0%B4%D0%B2%D0%B0%7C%D1%82%D1%80%D0%B8%7C%D1%87%D0%B5%D1%82%D1%8B%D1%80%D0%B5%7C%D0%BF%D1%8F%D1%82%D1%8C%7C%D1%88%D0%B5%D1%81%D1%82%D1%8C%7C%D1%81%D0%B5%D0%BC%D1%8C%7C%D0%B2%D0%BE%D1%81%D0%B5%D0%BC%D1%8C%7C%D0%B4%D0%B5%D0%B2%D1%8F%D1%82%D1%8C%7C%D0%B4%D0%B5%D1%81%D1%8F%D1%82%D1%8C%22][word%3D%22%D0%B4%D0%BD%D0%B5%D0%B9%7C%D0%BB%D0%B5%D1%82%7C%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8C%7C%D1%87%D0%B0%D1%81%D0%BE%D0%B2%7C%D0%BC%D0%B8%D0%BD%D1%83%D1%82%22][word!%3D%22%D0%BD%D0%B0%D0%B7%D0%B0%D0%B4%7C%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%7C%D0%B4%D0%BE%7C%D0%BE%D1%82%7C%D0%B7%D0%B0%7C%D1%82%D0%BE%D0%BC%D1%83%7C%D1%81%D0%BF%D1%83%D1%81%D1%82%D1%8F%22];q=f;corpname=AranRusi_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="несколько|пару|два|три|четыре|пять|шесть|семь|восемь|девять|десять"][word="дней|лет|недель|часов|минут"][word!="назад|после|до|от|за|тому|спустя"]', 'filename':GiveName('ex1')}

ex2a = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B7%D0%B0%22][][word%3D%22%D0%B4%D0%BD%D0%B5%D0%B9%7C%D0%BB%D0%B5%D1%82%7C%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8C%7C%D1%87%D0%B0%D1%81%D0%BE%D0%B2%7C%D0%BC%D0%B8%D0%BD%D1%83%D1%82%22];q=f;corpname=AranRusi_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="за"][][word="дней|лет|недель|часов|минут"]', 'filename':GiveName('ex2a')}

ex2b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B7%D0%B0%22][word%3D%22%D1%8D%D1%82%D0%BE%22][word%3D%22%D0%B2%D1%80%D0%B5%D0%BC%D1%8F%22];q=f;corpname=AranRusi_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="за"][word="это"][word="время"]', 'filename':GiveName('ex2b')}

ex3a = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B2%22][word%3D%22%D1%82%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%22][word%3D%22%D1%8D%D1%82%D0%BE%D0%B9%7C%D1%82%D0%BE%D0%B9%7C%D0%BF%D1%80%D0%BE%D1%88%D0%BB%D0%BE%D0%B3%D0%BE%7C%D1%82%D0%BE%D0%B3%D0%BE%7C%D1%8D%D1%82%D0%BE%D0%B3%D0%BE%7C%D0%BF%D1%80%D0%BE%D1%88%D0%BB%D0%BE%D0%B9%7C%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BD%D0%B5%D0%B3%D0%BE%7C%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BD%D0%B5%D0%B9%22][word%3D%22%D0%B3%D0%BE%D0%B4%D0%B0%7C%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B0%7C%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D0%B8%7C%D0%BB%D0%B5%D1%82%D0%B0%7C%D0%BE%D1%81%D0%B5%D0%BD%D0%B8%7C%D0%B2%D0%B5%D1%81%D0%BD%D1%8B%22];q=f;corpname=AranRusi_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="в"][word="течение"][word="этой|той|прошлого|того|этого|прошлой|последнего|последней"][word="года|месяца|недели|лета|осени|весны"]', 'filename':GiveName('ex3a')}

ex3b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranRusi_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%B2%22][word%3D%22%D1%82%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%22][word%3D%22%D0%B3%D0%BE%D0%B4%D0%B0%7C%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B0%7C%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D0%B8%7C%D0%BB%D0%B5%D1%82%D0%B0%7C%D0%BE%D1%81%D0%B5%D0%BD%D0%B8%7C%D0%B2%D0%B5%D1%81%D0%BD%D1%8B%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="в"][word="течение"][word="года|месяца|недели|лета|осени|весны"]', 'filename':GiveName('ex3b')}

#----

ex4 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranRusj_ru.ru_ar13__b_a&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%BD%D0%B0%22][word%3D%22%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%7C%D0%BF%D0%B0%D1%80%D1%83%7C%D0%B4%D0%B2%D0%B0%7C%D1%82%D1%80%D0%B8%7C%D1%87%D0%B5%D1%82%D1%8B%D1%80%D0%B5%7C%D0%BF%D1%8F%D1%82%D1%8C%7C%D1%88%D0%B5%D1%81%D1%82%D1%8C%7C%D1%81%D0%B5%D0%BC%D1%8C%7C%D0%B2%D0%BE%D1%81%D0%B5%D0%BC%D1%8C%7C%D0%B4%D0%B5%D0%B2%D1%8F%D1%82%D1%8C%7C%D0%B4%D0%B5%D1%81%D1%8F%D1%82%D1%8C%22][word%3D%22%D0%B4%D0%BD%D0%B5%D0%B9%7C%D0%BB%D0%B5%D1%82%7C%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8C%7C%D1%87%D0%B0%D1%81%D0%BE%D0%B2%7C%D0%BC%D0%B8%D0%BD%D1%83%D1%82%7C%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B5%D0%B2%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="на"][word="несколько|пару|два|три|четыре|пять|шесть|семь|восемь|девять|десять"][word="дней|лет|недель|часов|минут|месяцев"]', 'filename':GiveName('ex4')}

ex5a = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranRusj_ru.ru_ar13__b_a&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%B2%7C%D0%B2%D0%BE%7C%D0%B7%D0%B0%22][word%3D%22%D0%BC%D0%B3%D0%BD%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C%D0%B5%7C%D0%BC%D0%B3%D0%BD%D0%BE%D0%B2%D0%B5%D0%BD%D0%B8%D0%B5%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="в|во|за"][word="мгновенье|мгновение"]', 'filename':GiveName('ex5a')}

ex5b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/viewattrsx?q=aword%2C[lc%3D%22%D0%B2%D0%B4%D1%80%D1%83%D0%B3%22]&q=f&corpname=AranRusi_b&viewmode=sen&refs=%3Ddoc.urldomain&fromp=1&setattrs=word&allpos=kw&attr_tooltip=nott&setstructs=doc&setstructs=p&setstructs=g&setrefs=%3Ddoc.urldomain&refs_up=0&pagesize=1000&newctxsize=40&gdex_enabled=0&show_gdex_scores=0&gdexcnt=100&copy_icon=0&multiple_copy=0&use_noflash=0&select_lines=0&line_numbers=0&shorten_refs=0',
        'query': '[lc="вдруг"]', 'filename':GiveName('ex5b')}

ex6 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B4%D0%BE%D0%BB%D0%B3%D0%BE%22];q=f;corpname=AranRusj_ru.ru_ar13__b_a&viewmode=sen&attrs=word&ctxattrs=word&structs=s&refs=%3Ddoc.urldomain&pagesize=200000',
        'query': '[lc="долго"]', 'filename':GiveName('ex6')}

ex7 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B4%D0%B0%D0%B2%D0%BD%D0%BE%22];q=f;corpname=AranRusi_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="давно"]', 'filename':GiveName('ex7')}

#UUDET

lc10 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/viewattrsx?q=aword%2C[lc%3D%22%D1%81%22][lemma%3D%22%D1%8F%D0%BD%D0%B2%D0%B0%D1%80%D1%8C%7C%D1%84%D0%B5%D0%B2%D1%80%D0%B0%D0%BB%D1%8C%7C%D0%BC%D0%B0%D1%80%D1%82%7C%D0%B0%D0%BF%D1%80%D0%B5%D0%BB%D1%8C%7C%D0%BC%D0%B0%D0%B9%7C%D0%B8%D1%8E%D0%BD%D1%8C%7C%D0%B8%D1%8E%D0%BB%D1%8C%7C%D0%B0%D0%B2%D0%B3%D1%83%D1%81%D1%82%7C%D1%81%D0%B5%D0%BD%D1%82%D1%8F%D0%B1%D1%80%D1%8C%7C%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8C%7C%D0%BD%D0%BE%D1%8F%D0%B1%D1%80%D1%8C%7C%D0%B4%D0%B5%D0%BA%D0%B0%D0%B1%D1%80%D1%8C%22][word%3D%22%D0%BF%D1%80%D0%BE%D1%88%D0%BB%D0%BE%D0%B3%D0%BE%7C%D1%8D%D1%82%D0%BE%D0%B3%D0%BE%22][word%3D%22%D0%B3%D0%BE%D0%B4%D0%B0%22]&corpname=AranRusj_b&viewmode=sen&refs=%3Ddoc.urldomain&fromp=1&setattrs=word&allpos=kw&attr_tooltip=nott&setstructs=doc&setstructs=p&setstructs=g&setrefs=%3Ddoc.urldomain&refs_up=0&pagesize=1000&newctxsize=40&gdex_enabled=0&show_gdex_scores=0&gdexcnt=100&copy_icon=0&multiple_copy=0&use_noflash=0&select_lines=0&line_numbers=0&shorten_refs=0&shorten_refs=1',
        'query': '[lc="с"][lemma="январь|февраль|март|апрель|май|июнь|июль|август|сентябрь|октябрь|ноябрь|декабрь"][word="прошлого|этого"][word="года"]','filename':GiveName('lc10')}

lc11 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranRusi_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc!%3D%22%D1%87%D0%B5%D0%BC%22][lc%3D%22%D0%B2%22][word%3D%22199.%22][word%3D%22%D0%B3%D0%BE%D0%B4%D1%83%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="в"][word="199."][word="году"]','filename':GiveName('lc11')}

lc12 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranRusi_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%B2%22][word%3D%22%D0%BE%D0%B4%D0%BD%D0%BE%7C%D0%BE%D0%B4%D0%B8%D0%BD%22][word%3D%22%D1%83%D1%82%D1%80%D0%BE%7C%D0%B2%D0%B5%D1%87%D0%B5%D1%80%7C%D0%B4%D0%B5%D0%BD%D1%8C%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="в"][word="одно|один"][word="утро|вечер|день"]','filename':GiveName('lc12')}

lc13 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D1%81%22][word%3D%2219..%22][word%3D%22%D0%B3%D0%BE%D0%B4%D0%B0%22][word!%3D%22%D0%B4%D0%BE%7C%D0%BF%D0%BE%22];q=f;corpname=AranRusi_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="с"][word="19.."][word="года"][word!="до|по"]','filename':GiveName('lc13')}

lc14 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranRusj_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%BA%D0%B0%D0%BA-%D1%82%D0%BE%22][word%3D%22%D1%80%D0%B0%D0%B7%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="как-то"][word="раз"]','filename':GiveName('lc14')}

lc15 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranRusi_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%B2%22][lemma%3D%22%D1%82%D0%B0%D0%BA%D0%BE%D0%B9%22][lc%3D%22%D0%BC%D0%BE%D0%BC%D0%B5%D0%BD%D1%82%7C%D0%BC%D0%BE%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="в"][lemma="такой"][lc="момент|моменты"]','filename':GiveName('lc15')}

lc16 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%B2%7C%D0%B2%D0%BE%22][lc%3D%22%D0%B2%D1%82%D0%BE%D1%80%D0%BD%D0%B8%D0%BA%7C%D1%81%D1%80%D0%B5%D0%B4%D1%83%7C%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D0%B3%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="в|во"][lc="вторник|среду|четверг"]','filename':GiveName('lc16')}

lc17 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranRusj_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%B2%22][lc+%3D+%22%D0%BC%D0%B0%D1%80%D1%82%D0%B5%7C%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D0%B5%22][tag!%3D%22M.*%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="в"][lc = "марте|октябре"][tag!="M.*"]','filename':GiveName('lc17')}

ex8 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%BA%D0%B0%D0%BA%D0%BE%D0%B5-%D1%82%D0%BE%7C%D0%BD%D0%B5%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D0%BE%D0%B5%22][word%3D%22%D0%B2%D1%80%D0%B5%D0%BC%D1%8F%22][word!%3D%22%D0%BD%D0%B0%D0%B7%D0%B0%D0%B4%7C%D1%82%D0%BE%D0%BC%D1%83%22];q=f;corpname=AranRusi_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="какое-то|некоторое"][word="время"][word!="назад|тому"]','filename':GiveName('ex8')}

ex9 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8E%22][word!%3D%22%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%7C%D0%BD%D0%B0%D0%B7%D0%B0%D0%B4%7C%D1%81%D0%BF%D1%83%D1%81%D1%82%D1%8F%7C%D1%82%D0%BE%D0%BC%D1%83%22];q=f;corpname=AranRusj_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="неделю"][word!="после|назад|спустя|тому"]','filename':GiveName('ex9')}

ex10 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranRusi_a&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22%D0%B2%D1%81%D1%8E%22][lc%3D%22%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8E%22][word!%3D%22%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%7C%D0%BD%D0%B0%D0%B7%D0%B0%D0%B4%7C%D1%81%D0%BF%D1%83%D1%81%D1%82%D1%8F%7C%D1%82%D0%BE%D0%BC%D1%83%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="всю"][lc="неделю"][word!="после|назад|спустя|тому"]','filename':GiveName('ex10')}

#ARANEUM: '[lc!="kun|jos|koska"][lc!="kun|jos|koska"][lc!=".*lleen|kun|jos|koska|ei|ensi|viime|vain|ainakin|vähintään|kuin|edes|taas|viel.*|jo|vasta|joka|usean.*|vielÃ¤|Olipa" & tag!=".*Gen.*" & tag!="Num.*"][word="kerran"][tag != "PrfPrc.*|AgPcp.*" & tag!=".*Ine.*" & tag!=".*PrsPrc.*" & word !="viel.*|kun|jos|koska|toisensa|vuoteen|viikkoon|päivään|kuukauteen|tai|vaan"][word!="ajassa.*|toisenkin|kahdesti|kolmesti|neljästi"]'
