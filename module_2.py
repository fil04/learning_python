from first_package.module_1 import a


#def test_func():
#    print("jshkfjhsdkfhsdkjhfksdjhfkshdk")
#    return "Returned value"

#print(test_func())


b = [1,2,3,4,5,6,7,8]

def get_c(k, l=[], *args, **kwargs):
    c = [] 
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(args)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(kwargs)
    if len(l) is not 0:
        for i in l:
            i = unicode(i)
            i = i + 'gera pidar1'
            c.append(i)
    else:
        c = "Empty list"
    
    return c

#print(get_c(b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, l=[5,4,3,2,1], sanya='sgdjhasgdjhagsjdgaj'))
#print(get_c(b, b))
#print(get_c(b, b))
#print(get_c(b, b))
#print(get_c(b))

a = lambda x, b: x+b

def a(x):
 #   print("function a")
    return x+1

def b(x):
    print("function b")
    print x + 1
    return "Done"
c = [a, b]
#for i in c:
#    i(1)
#print(b(a))
b = [11, 12, 13]
a = 10
c = 'Vasya Pupkin'
#if 'Vasya' in c:
#    print("if a={0}".format(unicode(a)))
#elif a == 10:
#    print("elif a={}".format(unicode(a)))
#else:
#    print("else a={}".format(unicode(a)))

#for i in b:
#    print(i)
#i=0
#while i <=1 len(b):
#    print(b[i])
#    i = i + 3

def gen(x):
    for i in x:
        yield i

for i in gen(b):
    print(i)






def factor(x):
    if x:
        print("inside {}".format(unicode(x)))
        return x * factor(x-1)
    print("outside {}".format(unicode(x)))
    return 1
#print(factor(3999999999999999999999999999999))




