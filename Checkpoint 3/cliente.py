class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.interacoes = []  # lista de objetos Interacao

    def registrar_interacao(self, interacao):
        """Adiciona uma nova interação com o cliente."""
        self.interacoes.append(interacao)

    def exibir_detalhes(self):
        """Mostra todos os dados e interações do cliente."""
        print(f"\nCliente: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print("Interações:")
        if not self.interacoes:
            print("  Nenhuma interação registrada.")
        else:
            for i in self.interacoes:
                i.exibir_informacoes()
