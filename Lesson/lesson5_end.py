arr = [1,2,3,4,5,6,7]
arr_2 = []
arr_3 = []
q = 0
for i in arr:
    if i % 2 == 0:
        arr_2.append(i)
    else:
        arr_3.append(i)
if len(arr_2)> len(arr_3):
    for z in arr_2:
        q += z
        print(q)
else:
    print(arr[0]*arr[2]*arr[5])