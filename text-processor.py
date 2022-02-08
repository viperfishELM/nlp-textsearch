import json
import spacy

nlp = spacy.load("en_core_web_sm")

'''
Tokenizer method
'''
def tokenizer(input_string):
    doc = nlp(input_string.lower().replace("\n", " "))
    tokens_no_stop = [word for word in doc if not word.is_stop and not word.is_punct]
    lemmas = [token.lemma_ for token in tokens_no_stop if token.dep_]
    print(lemmas)
    return lemmas


'''
Load Json data file
'''
def load_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


'''
Persist Results
'''
def persist_data(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


'''
Load data, process, and persist
'''
cdcData = load_data('data.json')
for row in cdcData:
    row['tokenized_text'] = tokenizer(row['text'])
persist_data(cdcData, 'data.json')
