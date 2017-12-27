def score(backronym):
    result = 0
    if any(word.isupper() for word in backronym):
        result -= 2*sum(int(word.isupper())*len(word) for word in backronym) + 10
    result -= len(backronym.fills)
    return result
