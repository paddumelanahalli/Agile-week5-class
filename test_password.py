import pytest
from src.password_validator import validate_password

class TestPasswordValidator:

    # --- Boundary Value Analysis (BVA) ---
    
    def test_bva_exactly_8_chars(self):
        """TC1: Exactly 8 characters - Lower Boundary"""
        assert validate_password("Abc1234!") is True

    def test_bva_exactly_7_chars(self):
        """TC2: Exactly 7 characters - Below Boundary (Should Fail)"""
        assert validate_password("Ab1234!") is False

    def test_bva_25_chars(self):
        """TC3: Upper limit check (25 characters)"""
        long_pwd = "Abc1234!" + "a" * 17
        assert validate_password(long_pwd) is True

    # --- Black-Box / Functional Testing ---

    def test_functional_no_uppercase(self):
        """TC4: Missing Uppercase"""
        assert validate_password("abc1234!") is False

    def test_functional_no_lowercase(self):
        """TC5: Missing Lowercase"""
        assert validate_password("ABC1234!") is False

    def test_functional_no_digits(self):
        """TC6: Missing Digits"""
        assert validate_password("Abcdefgh!") is False

    def test_functional_no_special_chars(self):
        """TC7: Missing Special Characters"""
        assert validate_password("Abc12345") is False

    # --- Negative Testing / Data Integrity ---

    def test_negative_empty_string(self):
        """TC8: Empty String"""
        assert validate_password("") is False

    def test_negative_non_string_type(self):
        """TC9: Non-string input (triggers defensive assert in source)"""
        with pytest.raises(AssertionError):
            validate_password(12345678)

    def test_negative_only_spaces(self):
        """TC10: Password with only whitespace"""
        assert validate_password("        !") is False

    # --- White-Box Testing (Path Coverage) ---

    def test_whitebox_full_coverage(self):
        """TC11: One case that hits every True condition in the logic"""
        # This ensures the 'all()' branch in src/password_validator.py returns True
        assert validate_password("P@ssw0rd123") is True

    # --- Robustness & Edge Cases ---

    def test_robustness_unicode_emojis(self):
        """TC12: Edge case - Unicode/Emojis as special characters"""
        # Testing if the regex or logic handles non-ASCII special chars
        assert validate_password("Abc1234🚀") is True

    # --- Regression Testing ---

    def test_regression_fix_verification(self):
        """TC13: Re-verifying a previously fixed bug (e.g., length bug)"""
        # Simulating a check for a fix where length was previously calculated wrong
        assert validate_password("Xy1!asdf") is True

    # --- Functional / Security ---

    def test_security_common_passwords(self):
        """TC14: Checking against common weak passwords"""
        # If your validator has a list of banned words, this checks that list
        assert validate_password("password") is False
        assert validate_password("12345678") is False

    # --- Idempotency Check ---

    def test_idempotency_repeated_entry(self):
        """TC15: Ensuring the function returns the same result every time"""
        pwd = "Valid123!"
        result1 = validate_password(pwd)
        result2 = validate_password(pwd)
        assert result1 == result2 == True
