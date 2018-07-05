# coding:utf-8

rw_input = ["flower","flow","flight"]

i = 0
prefix=''
while True:
    try:
        tmp = rw_input[0][i]
        for strs in rw_input:
            if strs[i]==tmp:
                continue
            else:
                print (prefix)
                break
        i+=1
        prefix+=tmp
    except:
        print(prefix)
        break



