import translate

translate.load()

print('Enter a period at any time to end this test.')
print()

while True:
    acronym = input('Backronym of: ')
    if acronym == '.':
        break
    elif acronym == '':
        translate.load()
        print('Data reloaded.')
        print()
    else:
        print(acronym.upper(), '=', translate.all_backronyms(acronym))
        print()