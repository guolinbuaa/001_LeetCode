s='()'
d = {'(': ')', '{': '}', '[': ']'}
l = ''
if len(s) == 1 or len(s) == 0:
    print('false')
    # return False
for i in range(len(s)):
    print(s[i])
    if s[i] in d:
        l += d[s[i]]
        print(l)
        if i == len(s) - 1:
            print('false')
            # return False
    elif s[i] == l[len(l) - 1:]:
        l = l[:len(l) - 1]
        print(l)
        if i == len(s) - 1:
            if l == '':
                print('true')
            else:
                print('false')
    else:
        print('false')