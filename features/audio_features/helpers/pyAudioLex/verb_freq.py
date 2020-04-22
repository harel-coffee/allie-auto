'''
@package: pyAudioLex
@author: Drew Morris
@module: verb_freq

Frequency of a POS tag is computed by dividing the total number of words 
with that tag by the total number of words spoken by the subject in the 
recording.
'''

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag, map_tag

def verb_freq(s, tokens = None):
  if tokens == None:
    tokens = word_tokenize(s)

  pos = pos_tag(tokens)
  verbs = []

  for [token, tag] in pos:
    part = map_tag('en-ptb', 'universal', tag)
    if part == "VERB":
      verbs.append(token)

  if len(tokens) == 0:
    return float(0)
  else:
    return float(len(verbs)) / float(len(tokens))
