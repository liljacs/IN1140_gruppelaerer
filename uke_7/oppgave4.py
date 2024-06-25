from string import punctuation
from collections import Counter
from nltk import bigrams, trigrams, NaiveBayesClassifier, classify
from nltk.corpus import PlaintextCorpusReader, stopwords


def load_corpus(corpus_root):
    '''Tar inn rotmappen av et korpus.
    Returnerer NLTK-korpus.'''
    return PlaintextCorpusReader(corpus_root, '.*\.txt')


def clean_words(words):
    '''Tar inn en liste med token.
    Returnerer listen uten tegnsetting og stoppord'''
    stopwords_nor = stopwords.words('norwegian')
    return [word.lower() for word in words if word not in punctuation and word not in stopwords_nor]


def split_data(pos_feats, neg_feats):
    '''Tar inn lister med hhv. positive og negative trekk.
    Returnerer listene satt sammen og delt inn i train_set, dev_set, test_set.'''
    test_set = pos_feats[:122] + neg_feats[:122]
    dev_set = pos_feats[122:182] + neg_feats[122:182]
    train_set = pos_feats[182:] + neg_feats[182:]
    
    return train_set, dev_set, test_set


# OPPGAVE 4.2
def feature_extractor_top_1000(document):
    features = {}
    fd = Counter(document)
    frequent_words = [word for word, count in fd.most_common(1000)]

    for word in frequent_words:
        features[f'contains({word})'] = True

    return features


# OPPGAVE 4.3.1
def feature_extractor_bow(document):
    features = {}

    for word in clean_words(set(document)):
        features[f'contains({word})'] = True
    
    # din kode her...
        
    return features


# OPPGAVE 4.3.2
def feature_extractor_bow_bigrams(document):
    features = feature_extractor_bow(document)

    for bigram in set(bigrams(document)):
        features[f'contains({bigram})'] = True

    return features


# OPPGAVE 4.3.3
def feature_extractor_bow_bigrams_trigrams(document):
    features = feature_extractor_bow(document)

    for trigram in set(trigrams(document)):
        features[f'contains({trigram})'] = True
    
    return features



def main():
    # OPPGAVE 4.1
    # din kode her...
    pos_reviews = []
    neg_reviews = []

    korpus = load_corpus("NoReC")

    for dok in korpus.fileids():
        words = [word.lower() for word in korpus.words(dok)]
        if dok.startswith('pos'):
            pos_reviews.append(words)
        if dok.startswith('neg'):
            neg_reviews.append(words)



    # OPPGAVE 4.2
    print('1000 MEST FREKVENTE ORD =========================================')
    # din kode her...
    pos_features = []
    neg_features = []

    for dok in pos_reviews:
        pos_features.append((feature_extractor_top_1000(dok), 'pos'))
    
    for dok in neg_reviews:
        neg_features.append((feature_extractor_top_1000(dok), 'neg'))
    
    train_set, dev_set, test_set = split_data(pos_features, neg_features)

    classifier = NaiveBayesClassifier.train(train_set)
    accuracy = classify.accuracy(classifier, dev_set)
    print("Modell: 1000 mest frekvente ord", accuracy)
    print(classifier.show_most_informative_features(30))

    # svar på teorispørsmål her...

    # OPPGAVE 4.3.1
    print('\nBAG OF WORDS ==================================================')
    pos_features = []
    neg_features = []

    for dok in pos_reviews:
        pos_features.append((feature_extractor_bow(dok), 'pos'))
    
    for dok in neg_reviews:
        neg_features.append((feature_extractor_bow(dok), 'neg'))
    
    train_set, dev_set, test_set = split_data(pos_features, neg_features)

    classifier = NaiveBayesClassifier.train(train_set)
    accuracy = classify.accuracy(classifier, dev_set)
    print("Modell: bow", accuracy)
    print(classifier.show_most_informative_features(10))
    
    # OPPGAVE 4.3.2
    print('\nBAG OF WORDS + BIGRAM =========================================')
    pos_features = []
    neg_features = []

    for dok in pos_reviews:
        pos_features.append((feature_extractor_bow_bigrams(dok), 'pos'))
    
    for dok in neg_reviews:
        neg_features.append((feature_extractor_bow_bigrams(dok), 'neg'))
    
    train_set, dev_set, test_set = split_data(pos_features, neg_features)

    classifier = NaiveBayesClassifier.train(train_set)
    accuracy = classify.accuracy(classifier, dev_set)
    print("Modell: bow+bigram", accuracy)
    print(classifier.show_most_informative_features(10))


    # OPPGAVE 4.3.3
    print('\nBAG OF WORDS + BIGRAM + TRIGRAM ===============================')
    pos_features = []
    neg_features = []

    for dok in pos_reviews:
        pos_features.append((feature_extractor_bow_bigrams_trigrams(dok), 'pos'))
    
    for dok in neg_reviews:
        neg_features.append((feature_extractor_bow_bigrams_trigrams(dok), 'neg'))
    
    train_set, dev_set, test_set = split_data(pos_features, neg_features)

    classifier = NaiveBayesClassifier.train(train_set)
    accuracy = classify.accuracy(classifier, dev_set)
    print("Modell: bow+bigram+trigram", accuracy)

    # OPPGAVE 4.4
    print('\nModellen med ... gir høyest nøyaktighet på dev_set.')
    # din kode her...

    # forslag til forbedring her...


if __name__ == '__main__':
    main()
