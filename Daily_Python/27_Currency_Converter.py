print("Simple Currency Converter")
print("Getting exchange rates...")
print("Got rates successfully!\n")

print("Popular: USD EUR GBP JPY CAD AUD CNY INR")

conversion_rates = {
    'EUR': 0.92,
    'GBP': 0.79,
    'JPY': 155.00,
    'CAD': 1.36,
    'AUD': 1.51,
    'CNY': 7.21,
    'INR': 83.50
}

def convert_usd_to(currency, amount):
    if currency in conversion_rates:
        return amount * conversion_rates[currency]
    else:
        return None

def main():
    while True:
        print("\nEnter details:")
        input_curr = input("From currency code (e.g. USD): ").upper()
        output_curr = input("To currency code (e.g. EUR): ").upper()

        try:
            amt = float(input("Amount in USD: "))
        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue

        if input_curr == 'USD':
            result = convert_usd_to(output_curr, amt)
            if result:
                print(f"Result: {amt} {input_curr} = {result:.2f} {output_curr}")
                print(f"Rate: 1 USD = {conversion_rates[output_curr]} {output_curr}")
            else:
                print("Unsupported target currency.")
        else:
            print("This converter only supports USD as the source currency for now.")

        again = input("\nDo you want to convert more currencies? (y/n): ").lower()
        if not again.startswith('y'):
            print("\nThanks for using the Converter!")
            break

main()
