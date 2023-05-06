
import pytesseract
from PIL import Image
import re
import pandas as pd
import cv2


from PIL import Image

# Load image

img = cv2.imread('--IMAGE HERE--')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)

words = text.split()
parameter_types_cbc = {
        'hgb': ['hgb', 'haemoglobin', 'hemoglobin'],
        'mcv': ['mcv', 'mean corpuscular volume', 'm.c.v'],
        'mch': ['mch', 'mean corpuscular hemoglobin', 'm.c.h'],
        'mchc': ['mchc', 'mean corpuscular hemoglobin concentration', 'm.c.h.c'],
       
    }
lft_feature_keywords = {
    'alanine aminotransferase': ['alt', 'sgpt'],
    'aspartate aminotransferase': ['ast', 'sgot'],
    'alkaline phosphatase': ['alp'],
    
    'total bilirubin': ['tbil', 'tb'],
    'direct bilirubin': ['dbil', 'db'],
    'albumin': ['alb'],
    'prothrombin time': ['pt'],
    'A/G ratio': ['ag ratio'],
    'total proteins': ['tp', 'total protein']
}
def extract_features(words, feature_keywords):
    """
    Extracts numerical values associated with specific feature keywords from a list of words.
    
    Parameters:
        - words (list): A list of strings to search for the feature keywords and their values
        - feature_keywords (dict): A dictionary mapping feature names to lists of possible keywords
        
    Returns:
        A dictionary mapping feature names to their extracted numerical values
    """
    # Convert all words to lowercase for case-insensitive matching
    words = [w.lower() for w in words]
    
    # Define a regex pattern to match numbers
    number_pattern = r'\d+(\.\d+)?'
    
    # Extract the value for each feature, if present
    features = {}
    for feature_name, keywords in feature_keywords.items():
        for keyword in keywords:
            # Find all occurrences of the keyword in the list of words
            indices = [i for i, word in enumerate(words) if word == keyword]
            if indices:
                # For each occurrence, look for the first following numerical value
                value_found = False
                for index in indices:
                    current_index = index + 1
                    while current_index < len(words):
                        # Search for a number following the feature keyword
                        match = re.search(number_pattern, words[current_index])
                        if match:
                            try:
                                value = float(match.group(0))
                                features[feature_name] = value
                                value_found = True
                                break
                            except ValueError:
                                pass
                        current_index += 1
                    if value_found:
                        break
    
    return features

def choose_test_to_extract(features):
    # Define the keywords to look for in each feature
    cbc_keywords = ['cbc', 'complete', 'blood ', 'hematology ']
    lft_keywords = ['lft', 'liver', 'function ', 'biochemistry ']

    for feature in features:
        if any(cbc_item in feature.lower() for cbc_item in cbc_keywords):
            print("CBC test detected")
            
            return extract_features(features, parameter_types_cbc) 
            
        elif any(lft_item in feature.lower() for lft_item in lft_keywords):
            print("LFT test detected")
            
            return extract_features(features, lft_feature_keywords)

    # No matching test type was found
    return "This type of test is not supported"

# end Hady Code 


# Mohamed Code Start 
import joblib
def anemiaPredict(list):
    fileName='anemia_model.joblib'
    anemiaModel=joblib.load(fileName)
    return anemiaModel.predict([list])[0]
def liverFailurePredict(list):
    fileName='liver_model.joblib'
    liverModel=joblib.load(fileName)
    return liverModel.predict([list])[0]