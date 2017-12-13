import re
import cons
import ngrams as ng
import patmat as pm
import sscore as ss


def finder(pattern, word):
    found = re.search(pattern, word)
    if found:
        return word


def score(word):
    s = 1  # starting score of 1
    if finder(r'[aeiou]', word) is None: s -= 1
    if finder(r'[-]', word) is not None: s -= 1
    if cons.hasThree(word): s -= 1
    return s


# application
while 1:
    r = raw_input()
    if r in ["Q", "q"]: break
    print r, pm.match(r), ng.score2(r), ss.score(r)
