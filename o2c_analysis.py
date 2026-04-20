import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Order_Amount": [5000, 7000, 3000, 9000, 6000],
    "Days_to_Payment": [5, 7, 3, 10, 6]
}

df = pd.DataFrame(data)

print("Total Revenue:", df["Order_Amount"].sum())
print("Average Payment Days:", df["Days_to_Payment"].mean())

print("\nDelayed Orders:")
print(df[df["Days_to_Payment"] > 7])