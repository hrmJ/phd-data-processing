def GiveName(string):
    return 'fi_araneum_{}'.format(string)

#tag!=".*PrsPrc.*|.*AgPcp.*|PrfPrc_(Act|Pass)_(Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra)"
#word!="klo|illalla|aamulla|päivällä|kello|yhdeltä|kahdelta|kolmelta|neljältä|viideltä|kuudelta|keskiviikkona|maanantaina|tiistaina|keskiviikkona|torstaina|perjantaina"
#yhdeltä|kahdelta|kolmelta|neljältä|viideltä|kuudelta|seitsemältä|kahdeksalta|yhdeksältä|kymmeneltä|yhdeltätoista|kahdeltatoista

lc0a = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22eilen%22][tag!%3D%22Num.*%22+%26+word!%3D%22klo|illalla|aamulla|p%C3%A4iv%C3%A4ll%C3%A4%7Ckello|yhdelt%C3%A4%7Ckahdelta|kolmelta|nelj%C3%A4lt%C3%A4%7Cviidelt%C3%A4%7Ckuudelta|keskiviikkona|maanantaina|tiistaina|keskiviikkona|torstaina|perjantaina%22+%26+tag!%3D%22.*PrsPrc.*|.*AgPcp.*|PrfPrc_%28Act|Pass%29_%28Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra%29.*%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="eilen"][tag!="Num.*" & word!="klo|illalla|aamulla|päivällä|kello|yhdeltä|kahdelta|kolmelta|neljältä|viideltä|kuudelta|keskiviikkona|maanantaina|tiistaina|keskiviikkona|torstaina|perjantaina" & tag!=".*PrsPrc.*|.*AgPcp.*|PrfPrc_(Act|Pass)_(Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra).*"]', 'filename':GiveName('lc0a')}

lc0b = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_x&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22t%C3%A4n%C3%A4%C3%A4n%22][tag!%3D%22Num.*%22+%26+word!%3D%22klo|illalla|aamulla|p%C3%A4iv%C3%A4ll%C3%A4%7Ckello|yhdelt%C3%A4%7Ckahdelta|kolmelta|nelj%C3%A4lt%C3%A4%7Cviidelt%C3%A4%7Ckuudelta|keskiviikkona|maanantaina|tiistaina|keskiviikkona|torstaina|perjantaina%22+%26+tag!%3D%22.*PrsPrc.*|.*AgPcp.*|PrfPrc_%28Act|Pass%29_%28Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra%29.*%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="tänään"][tag!="Num.*" & word!="klo|illalla|aamulla|päivällä|kello|yhdeltä|kahdelta|kolmelta|neljältä|viideltä|kuudelta|keskiviikkona|maanantaina|tiistaina|keskiviikkona|torstaina|perjantaina" & tag!=".*PrsPrc.*|.*AgPcp.*|PrfPrc_(Act|Pass)_(Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra).*"]','filename':GiveName('lc0b')}

lc0c = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22huomenna%22][tag!%3D%22Num.*%22+%26+word!%3D%22klo|illalla|aamulla|p%C3%A4iv%C3%A4ll%C3%A4%7Ckello|yhdelt%C3%A4%7Ckahdelta|kolmelta|nelj%C3%A4lt%C3%A4%7Cviidelt%C3%A4%7Ckuudelta|keskiviikkona|maanantaina|tiistaina|keskiviikkona|torstaina|perjantaina%22+%26+tag!%3D%22.*PrsPrc.*|.*AgPcp.*|PrfPrc_%28Act|Pass%29_%28Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra%29.*%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="huomenna"][tag!="Num.*" & word!="klo|illalla|aamulla|päivällä|kello|yhdeltä|kahdelta|kolmelta|neljältä|viideltä|kuudelta|keskiviikkona|maanantaina|tiistaina|keskiviikkona|torstaina|perjantaina" & tag!=".*PrsPrc.*|.*AgPcp.*|PrfPrc_(Act|Pass)_(Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra).*"]','filename':GiveName('lc0c')}

lc1 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_x&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22viime%22][word%3D%22viikolla|vuonna|p%C3%A4ivin%C3%A4%7Cvuosina%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="viime"][word="viikolla|vuonna|päivinä|vuosina"]','filename':GiveName('lc1')}

