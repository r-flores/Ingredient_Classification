import csv
# Download a subset of data from Food ingre DB FoodData central (USDA)
## read csv in to a dictonary
with open('Code\\testset.csv') as data:
    reader = csv.reader(data)
    for row in reader:
        print(row)
data.close()
# Gether additional data from FoodON (food Ontology)
# Compare and return terms that would be considered ingredients by comparsion (If it exist in FoodOn its probably an ingrdient)