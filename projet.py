dico = {'d' : 'de',
        's' : 'se',
        'l' : 'le',
        'j' : 'je',
        'n' : 'ne',
        'c' : 'ce'}

def read_file(path):
    descripteur = open(path,"r",encoding='utf8')
    
    ## Ici pour favoriser le traitement de données on mettra tout le texte en minuscule
    ## sera beaucoup plus simple pour compter les mots et utiliser les fonctions intermédiaires
    raw_text_to_lower = map(lambda s : s.lower().strip(),descripteur.readlines())
    
    return raw_text_to_lower

with open("stopwords_fr.txt", "r", encoding='utf8') as f:
    ## en transformant stop_words en set, l'accession de données se fait beaucoup plus rapidement qu'avec une liste
    stop_words = set(f.read().split())
    
def remove_punctuation_word(word):
    characters = list(word) # "word" -> "["w","o","r","d"]"
    
    ## on remplace toute la ponctuation par " " (pour gérer le tiret) en gardant les caractères alphanumériques
    ## Puis on retire les espaces inutiles au début et à la fin
    return "".join(map(lambda c : c if c.isalnum() else " ",characters)).strip()

def remove_punctuation(text):
    
    t = " ".join(text).split()
    return " ".join([remove_punctuation_word(word) for word in t])


def stemming(word):
    ## Si le mot est de longueur une et est dans le dico alors on retourne sa valeur associée
    if len(word) == 1 and word in dico:
        return dico[word]
    ## sinon on retourne le même mot
    else:
        return word
    
def replace_contracted_words(text):
    return map(stemming,text.split())
  
def remove_stop_words(text):
    
    return filter(lambda word : word not in stop_words and len(word) > 2  and not word.isspace(),text)

def cleaning(path):
    ## on lit le fichier voulu
    raw_text = read_file(path) 
    
    ## on enlève toute la ponctuation
    punctuation_removed = remove_punctuation(raw_text) 
    
    ## on convertit les mots à une lettre grâce au dico
    contracted_words_replaced = replace_contracted_words(punctuation_removed) 
    
    ## on enleve tous les stop_words du fichier, tous les mots de longueur < 2 et tous les espaces superflus
    stop_words_removed = remove_stop_words(contracted_words_replaced)
    
    
    return list(stop_words_removed)



def reduce(cleaned_words):
    ## les mots sont déjà tous en minuscule donc on peut directement effectuer le décompte de façon case-insensitive
    word_count = {}
    for word in cleaned_words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


word_count = reduce(cleaning("livre01.txt"))





# import de la bibliothèque
import seaborn as sns 
import matplotlib.pyplot as plt

#modifier la taille de la figure pour l'adapter
sns.set(rc={'figure.figsize':(10,5)})

# afficher un histogramme. les données doivent être dans une liste
# transformez donc vos clés et valeurs du dictionnaire en liste
# idéalement ordonnez vos clés

word_count = sorted(word_count.items(), key= lambda item : item[1], reverse=True)
words = [word for word,count in word_count]
counts = [count for word,count in word_count]

sns.barplot(data=None,x = words, y = counts)



''' 
On remarque que plus le volume de donnée est important, plus la lisibilité du graphique est moindre.

Il faudrait rendre le comptage des mots "case insensitive" en mettant tout en minuscule pour éviter de nouvelles colonnes superfluee
On pourrait aussi songer à supprimer de notre graphique les mots dont les occurences sont assez faibles.


'''
