arr = input('Enter your word')
low = 0
up = 0
vowels = 0
ne_vowels = 0


for i, k in zip(arr, arr[1:]):
    if i.islower() and k.islower():
        low += 1
    elif i.isupper() and k.isupper():
        up += 1
for l in arr:
    if l.lower() in 'aeiouy':
        vowels += 1
    elif l.lower() in 'bcdfghjklmnpqrstvwxz':
        ne_vowels += 1


print(f'пар в нижнем регистра: {low}, в верхнем: {up}')
print('Всего букв в слове:', len(arr))
print(f'Глассных: {vowels}, согласных: {ne_vowels}')
