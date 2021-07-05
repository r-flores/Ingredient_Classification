############################
## ingre_class.py
## The purpose of this file is to classify terms
## found in ingredient labels  
############################
import csv
import owlready2
import tkinter
from tkinter.filedialog import askopenfilename
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def file_selection():
    """ Sets file path to csv with ingredients
    Args: N/A
    Returns: Filepath as string
    """
    path = askopenfilename(
        filetypes=[("comma sep. vals.", "*.csv")]
        )
    if not path:
        print("No File Selected")
        return
    if path:
        return path

def file_reader(file_path):
    """ Reads the csv with ingredients and toeknizes terms
    Args: Filepath to csv file
    Returns: list of terms found on ingredient labels
    """
    terms = []
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


            print(ingre_words)

def ontloogy_classifier():
    """ Identifies terms in the food Ontology (FoodOn) and classifies them
    Args: Terms found on ingredient labels
    Returns: Classified food label terminology
    """
    # Gather additional data from FoodON (food Ontology, using Owlready2 package)
    ## local loading
    
    owlready2.onto_path.append('Code\\')
    food_onto = owlready2.get_ontology('Code\\foodon.owl').load()

    print(list(food_onto.search(label = "food (chopped)")))
    

    #food_onto = owlready2.get_namespace('http://purl.obolibrary.org/obo/')
    #print(food_onto.FOODON_03307455.label)
    ## from web loading
    #food_onto = owlready2.get_ontology("http://purl.obolibrary.org/obo/foodon.owl").load
    #food_onto.save(file = "FoodOn.xml", format = 'rdfxml')

root = tkinter.Tk()
root.withdraw()
# nltk.download('punkt')
# nltk.download('stopwords')
file_path = file_selection()
file_reader(file_path)