def transfer_money(transaction):
    result = [] 
    for amount in transaction:
        if amount > 0:
            result.append(amount)
    return result

print(transfer_money([120, -50, 300, -20, 450, -100, 80]))