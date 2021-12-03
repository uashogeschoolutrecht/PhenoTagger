import re
#import os

def fix_formatting(file = "../data/MP_annotations/ontology_training.tsv"):
    # Pattern to find one or more tab characters followed by a newline
    pattern = re.compile("[\\t]{2,}(?=\\n){2}")
    
    # Open file
    with open(file, "r", encoding='utf-8') as myfile:
        data = myfile.read()
    
    # Remove all tabs followed by a newline
    newdata = re.sub(pattern, "", data)

    # Overwrite file
    with open(file, "w", encoding='utf-8') as myfile:
        myfile.write(newdata)