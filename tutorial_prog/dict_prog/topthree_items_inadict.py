items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
a = sorted(items.items(),key=lambda x:x[1],reverse=True)
print(a[0][0],a[0][1])
print(a[1][0],a[1][1])
print(a[2][0],a[2][1])
