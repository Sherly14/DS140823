class A:
    def a(self):
      print("A")
class B(A):
    def b(self):
      print("B")
class C(A):
    def c(self):
      print("C")
class D(B):
    def d(self):
      print("D")
class E(B):
    def e(self):
      print("E")
class F(C):
    def f(self):
      print("F")
class G(E,F):
    def g(self):
      print("G")

g=G()
g.g()
g.e()
g.f()

f=F()
f.f()
f.c()

e=E()
e.b()

d=D()
d.d()
d.b()

c=C()
c.c()
c.a()

b=B()
b.b()
b.a()