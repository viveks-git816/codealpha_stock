stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}


portfolio = {}
while True:
    stock = input("Enter stock symbol or name (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break

    
    if stock not in stock_prices:
        try:
            new_price = float(input(f"{stock} not found. Enter price to add it: "))
            stock_prices[stock] = new_price
            print(f"{stock} added with price ${new_price}")
        except ValueError:
            print("Invalid price. Skipping this stock.")
            continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

total = 0
print("\n📊 Investment Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n Total Investment: ${total}")


save = input("Do you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment: ${total}\n")
    print(f"✅ Summary saved to {filename}")
