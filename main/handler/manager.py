from . import ApproverABS

class Manager(ApproverABS):
    def __init__(self):
        self.next = None

    def setNext(self, approver: ApproverABS) -> None:
        self.next = approver

    def getNext(self) -> ApproverABS:
        return self.next

    def requestLoan(self, money: int) -> None:
        if 50000 < money <= 100000:
            print("Lo manejo yo, el gerente!")
        else:
            self.next.requestLoan(money)