from score import score

import itertools
import collections


class Category:
    def __init__(self, raw):
        self.name = raw[:raw.find(':')]
        self.words = collections.defaultdict(list)
        for phrase in raw[raw.find(':')+2:].split(', '):
            self.words[''.join(word[0] for word in phrase.split(' ')).upper()].append(' '.join([word.title() for word in phrase.split(' ')]))

    def find(self, c):
        c = c.upper()
        result = self.words.get(c)
        return result if result else [c]

    def has(self, c):
        return c.upper() in self.words


class Template:
    def __init__(self, raw):
        self.cats = list()
        self.fills = ['']
        for word in raw.split(' '):
            if word.isupper():
                self.cats.append(word)
                if len(self.fills) <= len(self.cats):
                    self.fills.append('')
            else:
                if self.fills[-1] != '':
                    self.fills[-1] += ' '
                self.fills[-1] += word

    def cat(self, i):
        return self.cats[i]

    def match(self, s):
        if len(s) != len(self.cats):
            return []
        return [Backronym(''.join(s), b, self.fills) for b in itertools.product(*[CATEGORY[self.cat(i)].find(s[i]) for i in range(len(s))])]


class Backronym:
    def __init__(self, s, words, fills):
        self.s = s.upper()
        self.words = words
        self.fills = fills

    def __iter__(self):
        return self.words.__iter__()

    def __str__(self):
        result = self.fills[0]
        for i in range(len(self.words)):
            if not result.endswith(' ') and len(result) > 0:
                result += ' '
            result += self.words[i]
            if self.fills[i+1] != '':
                result += ' ' + self.fills[i+1]
        return result


CATEGORY = dict()
TEMPLATE = list()


# Parsing categories.txt
def load():
    f = open('categories', 'r')
    global CATEGORY
    CATEGORY = dict()
    for line in f.read().splitlines():
        if line and line[0] != '#':
            cat = Category(line)
            CATEGORY[cat.name] = cat
    f.close()

    # Parsing templates.txt
    f = open('templates', 'r')
    global TEMPLATE
    TEMPLATE = list()
    TEMPLATE = [Template(line) for line in f.read().splitlines() if line and line[0] != '#']
    f.close()


def partitions(a):
    if len(a) == 0:
        return [[]]
    result = list()
    for i in range(1, len(a)+1):
        for partition in partitions(a[i:]):
            result.append([a[:i]] + partition)
    return result


def all_matches(s, template):
    s = s.upper()
    results = list()
    for partition in partitions(list(s)):
        results.extend(template.match([''.join(part) for part in partition]))
    results = list(set(results))
    results.sort(key=lambda x: -score(x))
    return results


def all_backronyms(s):
    s = s.upper()
    results = [match for template in TEMPLATE for match in all_matches(s, template)]
    results = list(set(results))
    results.sort(key=lambda x: -score(x))
    return [str(result) for result in results]


def best_backronym(s):
    s = s.upper()
    temp = all_backronyms(s)
    return temp[0] if temp else s