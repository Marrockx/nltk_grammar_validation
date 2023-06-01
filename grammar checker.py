import nltk
import pprint

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

from nltk import CFG
from nltk.parse import SteppingRecursiveDescentParser

# a function to check if a sentence is valid


def is_valid_sentence(sentence, grammar):
    parser = SteppingRecursiveDescentParser(grammar,  trace=1)
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    try:
        for token in tokens:
            if (token.isalpha()):
                parse_tree = list(parser.parse(tokens))
                # Check if any parse tree is found for the sentence
                if len(parse_tree) > 0:
                    return parse_tree[0]
                else:
                    return None
    except:
        return None

# context free grammar definitions for English Language

# This grammar defines a sentence (S) that consists of a noun phrase (NP) followed by a verb phrase (VP).
# The noun phrase can include a determiner (Det), an optional adjective (Adj), and a noun (N).
# The verb phrase can include a verb (V), a noun phrase (NP), and an optional prepositional phrase (PP).
# The prepositional phrase consists of a preposition (P) followed by a noun phrase (NP).


def grammar_english():
    # English grammar implementation
    return CFG.fromstring("""
    S -> NP VP
    NP -> Det | N | Det N | Det Adj N
    VP -> V | V NP | V NP PP | V Adj N | V VP | V Adj N PP
    PP -> P | P Det | P NP
    Det -> 'the' | 'a' | 'an' | 'my' | 'they' | 'it' | 'our' | 'us' | 'that' | 'this' | 'their'
    N -> 'person' | 'brother' | 'sister' | 'wife' | 'husband' | 'son' | 'mother' | 'father' | 'inlaw' | 'grandparent' | 'ancestor' | 'family' | 'daughter' | 'niece' | 'parent' | 'parents' | 'child' | 'children' | 'twins' | 'uncle' | 'nephew' | 'vacation' | 'musician' 
    Adj -> 'kind' | 'proud' | 'talented' | 'great'
    V -> 'is' | 'are' | 'planning'
    P -> 'on' | 'in' | 'of'
""")
    pass


def grammar_yoruba():
    # Yoruba grammar implementation
    return CFG.fromstring("""
    S -> NP VP | VP
    NP -> N | N Det | N NP
    VP -> V | V NP | V VP | Det V
    Det -> 'òun' | 'ọ̀rẹ́' | 'mi' | 'mẹ́tà' | 'mo'
    N -> "èníyàn" | "ọkùnrin" | "ọkọ" | "ìyá" | "ìyàwo" | "bàbá" | "àná" | "ẹ̀bí" | "òbí" | "ọmọ" | "òjú" | "ọ́nà" | "ọkọ́" | "àtẹ́lẹwọ́" | "ewe" | "ọ̀sán"
    V -> 'jẹ' | 'jẹún' | 'sọrọ' | 'gbo' | 'ranti' | 'wá' | 'ní' | ni | 'fọ́' | 'dúró' | 'ti'
""")
    pass


def grammar_tiv():
    # Tiv grammar implementation
    return CFG.fromstring("""
    S -> NP VP
    NP -> N | Det N | Det Adj N
    VP -> V | V NP | V PP
    PP -> P NP
    Det -> 'ka' | 'a' | 'na' | 'in' | 'nyi'
    N -> 'doo' | 'mba' | 'kwagh' | 'terver' | 'shima' | 'tarkaa'
    Adj -> 'kpa' | 'nyin' | 'mbaaka' | 'ughondo' | 'hemen'
    V -> 'ver' | 'ba' | 'yan' | 'be' | 'ga' | 'kpa'
    P -> 'ga' | 'na' | 'wa' 
""")
    pass


def grammar_efik():
    # Efik grammar implementation
    return CFG.fromstring("""
    S -> NP VP | VP
    NP -> Det N | Det Adj N
    VP -> V | V NP | V NP PP
    PP -> P NP
    Det -> 'mkpò' | 'nse'
    N -> 'eti' | 'ubok' | 'inua'
    Adj -> 'idip' | 'ófen'
    V -> 'bó'
    P -> 'me' | 'ye' | 'kò'
""")
    pass


def select_language(language):
    selected_language = language
    if language == grammar_english:
        selected_language = 'English'
    elif language == grammar_yoruba:
        selected_language = 'Yoruba'
    elif language == grammar_tiv:
        selected_language = 'Tiv'
    elif language == grammar_efik:
        selected_language = 'Efik'
    print("Context Free Grammar (CFG) for",
          selected_language, "Language\n", language())
    return selected_language


def is_sentence_correct(sentence: str, language):

    # to remove whitespace from sentence
    sentence = sentence.replace('.', '').strip().lower()
    # sentence = "the cat chased a dog"
    parse_tree = is_valid_sentence(sentence, language())

    selected_language = select_language(language)

    if parse_tree is not None:
        print(
            f"In the defined grammar of {selected_language} Language above, we would evaluate the sentence", {sentence}, ";\n".format(selected_language, sentence))
        print("This sentence is grammatically correct and hence valid!\n")
        print("The parse tree is:\n")
        try:
            parse_tree.pretty_print()
        except:
            return (f'not defined in {selected_language} grammar').format()
    else:
        print("This sentence is not grammatically correct. It is not valid, you may have to update the grammar")


# ENGLISH SENTENCES THAT ARE CORRECT
correct_english_sentences = [
    "My wife is a kind person.",
    "They are proud parents of twins.",
    "My sister is a talented musician.",
    "My brother is a great father."
]

incorrect_english_sentences = [
    "My wife is a kind trait.",
    "They is proud parents of twins.",
    "Our family is planning a vacation.",
    "My sister is a talented musicians.",
    "My brother is a great fathers."
]

correct_yoruba_sentences = [
    "ìyá mi ti jẹún ní òjú ọ́nà.",
    "Mo jẹún",
    "Ọmọ mi ti wà lára ilé.",
    "Bàbá mi ní ọkọ́ mẹ́tà.",
    "Ẹ̀yin ni èrò ẹni nínú ilé."
]

incorrect_yoruba_sentences = [
    "Iyá mi ti wá jẹun lọ́nà.",
    "Mo jẹún ni àtẹ́lẹwọ́ ni òjú ewe.",

]

correct_tiv_sentences = [
    "Doo ver.",
    "A mba yan.",
    "Na tarkaa ga mba.",
]

incorrect_tiv_sentences = [
    "Nyin ver in kwagh.",
    "Ka doo.",
]

correct_efik_sentences = [
    "Mkpò eti bó.",
    "Nse ubok bó.",
]

incorrect_efik_sentences = [
    "Nse inua ófen.",
    "Mkpò eti bó me ubok.",
    "Nse inua idip me eti."
]

print(is_sentence_correct(correct_english_sentences[2], grammar_english))
print(is_sentence_correct(incorrect_english_sentences[3], grammar_english))
print(is_sentence_correct(correct_yoruba_sentences[1], grammar_yoruba))
print(is_sentence_correct(correct_tiv_sentences[2], grammar_tiv))
print(is_sentence_correct(correct_efik_sentences[0], grammar_efik))
