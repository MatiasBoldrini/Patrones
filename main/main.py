from main.handler import Bank

class Cliente():

    def run(self):
        bank = Bank()
        while True:
            try:
                userInput = int(input("Que cantidad de dinero desea solicitar?  "))
                bank.requestLoan(userInput)
                break
            except ValueError:
                continue