"""End-to-end tests for the travel planning system"""
import pytest
from datetime import date
from src.graph import run_trip_planning

def test_trip_planning_basic():
    """Test basic trip planning"""
    result = run_trip_planning(
        user_id="test_user",
        destination="Bali",
        date_from=date(2024, 12, 15),
        date_to=date(2024, 12, 25),
        budget_inr=100000,
        preferences=["beach", "culture"]
    )
    assert result is not None

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
