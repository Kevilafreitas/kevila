from abc import ABC, abstractmethod

class PatioLotadoError(Exception):
    pass

class VeiculoNaoEncontradoError(Exception):
    pass

class Veiculo(ABC):
    def __init__(self, placa, horas):
        self.placa = placa
        self.horas = horas

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, nova_placa):
        placa_limpa = nova_placa.strip().upper()

        if len(placa_limpa) != 7:
            raise ValueError("A placa deve conter 7 caracteres.")

        self._placa = placa_limpa

    @abstractmethod
    def tarifa_hora(self):
        pass

    def valor_a_pagar(self):
        return self.horas * self.tarifa_hora()

    def __str__(self):
        return (
            f"{self.placa} "
            f"({self.__class__.__name__}) "
            f"— R$ {self.valor_a_pagar():.2f}"
        )

class Carro(Veiculo):
    def tarifa_hora(self):
        return 5

class Moto(Veiculo):
    def tarifa_hora(self):
        return 3

class Caminhao(Veiculo):
    def tarifa_hora(self):
        return 10

class Estacionamento:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.veiculos = []

    def entrar(self, veiculo):
        if len(self.veiculos) >= self.capacidade:
            raise PatioLotadoError("Não há vagas disponíveis.")

        self.veiculos.append(veiculo)
        print(f"{veiculo.placa} entrou no estacionamento.")

    def sair(self, placa):
        placa = placa.upper()

        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                self.veiculos.remove(veiculo)
                return veiculo

        raise VeiculoNaoEncontradoError(
            f"Veículo com placa {placa} não encontrado."
        )

    def faturamento(self):
        total = 0

        for veiculo in self.veiculos:
            total += veiculo.valor_a_pagar()
        return total

    def listar(self):
        if not self.veiculos:
            print("Nenhum veículo estacionado.")
        else:
            print("\nVeículos no pátio:")
            for item in self.veiculos:
                print(item)


if __name__ == "__main__":

    estacionamento = Estacionamento(capacidade=3)

    try:
        v1 = Carro("abc1d23", 3)
        v2 = Moto("xyz4e56", 5)
        v3 = Caminhao("def7g89", 2)

        estacionamento.entrar(v1)
        estacionamento.entrar(v2)
        estacionamento.entrar(v3)

        estacionamento.listar()

        print(
            f"\nFaturamento: R$ {estacionamento.faturamento():.2f}")
        
        removido = estacionamento.sair("xyz4e56")

    except ValueError as erro:
        print("Erro na placa:", erro)

    except PatioLotadoError as erro:
        print("Erro:", erro)

    except VeiculoNaoEncontradoError as erro:
        print("Erro:", erro)

    else:
        print(f"\nVeículo removido: {removido}")
    finally:
        print("\nOperação finalizada.")