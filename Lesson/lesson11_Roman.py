s = input()
dic = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
result = 0
for i, c in enumerate(s):
    if (i+1) == len(s) or dic[c] >= dic[s[i+1]]:
        result += dic[c]
    else:
        result -= dic[c]

print(result)