import re
import math
import csv
import pprint

def score4(word):
    score = 0.0
    with open("./tables/4grams.tsv") as tsv:
      pairs = []
      for a,b in (r[0:2] for r in csv.reader(tsv, dialect="excel-tab")):
          pairs.append([a, b])
    for pair in pairs:
        if pair[0] in word:
            score += (math.log(float(pair[1]))/math.log(float(pairs[0][1])))/2
    return score


def score2(word):
    score = 0.0
    word = word.upper()
    with open("./tables/2grams.tsv") as tsv:
      for row in csv.reader(tsv, dialect="excel-tab"):
          if row[0] in word:
            for match_index in (m.start() for m in re.finditer('(?='+row[0]+')', word)):
              if match_index == 0:
                  if row[16] != '0':
                    score += (math.log(float(row[16]))/math.log(float(row[5])))
                  else:
                      score -= 1
              elif match_index == 1:
                  if row[17] != '0':
                    score += (math.log(float(row[17]))/math.log(float(row[5])))
                  else:
                      score -= 1
              elif match_index == 2:
                  if row[18] != '0':
                    score += (math.log(float(row[18]))/math.log(float(row[5])))
                  else:
                    score -= 1
              elif match_index == 3:
                  if row[19] != '0':
                    score += (math.log(float(row[19]))/math.log(float(row[5])))
                  else:
                    score -= 1

    return score

def score3(word):
    score = 0.0
    word = word.upper()
    with open("./tables/3grams.tsv") as tsv:
      for row in csv.reader(tsv, dialect="excel-tab"):
          if row[0] in word:
            for match_index in (m.start() for m in re.finditer('(?='+row[0]+')', word)):
              if match_index == 0:
                  if row[12] != '0':
                    score += (math.log(float(row[12]))/math.log(float(row[4]))) #TODO normalise score
              elif match_index == 1:
                  if row[13] != '0':
                    score += (math.log(float(row[13]))/math.log(float(row[4]))) #TODO normalise score
              elif match_index == 2:
                  if row[14] != '0':
                    score += (math.log(float(row[14]))/math.log(float(row[4]))) #TODO normalise score
            return score

def score(word):
    return score2(word), score3(word), score4(word)
