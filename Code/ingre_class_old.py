#!/usr/bin/python3
############################
# ingre_class.py
# The purpose of this file is to classify terms
# found in ingredient labels
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
        input("Press enter to quit")
        quit()

    if path:
        print(path)
        return path


def ontology_classifier(filename):
    """ Identifies terms in the food Ontology (FoodOn) and classifies them
    Args: list of terms found on ingredient labels
    Returns: Classified food label terminology
    """
    # Gather additional data from FoodON (food Ontology, using Owlready2 package)
    # local loading
    print('Loading Ontology...')
    food_onto = owlready2.get_ontology('foodon.owl').load()

    # create a new files for writing results
    classified_terms = open("classified_Terms.csv", 'w', newline='')
    write = csv.DictWriter(classified_terms, fieldnames=['Term', 'Membership'])
    write.writeheader()

    # collection of already examined words
    tested_terms = []

    with open(filename) as data:
        entry = csv.DictReader(data)
        for row in entry:
            # make text lowercase
            ingredients = row['ingredients'].lower()

            # strip end line characters
            ingredients = ingredients.rstrip()

            # tokenize text
            tok_ingre = word_tokenize(ingredients, language='english')

            # remove punctuation
            all_words = [word for word in tok_ingre if word.isalpha()]

            # remove stop words
            stop_words = set(stopwords.words('english'))
            word_list = [ingredient for ingredient in all_words if ingredient not in stop_words]

            for t in word_list:
                if t not in tested_terms:
                    tested_terms.append(t)

                    # TODO: improve search in Ontology to retrieve more results
                    # Search for the term exactly as is.
                    term_class = food_onto.search_one(label=t)
                    if term_class is None:
                        term_class = food_onto.search_one(label='*'+t)

                    if term_class is None:
                        term_class = food_onto.search_one(label='*'+t+'*')

                    try:

                        # All FoodOn properties https://www.ebi.ac.uk/ols/ontologies/foodon/properties
                        # R0_0002350 = "member of' Property , is member of is a mereological relation
                        # between a item and a collection.
                        write.writerow({'Term': str(t),
                                        'Membership': str(food_onto.search_one(is_a=term_class.RO_0002350).label)})

                    except AttributeError as e:
                        #print(e)
                        write.writerow({'Term': str(t), 'Membership': 'No Class'})
                        continue

    classified_terms.close()
    data.close()


# create and remove gui window for file select screen
root = tkinter.Tk()
root.withdraw()

# The follwing additions will be required from NLTK
# nltk.download('punkt')
# nltk.download('stopwords')

# File_path will have the user pick a csv file with a colnum of ingredients
file_path = file_selection()

# Ontology classifier will identify term membership from FoodOn
ontology_classifier(file_path)
