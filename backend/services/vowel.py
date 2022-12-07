VOWELS = ("a", "e", "i", "o", "u")


def count(words):
    resp = {}
    for d in words:
        total = 0
        for c in d:
            if c.lower() in VOWELS:
                total += 1
        resp[d] = total
    return resp
