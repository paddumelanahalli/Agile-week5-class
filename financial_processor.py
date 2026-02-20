def process_transaction(balance, amount, trans_type="debit"):
    # Asserting that amount is always positive before processing
    assert amount > 0, "Transaction amount must be positive"
    
    trans_type = trans_type.lower()
    if trans_type == "debit":
        if amount > balance:
            return "Insufficient Funds"
        return balance - amount
    elif trans_type == "credit":
        return balance + amount
    return "Invalid Transaction Type"
