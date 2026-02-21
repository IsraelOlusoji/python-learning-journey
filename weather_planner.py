def is_trip_feasible(
    distance_mi: float,
    is_raining: bool,
    has_bike: bool,
    has_car: bool,
    has_ride_share_app: bool,
) -> bool:
    if not distance_mi:
        return False

    if distance_mi <= 1:
        return not is_raining

    elif distance_mi <= 6:
        return has_bike and not is_raining

    else:
        return has_car or has_ride_share_app


if __name__ == "__main__":
    can_travel = is_trip_feasible(
        distance_mi=3.0,
        is_raining=False,
        has_bike=True,
        has_car=False,
        has_ride_share_app=False,
    )
    print(f"Trip feasible: {can_travel}")
