#Crie Dispositivo(marca, modelo) com ligar(). Implemente AgendamentoMixin com agendar(horario) que imprime o horário de ativação. Crie Irrigador(Dispositivo, AgendamentoMixin) e demonstre chamando ligar() e agendar('06
class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"{self.marca} {self.modelo} está ligado.")


class AgendamentoMixin:
    def agendar(self, horario):
        print(f"Ativação agendada para {horario}.")


class Irrigador(Dispositivo, AgendamentoMixin):
    pass

irrigador = Irrigador("Tramontina", "IR-100")

irrigador.ligar()
irrigador.agendar("06:00")