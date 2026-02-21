def apply_discount(price: float, discount: float) -> float:

    if not isinstance(price, (float, int)):
        raise TypeError("The price must be a number")

    if not isinstance(discount, (float, int)):
        raise TypeError("The discount must be a number")

    if price <= 0:
        raise ValueError("The price must be greater than 0")

    if not (0 <= discount <= 100):
        raise ValueError("The discount must be between 0 and 100")

    final_price = price - (price * discount / 100)
    return final_price


if __name__ == "__main__":
    try:
        print(f"Price 100, Discount 20: {apply_discount(100, 20)}")
        print(f"Price 50, Discount 0: {apply_discount(50, 0)}")
        print(f"Price 200, Discount 100: {apply_discount(200, 100)}")

    except Exception as e:
        print(f"An error occurred: {e}")