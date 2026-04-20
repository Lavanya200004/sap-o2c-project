import pandas as pd

data = {
    "Customer": ["A", "B", "C", "A", "B"],
    "Order_Amount": [5000, 7000, 3000, 2000, 4000]
}

df = pd.DataFrame(data)

# Total sales per customer
summary = df.groupby("Customer")["Order_Amount"].sum()

print("Sales Summary per Customer:\n")
print(summary)