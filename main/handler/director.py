from . import ApproverABS

class Director(ApproverABS):
    def __init__(self) -> None:
        self.next = None

    def setNext(self, approver: ApproverABS) -> None:
        self.next = approver

    def getNext(self) -> ApproverABS:
        return self.next

    def requestLoan(self, money: int) -> None:
        if money > 100000:
            print("Lo manejo yo, el director!")