lc2 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc!%3D%22eilen|huomenna|t%C3%A4n%C3%A4%C3%A4n|maanantaina|tiistaina|keskiviikkona|torstaina|perjantaina|lauantaina|sunnuntauna|my%C3%B6h%C3%A4%C3%A4n|varhain|aikaisin|yhdelt%C3%A4%7Ckahdelta|kolmelta|nelj%C3%A4lt%C3%A4%7Cviidelt%C3%A4%7Ckuudelta|seitsem%C3%A4lt%C3%A4%7Ckahdeksalta|yhdeks%C3%A4lt%C3%A4%7Ckymmenelt%C3%A4%7Cyhdelt%C3%A4toista|kahdeltatoista%22][lc%3D%22aamulla|illalla%22][word!%3D%22varhain|puoli|kello|klo|yhdelt%C3%A4%7Ckahdelta|kolmelta|nelj%C3%A4lt%C3%A4%7Cviidelt%C3%A4%7Ckuudelta|seitsem%C3%A4lt%C3%A4%7Ckahdeksalta|yhdeks%C3%A4lt%C3%A4%7Ckymmenelt%C3%A4%7Cyhdelt%C3%A4toista|kahdeltatoista%22+%26+tag!%3D%22Num.*%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc!="eilen|huomenna|tänään|maanantaina|tiistaina|keskiviikkona|torstaina|perjantaina|lauantaina|sunnuntauna|myöhään|varhain|aikaisin|yhdeltä|kahdelta|kolmelta|neljältä|viideltä|kuudelta|seitsemältä|kahdeksalta|yhdeksältä|kymmeneltä|yhdeltätoista|kahdeltatoista"][lc="aamulla|illalla"][word!="varhain|puoli|kello|klo|yhdeltä|kahdelta|kolmelta|neljältä|viideltä|kuudelta|seitsemältä|kahdeksalta|yhdeksältä|kymmeneltä|yhdeltätoista|kahdeltatoista" & tag!="Num.*"]','filename':GiveName('lc2')}

lc3 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22sodan%22][word%3D%22j%C3%A4lkeen%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="sodan"][word="jälkeen"]','filename':GiveName('lc3')}

lc4 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22siit%C3%A4%22][word%3D%22asti|l%C3%A4htien|pit%C3%A4en%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="siitä"][word="asti|lähtien|pitäen"]','filename':GiveName('lc4')}

lc5 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[][word%3D%22vuoden|p%C3%A4iv%C3%A4n|viikon|tunnin%22][word%3D%22p%C3%A4%C3%A4st%C3%A4%7Ckuluttua%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[][word="vuoden|päivän|viikon|tunnin"][word="päästä|kuluttua"]','filename':GiveName('lc5')}

lc6 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22kahdelta|kolmelta|nelj%C3%A4lt%C3%A4%7Cviidelt%C3%A4%7Ckuudelta|seitsem%C3%A4lt%C3%A4%7Ckahdeksalta|yhdeks%C3%A4lt%C3%A4%7Ckymmenelt%C3%A4%7Cyhdelt%C3%A4toista|kahdeltatoista%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="kahdelta|kolmelta|neljältä|viideltä|kuudelta|seitsemältä|kahdeksalta|yhdeksältä|kymmeneltä|yhdeltätoista|kahdeltatoista"]','filename':GiveName('lc6')}

lc7a = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22siihen%22][word%3D%22aikaan%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="siihen"][word="aikaan"]','filename':GiveName('lc7a')}

lc7b = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_x&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22silloin%22][lc!%3D%22kuin|kun|%2C|t%C3%A4ll%C3%B6in%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="silloin"][lc!="kuin|kun|,|tällöin"]','filename':GiveName('lc7b')}

lc8 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_x&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22pian%22][word!%3D%22t%C3%A4m%C3%A4n|kuin%22+%26+tag!%3D%22.*PrsPrc.*|.*AgPcp.*|PrfPrc_%28Act|Pass%29_%28Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra%29%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="pian"][word!="tämän|kuin" & tag!=".*PrsPrc.*|.*AgPcp.*|PrfPrc_(Act|Pass)_(Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra)"]','filename':GiveName('lc8')}

lc9a = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_x&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22nykyisin|nyky%C3%A4%C3%A4n%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="nykyisin|nykyään"]','filename':GiveName('lc9a')}

