import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Days_to_Payment": [5, 12, 3, 15, 6]
}

df = pd.DataFrame(data)

# Identify high-risk delays
risk = df[df["Days_to_Payment"] > 10]

print("High Risk Payments:\n")
print(risk)