# ex05.py - Modificadores de acesso
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0  # convenção de "privado"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor de depósito inválido.")

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria()
conta.depositar(500)
conta.depositar(-50)

print("Saldo: R$", conta.consultar_saldo())
