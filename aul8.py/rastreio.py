#Reimplemente a hierarquia A, B(A), C(A), D(B, C). Em cada identificar(), chame super().identificar() antes de imprimir a própria mensagem. Chame obj.identificar() e observe todos os níveis aparecerem em sequência — o MRO em ação.
class A:
    def identificar(self):
        print("Classe A")

class B(A):
    def identificar(self):
        super().identificar()
        print("Classe B")

class C(A):
    def identificar(self):
        super().identificar()
        print("Classe C")

class D(B, C):
    def identificar(self):
        super().identificar()
        print("Classe D")

obj = D()
obj.identificar()