import nltk

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

from nltk import CFG
from nltk.parse import SteppingRecursiveDescentParser

import language_grammar
from sentences import *


def parse_grammar(grammar):
    return CFG.fromstring(grammar)


def get_language_grammar(language):
    if language == "english":
        return language_grammar.english
    elif language == "yoruba":
        return language_grammar.yoruba
    elif language == "tiv":
        return language_grammar.tiv
    elif language == "elif":
        return language_grammar.efik


def is_valid_sentence(sentence, grammar):
    parser = SteppingRecursiveDescentParser(grammar, trace=1)
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    try:
        for token in tokens:
            if token.isalpha():
                parse_tree = list(parser.parse(tokens))
                # Check if any parse tree is found for the sentence
                if len(parse_tree) > 0:
                    return parse_tree[0]
                else:
                    return None
    except:
        print("Failed to parse....")
        return None


def is_sentence_correct(sentence: str, language):
    grammar = parse_grammar(get_language_grammar(language))

    # To remove whitespace from sentence
    sentence = sentence.replace('.', '').strip().lower()
    # sentence = "the cat chased a dog"
    parse_tree = is_valid_sentence(sentence, grammar)

    if parse_tree is not None:
        print(
            f"In the defined grammar of {language} Language above, we would evaluate the sentence", {sentence},
            ";\n".format(language, sentence))
        print("This sentence is grammatically correct and hence valid!\n")
        print("The parse tree is:\n")
        try:
            parse_tree.pretty_print()
        except:
            return (f"not defined in {language} grammar").format()
    else:
        print("This sentence is not grammatically correct. It is not valid, you may have to update the grammar")


def main():
    is_sentence_correct(correct_tiv_sentences[0], "tiv")


if __name__ == '__main__':
    main()
