# Backronym Engine

Given any sequence of letters, this program guesses what they might stand for (it finds potential [backronyms](https://en.wikipedia.org/wiki/Backronym)).

## How it works

It does this by finding all matches for the sequence of letters from a set of **categories** and a set of **templates**.

A **category** is a set of phrases (one or more words) that are interchangeable in some context, and a **template** is a string to be interpolated with category words.

After generating all the candidate backronyms, it sorts them with a scoring heuristic and displays the top result (or the entire list).

### Example

If we have the following two categories:

```
FRUIT: apple, banana, blueberry, papaya
DRINK: juice, milkshake, shake, smoothie
```

And the following templates:

```
FRUIT DRINK
FRUIT and FRUIT DRINK
```

And we query the engine with the acronym `bps`, we would get the following matches:

```
banana and papaya shake
banana and papaya smoothie
blueberry and papaya shake
blueberry and papaya smoothie
```

## Dependencies

- Python 3.x

## Download

Download this repository with the following [git](https://git-scm.com/) command:

`git clone https://github.com/BenFrankel/BackronymEngine`

Navigate into the downloaded folder and run `python repl.py` to interact with the engine.

## License

This project is licensed under the [Apache 2.0](https://github.com/BenFrankel/BackronymEngine/blob/master/LICENSE) license, so you are free to use, distribute, and modify it.
