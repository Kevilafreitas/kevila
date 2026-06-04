#Crie uma função pode_ser_triangulo(a, b, c): a soma de quaisquer 
# dois lados deve ser maior que o terceiro. Se válido, classifique:
#  Equilátero, Isósceles ou Escaleno.
class Triangulo:
    def pode_ser_triangulo(self, a, b, c):
        # Verifica se forma um triângulo
        if a + b > c and a + c > b and b + c > a:

            # Classificação
            if a == b == c:
                return "Triângulo Equilátero"

            elif a == b or a == c or b == c:
                return "Triângulo Isósceles"

            else:
                return "Triângulo Escaleno"

        else:
            return "Os valores não formam um triângulo"


# Criando o objeto
triangulo1= Triangulo()

# Entrada de dados
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Exibindo o resultado
print(triangulo.pode_ser_triangulo(lado1, lado2, lado3))