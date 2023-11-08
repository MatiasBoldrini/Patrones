from abc import ABCMeta, abstractmethod

class ApproverABS(metaclass=ABCMeta):

    @abstractmethod
    def setNext(self, approver) -> None:
        pass

    @abstractmethod
    def getNext(self):
        pass

    @abstractmethod
    def requestLoan(self, money: int) -> None:
        pass
