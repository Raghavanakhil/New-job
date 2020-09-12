class example:
    def add(self,a ,g):
       self.a = a
       self.b = g

       c =example.sums(self)
       print(c)


    def sums(self):
        c = self.a+self.b
        return(c)

Ex= example()
Ex.add(5,6)


a = 'september last day is my working day in old company'
class exam:
    a = 'i got a new job'

    def input1(self,a):
        a = 'coimbatore i am going to join'

        print("we can call it using class variables",exam.a)
        print("we can call it using instance variables",self.a)
        print("outside the class",a)


Exam = exam()
Exam.input1('Raghavan')


'''
def emp_add(emp,emplist=[]):
    emplist.append(emp)
    print(emplist)

print(emp_add.__defaults__)
emp_add('chellakuty')
print("default1",emp_add.__defaults__)
emp_add('akhil',['jaya','yogesh'])
print("default2",emp_add.__defaults__)
#emp_add(('dumlikuty','bagadi'))
'''

def empadd(emp,emplist=None):
    if emplist is None:
        emplist =[]
    emplist.append(emp)
    print(emplist)

print("default1",empadd.__defaults__)
empadd('Raghavan')
print("default",empadd.__defaults__)
empadd(('Rghavan','chellakuty','lolakuty'))


#genertors


def sqrnum(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

n = sqrnum([1,2,3,4,5])
print(n)


def squrnum(nums):
    for i in nums:
        yield  i*i

s = squrnum([10,20,30,40,50])
for i in s:
    print(list(i))



























