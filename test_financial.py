import pytest
from src.financial_processor import process_transaction

def test_bva_exact_balance():
    """TC: Boundary Value Analysis - Zeroing out balance"""
    assert process_transaction(100, 100, "debit") == 0

def test_negative_overdraft():
    """TC: Negative Testing - Logic error check"""
    assert process_transaction(50, 100, "debit") == "Insufficient Funds"

def test_assert_trigger_on_negative_input():
    """TC: Verifying the internal source code assertion works"""
    with pytest.raises(AssertionError):
        process_transaction(100, -50, "credit")
