def check_booking_eligibility(age: int) -> bool:
    if age > 17:
        print("User is eligible to book a ticket")
        return True
    return False


def check_evening_show_eligibility(age: int) -> bool:
    if age >= 21:
        print("User is eligible for Evening shows")
        return True
    else:
        print("User is not eligible for Evening shows")
        return False


def calculate_discount(age: int, is_member: bool) -> float:
    discount = 0.0
    if is_member and age >= 21:
        discount = 3.0
        print("User qualifies for membership discount")
    else:
        print("User does not qualify for membership discount")
    print("Discount:", discount)
    return discount


def calculate_extra_charges(is_weekend: bool, show_time: str) -> float:
    extra_charges = 0.0
    if is_weekend or show_time == "Evening":
        extra_charges = 2.0
        print("Extra charges will be applied")
    else:
        print("No extra charges will be applied")
    print("Extra charges:", extra_charges)
    return extra_charges


def calculate_service_charges(seat_type: str) -> float:
    if seat_type == "Premium":
        return 5.0
    elif seat_type == "Gold":
        return 3.0
    else:
        return 1.0


def process_booking(
    age: int,
    seat_type: str,
    show_time: str,
    is_member: bool,
    is_weekend: bool,
    base_price: int = 15,
):
    if age > 17:
        print("User is eligible to book a ticket")

    check_evening_show_eligibility(age)

    discount = calculate_discount(age, is_member)

    extra_charges = calculate_extra_charges(is_weekend, show_time)

    # Main booking condition

    booking_condition_met = False
    if age >= 21:
        booking_condition_met = True
    elif age >= 18 and (show_time != "Evening" or is_member):
        booking_condition_met = True

    if booking_condition_met:
        print("Ticket booking condition satisfied")
        service_charges = calculate_service_charges(seat_type)
        print("Service charges:", service_charges)

        # Calculate final price with updated values
        final_price = base_price + extra_charges + service_charges - discount
        print("Final price of ticket:", final_price)
    else:
        print("Ticket booking failed due to restrictions")


if __name__ == "__main__":
    # Test values
    process_booking(
        age=21, seat_type="Gold", show_time="Evening", is_member=True, is_weekend=False
    )
