class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depositado R${valor:.2f}. Novo saldo: R${self.saldo:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Sacado R${valor:.2f}. Novo saldo: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser positivo.")
conta = ContaBancaria("Cauã", 1000.0)

conta.depositar(250.0)

conta.sacar(300.0)

conta.sacar(2000.0)

conta.depositar(-50.0)