import stopwordsiso
from stopwordsiso import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer

from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

# stop words
stop_words = set(stopwords('tl'))
others = ['ate', 'kuya', 'aginaldo', 'di', 'din', 'na', 'ba', 'eh', 'kasi', 'lang', 'mo', 'naman', 'opo', 'po', 'si', 'talaga', 'yung']   # https://github.com/explosion/spaCy/discussions/6122
stop_words.update(others)

# sample
corpus = ["ang pasko ay lamig ng simoy-disyembre, may bango ng palay at hinog na ani. sapagkat bakasyon, bukas walang pasok, masarap matulog na balot ng kumot. “bangon at magbihis! ” ang utos ng ina. tawag ng kampana, “halina, magsimba! ” pasko'y simbang-gabi kahit inaantok bilang pasasalamat sa buti ng diyos. pero itong pasko’y suman, puto-bumbong, bibingka't salabat sa busog at gutom. kahit inaantok, puso'y sumisigla basta't may meryenda paglabas sa misa. ang pasko ay parol sa bintana’t pinto, masaya ang bati sa kulay at anyo; habang naglalaro sa pagkakasabit, parang sinasabing, “ ang pasko'y pag-ibig.” ang pasko ay belen na itinatanghal ang sanggol na hesus sa isang sabsaban. sagisag ng pasko ay pista ng bata at mahal ng diyos ang pobre at dukha. ang pasko'y karoling at pananapatan sa saliw ng balde't kuleleng na tansan. kahit sintunado ang kanta at tugtog, sa ngalan ng pasko, libreng mangalantog. pasko'y notse b'wena ng adobo, litson, at pagkaing tambak minsan isang taon. pag hindi napigil ng kamay ang bibig puputok ang tiyan sa sobrang paghatset. siyempre, di kumpleto ang diwa ng pasko kung walang laruan at ibang regalo. kaya raw may ninong kapag nagbibinyag, nang may aginaldo kaming inaanak. at higit sa lahat, ang pasko’y okasyon para ang pamilya’y muling magkatipon. si ate at kuya'y tiyak paparito, lahat sama-sama, pagdating ng pasko. bukas ay pasko na. sabik na si berting. asong aginaldo kaya ang tatanggapin? bukas ay pasko na. pero ama niya'y kayod sa pabrika. mahirap lang sila. bukas ay pasko na. pero naglalaba ang ina ni berting. mahirap lang sila. ano naman kaya ang dapat hilingin? baril na kaparis ng koboy sa komiks? pero naisip niya, “baril ay maingay. at nakasasakit pag may tinamaan.” baka mas mainam ay magandang damit para may kapalit ang suot na punit. pero naisip niya: “damit ay aanhin? wala namang parti o pistang darating. damit na may punit, masusulsihan din.” mahirap lang sila. bukas ay pasko na. maghapong abala ang isip ni berting sa hihilingin n’ya. pero naisip n'ya: “aanhin ang bola, kendi at laruan?” mahirap lang sila. nang hatinggabi na, ama ay wala pa. ang tanong ni berting, “nasan si ama?” ang sagot ni ina, “nasa sa pabrika. may obertaym sila.” nag-isip si berting at saka nagsabi: “kahit wala akong bagong aginaldo, basta't lagi lamang sama-sama tayo'y masaya ang pasko.” nang binyagan ako, galante ang ninong ko. bukod sa limampung piso, may bigay pang regalo. nang binyagan si arturo, galante rin ang ninong ko. bukod sa limampung piso, nagbigay rin ng regalo. naging popular ang ninong ko, naging kumpare ng buong baryo. pag sumasapit ang pasko, galante ang ninong ko. ang bigay na aginaldo malulutong na sampung piso. pero pagsapit ng ibang pasko, ang sampu'y naging piso, ang piso ay naging singko. kuripot ang ninong ko, nagtatago pa kung pasko. kaya ngayong pasko, walang ibig magmano sa ninong ko. ako tuloy ang sumolo sa kanyang aginaldo."]
filtered = [word.lower() for word in corpus if word.lower() not in stop_words]

# TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(filtered)
feature_names = tfidf_vectorizer.get_feature_names_out()    # words

# wordcloud
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10)
wordcloud.generate(' '.join(feature_names))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()