lc9b = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22nyt%22];q=f;corpname=AranFinn_x&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="nyt"]','filename':GiveName('lc9b')}


# Freq >>>>>>>>>>

fr1 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22joka%22][word%3D%22p%C3%A4iv%C3%A4%7Cviikko|vuosi|kuukausi%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="joka"][word="päivä|viikko|vuosi|kuukausi"]','filename':GiveName('fr1')}

fr2 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22maanantaisin|tiistaisin|keskiviikkoisin|torstaisin|perjantaisin|lauantaisin|sunnuntaisin%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="maanantaisin|tiistaisin|keskiviikkoisin|torstaisin|perjantaisin|lauantaisin|sunnuntaisin"]','filename':GiveName('fr2')}

fr3a = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_x&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%222|3|4|5|6|7|8|9|10|kaksi|kolme|nelj%C3%A4%7Cviisi|kuusi|seitsem%C3%A4n|kahdeksan|yhdeks%C3%A4n|kymmenen%22][word%3D%22kertaa%22][tag!%3D%22A_Com%22+%26+word!%3D%22.*empi.*|.*empaa.*|useammin|harvemmin|.*mmin|niin|enemm%C3%A4n|isompi|suurempi|isomma*|suuremma*|viikossa|p%C3%A4iv%C3%A4ss%C3%A4%7Cvuodessa|kuukaudessa|tunnissa|sekunnissa|aamussa|illassa%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="2|3|4|5|6|7|8|9|10|kaksi|kolme|neljä|viisi|kuusi|seitsemän|kahdeksan|yhdeksän|kymmenen"][word="kertaa"][tag!="A_Com" & word!=".*empi.*|.*empaa.*|useammin|harvemmin|.*mmin|niin|enemmän|isompi|suurempi|isomma*|suuremma*|viikossa|päivässä|vuodessa|kuukaudessa|tunnissa|sekunnissa|aamussa|illassa"]','filename':GiveName('fr3a')}

fr3b = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22kahdesti|kolmesti|nelj%C3%A4sti|viidesti%22][word!%3D%22viikossa|p%C3%A4iv%C3%A4ss%C3%A4%7Cvuodessa|kuukaudessa|tunnissa|sekunnissa|aamussa|illassa%22];fromp=2;corpname=AranFinn_x&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott;navpos=next',
        'query': '[lc="kahdesti|kolmesti|neljästi|viidesti"][word!="viikossa|päivässä|vuodessa|kuukaudessa|tunnissa|sekunnissa|aamussa|illassa"]','filename':GiveName('fr3b')}

fr4a = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22usein%22];q=f;corpname=AranFinn_x&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="usein"]','filename':GiveName('fr4a')}

fr4b = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22aina%22];q=f;corpname=AranFinn_x&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="aina"]','filename':GiveName('fr4b')}

fr5a = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22harvoin%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="harvoin"]','filename':GiveName('fr5a')}

fr5b = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22joskus%22];q=f;corpname=AranFinn_x&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="joskus"]','filename':GiveName('fr5b')}

fr6 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22tavallisesti|yleens%C3%A4%22];q=f;corpname=AranFinn_x&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="tavallisesti|yleensä"]','filename':GiveName('fr6')}

fr7 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22ajoittain%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="ajoittain"]','filename':GiveName('fr7')}

# Ext >>>>>>>>>>>>>


ex1 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%222|3|4|5|6|7|8|9|10|kaksi|kolme|nelj%C3%A4%7Cviisi|kuusi|seitsem%C3%A4n|kahdeksan|yhdeks%C3%A4n|kymmenen%22][word+%3D+%22p%C3%A4iv%C3%A4%C3%A4%7Cvuotta|viikkoa|tuntia%22][tag!%3D%22.*PrsPrc.*|.*AgPcp.*|PrfPrc_%28Act|Pass%29_%28Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra%29%22+%26+word!%3D%22kest%C3%A4nyt|vankeutta|ehdonalaista%22+%26+lemma+!%3D+%22ennen|j%C3%A4lkeen|aiempi|my%C3%B6hempi|aiemmin|my%C3%B6hemmin|vanha|sitten%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="2|3|4|5|6|7|8|9|10|kaksi|kolme|neljä|viisi|kuusi|seitsemän|kahdeksan|yhdeksän|kymmenen"][word = "päivää|vuotta|viikkoa|tuntia"][tag!=".*PrsPrc.*|.*AgPcp.*|PrfPrc_(Act|Pass)_(Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra)" & word!="kestänyt|vankeutta|ehdonalaista" & lemma != "ennen|jälkeen|aiempi|myöhempi|aiemmin|myöhemmin|vanha|sitten"]','filename':GiveName('ex1')}

