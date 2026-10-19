#!/usr/bin/env python3
"""Demo script showing 2 trips with personalization"""
import logging
from datetime import date
from src.graph import run_trip_planning

logging.basicConfig(level=logging.INFO)

def demo_trip_1():
    print("\n=== TRIP 1: Bali Baseline ===")
    result = run_trip_planning(
        user_id="demo_user_1",
        destination="Bali",
        date_from=date(2024, 12, 15),
        date_to=date(2024, 12, 25),
        budget_inr=100000,
        preferences=["beach", "culture"]
    )
    print("Trip 1 completed!")
    return result

def demo_trip_2():
    print("\n=== TRIP 2: Lombok (Personalized) ===")
    result = run_trip_planning(
        user_id="demo_user_1",
        destination="Lombok",
        date_from=date(2025, 3, 1),
        date_to=date(2025, 3, 10),
        budget_inr=85000,
        preferences=["beach", "snorkeling"]
    )
    print("Trip 2 completed! (personalized from Trip 1)")
    return result

if __name__ == "__main__":
    demo_trip_1()
    demo_trip_2()
    print("\n✅ Demo complete!")
