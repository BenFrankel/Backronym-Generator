import generate

generate.load()

print(('Enter a period at any time to end the session\n'
       'Enter a comma to reload categories and templates\n'))

while True:
    try:
        acronym = input('Backronym of: ')
    except EOFError:
        break
    if acronym == '.':
        break

    if acronym == ',':
        generate.load()
        print('Reloaded successfully')
    else:
        print(acronym.upper(), '=', generate.all_backronyms(acronym))
    print()
