from . import *


class Bank(ApproverABS):
    def __init__(self) -> None:
        self.next = None

    def setNext(self, approver: ApproverABS) -> None:
        self.next = approver

    def getNext(self) -> ApproverABS:
        return self.next

    def requestLoan(self, money: int) -> None:
        accountExecutive = AccountExecutive()
        self.setNext(accountExecutive)
        ejecutiveTeamLeader = EjecutiveTeamLeader()
        accountExecutive.setNext(ejecutiveTeamLeader)
        manager = Manager()
        ejecutiveTeamLeader.setNext(manager)
        director = Director()
        manager.setNext(director)
        self.next.requestLoan(money)
