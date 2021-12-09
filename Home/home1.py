print("Hello world")
print("Hello \nWorld")


a = "Hello "
b = "world"
print(a + b)


def hello_world():
    print("Hello world")
hello_world()


print(input("Hello world? "))


while True:
    print("Hello world")
    break


text = ('Hello', 'world')
delimetr = '_*_'
for i in (text):
    print(i, end=' ')
print(delimetr.join(text))


print("\n{:_^11} {:_^11}".format('Hello', 'World'))


try:
    print(input("Нажми ctrl + D!"))
except:
    print("Hello World!")

hi = {1: 'Hello World',
      2: 'Bye World'
      }
print(hi[1])


print("Hello", end=' World\n')


q = 'hello world'
print(q.upper())


w = ['Hello']
w.append("World")
print(w)

text = 'Hello World'
for i in text:
    print(i, sep=' ')

text = 'Hello World'
for i in text:
    print(i, end=' ')