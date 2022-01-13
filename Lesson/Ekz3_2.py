def palindrom(text):
    text = text.replace(' ', '').lower()
    return 'Палиндром' if text == text[::-1] else "Не палиндром"

print(palindrom('123322'))