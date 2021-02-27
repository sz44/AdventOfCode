
'''
find a, find what points to it.
say b
find b see what points to it
say d AND c
find d see what points to it
 say 4
find c see what points to it
 say 2
a = return(b)
b = return(d AND c)
d = return(4)
c = return
'''

values = {}
oper = ['AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT']

def search(name, lines):
    for line in lines:
        l = line.strip('\n').split(' ')
        if name in l:
            if 'AND' in l:
                #do and
                return search(l[0],lines) & search(l[2],lines)
            elif 'OR' in l:
                #do or
                return search(l[0],lines) | search(l[2],lines)
            elif 'NOT' in l:
                #do not
                return search(l[0],lines) ^ 65535
            elif 'LSHIFT' in l:
                #do lshift
                return search(l[0],lines) << l[2]
            elif 'RSHIFT' in l:
                return search(l[0],lines) >> l[2]
                #do lshift
            else:
                #just simple pointing
                #terminate if number reached
                if type(l[0])==int:
                    return l[0]
                else:
                    #continue
                    return search(l[0],lines)


with open('day7txt', 'r') as data:
    lines = data.readlines()
    result = search('a', lines)
    '''
    for line in data.readlines():
        l = line.strip('\n').split(' ')

        if len(l) != 5:
            print(l)
    '''
    print(result)
