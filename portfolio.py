# STOCK PORTFOLIO TRACKER WITH PROFIT / LOSS + CSV EXPORT

import csv

# Buy prices (user purchase price)
buy_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

# Current market prices (manually defined)
current_prices = {
    "AAPL": 195,
    "TSLA": 230,
    "GOOGL": 150,
    "MSFT": 310
}

portfolio = {}
total_investment = 0
total_profit_loss = 0

print("📊 STOCK PORTFOLIO TRACKER (CSV EXPORT)")
print("--------------------------------------")

print("\nAvailable Stocks:")
for stock in buy_prices:
    print(stock, "→ Buy ₹", buy_prices[stock], "| Current ₹", current_prices[stock])

# Input loop
while True:
    stock_name = input("\nEnter stock name to buy (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in buy_prices:
        print("❌ Stock not available")
        continue

    quantity = int(input("Enter quantity: "))

    buy_price = buy_prices[stock_name]
    current_price = current_prices[stock_name]

    investment = buy_price * quantity
    profit_loss = (current_price - buy_price) * quantity

    portfolio[stock_name] = {
        "quantity": quantity,
        "buy_price": buy_price,
        "current_price": current_price,
        "investment": investment,
        "profit_loss": profit_loss
    }

    total_investment += investment
    total_profit_loss += profit_loss

    print("✅", stock_name, "added")

# Display summary
print("\n📈 PORTFOLIO SUMMARY")
print("-------------------")

for stock in portfolio:
    pl = portfolio[stock]["profit_loss"]
    status = "PROFIT" if pl > 0 else "LOSS" if pl < 0 else "NO CHANGE"

    print(
        stock,
        "| Qty:", portfolio[stock]["quantity"],
        "| Investment: ₹", portfolio[stock]["investment"],
        "|", status, ": ₹", abs(pl)
    )

print("\n💰 Total Investment: ₹", total_investment)
print("📊 Net Profit/Loss: ₹", total_profit_loss)

# -------- CSV EXPORT --------
with open("portfolio_report.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Header row
    writer.writerow([
        "Stock",
        "Quantity",
        "Buy Price",
        "Current Price",
        "Investment",
        "Profit/Loss"
    ])

    # Data rows
    for stock in portfolio:
        data = portfolio[stock]
        writer.writerow([
            stock,
            data["quantity"],
            data["buy_price"],
            data["current_price"],
            data["investment"],
            data["profit_loss"]
        ])

    # Summary row
    writer.writerow([])
    writer.writerow(["Total Investment", "", "", "", total_investment, total_profit_loss])

print("\n📁 CSV file saved as portfolio_report.csv")

