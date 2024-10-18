import spacy

nlp = spacy.load('en_core_web_sm')
def extract_predicates(sentence): 
    doc = nlp(sentence)
    predicates = []
    for token in doc:
        if token.dep_== 'attr' or token.dep_== 'acomp':
            predicates.append(token.text)

    for token in doc:
        if token.pos == 'VERB' and token.dep_ != 'aux': 
            predicates.append(token.lemma_)

    return sorted(set(predicates))

sentences = [
    "Chinki is a cat.",
    "Sanchin is a cricketer and plays cricket.",
    "Some boys are intelligent."
]

for sentence in sentences:
    predicates = extract_predicates(sentence)
    print(f"Predicates in the sentence '{sentence}': {predicates}")