ex2a = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22kahdessa|kolmessa|nelj%C3%A4ss%C3%A4%7Cviidess%C3%A4%7Ckuudessa|seitsem%C3%A4ss%C3%A4%7Ckahdeksassa|yhdeks%C3%A4ss%C3%A4%7Ckymmeness%C3%A4%22][word+%3D+%22p%C3%A4iv%C3%A4ss%C3%A4%7Cvuodessa|viikossa|tunnissa%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="kahdessa|kolmessa|neljässä|viidessä|kuudessa|seitsemässä|kahdeksassa|yhdeksässä|kymmenessä"][word = "päivässä|vuodessa|viikossa|tunnissa"]','filename':GiveName('ex2a')}

ex2b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22siin%C3%A4%22][word%3D%22ajassa%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="siinä"][word="ajassa"]','filename':GiveName('ex2b')}

ex3a = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22viime|koko|sen|tuon%22][word%3D%22vuoden|viikon|kuukauden|kes%C3%A4n|kev%C3%A4%C3%A4n|syksyn|talven%22][word%3D%22aikana%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="viime|koko|sen|tuon"][word="vuoden|viikon|kuukauden|kesän|kevään|syksyn|talven"][word="aikana"]','filename':GiveName('ex3a')}

ex3b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22vuoden|viikon|kuukauden|kes%C3%A4n|kev%C3%A4%C3%A4n|syksyn|talven%22][word%3D%22kuluessa%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="vuoden|viikon|kuukauden|kesän|kevään|syksyn|talven"][word="kuluessa"]','filename':GiveName('ex3b')}

ex4 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%222|3|4|5|6|7|8|9|10|kahdeksi|kolmeksi|nelj%C3%A4ksi|viisiksi|kuusiksi|seitsem%C3%A4nksi|kahdeksaksi|yhdeks%C3%A4ksi|kymmeneksi%22][word+%3D+%22kuukaudeksi|viikoksi|p%C3%A4iv%C3%A4ksi|vuodeksi|tunniksi%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="2|3|4|5|6|7|8|9|10|kahdeksi|kolmeksi|neljäksi|viisiksi|kuusiksi|seitsemäksi|kahdeksaksi|yhdeksäksi|kymmeneksi"][word = "kuukaudeksi|viikoksi|päiväksi|vuodeksi|tunniksi"]','filename':GiveName('ex4')}

ex5a = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22hetkess%C3%A4%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="hetkessä"]','filename':GiveName('ex5a')}

ex5b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22%C3%A4kki%C3%A4%7Cyht%C3%A4kki%C3%A4%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="äkkiä|yhtäkkiä"]','filename':GiveName('ex5b')}

ex6 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22kauan%22][word!%3D%22kuin|sitten%22+%26+tag!%3D%22.*PrsPrc.*|.*AgPcp.*|PrfPrc_%28Act|Pass%29_%28Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra%29%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="kauan"][word!="kuin|sitten" & tag!=".*PrsPrc.*|.*AgPcp.*|PrfPrc_(Act|Pass)_(Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra)"]','filename':GiveName('ex6')}

ex7 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22pitk%C3%A4%C3%A4n|pitkiin%22][word%3D%22aikaan|aikoihin%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="pitkään|pitkiin"][word="aikaan|aikoihin"]','filename':GiveName('ex7')}

# UUDET

