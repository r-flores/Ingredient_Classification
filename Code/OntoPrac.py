import csv
import owlready2
import tkinter
from tkinter.filedialog import askopenfilename
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#owlready2.onto_path.append('Code\\')

food_onto = owlready2.get_ontology('Code\\foodon.owl').load()
print("Ontology Loaded...")

# Food product = FOODON_00001002
# General Label Claim = FOODON_03510059

test_re = open("test.txt", 'w')
tested_terms = []

file_path = "Code\\testset.csv"
with open(file_path) as data:
        entry = csv.DictReader(data)
        for row in entry:

            # make text lowercase
            ingredients = row['ingredients'].lower()

            # strip end line characters
            ingredients = ingredients.rstrip()

            # tokenize text
            tok_ingre = word_tokenize(ingredients)

            # remove punctuation
            all_words = [word for word in tok_ingre if word.isalpha()]

            # remove stop words
            stop_words = set(stopwords.words('english'))
            ingre_words = [ingredient for ingredient in all_words if not ingredient in stop_words]
            for t in ingre_words:
                if t not in tested_terms:
                    tested_terms.append(t)
                    test_re.write(str(t))
                    test_re.write("    |    ")
                    term_class = food_onto.search_one(label = "*"+t+"*")
                    try:
                        test_re.write(str(term_class.RO_0002350))
                    except AttributeError as e:
                        test_re.write("No Class")
                        continue

                    test_re.write("\n")
                else:
                    print(str(t) + " is duplicate")
        

print("closign")
test_re.close()               
#ans = food_onto.search_one(label = str("salt"))
#print(ans)
#print(ans.label)
#print(ans.RO_0002350)