def contact(name, last_name, age, number):
    with open('contacts.txt', 'w', encoding='utf-8') as f:
        f.write(f'{name}:{last_name}:{age}:{number}')


contact('Alex', 'Green', 27, 123456789)


def read_contact():
    with open('contacts.txt', encoding='utf-8') as f:
        nickname = {}
        for line in f:
            line = line.replace('\n', '')
            line = line.split(':')
            nickname = {'name': line[0],
                        'last_name': line[1],
                        'age': line[2],
                        'number': line[-1]}
    return nickname


print(read_contact())
