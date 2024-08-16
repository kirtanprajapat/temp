dict1 = {}

def dictup():
    upd = int(input("No. of pairs you want to add:"))
    for i in range(upd):
        key = input("Enter key:")
        value = input("Enter value:")
        dict1[key] = value

dictup()

print(dict1)