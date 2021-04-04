from abc import ABCMeta, abstractmethod
import hashlib
import random

class PaymentInterface(ABCMeta):
    @abstractmethod
    def pay(self, amount : float) -> str:
        pass

    def paymentMode(self) -> str:
        return self.__class__.__name__


class CreditCard(PaymentInterface):

    def __init__(self, cardNumber, expiry, cvv):
        self.cardNumber = cardNumber
        self.expiry = expiry
        self.cvv = cvv

    def process(self) -> str:
        id = hashlib.md5(str(random.randint()).encode("utf-8")).hexdigest()[:10]
        return id

    def pay(self,  amount :  float) -> str:
        payment_id=self.process()
        return payment_id


class NetBanking(PaymentInterface):
    pass
