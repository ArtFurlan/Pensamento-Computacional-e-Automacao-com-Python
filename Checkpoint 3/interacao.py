class Interacao:
    def __init__(self, tipo, descricao, responsavel):
        self.tipo = tipo
        self.descricao = descricao
        self.responsavel = responsavel

    def exibir_informacoes(self):
        print(f"  - Tipo: {self.tipo} | Descrição: {self.descricao} | Responsável: {self.responsavel}")
