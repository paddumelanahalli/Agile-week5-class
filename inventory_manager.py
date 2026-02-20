def merge_inventories(inv1, inv2):
    assert isinstance(inv1, dict) and isinstance(inv2, dict), "Inputs must be dictionaries"
    
    merged = inv1.copy()
    for item, qty in inv2.items():
        merged[item] = merged.get(item, 0) + qty
    return merged
