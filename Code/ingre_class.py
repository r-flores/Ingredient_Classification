import csv
import owlready2

# Download a subset of data from Food ingre DB FoodData central (USDA)
## read csv in to a dictonary (for now possible api later)
#with open('Code\\testset.csv') as data:
#    reader = csv.reader(data)
#    for row in reader:
#        print(row)
#data.close()

# Gather additional data from FoodON (food Ontology, using Owlready2 package)
## local loading
food_onto = owlready2.get_ontology('Code\\foodon.owl').load()
print(list(food_onto.individuals()))
## from web loading
#food_onto = owlready2.get_ontology("http://purl.obolibrary.org/obo/foodon.owl").load
#food_onto.save(file = "FoodOn.xml", format = 'rdfxml')

# Compare and return terms that would be considered ingredients by comparsion (If it exist in FoodOn its probably an ingrdient)
