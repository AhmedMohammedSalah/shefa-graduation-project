from .models import MedicalTest
import pytesseract
from PIL import Image
import re
import pandas as pd
import cv2
# import tesseract
import joblib
def anemiaPredict(gender: list, list):
    parameters = [gender[1]] + list
    fileName = '/home/ahmed/Desktop/@work/Django Projects/shefa-graduation-project/shefa-board-new/src/medicalAnalysis/anemia_model.joblib'
    type="تحليل الدم الشامل  "
    anemiaModel = joblib.load(fileName)
    return anemiaModel.predict([parameters])[0],type
def liverFailurePredict(ageGender, list):
    gender = [1, 0] if ageGender[1] == 1 else [0, 1]
    parameters = [ageGender[0]]+list+gender
    fileName = '/home/ahmed/Desktop/@work/Django Projects/shefa-graduation-project/shefa-board-new/src/medicalAnalysis/liver_model.joblib'
    liverModel = joblib.load(fileName)
    type="تحليل فشل كلوي  "
    return liverModel.predict([parameters])[0],type

# 1

# 2

    # No matching test type was found
    return -1  # "This type of test is not supported"


# tests =MedicalTest.objects.all()

# for test in tests:
# Load image
def extract_features(words, feature_keywords):
    """
    Extracts numerical values associated with specific feature keywords from a list of words.
    Parameters:
        - words (list): A list of strings to search for the feature keywords and their values
        - feature_keywords (dict): A dictionary mapping feature names to lists of possible keywords

    Returns:
        A dictionary mapping feature names to their extracted numerical values as a list
    """
    # Convert all words to lowercase for case-insensitive matching
    words = [w.lower() for w in words]

    # Define a regex pattern to match numbers
    number_pattern = r'\d+(\.\d+)?'

    # Extract the value for each feature, if present
    features = []
    for feature_name, keywords in feature_keywords.items():
        feature_values = []
        for keyword in keywords:
            # Find all occurrences of the keyword in the list of words
            indices = [i for i, word in enumerate(words) if word == keyword]
            if indices:
                # For each occurrence, look for the first following numerical value
                for index in indices:
                    current_index = index + 1
                    while current_index < len(words):
                        # Search for a number following the feature keyword
                        match = re.search(number_pattern, words[current_index])
                        if match:
                            try:
                                value = float(match.group(0))
                                feature_values.append(value)
                                break
                            except ValueError:
                                pass
                        current_index += 1
        if feature_values:
            features.extend(feature_values)
    print (features)
    return features


def choose_test_to_extract(features, ageGender):
    cbc_keywords = ['cbc', 'complete', 'blood ', 'hematology ','mcv']
    lft_keywords = ['lft', 'liver', 'function ', 'biochemistry','A/G ratio', 'sgpt']
    parameter_types_cbc = {
        'hgb': ['hgb', 'haemoglobin', 'hemoglobin'],'mch': ['mch', 'mean corpuscular hemoglobin', 'm.c.h'],
        'mchc': ['mchc', 'mean corpuscular hemoglobin concentration', 'm.c.h.c'],
        'mcv': ['mcv', 'mean corpuscular volume', 'm.c.v'],
    }
    lft_feature_keywords = {
        'total bilirubin': ['tbil', 'tb'],'direct bilirubin': ['dbil', 'db'],'alkaline phosphatase': ['alp'],
        'alanine aminotransferase': ['alt', 'sgpt'],'aspartate aminotransferase': ['ast', 'sgot'],
        'total proteins': ['tp', 'total protein'],'albumin': ['alb'],'A/G ratio': ['ag ratio'],
    }
    for feature in features:
        if any(cbc_item in feature.lower() for cbc_item in cbc_keywords):
            print("CBC test detected")
            cbc = extract_features(features, parameter_types_cbc)
            print (cbc)
            if (cbc==[]):
                return -1,"هذا التحليلتم رفعه بجودة سيءة من فضلك اعد رفع  بجودة احسن   "
            return anemiaPredict(ageGender, cbc)
        elif any(lft_item in feature.lower() for lft_item in lft_keywords):
            print("LFT test detected")
            lft = extract_features(features, lft_feature_keywords)
            if (lft==[]):
                return -1,"هذا التحليل تم رفعه بجودة سيئة من فضلك اعد رفع  بجودة احسن   "
            return liverFailurePredict(ageGender, lft)
    return -1,"هذا التحليل غير مدعوم "  


def result(image, ageGender):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    words = text.split()
    parameter_types_cbc = {
        'hgb': ['hgb', 'haemoglobin', 'hemoglobin'],
        'mch': ['mch', 'mean corpuscular hemoglobin', 'm.c.h'],
        'mchc': ['mchc', 'mean corpuscular hemoglobin concentration', 'm.c.h.c'],
        'mcv': ['mcv', 'mean corpuscular volume', 'm.c.v'],
    }
    lft_feature_keywords = {
        'total bilirubin': ['tbil', 'tb'],
        'direct bilirubin': ['dbil', 'db'],
        'alkaline phosphatase': ['alp'],
        'alanine aminotransferase': ['alt', 'sgpt'],
        'aspartate aminotransferase': ['ast', 'sgot'],
        'total proteins': ['tp', 'total protein'],
        'albumin': ['alb'],
        'A/G ratio': ['ag ratio'],
    }
    result = choose_test_to_extract(words, ageGender)
    return result


# result
# extract_features(words, feature_keywords):
# return features
# def choose_test_to_extract(features,ageGender):
# ageGender : from DB [age,Gender]
def update_result (test:MedicalTest):
    if test.user.is_patient:
        image = test.image.path
        print(image)
        age = test.user.age
        gender = test.user.gender
        if gender == "male":
            g = 0
        else:
            g = 1
        ageGender = [age, g]
        res ,test.test_type= result(image, ageGender)
        test.save()
        if res == 0:
            test.result = "انت بصحة جيدة والنتيجة سلبية "
            test.save()
        elif res == 1:
            test.result = "انت بحاجة لزيارة الطبيب   والنتيجة ايجابية  "
            test.save()
        else:
            test.result = "هذا التحليل غير مدعوم لدينا "
            test.save()
