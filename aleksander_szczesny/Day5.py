class Monika():
    university = "PWr"
    year="3d"
    course ="Computer Science"
    age ="22"
    color = "violet"
    city ="Wroclaw"
    b="frfrfr"
    __fre="kek"# weak private

    def listening_music(self):#instance method
        print("Listen to folk music")
        self.a="This is Monica"#lookup of variables


    def listening_music2(self):
        self.b="This is Monica"#lookup of variables


    def dance(self):
        print("bfvkerh")


    @classmethod
    def this_is_new(cls):#class method
        print("This is a class ")

    @classmethod
    def this_is_new2(cls):  # class method
        print(cls.__dict__) #cls

monika = Monika();
monika.dance();
print(monika.b);
monika.listening_music2();
print(Monika.__dict__);
#no constant
#no private section
class strange_integer(int):
    def __init__(self,x):# run whenever new instance is being created
        self.x=x
    def __add__(self, y):
        print ("called")
        return self.x +y

a=strange_integer(10)
#a.super_number =5 --->u f.e. cannot give a value 5 (create with something else
#strange_integer.__
isinstance(a,strange_integer)
b=strange_integer(2)
c=a+b+10
a+5
d=a+5
type(a)
type(d)
#tuple- frozen list
a=(5,10)
class new_tuple(tuple):
    def __init__(self,x):
        self.x=x
        self.y=[]
    def append(self,l):
        self.y.append(l)

a= new_tuple([10])
type(a)
#jupyter
class A():
    var ="ciao"
class B():
    var="hello"
class C(A,B):
    pass
print(C.var)
#C.__mro__  --->the order of a lookup
print (C.__mro__[2].var)
