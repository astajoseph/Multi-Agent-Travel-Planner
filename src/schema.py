from typing import TypedDict, Optional, List, Dict, Any
from datetime import datetime, date
from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    user_id: str
    name: str
    home_city: str
    passport_country: str
    preferences: Dict[str, Any] = Field(default_factory=dict)

class FlightOption(BaseModel):
    departure: str
    arrival: str
    airline: str
    duration_hours: float
    stops: int
    price_inr: float
    departure_time: str
    arrival_time: str

class FlightResult(BaseModel):
    origin: str
    destination: str
    date_from: date
    date_to: date
    options: List[FlightOption] = Field(default_factory=list)
    cheapest_option: Optional[FlightOption] = None
    total_price_inr: float = 0.0

class HotelOption(BaseModel):
    name: str
    city: str
    rating: float
    price_per_night_inr: float
    nights: int
    amenities: List[str] = Field(default_factory=list)
    url: str = ""

class HotelResult(BaseModel):
    destination: str
    check_in: date
    check_out: date
    options: List[HotelOption] = Field(default_factory=list)
    selected_option: Optional[HotelOption] = None
    total_price_inr: float = 0.0

class WeatherDay(BaseModel):
    date: date
    temperature_high_c: float
    temperature_low_c: float
    condition: str
    humidity: int
    rainfall_mm: float

class WeatherResult(BaseModel):
    destination: str
    forecast: List[WeatherDay] = Field(default_factory=list)
    best_time_to_visit: str = ""

class VisaRequirement(BaseModel):
    country: str
    visa_required: bool
    visa_type: str = ""
    validity_days: int = 0
    processing_days: int = 0
    estimated_cost_inr: float = 0.0
    notes: str = ""

class VisaResult(BaseModel):
    passport_country: str
    destination_country: str
    requirements: Optional[VisaRequirement] = None
    checklist: List[str] = Field(default_factory=list)

class Attraction(BaseModel):
    name: str
    city: str
    category: str
    description: str
    estimated_cost_inr: float = 0.0
    duration_hours: float = 2.0
    lat: float = 0.0
    lon: float = 0.0

class AttractionsResult(BaseModel):
    destination: str
    attractions: List[Attraction] = Field(default_factory=list)
    suggested_itinerary: str = ""

class BudgetConflict(BaseModel):
    item_type: str
    item_name: str
    cost_inr: float
    budget_threshold_exceeded: bool
    percentage_of_budget: float

class BudgetPlan(BaseModel):
    base_cost_inr: float = 0.0
    explorer_cost_inr: float = 0.0
    total_estimated_inr: float = 0.0
    is_within_budget: bool = True
    conflicts: List[BudgetConflict] = Field(default_factory=list)
    trade_offs: List[str] = Field(default_factory=list)

class ExplorerOption(BaseModel):
    destination: str
    reason: str
    estimated_cost_inr: float = 0.0
    novel_aspects: List[str] = Field(default_factory=list)

class Approval(BaseModel):
    item_id: str
    approved: bool
    notes: str = ""
    timestamp: datetime = Field(default_factory=datetime.now)

class ItineraryDay(BaseModel):
    date: date
    morning: str
    afternoon: str
    evening: str
    meals: str = ""
    cost_inr: float = 0.0
    weather: str = ""
    notes: str = ""

class Itinerary(BaseModel):
    destination: str
    days: List[ItineraryDay] = Field(default_factory=list)
    total_estimated_cost_inr: float = 0.0
    visa_checklist: List[str] = Field(default_factory=list)
    packing_suggestions: List[str] = Field(default_factory=list)
    emergency_contacts: List[str] = Field(default_factory=list)

class Trip(BaseModel):
    id: str
    user_id: str
    destination: str
    start_date: date
    end_date: date
    budget_inr: float
    actual_cost_inr: float = 0.0
    preferences: Dict[str, Any] = Field(default_factory=dict)
    itinerary: Optional[Itinerary] = None
    rating: int = 0
    feedback: str = ""
    created_at: datetime = Field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None

class TripState(TypedDict, total=False):
    user_id: str
    request: str
    profile: UserProfile
    past_trips: List[Trip]
    flights: FlightResult
    hotels: HotelResult
    weather: WeatherResult
    visa: VisaResult
    attractions: AttractionsResult
    explorer_option: ExplorerOption
    budget_plan: BudgetPlan
    conflicts: List[BudgetConflict]
    replan_count: int
    approvals: Dict[str, Approval]
    final_itinerary: Itinerary
    user_rating: int
    execution_id: str
    created_at: datetime

class CacheEntry(BaseModel):
    key: str
    source: str
    response_json: Dict[str, Any]
    fetched_at: datetime
    ttl_hours: int
