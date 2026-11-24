
from aggregator import AggregatorFactory

def main():
    while True:
        ag = input("\nGateway (stripe/razorpay) or exit: ").strip().lower()

        if ag == "exit":
            break

        try:
            obj = AggregatorFactory.get_aggregator_object(ag)
        except ValueError:
            print("Wrong gateway.")
            continue

        typ = input("Method (card/upi): ").strip().lower()

        kw = {}

        if typ == "card":
            kw["card_number"] = input("Card number: ")
        elif typ == "upi":
            kw["upi_id"] = input("UPI ID: ")
        else:
            print("Wrong method.")
            continue

        try:
            amt = float(input("Amount: "))

            if amt <= 0:
                print("Invalid amount.")
                continue

        except ValueError:
            print("Enter a valid amount.")
            continue

        print("\nProcessing...")

        try:
            res = obj.call_get_payment_object(typ, amt, **kw)

            if res:
                print("Payment successful!")

        except Exception as e:
            print("Payment failed:", e)


if __name__ == "__main__":
    main()
