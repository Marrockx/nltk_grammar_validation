english = """
    S -> NP VP
    NP -> Det | N | Det N | Det Adj N
    VP -> V | V NP | V NP PP | V Adj N | V VP | V Adj N PP
    PP -> P | P Det | P NP
    Det -> 'the' | 'a' | 'an' | 'my' | 'they' | 'it' | 'our' | 'us' | 'that' | 'this' | 'their'
    N -> 'person' | 'brother' | 'sister' | 'wife' | 'husband' | 'son' | 'mother' | 'father' | 'inlaw' | 'grandparent' | 'ancestor' | 'family' | 'daughter' | 'niece' | 'parent' | 'parents' | 'child' | 'children' | 'twins' | 'uncle' | 'nephew' | 'vacation' | 'musician' 
    Adj -> 'kind' | 'proud' | 'talented' | 'great'
    V -> 'is' | 'are' | 'planning'
    P -> 'on' | 'in' | 'of'
"""

tiv = """
    S -> NP | NP VP
    NP -> N | N Det 
    VP -> V | V Adj | V PP
    PP -> P NP
    Det -> 'wan' | 'a' | 'na' | 'in' | 'nyi'
    N -> 'kwase' | 'Tsombôr' | 'wanye' | 'takerada' | 'kyon'
    Adj -> 'didoo' | 'ave' | 'iyol' | 'doo' | 'or' | 
    V -> 'ngu' | 'bee' | 'fa' | 'tema'
    P -> 'i' | 'na' | 'wa' | 'sha'
"""

yoruba = """
    S -> NP VP | VP
    NP -> N | N Det | N NP
    VP -> V | V NP | V VP | Det V
    Det -> 'òun' | 'ọ̀rẹ́' | 'mi' | 'mẹ́tà' | 'mo'
    N -> "èníyàn" | "ọkùnrin" | "ọkọ" | "ìyá" | "ìyàwo" | "bàbá" | "àná" | "ẹ̀bí" | "òbí" | "ọmọ" | "òjú" | "ọ́nà" | "ọkọ́" | "àtẹ́lẹwọ́" | "ewe" | "ọ̀sán"
    V -> 'jẹ' | 'jẹún' | 'sọrọ' | 'gbo' | 'ranti' | 'wá' | 'ní' | ni | 'fọ́' | 'dúró' | 'ti'
"""

efik = """
    S -> NP VP | VP
    NP -> Det N | Det Adj N
    VP -> V | V NP | V NP PP
    PP -> P NP
    Det -> 'mkpò' | 'nse'
    N -> 'eti' | 'ubok' | 'inua'
    Adj -> 'idip' | 'ófen'
    V -> 'bó'
    P -> 'me' | 'ye' | 'kò'
"""