lc10 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C%5Bword%3D%22T%C3%A4m%C3%A4n%7CViime%7CToissa%7Ct%C3%A4m%C3%A4n%7Cviime%7Ctoissa%22%5D%5Bword%3D%22vuoden%22%5D%5Bword%3D%22tammikuusta%7Chelmikuusta%7Cmaaliskuusta%7Chuhtikuusta%7Ctoukokuusta%7Ckes%C3%A4kuusta%7Chein%C3%A4kuusta%7Celokuusta%7Csyyskuusta%7Clokakuusta%7Cmarraskuusta%7Cjoulukuusta%22%5D;corpname=AranFinn_b&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000;viewmode=sen;fromp=1',
        'query': '[word="Tämän|Viime|Toissa|tämän|viime|toissa"][word="vuoden"][word="tammikuusta|helmikuusta|maaliskuusta|huhtikuusta|toukokuusta|kesäkuusta|heinäkuusta|elokuusta|syyskuusta|lokakuusta|marraskuusta|joulukuusta"]','filename':GiveName('lc10')}

lc10b = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22vuoden%22][][word%3D%22tammikuusta|helmikuusta|maaliskuusta|huhtikuusta|toukokuusta|kes%C3%A4kuusta|hein%C3%A4kuusta|elokuusta|syyskuusta|lokakuusta|marraskuusta|joulukuusta%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="vuoden"][][word="tammikuusta|helmikuusta|maaliskuusta|huhtikuusta|toukokuusta|kesäkuusta|heinäkuusta|elokuusta|syyskuusta|lokakuusta|marraskuusta|joulukuusta"]','filename':GiveName('lc10b')}

lc11 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22vuonna%22][word%3D%22199.%22][tag!%3D%22.*PrsPrc.*|.*AgPcp.*|PrfPrc_%28Act|Pass%29_%28Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra%29%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&iquery=Pienehk%C3%B6+sivistyssanakirja&attr_tooltip=nott',
        'query': '[lc="vuonna"][word="199."][tag!=".*PrsPrc.*|.*AgPcp.*|PrfPrc_(Act|Pass)_(Abe|Abl|Abl|Ade|Ade|Adv|All|All|Com|Ela|Ela|Ess|Ess|Gen|Gen|Ill|Ill|Ine|Ine|Ins|Par|Par|Tra|Tra)"]','filename':GiveName('lc11')}


lc12 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22yhten%C3%A4%22][word%3D%22aamuna|p%C3%A4iv%C3%A4n%C3%A4%7Ciltana%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="yhtenä"][word="aamuna|päivänä|iltana"]','filename':GiveName('lc12')}

#---

lc13 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22vuodesta%22][word%3D%2219..%22][word!%3D%22vuoteen%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="vuodesta"][word="19.."][word!="vuoteen"]','filename':GiveName('lc13')}

lc14 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc!%3D%22kun|jos|koska%22][lc!%3D%22kun|jos|koska%22][lc!%3D%22.*lleen|kun|jos|koska|ei|ensi|viime|vain|ainakin|v%C3%A4hint%C3%A4%C3%A4n|kuin|edes|taas|viel.*|jo|vasta|joka|usean.*|viel%C3%83%C2%A4%7COlipa|kerta%22+%26+tag!%3D%22.*Gen.*%22+%26+tag!%3D%22Num.*%22][word%3D%22kerran%22][tag+!%3D+%22.*PrfPrc.*|.*AgPcp.*%22+%26+tag!%3D%22.*Ine.*%22+%26+tag!%3D%22.*PrsPrc.*%22+%26+word+!%3D%22.*tua|viel.*|kun|jos|koska|toisensa|vuoteen|viikkoon|p%C3%A4iv%C3%A4%C3%A4n|kuukauteen|tai|vaan%22][word!%3D%22ajassa.*|toisenkin|kahdesti|kolmesti|nelj%C3%A4sti|j%C3%A4lkeen%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc!="kun|jos|koska"][lc!="kun|jos|koska"][lc!=".*lleen|kun|jos|koska|ei|ensi|viime|vain|ainakin|vähintään|kuin|edes|taas|viel.*|jo|vasta|joka|usean.*|vielÃ¤|Olipa|kerta" & tag!=".*Gen.*" & tag!="Num.*"][word="kerran"][tag != ".*PrfPrc.*|.*AgPcp.*" & tag!=".*Ine.*" & tag!=".*PrsPrc.*" & word !=".*tua|viel.*|kun|jos|koska|toisensa|vuoteen|viikkoon|päivään|kuukauteen|tai|vaan"][word!="ajassa.*|toisenkin|kahdesti|kolmesti|neljästi|jälkeen"]','filename':GiveName('lc14')}

