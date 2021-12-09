ne_dic = ('an apple a day keeps the doctor away') # � ������ ��������� ������ ��� .lover/upper
key = []
value = []

print(ne_dic)
for i in ne_dic:
    value.append(ne_dic.count(i))
    key.append(i)

dic = dict(zip(key, value))
print(dic)
