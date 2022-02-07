import json
import spacy

'''
Tokenizer method
'''
def tokenizer(input_string):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_string.lower().replace("\n", " "))
    lemmas = []
    for token in doc:
        if token.is_stop or token.is_punct or token.is_space:
            continue
        lemmas.append(token.lemma_)
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
