#Crie funções de conversão:
#• km_para_milhas: × 0.621371
#• kg_para_libras: × 2.20462
#• celsius_para_fahrenheit: × 1.8 + 32
#Exiba um menu e use if/elif para a escolha.
class Conversor:
    def km_para_milhas(self, km):
        return km * 0.621371

    def kg_para_libras(self, kg):
        return kg * 2.20462

    def celsius_para_fahrenheit(self, celsius):
        return celsius * 1.8 + 32


# Criando objeto
conversor = Conversor()

# Menu
print("=== CONVERSOR DE UNIDADES ===")
print("1 - Km para Milhas")
print("2 - Kg para Libras")
print("3 - Celsius para Fahrenheit")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    km = float(input("Digite a distância em km: "))
    resultado = conversor.km_para_milhas(km)
    print(f"{km} km = {resultado:.2f} milhas")

elif opcao == 2:
    kg = float(input("Digite o peso em kg: "))
    resultado = conversor.kg_para_libras(kg)
    print(f"{kg} kg = {resultado:.2f} libras")

elif opcao == 3:
    celsius = float(input("Digite a temperatura em °C: "))
    resultado = conversor.celsius_para_fahrenheit(celsius)
    print(f"{celsius} °C = {resultado:.2f} °F")

else:
    print("Opção inválida!")
