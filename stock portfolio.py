# stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 310
}

portfolio = {}
total_value = 0

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculation of total investment
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\nTotal investment value: ${total_value}")

# Save to a file
save = input("Would you like to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
        file.write(f"\nTotal investment value: ${total_value}")
    print("Portfolio saved to 'portfolio_summary.txt'")
