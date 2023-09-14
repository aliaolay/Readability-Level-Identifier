HOW TO RUN POS TAGGER

Go to command line and enter this line:
java -mx500m -cp “stanford-postagger.jar;” edu.stanford.nlp.tagger.maxent.MaxentTagger -model “\POSTagger\filipino-left5words-owlqn2-distsim-pref6-inf2.tagger” -textFile “clean-txt\[input].txt” > “POSTagged-txt\[output].txt”