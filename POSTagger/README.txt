HOW TO RUN POS TAGGER

Go to the command line, make sure you are in the Readability-Level-Identifier folder, and enter this line:
java -mx500m -cp “stanford-postagger.jar;” edu.stanford.nlp.tagger.maxent.MaxentTagger -model “\POSTagger\filipino-left5words-owlqn2-distsim-pref6-inf2.tagger” -textFile “clean-txt\[input]_cleaned.txt” > “POSTagged-txt\[output]_tagged.txt”

   --> change [input] and [output] to the respective titles/filenames

TITLES:
Ang Aklatang Pusa
Ang Anghel ng Santa Ana 
Ang Batang Maraming Bawal
Ang Dyip ni Mang Tomas
Inang Kalikasans Bad Hair Day 
Ipapasyal Namin si Lolo
Karapat-Dapat 
Si Lupito at ang Barrio Sirkero
Si Ponyang at ang Lihim ng Kuweba
Tahan na Tahanan