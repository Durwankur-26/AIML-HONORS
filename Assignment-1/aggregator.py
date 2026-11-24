
from abc import ABC, abstractmethod
from payment import RazorpayFactory, StripeFactory

class Aggregator(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def pay(self, typ, amt, **kw):
        pass


class RazorpayAggregator(Aggregator):
    def __init__(self):
        super().__init__("Razorpay")
        self.fee = 0.02

    def pay(self, typ, amt, **kw):
        p = RazorpayFactory.get_payment_object(typ, **kw)
        total = amt + (amt * self.fee)
        print("Razorpay:", amt, "Total:", total)
        return p.pay(total)


class StripeAggregator(Aggregator):
    def __init__(self):
        super().__init__("Stripe")
        self.fee = 0.029

    def pay(self, typ, amt, **kw):
        p = StripeFactory.get_payment_object(typ, **kw)
        total = amt + (amt * self.fee)
        print("Stripe:", amt, "Total:", total)
        return p.pay(total)


class AggregatorFactory:
    factory = {
        "stripe": StripeAggregator,
        "razorpay": RazorpayAggregator
    }

    @classmethod
    def get_aggregator(cls, name):
        name = name.lower()

        if name not in cls.factory:
            raise ValueError("Gateway not found")

        return cls.factory[name]()
