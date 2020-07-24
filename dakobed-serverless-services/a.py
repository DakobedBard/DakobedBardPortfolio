silly = 'dumb'
a = {1:2}
try:
    silly = a[1]
except Exception as e:
    print(e)
print(silly)