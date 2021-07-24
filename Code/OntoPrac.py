import csv
import re
import owlready2
import tkinter
from tkinter.filedialog import askopenfilename
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords

tested_terms = []
with open('testset.csv') as data:
    entry = csv.DictReader(data)
    for row in entry:

        # make text lowercase
        ingredients = row['ingredients'].lower()

        # strip end line characters
        ingredients = ingredients.rstrip()

        # split on common delimiters for ingredients NOT spaces
        # this will keep multi word ingredients together (for example Vegetable Oil)
        ingredients = re.split(',|:|-', ingredients)
        ingredients = [word.split() for word in ingredients]

        # join ingredients on space
        ingredients = [' '.join(word) for word in ingredients]

        # Tokenize list of ingredients
        tok_ingre = [word_tokenize(ingredient) for ingredient in ingredients]

        # check to make sure words are alpha and do not include stop words
        all_words = []
        for entry in tok_ingre:
            stop_words = set(stopwords.words('english'))
            all_words.append(' '.join([word for word in entry if word.isalpha() and word not in stop_words]))

        print(all_words)

        # tokenize text
        # tok_ingre = word_tokenize(ingredients, language='english')
        # print(tok_ingre)

        '''
        # remove punctuation
        all_words = [word for word in tok_ingre if word.isalpha()]

        # remove stop words
        stop_words = set(stopwords.words('english'))
        word_list = [ingredient for ingredient in all_words if ingredient not in stop_words]

        for t in word_list:
            if t not in tested_terms:
                tested_terms.append(t)

    print(tested_terms)
'''

data.close()