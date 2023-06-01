<!-- @format -->

### NLTK GRAMMAR VALIDATION

---

clone the repo then

- ## To run the script, run the following command
  ```
  python grammar_checker.py
  ```

###### support for 3 indigeneous languages - Yoruba, Tiv and Ibibio

&nbsp;&nbsp;&nbsp;

**use case in Tiv Language**

Parsing 'na tarkaa ga mba'

<div style="font-size: 12px; display: flex; flex-direction: column; whitespace: pre-line">
    Found a parse:
    (S (NP (Det na) (N tarkaa)) (VP (V ga) (NP (N mba))))


    Context Free Grammar (CFG) for Tiv Language
     Grammar with 33 productions (start state = S)
        S -> NP VP
        NP -> N
        NP -> Det N
        NP -> Det Adj N
        VP -> V
        VP -> V NP
        VP -> V PP
        PP -> P NP
        Det -> 'ka'
        Det -> 'a'
        Det -> 'na'
        Det -> 'in'
        Det -> 'nyi'
        N -> 'doo'
        N -> 'mba'
        N -> 'kwagh'
        N -> 'terver'
        N -> 'shima'
        N -> 'tarkaa'
        Adj -> 'kpa'
        Adj -> 'nyin'
        Adj -> 'mbaaka'
        Adj -> 'ughondo'
        Adj -> 'hemen'
        V -> 'ver'
        V -> 'ba'
        V -> 'yan'
        V -> 'be'
        V -> 'ga'
        V -> 'kpa'
        P -> 'ga'
        P -> 'na'
        P -> 'wa'

</div>
In the defined grammar of Tiv Language above, we would evaluate the sentence {'na tarkaa ga mba'} ;

This sentence is grammatically correct and hence valid!

The parse tree is:

> OUTPUT

                S
        __________|_______
        |                 VP
        |               ___|___
        NP             |       NP
    ____|___           |       |
    |       |          V       N
    Det     N          |       |
    |       |          |       |
    na      tarkaa    ga      mba

None
