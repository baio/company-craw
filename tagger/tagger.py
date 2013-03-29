__author__ = 'baio'
import nltk
from nltk.corpus import TaggedCorpusReader

def tag_text(str_trained_folder, str_fname_in, str_fname_out):

    #http://nltk.googlecode.com/svn/trunk/doc/howto/tag.html

    #build trigram tagger based on your tagged_corpora

    tagged_corpora = TaggedCorpusReader(str_trained_folder, '.*')

    #print tagged_corpora.tagged_sents()[50]

    trigram_tagger = nltk.TrigramTagger(tagged_corpora.tagged_sents())

    with open(str_fname_in) as f_in:

        with open(str_fname_out, "w+") as f_out:

            for line in f_in:

                tagged_result = trigram_tagger.tag(line.split())

                str = " ".join([t[0] for t in tagged_result if t[1] == 'C'])

                if str:
                    f_out.write(str + "\n")

tag_text("./store/_trained", "c:/dev/company-craw/store/parsed/doc1.txt", "c:/dev/company-craw/store/out/doc1.txt")