from cliente import Cliente
from interacao import Interacao

# cria cliente
cliente1 = Cliente("João Silva", "joao@email.com", "(11) 9999-9999")

# cria interações
int1 = Interacao("Ligação", "Cliente solicitou informações sobre o produto", "Mariana")
int2 = Interacao("Reunião", "Apresentação da proposta comercial", "Carlos")

# registra interações no cliente
cliente1.registrar_interacao(int1)
cliente1.registrar_interacao(int2)

# exibe relatório do cliente
cliente1.exibir_detalhes()
