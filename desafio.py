class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        for contato in self.contatos:
            print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}, Favorito: {contato.favorito}")

    def editar_contato(self, nome, novo_nome, novo_telefone, novo_email):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.nome = novo_nome
                contato.telefone = novo_telefone
                contato.email = novo_email
                break

    def marcar_favorito(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.favorito = not contato.favorito
                break

    def listar_favoritos(self):
        for contato in self.contatos:
            if contato.favorito:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")

    def deletar_contato(self, nome):
        self.contatos = [contato for contato in self.contatos if contato.nome != nome]

# Exemplo de uso
agenda = Agenda()
agenda.adicionar_contato(Contato("Alice", "123456789", "alice@example.com"))
agenda.listar_contatos()
