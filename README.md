#5char

A python script for scraping char5.com for 'pronouncable' words.

3 score techniques:
- a) ngrams.py - A simple algorythm based on frequency and position of bigrams scored against publicly available data complied by Peter Norvig http://norvig.com/mayzner.html
- b) sscore.py - A scoring system based on a "scrabble score" of a word - I found this helpful in filtering out potential words with exsessive Qs Zs Xs etc. Although it was not a very good model as it would rank words like 'zizzy' low.
- c) patmat.py - Matching five letter words based on patterns of consonants ( C ) and vowels ( V )
