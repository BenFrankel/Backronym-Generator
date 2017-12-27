import generate

generate.load()

print('Enter a period at any time to end the session')
print('Enter a comma to reload categories and templates')
print()

while True:
    acronym = input('Backronym of: ')
    if acronym == '.':
        break
    elif acronym == ',':
        generate.load()
        print('Reloaded successfully')
        print()
    else:
        print(acronym.upper(), '=', generate.all_backronyms(acronym))
        print()
