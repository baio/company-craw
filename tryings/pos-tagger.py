__author__ = 'baio'
from nltk.corpus import TaggedCorpusReader
reader = TaggedCorpusReader('.', r'.*\.pos')
print reader.words


