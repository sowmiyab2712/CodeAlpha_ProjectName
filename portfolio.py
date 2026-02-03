# STOCK PORTFOLIO TRACKER

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_value = 0
portfolio = []

print("📈 STOCK PORTFOLIO TRACKER")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity

    total_value += investment
    portfolio.append(f"{stock}, {quantity}, {investment}")

    print(f"{stock} investment value: ₹{investment}")

# Save portfolio to file (UTF-8 to support ₹ symbol)
with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("Stock, Quantity, Investment\n")
    for item in portfolio:
        file.write(item + "\n")
    file.write(f"\nTotal Investment: ₹{total_value}")

print("\n📁 Portfolio saved to portfolio.txt")
print("💰 Total Investment Value: ₹", total_value)
