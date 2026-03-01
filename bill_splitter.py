def split_bill(
    appetizers: float,
    main_courses: float,
    desserts: float,
    drinks: float,
    num_of_friends: int,
    tip_percentage: float = 0.25,
) -> dict[str, float]:

    if any(cost < 0 for cost in [appetizers, main_courses, desserts, drinks]):
        raise ValueError("Costs cannot be negative")

    if tip_percentage < 0:
        raise ValueError("Tip percentage cannot be negative")

    if num_of_friends < 1:
        raise ValueError("Number of friends must be at least 1")

    running_total = appetizers + main_courses + desserts + drinks
    tip = running_total * tip_percentage
    total_with_tip = running_total + tip

    # Calculate amount per person, round to 2 decimal places to mimic currency standard
    each_pays = round(total_with_tip / num_of_friends, 2)

    return {
        "running_total": running_total,
        "total_with_tip": total_with_tip,
        "each_pays": each_pays,
    }


if __name__ == "__main__":
    try:
        result = split_bill(
            appetizers=37.89,
            main_courses=57.34,
            desserts=39.39,
            drinks=64.21,
            num_of_friends=4,
            tip_percentage=0.25,
        )
        print("Total bill so far:", result["running_total"])
        print("Total with tip:", result["total_with_tip"])
        print("Each person pays:", result["each_pays"])
    except ValueError as e:
        print(f"Error: {e}")
