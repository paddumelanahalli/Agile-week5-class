import pytest
from src.financial_processor import process_transaction

class TestFinancialAutomation:

    # --- Boundary Value Analysis (BVA) ---
    def test_bva_debit_exact_balance(self):
        """TC1: Debit exactly equal to balance (Should result in 0)"""
        assert process_transaction(100, 100, "debit") == 0

    def test_bva_minimum_transaction(self):
        """TC2: Smallest possible transaction amount"""
        assert process_transaction(100, 0.01, "credit") == 100.01

    def test_bva_large_transaction(self):
        """TC3: Large transaction amount (Upper boundary)"""
        assert process_transaction(1000000, 1000000, "debit") == 0

    # --- Black-Box / Functional Testing ---
    def test_functional_standard_credit(self):
        """TC4: Standard valid credit transaction"""
        assert process_transaction(500, 200, "credit") == 700

    def test_functional_standard_debit(self):
        """TC5: Standard valid debit transaction"""
        assert process_transaction(500, 200, "debit") == 300

    def test_functional_case_insensitivity(self):
        """TC6: Verify 'CREDIT' in caps still works"""
        assert process_transaction(100, 50, "CREDIT") == 150

    def test_functional_default_type(self):
        """TC7: Verify default transaction type is 'debit'"""
        assert process_transaction(100, 40) == 60

    # --- Negative Testing / Logic Error ---
    def test_negative_insufficient_funds(self):
        """TC8: Debit more than current balance"""
        assert process_transaction(50, 100, "debit") == "Insufficient Funds"

    def test_negative_credit_negative_amount(self):
        """TC9: Attempt to credit a negative number (Should trigger source assert)"""
        with pytest.raises(AssertionError):
            process_transaction(100, -50, "credit")

    def test_negative_invalid_type(self):
        """TC10: Providing an unsupported transaction type"""
        assert process_transaction(100, 50, "loan") == "Invalid Transaction Type"

    # --- Data Integrity / Type Testing ---
    def test_integrity_string_amount(self):
        """TC11: Passing a string as the amount"""
        with pytest.raises(AssertionError):
            process_transaction(100, "50")

    def test_integrity_none_balance(self):
        """TC12: Passing None as balance"""
        with pytest.raises(TypeError):
            process_transaction(None, 50)

    # --- White-Box Testing (Coverage) ---
    def test_whitebox_precision(self):
        """TC13: Testing decimal precision (Floating point)"""
        assert process_transaction(100.55, 0.45, "credit") == 101.0

    # --- Robustness & Stress ---
    def test_robustness_zero_amount(self):
        """TC14: Transaction amount of 0 (Should fail source assert)"""
        with pytest.raises(AssertionError):
            process_transaction(100, 0)

    # --- Idempotency ---
    def test_idempotency_repeat(self):
        """TC15: Repeat same transaction; output must remain consistent"""
        res1 = process_transaction(100, 10, "debit")
        res2 = process_transaction(100, 10, "debit")
        assert res1 == res2 == 90
