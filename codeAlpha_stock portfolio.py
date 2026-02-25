# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_investment = 0
portfolio = {}

print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input(f"Enter quantity for {stock}: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    portfolio[stock] = quantity

print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares × {stock_prices[stock]} = {qty * stock_prices[stock]}")

print("Total Investment Value:", total_investment)

# Optional file saving
save = input("\nSave result to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock},{qty},{stock_prices[stock]},{qty * stock_prices[stock]}\n")
        file.write(f"Total Investment,{total_investment}\n")

    print("Portfolio saved to portfolio.txt")