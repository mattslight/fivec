import re
def hasThree(word):
  input = word
  ok = 1
  for word in re.findall(r'[bcdfghjklmnpqrstvwxz]+', input, re.IGNORECASE):
    if len(word) >= 3:
      ok = 0
  for word in re.findall(r'[aeiou]+', input, re.IGNORECASE):
    if len(word) >= 3:
      ok = 0
  for word in re.findall(r'[y]+', input, re.IGNORECASE):
    if len(word) >= 2:
      ok = 0
  if ok: return False
  else: return True
