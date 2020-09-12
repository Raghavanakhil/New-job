'''

class Duck:

    def  quack(self):
        print("quack like duck")

    def walk(self):
        print('walk like a duck')

class Person:

    def quack(self):
        print("person cant quack")

    def walk(self):
        print('person can walk but he should walk like a man')



def quackandwalk(thing):
    if isinstance(thing,Duck):
        thing.walk()
        thing.quack()
    else:
        print("please enter a correct obect")


d = Duck()
p = Person

quackandwalk(p)
'''
'''
def squares(x):
    return x*x

def math_user(fun,liss):
    result = []
    for i in liss:
        result.append(fun(i))

    return result


print(math_user(squares,[1,2,3,4,5]))

# we need to treat funcations like any other object or attribute

def logger(msg):
    def inner_log():
        print("messaage",msg)
    return ("lets see")

    #return inner_log

log= logger("hello")
print(log)




def outer(msg):
    def inner():
        print ('itshould print',msg)

    return inner()


outer("job in healtlygx")




def add(number):
    def addition (nums):
        return number+nums
    return addition

ad = add(20)
print(ad(90))

class Emp:
    def __init__(self,firstname,lastname):
        self.name  = firstname
        self. lname  = lastname
        self.email  = self.name + self.lname +".email.com"

    def fullname(self):
        return '{}{}'.format(self.name,self.lname)

emp  = Emp('chellakuty','Akhil')
print(emp.name)
print(emp.email)
print(emp.fullname())
emp.name = 'oscar'
print(emp.name)
print(emp.email)

'''


'''
def  outer(msg):
    message  =msg

    def inner():
        print(message)
    return inner




def whisper(msg):
    print(msg)

    def inner():
        print("closures -->",msg)

        def inerclosur():
            print("chain of closure",msg)

        return inerclosur

    return inner

inners = whisper
inn = inners("onetwothree")
c = inn()
c()



#The split() method converts the string into other data types like lists by breaking a string into pieces.
# Python provides us with two methods: .split() and .rsplit().


#join method converts a list into string.
y = input("enter two values").split(',')
li =  []
for x in y :
    li.append(x)

print(li)


print(type(y))
a=''
def dotscommas(number):
    for i in number:
        if(i==','):
            print('.')
        elif (i=='.'):
            print(',')
        else:
           print(i)


c =dotscommas('14, 625, 498.002')


def Replace(str1):
    str1 = str1.replace(', ', 'raghu')
    print("first print",str1)
    str1 = str1.replace('.', ', ')
    print("second print",str1)
    str1 = str1.replace('third', '.')
    return str1


string = "14, 625, 498.002"
print(Replace(string))
'''
'''
def Replace(arg):
    arg = arg.replace(',','raghu')
    arg = arg.replace('.',',')
    arg = arg.replace('raghu','.')
    return arg
string = "14, 625, 498.002"
print(Replace(string))

  # for maketrans()
def splitstr(string):
    return string.split("-")

abcd = splitstr('Geeks - for - Geeks')
print(abcd)




def inputpresent(string1,string2):

    if(string1.find(string2)==-1):
        print("No")
    else:
        print("yes")


inputpresent('geeks of geeks','rahgu ')

'''
'''
    str  = string2.split()
    print(str)
    for i in range(len(str)):
        if(string1 in str[i]):
            print(str[i])
            return True
        else:
            i+=1



9752509986
aa = inputpresent('geek','geeks of geeks')
print(aa)
'''
'''

def fullname(string):
    k=''
    li = string.split()
    s=len(li)
    for i in li[0:s-1]:
        a=(i[0].join(i[0].upper())+'.')
        k+=a
        #print(a)
    print(k+li[-1].title())

'''
'''
a=[]
str = 'aeiou'
def vow(string):
    for i in string:
        if (i in str):
            #print(i)
            a.append(i)
    return a
s =vow('geeks of geeks')
print(a)
print(len(a))

str_ = "geeks for geeks"
str1 ="gfo"
str2 = "abc"
mapped = str.maketrans(str1,str2)
print(mapped)
print(str_.translate(mapped))


def halves(string):
    half= len(string)
    if(half%2==0):
        finput = string[0:half//2]
        sinput = string[half//2:]

        for i in finput:
            for j in sinput:
                if(i in j):
                    return True
            return False


'''
'''
a = halves("abbaab")
print(a)

a=[]
def duplicates(values):
    for i in set(values):
        counts = values.count(i)
        print(i,counts)

duplicates('raghavan')
'''

'''

def rword(string):
    lists = string.split()
    dict = Counter(lists)
    print(dict)
    print(dict.keys())
    for key in lists:
        print(key)



'''


#rword("Ravi had been saying that he had been there")


#if i in lists[0:len(lists)+1]:

'''

rag = {}
rag.keys()

rag[1] = 'hello'
rag[2] = 'hai'

if rag.values() =='hello':
    rag[1] +=1

print(rag)

s = input("enter any string")
le = len(s)
print(le)

for i in range(1,le+1):
    print(i,le-i)
    print(s[le-i])


def reverse(text):
    rev_text = ""
    for char in text:
        rev_text = char + rev_text
    return rev_text

a = reverse("hello")
print(a)
def reverse(text):
    rev_text = ""
    for char in text:
        rev_text = char + rev_text
    return rev_text

reverse("hello")
'''
'''
def rev(name):
    s1 =name.split()
    s2=[]
    for i in range(len(s1)):
        if(i<=len(s1)):
            i = (len(s1)-1) - i
            s2.append(s1[i])


    return(s2)



aa =   rev("durga software solution")
print(aa)

'''

def mixingname(name1,name2):

    len1 = len(name1)
    len2 = len(name2)
    a=''
    c=0
    if(len1>len2):
        for k in range(len2):
           a =a+name1[k]+name2[k]
           c = len1-len(a)
           print(name1[c:])
        print(a+ name1[c:])
    elif(len2>len1):
        for k in range(len1):
            a = a + name1[k] + name2[k]
            c = len2 - len(a)
        print(a + name2[c:])

mixingname('ravisoft','teja')



a = 'a2b5d6c8'
s1 =s2 = output =""
for i in a:
    if(i.isdigit()):
        s1 = s1 + i
    else:
        s2= s2 + i

output = sorted(s1+s2)
print(output)



a= "a4k3b2"
output =''
previous =''
for i in a:
    if(i.isalpha()):
        output = output + i
        previous= i
    else:
        newchar = chr(ord(previous)+int(i))
        output  = output + newchar
print(output)


print(ord("e"))
print(chr(101))

#ord("character") ==> to find the unicode of the character
# chr(unicode) ==> to find the character of the unicode



def addtwovalues(enter,name):
    outputa = ''
    i = j = 0
    while(i<len(enter) or j<len(name)):
        if(i<len(enter)):
            outputa = outputa + enter[i]
            i = i+1
        if(j<len(name)):
            outputa = outputa +name[j]
            j=j+1

    print(outputa)
addtwovalues('ravisoft','evil')


a ='aabbddcceeeffggghh'
print(''.join(sorted(set(a))))

h ='aabbddcceeeffggghh'
d = []
for i in  h:
    if i not in d:
        d.append(i)
    else:
        i
j = ''.join(d)
print(j)


dup = 'a4b3c2d5'
output=''
previous =''

for i in dup:
    if(i.isalpha()):
        output = output + i
        previous = i
    else:
        newchar = ord(previous)+int(i)
        output =  output+chr(newchar)

print(output)


# Lists:
#--------------

l = []
print(l)
print(type(l))
























