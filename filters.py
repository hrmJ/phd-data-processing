import re

try:
    from datascripts import searchutils
except ImportError:
    print('Varmista, että searchutils tuotu oikein...')

class Filter():

    def __init__(self, matches, lang):
        self.lang = lang
        self.passed = matches
        print('Filtering...')

    def UpdatePassed(self, passed, filtname):
        #Päivitetään filtteri:
        print("After  {} filter, {} of {} matches passed".format(filtname, len(passed),len(self.passed)))
        self.passed = passed

    def DirectLinkToVerb(self):
        """
        - Poista, jos ei suoraan riippuvainen verbistä
        - Saako olla ei-fin?
            - saa, jos suomen apuverbitapaus jne
        """
        if not self.passed:
            #Jos ei yhtään filtteröitävää, lopeta. 
            print('EMPTY list of matches, cancelling the filter...')
            return 0

        passed = list()
        for idx, match in enumerate(self.passed):
            #Tutki, onkopääsana finiittinen
            try:
                if not match.matchedword.compoundfinitehead:
                    #toisin sanoen filtteröidään pois esim. nomineista riippuvat ilmaukset
                    if match.matchedword.headword.IsThisFiniteVerb():
                        passed.append(match)
                else:
                    #JOS kyseessä suomen apu-/yms.-verbi, hyväksy automaattisesti,,
                    #koska näissä tapauksissa on jo aiemmin testattu, että 
                    #pääsana (esim. "testattu") riippuu suoraan finiitti verbistä (esim "on")
                    passed.append(match)
            except AttributeError:
                    print('Problems with sentence {}'.format(match.matchedsentence.sentence_id))
                    #import ipdb; ipdb.set_trace()
        self.UpdatePassed(passed, "DirectLInkToVerb")

    def Ohjelmatiedot(self):
        """
        - Poista, jos ei suoraan riippuvainen verbistä
        - Saako olla ei-fin?
        """
        if not self.passed:
            #Jos ei yhtään filtteröitävää, lopeta. 
            print('EMPTY list of matches, cancelling the filter...')
            return 0
        passed = list()
        pat = re.compile("\d{2}(\.|:)\d{2}")
        for idx, match in enumerate(self.passed):
            firstword = match.matchedsentence.words[1]
            if not pat.search(firstword.token):
                #Jos eka sana sisältää nn.nn tai nn:nn merkkijonon, unohda se
                if "Региона»" not in firstword.token:
                #Jos eka sana sisältää venäjässä lehtikorpuksen omituisen poikkeuksen, unohda
                    passed.append(match)
        self.UpdatePassed(passed, "Yksittäisiä korpuspohjaisia sääntöjä")

    def ByOrder(self, order, StrictObject):
        """Jos jotenkin jo lähtisi siitä, että tähän haaviin ei jää läheskään kaikkea, mutta..."""
        if not self.passed:
            #Jos ei yhtään filtteröitävää, lopeta. 
            print('EMPTY list of matches, cancelling the filter...')
            return 0
        passed = list()
        for idx, match in enumerate(self.passed):
            #print('Filtering: {}/{}'.format(idx, len(matches)), end='\r')
            #if match.matchedsentence.sentence_id == 113:
            #    import ipdb; ipdb.set_trace()
            s=False
            oloc=sloc=vloc=0
            #1. Etsi osuman oma finiittinen pääverbi
            if match.matchedword.IterateToFiniteHead(match.matchedsentence):
                vloc = match.matchedword.finitehead.tokenid
                #2. Oleta, että subjekti ja objekti ovat tämän dependenttejä
                #PAITSI, jos finiittipääverbi on haettu "apuverbin ylitse",
                #jolloin s ja o ovat ei-finiittisen pääverbin depsuja
                if not match.matchedword.compoundfinitehead:
                    findeplist = match.matchedword.finitehead.ListDependents(match.matchedsentence)
                else:
                    findeplist = match.matchedword.headword.ListDependents(match.matchedsentence)

                for thisword in findeplist:
                    #3. Määrittele subjektin ja objektin sijainnit
                    if match.matchedword.tokenid != thisword.tokenid:
                        #IGNORE the matching word
                        if thisword.IsSubject(self.lang):
                            sloc = thisword.tokenid
                        if thisword.IsObject(self.lang, match.matchedsentence, StrictObject):
                            oloc = thisword.tokenid
                    if sloc and oloc:
                        break

                #tallenna informaatio mahdollisesta puuttuvasta subjektista
                if sloc == 0:
                    match.TestProDrop(self.lang)
                if not (sloc==0 and match.prodrop == 'No'):
                    #4. Testaa järjestystä, mutta katso epäonnistuneeksi, jos ei subj eikä myöskään pro-drop
                    orders = {'SOV':SOV(sloc,vloc,oloc)}
                    if orders[order]:
                        passed.append(match)
        self.UpdatePassed(passed, "ByOrder")


def SVO(sloc,vloc,oloc):
    """Jos O tulee V:n ja S:n jälkeen ja V tulee S:n jälkeen, hyväksy mukaan"""
    if (oloc > sloc and oloc > vloc) and (vloc > sloc):
        return True
    return False

def SOV(sloc,vloc,oloc):
    """Jos V tulee S:n ja O:n jälkeen ja O tulee S:n jälkeen, hyväksy mukaan"""
    if (vloc > sloc and vloc > oloc) and (sloc < vloc):
        return True
    return False

def VS(sloc,vloc):
    """Jos O tulee V:n ja S:n jälkeen ja V tulee S:n jälkeen, hyväksy mukaan"""
    if (sloc > vloc):
        return True
    return False

def FiniteHeadNsubj(matches, ttype="Positive"):
    cond = searchutils.Condition('deprel',('nsubj','предик'),ttype)
    passed = list()
    for match in matches:
        f = searchutils.MatchFilter(match, cond)
        if f.FilterByFiniteHeadDep():
            passed.append(match)
    return passed

def FiniteHeadDobj(matches, ttype="Positive"):
    cond = searchutils.Condition('deprel',('dobj','1-компл'),ttype)
    passed = list()
    for match in matches:
        f = searchutils.MatchFilter(match, cond)
        if f.FilterByFiniteHeadDep():
            passed.append(match)
    return passed
