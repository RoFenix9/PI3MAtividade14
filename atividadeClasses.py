class Morador:
    def __init__(self, nome, papel, turno):
        self.nome = nome
        self.papel = papel
        self.turno = turno

    def __str__(self):
        return f"Morador: {self.nome} | Papel: {self.papel} | Turno: {self.turno}"

    def alterar_turno(self, novo_turno):
        self.turno = novo_turno

    def assumir_tarefa(self, tarefa):
        tarefa.responsavel = self


class Tarefa:
    def __init__(self, descricao, responsavel, concluida=False):
        self.descricao = descricao
        self.responsavel = responsavel
        self.concluida = concluida

    def __str__(self):
        return f"Tarefa: {self.descricao} | Responsável: {self.responsavel.nome} | Concluída: {self.concluida}"

    def concluir(self):
        self.concluida = True

    def alterar_responsavel(self, novo_responsavel):
        self.responsavel = novo_responsavel


class ListaTarefas:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __str__(self):
        return f"Lista: {self.nome} | Quantidade de tarefas: {len(self.tarefas)}"

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(tarefa)


# TESTES

morador1 = Morador("João", "Pai", "Noite")
morador2 = Morador("Maria", "Mãe", "Manhã")

print("Moradores:")
print(morador1)
print(morador2)

morador1.alterar_turno("Tarde")

print("\nApós alteração de turno:")
print(morador1)

tarefa1 = Tarefa("Lavar louça", morador1)
tarefa2 = Tarefa("Varrer a casa", morador1)

print("\nTarefas criadas:")
print(tarefa1)
print(tarefa2)

morador2.assumir_tarefa(tarefa2)

print("\nApós Maria assumir a tarefa de varrer a casa:")
print(tarefa2)

tarefa1.concluir()

print("\nApós concluir a tarefa de lavar louça:")
print(tarefa1)

lista1 = ListaTarefas("Tarefas da Semana")
lista2 = ListaTarefas("Tarefas do Final de Semana")

lista1.adicionar_tarefa(tarefa1)
lista2.adicionar_tarefa(tarefa2)

print("\nListas:")
print(lista1)
print(lista2)

print("\nTarefas da Semana:")
lista1.listar_tarefas()

print("\nTarefas do Final de Semana:")
lista2.listar_tarefas()
