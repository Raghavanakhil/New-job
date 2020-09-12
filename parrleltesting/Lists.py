l = []
print(type(l))
'''
l =eval(input("enter any values"))
print(type(l))
print(l)
'''
l1 =['a','b','c','d']
le = len(l1)
for x in range(le):
    print(x-le)


l1 =[]
l1.append('chellakuty')
l1.append('akhil')
l1.append('dumlikuty')
l1.append('ln')

print(l1)

l1.insert(999,10)
l1.insert(-999,10)
print(l1)
# append
# insert
# count
# extend
#index  - always gives the first index of the number
#remove
#pop
#pop(index)
#reverse
#sort

print(l1.count(10))
l2 =[40,50,60]

print(l1)
print(l2)
print(l1.index('ln'))
l1.extend('Raghavan')
print(l1)
l1.append('raghavan')
print(l1)

l1.remove('dumlikuty')
print(l1)

c= l1.pop()
print(c)
print(l1)

#d= l1.pop(30)
#print(d) # index out of range if the particular index is not available

# remove method will give value error if that particular value is not present

# pop method  will remove the last element by default if index is not mentioned. and will return index out of range if index is not available

#sort() - when trying to sort() . the list should contains only homogeneous objects .

# copy ()- it is method where a different object is being created for the list. and changes in the current list wont affect the previous list.
# copy can be performed in 2 ways - 1. by using slice operator ,2nd using copy function.

# eval = is used to convert into  the particular datataype automatically.

l2 = [50,60,70,80]
l2.reverse()
print(l2)
l2.sort()
print(l2)


lis = [10,40,20,50,25,80]
lis.sort(reverse = True)
print(lis)


k = [10,20,30,40]
#y = k # not recommended as both the rference are pointing to the same object.
print(id(k))
#print(id(y))

y =k[:]
y =k.copy()
print(y)

x =[10,20,30]
y =[40,70,20,90,10,100]

# > than symbol will always compare the first item in two lists.

M =[50,60,70,80]
print(M)
M.clear()
print(M)

# List Comprehensions:
#----------------------

#syntax - [ expression for x in sequence if condition.]
# for x in sequenue if condition is satisfied then the condition.
l1 = []
for i in range(11):
    l1.append(i**2)
print(l1)

l1 = [x**2 for x in range(11)]
print(l1)


words = ['BAL','EDA','ABC','SDAA']
for x in words:
    print(x[0])



# tuple packing and unpacking.



N = [10,40,80,120]
print(N)

N[2]=100
print(N)
N.insert(2,100)
print(N)
#a,b,c,d,e,f= N
#print(a)

u = 100
v = 200
w = 300

l = [u,v,w]
print(l)
print(type(l))

### slice operator and indexing is not applicable in set  objects.

s = {}
print(type(s))
p = set(l)
print(p)
#print(p[0])


## Dictionary
#--------------------------------------

d= {} # represent empty dictionary.
d['name']='chelakuty'
d['age']=30
d['age']=890
print(d)

#print(d[700])

'''
student = eval(input("enter user name and marks"))
print(type(student))
for x in student:
    v = student[x]
    print('the name is'+ x+ 'the marks are '+ str(v))
'''
# important functions and methods in dictionary.


d =dict({(100,'durga'),(200,'suresh'),(300,'mahesh'),(400,'kisher')})
print(d)
d.clear()
print(d)

# clear() this will delete the whole set and keeps it empty.
# del dict  this will delete the dict it self
#  dict.get(key) there are two get methods one with only key and the other with key and default value.
#pop(key) - it removes the entry

dic = {'satish':100,'mahesh':200,'suresh':500,100:'rajesh'}
print(dic)
# pop(),popitem(),key(),values(),items,update,copy,get
c =dic.pop('raghavan',900)
print(dic)
print(c)

e =(dic.keys())
print(e)

for z,c in dic.items():
    print('the key is'+str(z)+ 'the value is '+ str(c))

dic.update([('chelauty',999)])
print(dic)
'''
add=0
sum = eval(input("enter the values please"))
for key in sum:
    add = add + sum[key]
print(add)
'''

string = 'MISSISSIPPI'
dicti = {}
for x in string:
    if x not in dicti:
        dicti[x] =1
    else:
        dicti[x] = dicti[x]+1

for k, v in sorted(dicti.items()):

    print(k,"occurred",v)


mn ={'A':10,'B':20,'C':40,'D':90}

print(mn.get('F'))

