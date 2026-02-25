def calculate_discounted_price(price, discount_rate):
    # User Input Validation (Handled via if/raise)
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount must be between 0 and 1")
    discounted_price = price * (1 - discount_rate)

# INTERNAL LOGIC ASSERTION
# "I am 100% sure the price cannot be more than the original"
    assert discounted_price <= price, f"Logic Error: {discounted_price} is more than {price}!"
    return discounted_price
# If a bug in the math caused the price to increase, the assert triggers immediately.

def main():
    try:
        # Get user input
        price = float(input("Enter original price: "))
        discount_rate = float(input("Enter discount rate (0 to 1): "))

        # Call function
        final_price = calculate_discounted_price(price, discount_rate)

        # Display result
        print(f"Discounted price: {final_price:.2f}")

    except ValueError as ve:
        print("Input Error:", ve)

    except AssertionError as ae:
        print("Assertion Error:", ae)

    except Exception as e:
        print("Unexpected Error:", e)


if __name__ == "__main__":
    main()
