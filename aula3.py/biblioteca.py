#Crie Livro com titulo, autor, disponivel=True e __str__. Crie Biblioteca com adicionar(), emprestar(titulo), devolver(titulo) e listar_disponiveis().
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Título: {self.titulo} | Autor: {self.autor} | Status: {status}"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar(self, livro):
        self.livros.append(livro)

    def emprestar(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Livro '{titulo}' emprestado com sucesso!")
                else:
                    print(f"Livro '{titulo}' já está emprestado.")
                return
        print("Livro não encontrado.")

    def devolver(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.disponivel = True
                print(f"Livro '{titulo}' devolvido com sucesso!")
                return
        print("Livro não encontrado.")

    def listar_disponiveis(self):
        print("Livros disponíveis:")
        for livro in self.livros:
            if livro.disponivel:
                print(livro)


livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
livro3 = Livro("1984", "George Orwell")

biblioteca = Biblioteca()

biblioteca.adicionar(livro1)
biblioteca.adicionar(livro2)
biblioteca.adicionar(livro3)

biblioteca.listar_disponiveis()

print("\nEmprestando '1984'...")
biblioteca.emprestar("1984")

print("\nLivros disponíveis após o empréstimo:")
biblioteca.listar_disponiveis()

print("\nDevolvendo '1984'...")
biblioteca.devolver("1984")

print("\nLivros disponíveis após a devolução:")
biblioteca.listar_disponiveis()