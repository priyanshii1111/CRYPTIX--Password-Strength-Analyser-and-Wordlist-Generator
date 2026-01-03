import itertools
import os

LEET_MAP = {"a":"@","e":"3","i":"1","o":"0","s":"$"}

def leetspeak(word):
    return "".join(LEET_MAP.get(c.lower(), c) for c in word)

def case_variants(word):
    return {word, word.lower(), word.upper(), word.capitalize()}

def generate_wordlist(name, year, extra):
    words = set()

    # base words
    for w in [name, extra]:
        if w:
            words.update(case_variants(w))

    # adding leetspeak variants
    words.update({leetspeak(w) for w in words})

    # separators to mix words
    seps = ["", "-", "_", ".", "@"]

    variations = set()

    #singleword patterns
    for w in words:
        variations.update({
            w,
            w[::-1],
            w + year,
            year + w,
            w + year[-2:],     # last two digits
        })

    #twoword combos
    if extra:
        for a, b in itertools.permutations(words, 2):
            for s in seps:
                variations.add(a + s + b)
                variations.add(a + s + b + year)

    # numeric suffix patterns
    for w in list(variations):
        for n in ["!", "123", "007", "01", "99"]:
            variations.add(w + n)

    # year range addins
    for w in list(words):
        for y in range(2000, 2026):
            variations.add(w + str(y))

    # save file
    os.makedirs("reports", exist_ok=True)
    filepath = "reports/custom_wordlist.txt"

    with open(filepath, "w") as f:
        for item in sorted(variations):
            f.write(item + "\n")

    return filepath

