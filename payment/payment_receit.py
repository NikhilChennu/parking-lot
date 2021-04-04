from abc import ABCMeta
from datetime import datetime

class PaymentNotifierInterface(ABCMeta):

    def Notify(self):
        pass


class PaymentNotifier(PaymentNotifierInterface):

    def __init__(self, payment_id: str, ticket_id: str, start_time: datetime, end_time: datetime, payment_mode: str,
                 amount: float) -> None:
        self.paymane_id = payment_id
        self.startt_time = start_time
        self.end_time = end_time
        self.payment_mode = payment_mode
        self.amount = amount
        self.ticket_id = ticket_id


class PrintReceit(PaymentNotifier):

    def __init__(self, payment_id: str, ticket_id: str, start_time: datetime, end_time: datetime, payment_mode: str,
                 amount: float) -> None:
        super(PrintReceit, self).__init__(payment_id, ticket_id, start_time, end_time, payment_mode, amount)

    def notify(self):
        print("payment_id {}, ticket_id {}".format(self.payment_id, self.ticket_id))


class Email(PaymentNotifierInterface):
    pass
