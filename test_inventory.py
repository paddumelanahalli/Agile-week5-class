import pytest
from src.inventory_manager import merge_inventories

class TestInventoryAutomation:

    # --- Functional / Integration Testing ---
    def test_functional_simple_merge(self):
        """TC1: Merging two dictionaries with unique keys"""
        inv1 = {"apples": 10}
        inv2 = {"oranges": 20}
        result = merge_inventories(inv1, inv2)
        assert result == {"apples": 10, "oranges": 20}

    def test_functional_overlap_merge(self):
        """TC2: Merging dictionaries with overlapping keys (Summing)"""
        inv1 = {"apples": 10, "bananas": 5}
        inv2 = {"apples": 5}
        result = merge_inventories(inv1, inv2)
        assert result["apples"] == 15

    # --- Boundary Value Analysis (BVA) ---
    def test_bva_empty_first_dict(self):
        """TC3: First dictionary is empty"""
        assert merge_inventories({}, {"item": 1}) == {"item": 1}

    def test_bva_empty_second_dict(self):
        """TC4: Second dictionary is empty"""
        assert merge_inventories({"item": 1}, {}) == {"item": 1}

    def test_bva_both_empty(self):
        """TC5: Both dictionaries are empty"""
        assert merge_inventories({}, {}) == {}

    # --- Negative Testing / Error Handling ---
    def test_negative_invalid_input_type(self):
        """TC6: Input is a list instead of dict (Triggers source assert)"""
        with pytest.raises(AssertionError):
            merge_inventories([], {})

    def test_negative_string_quantity(self):
        """TC7: Quantity is a string (Check if logic breaks during addition)"""
        with pytest.raises(TypeError):
            merge_inventories({"a": 1}, {"a": "many"})

    # --- Logic & Data Integrity ---
    def test_integrity_zero_quantity(self):
        """TC8: Item quantity is zero"""
        result = merge_inventories({"a": 0}, {"a": 10})
        assert result["a"] == 10

    def test_integrity_negative_quantity(self):
        """TC9: Item quantity is negative (Logic should still sum it)"""
        result = merge_inventories({"a": 10}, {"a": -5})
        assert result["a"] == 5

    # --- White-Box Testing ---
    def test_whitebox_immutability(self):
        """TC10: Ensure the original dictionaries are not modified"""
        i1 = {"a": 1}
        i2 = {"b": 2}
        merge_inventories(i1, i2)
        assert i1 == {"a": 1} # i1 should remain unchanged

    # --- Robustness & Search ---
    def test_robustness_special_chars_keys(self):
        """TC11: Keys with special characters or spaces"""
        inv = {"Item #1": 10}
        assert merge_inventories(inv, inv) == {"Item #1": 20}

    def test_robustness_case_sensitivity(self):
        """TC12: Verify 'Apple' and 'apple' are treated as unique keys"""
        result = merge_inventories({"Apple": 1}, {"apple": 1})
        assert len(result) == 2

    # --- Stress / Large Data ---
    def test_stress_large_dict(self):
        """TC13: Merging dictionaries with 1000 items"""
        inv1 = {f"item{i}": 1 for i in range(1000)}
        inv2 = {"item0": 1}
        result = merge_inventories(inv1, inv2)
        assert result["item0"] == 2
        assert len(result) == 1000

    # --- Regression Testing ---
    def test_regression_float_quantities(self):
        """TC14: Verify floats can be merged correctly after previous int-only bug"""
        assert merge_inventories({"a": 1.5}, {"a": 2.5}) == {"a": 4.0}

    # --- Final Result Integrity ---
    def test_integrity_total_count(self):
        """TC15: Verify final count of unique keys"""
        result = merge_inventories({"a": 1, "b": 1}, {"c": 1, "a": 1})
        assert len(result) == 3
