def get_constraints() -> list:
    return [
        {
            "type": "fixed_block",
            "label": "Work hours",
            "start": "08:00",
            "end": "17:00",
            "days": ["mon", "tue", "wed", "thu", "fri"],
        },
    ]