lc15 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lemma%3D%22sellainen|semmoinen|tuollainen|t%C3%A4llainen%22][lc%3D%22hetken%C3%A4%7Chetkin%C3%A4%7Chetkell%C3%A4%7Chetkill%C3%A4%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lemma="sellainen|semmoinen|tuollainen|tällainen"][lc="hetkenä|hetkinä|hetkellä|hetkillä"]','filename':GiveName('lc15')}

lc16 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_x&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc!%3D%22viime|ensi|edellisen%C3%A4%7Cseuraavana|sin%C3%A4%7Cviikon%22][lc%3D%22tiistaina|keskiviikkona|torstaina%22][lc!%3D%22%281|2|3|4|5|6|7|8|9%29.*|kello|klo|yhdelt%C3%A4%7Ckahdelta|kolmelta|nelj%C3%A4lt%C3%A4%7Cviidelt%C3%A4%7Ckuudelta|seitsem%C3%A4lt%C3%A4%7Ckahdeksalta|yhdeks%C3%A4lt%C3%A4%7Ckymmenelt%C3%A4%7Cyhdelt%C3%A4toista|kahdeltatoista%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc!="viime|ensi|edellisenä|seuraavana|sinä|viikon"][lc="tiistaina|keskiviikkona|torstaina"][lc!="(1|2|3|4|5|6|7|8|9).*|kello|klo|yhdeltä|kahdelta|kolmelta|neljältä|viideltä|kuudelta|seitsemältä|kahdeksalta|yhdeksältä|kymmeneltä|yhdeltätoista|kahdeltatoista"]','filename':GiveName('lc16')}

