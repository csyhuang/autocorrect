# Python 3 Spelling Corrector
#
# Copyright 2014 Jonas McCallum.
# Updated for Python 3, based on Peter Norvig's
# 2007 version: http://norvig.com/spell-correct.html
#
# Open source, MIT license
# http://www.opensource.org/licenses/mit-license.php
"""
Spell function

Author: Jonas McCallum
https://github.com/foobarmus/autocorrect

"""


def spell(word, lang_sample, file_format='bz'):
    from autocorrect.nlp_parser import parse
    from autocorrect.word import Word, common, exact, known, get_case

    """most likely correction for everything up to a double typo"""

    if file_format == 'bz':
        NLP_WORDS, NLP_COUNTS = parse('big.txt', 'bz')
    elif file_format == 'txt':
        NLP_WORDS, NLP_COUNTS = parse(lang_sample, 'txt')


    w = Word(word)
    candidates = (common([word], NLP_WORDS) or exact([word]) or
                  known([word]) or
                  known(w.typos()) or common(w.double_typos()) or
                  [word])
    correction = max(candidates, key=NLP_COUNTS.get)
    return get_case(word, correction)
