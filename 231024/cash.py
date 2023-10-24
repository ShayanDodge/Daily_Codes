from cashRegister import CashRegister

cash = CashRegister()
cash.addItem(100)
cash.addItem(100)
cash.addItem(100)
cash.addItem(100)
cash.addItem(100)
result = cash.getTotal()
print("Value:", result)