lc16alku = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_x&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[word%3D%22\.|\%3F|!%22][word%3D%22Tiistaina|Keskiviikkona|Torstaina%22][word!%3D%22%281|2|3|4|5|6|7|8|9%29.*|yhdelt%C3%A4%7Ckahdelta|kolmelta|nelj%C3%A4lt%C3%A4%7Cviidelt%C3%A4%7Ckuudelta|seitsem%C3%A4lt%C3%A4%7Ckahdeksalta|yhdeks%C3%A4lt%C3%A4%7Ckymmenelt%C3%A4%7Cyhdelt%C3%A4toista|kahdeltatoista%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[word="\.|\?|!"][word="Tiistaina|Keskiviikkona|Torstaina"][word!="(1|2|3|4|5|6|7|8|9).*|yhdeltä|kahdelta|kolmelta|neljältä|viideltä|kuudelta|seitsemältä|kahdeksalta|yhdeksältä|kymmeneltä|yhdeltätoista|kahdeltatoista"]','filename':GiveName('lc16alku')}


lc17 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[word+!%3D+%22ensi|viime|vuonna|vuoden%22+%26+tag!%3D%22Num.*%22][lc%3D%22maaliskuussa|lokakuussa%22][word+!%3D+%22vuonna%22++%26+tag!%3D%22Num.*%22+%26+lc+!%3D+%2219..%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[word != "ensi|viime|vuonna|vuoden" & tag!="Num.*"][lc="maaliskuussa|lokakuussa"][word != "vuonna"  & tag!="Num.*" & lc != "19.."]','filename':GiveName('lc17')}

lc17alku = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[word%3D%22\.|\%3F|!%22][word%3D%22Maaliskuussa|Lokakuussa%22][word+!%3D+%22vuonna%22++%26+tag!%3D%22Num.*%22+%26+lc+!%3D+%2219..%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[word="\.|\?|!"][word="Maaliskuussa|Lokakuussa"][word != "vuonna"  & tag!="Num.*" & lc != "19.."]','filename':GiveName('lc17alku')}

ex8 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22jonkin|jonkun%22][word%3D%22aikaa%22][word!%3D%22sitten|takaperin%22];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="jonkin|jonkun"][word="aikaa"][word!="sitten|takaperin"]','filename':GiveName('ex8')}

ex9 = {'url': 'http://unesco.uniba.sk/aranea/run.cgi/view?q=aword%2C[lc%3D%22viikon%22][lc!%3D%22mittaa.*|ajaksi|ajan|aikana|j%C3%A4lkeen|kuluttua|per%C3%A4st%C3%A4%7Cper%C3%A4%C3%A4n|p%C3%A4%C3%A4st%C3%A4%7Ctakainen|v%C3%A4lein|sis%C3%A4ll%C3%A4%7Ckerrallaan|.*matkalle|my%C3%B6h%C3%A4ss%C3%A4%7Cverran|vertanen|kuluessa|varoitusa.*|ajalta|jokaiselle|.*upuolella|v%C3%A4liajoin|my%C3%B6hemm%C3%A4ss%C3%A4%7Cvarrella|.*aikaa|sis%C3%A4%C3%A4.*|kohokohta|tarpeisiin|.*matka|tarkkuudella|varrelta|t%C3%A4rkeimm%C3%A4t|.*kuuri.*|pahin|paras%22+%26+lemma+!%3D+%22tapahtuma|jatko|tarve|treeni|ruoka|aihe|teema|takainen|loma|viimeinen|p%C3%A4iv%C3%A4%7Cik%C3%A4inen|vanha|anti|vaihde|alku|tauko|loppu|mittainen|pituinen|ty%C3%B6%7Cj%C3%A4lkeinen|tapahtuma|my%C3%B6hempi%22+%26+tag+!%3D+%22.*Gen.*|.*Num.*%22++%26+tag+!%3D+%22.*PrfPrc_Act%28E|G|I|P|T|A%29.*|.*_Ess.*|.*PrsPrc_Act_.*%22+];q=f;corpname=AranFinn_b&viewmode=sen&attrs=word&ctxattrs=word&structs=doc%2Cp%2Cg&refs=%3Ddoc.urldomain&pagesize=1000&gdexconf=&attr_tooltip=nott',
        'query': '[lc="viikon"][lc!="mittaa.*|ajaksi|ajan|aikana|jälkeen|kuluttua|perästä|perään|päästä|takainen|välein|sisällä|kerrallaan|.*matkalle|myöhässä|verran|vertanen|kuluessa|varoitusa.*|ajalta|jokaiselle|.*upuolella|väliajoin|myöhemmässä|varrella|.*aikaa|sisää.*|kohokohta|tarpeisiin|.*matka|tarkkuudella|varrelta|tärkeimmät|.*kuuri.*|pahin|paras" & lemma != "tapahtuma|jatko|tarve|treeni|ruoka|aihe|teema|takainen|loma|viimeinen|päivä|ikäinen|vanha|anti|vaihde|alku|tauko|loppu|mittainen|pituinen|työ|jälkeinen|tapahtuma|myöhempi" & tag != ".*Gen.*|.*Num.*"  & tag != ".*PrfPrc_Act(E|G|I|P|T|A).*|.*_Ess.*|.*PrsPrc_Act_.*" ]','filename':GiveName('ex9')}

ex10 = {'url': 'http://ella.juls.savba.sk/aranea/run.cgi/first?corpname=AranFinn_b&reload=&iquery=&queryselector=cqlrow&lemma=&lpos=&phrase=&word=&wpos=&char=&cql=[lc%3D%22koko%22][lc%3D%22viikon%22][word!%3D%22ajan|kuluessa|aikana|kovin|ohjelma|edest%C3%A4%7Ctapahtumat|ohjelmisto|ateriat|kest%C3%A4nyt|jatkunut|p%C3%A4%C3%A4tteeksi|mittai%28n|s%29e.*|aikataulu|ruokalista%22+%26+tag+!%3D+%22.*PrsPrc.*%22]&default_attr=word&fc_lemword_window_type=both&fc_lemword_wsize=5&fc_lemword=&fc_lemword_type=all&fc_pos_window_type=both&fc_pos_wsize=5&fc_pos_type=all&fsca_doc.did=&fsca_doc.url=&fsca_doc.langdiff=&fsca_doc.wordcount=&fsca_doc.aref=&fsca_doc.tld=&fsca_doc.t2ld=&fsca_doc.urldomain=&fsca_gap.chars=',
        'query': '[lc="koko"][lc="viikon"][word!="ajan|kuluessa|aikana|kovin|ohjelma|edestä|tapahtumat|ohjelmisto|ateriat|kestänyt|jatkunut|päätteeksi|mittai(n|s)e.*|aikataulu|ruokalista" & tag != ".*PrsPrc.*"]','filename':GiveName('ex10')}
