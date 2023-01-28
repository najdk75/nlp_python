

descripteur = open("livre01.txt","r",encoding='utf8')
liste_lignes = descripteur.readlines()
lines = []
for line in liste_lignes :
    lines.append(line.strip())

with open("stopwords_fr.txt", "r", encoding='utf8') as f:
    stop_words = f.read().split()
stop_words

### Idée : toute la ponctuation va être désintégrer en laissant place à un espace, c est à dire que:
## pour tout p € Ponctuation , Desintégratiton(p) = " "

## on se chargera de la destruction de ces espaces à la fin.


dico = {'d' : 'de',
        's' : 'se',
        'l' : 'le',
        'j' : 'je',
        'n' : 'ne',
        'c' : 'ce'}

def remove_contraction(word):
    
    if len(word) == 1:
        if word.isupper() and (word.lower() in dico):
                return (dico[word.lower()]).upper()
        elif word in dico:
            return dico[word]
        else:
            return ""
    else:
        return word
    
def remove_punctuation(text):
    if text.isalnum(): # si la phrase ne contient pas de ponctuation on retourne la même
        return text
    else:
        characters = list(text) # ["le mot"] -> ["l","e"," ","m","o","t"]
        cleaned_text = "".join(map(lambda c : c if c.isalnum() else " ", characters)).strip() 
        return cleaned_text
    
    
def cleaning(lines):
    cleaned_lines = []
    for line in lines: 
        if line != "": # on ajoute pas de ligne vide
            punctuation_removed = " ".join(map(remove_punctuation,line.split())) # on enleve ponctuation + séparation tiret
        
            contraction_removed = " ".join(map(remove_contraction,punctuation_removed.split())) 
        
            stop_words_removed = map(lambda m : "" if m.lower() in stop_words else m ,contraction_removed.split())
        
            extra_whitespace_removed = " ".join(filter(lambda s : s != "", stop_words_removed))
            
            cleaned_lines.append(extra_whitespace_removed)
        
    return cleaned_lines

lines = cleaning(lines)



def reduce(lines):
    lines = list(map(lambda phrase : phrase.lower(),lines))
    res = {}
    for line in lines:
        for word in line.split():
            res[word] = res.get(word, 0) + 1
    return res

word_count = reduce(lines)

cleaned = sorted(word_count.items(),key=lambda x : x[1], reverse=True)
print(cleaned)
words = [word for word,count in cleaned]
counts = [count for word,count in cleaned]




# import de la bibliothèque
import seaborn as sns 
import matplotlib.pyplot as plt

#modifier la taille de la figure pour l'adapter
sns.set(rc={'figure.figsize':(100,50)})

# afficher un histogramme. les données doivent être dans une liste
# transformez donc vos clés et valeurs du dictionnaire en liste
# idéalement ordonnez vos clés
sns.barplot(data=None,x = words, y = counts)

plt.savefig("wordcount.png")