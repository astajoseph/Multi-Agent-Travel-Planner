"""LangGraph state machine for travel planning orchestration"""
import logging
from datetime import datetime, date
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send

from src.schema import TripState

logger = logging.getLogger(__name__)

def create_travel_planner_graph():
    """Create the LangGraph state machine"""
    workflow = StateGraph(TripState)
    
    # Stub nodes for now - full implementation in documentation
    def stub_node(state):
        return state
    
    workflow.add_node("memory_load", stub_node)
    workflow.add_node("supervisor", stub_node)
    workflow.add_node("explorer", stub_node)
    workflow.add_node("arbiter", stub_node)
    workflow.add_node("composer", stub_node)
    
    workflow.add_edge(START, "memory_load")
    workflow.add_edge("memory_load", "supervisor")
    workflow.add_edge("supervisor", "explorer")
    workflow.add_edge("explorer", "arbiter")
    workflow.add_edge("arbiter", "composer")
    workflow.add_edge("composer", END)
    
    return workflow.compile()

graph = create_travel_planner_graph()

async def run_trip_planning(user_id: str, destination: str, date_from: date, 
                          date_to: date, budget_inr: float, preferences: list = None):
    """Run the trip planning graph"""
    if preferences is None:
        preferences = []
    
    initial_state: TripState = {
        "user_id": user_id,
        "request": f"{destination}, {date_from}–{date_to}, ₹{budget_inr/1000:.0f}k",
        "created_at": datetime.now(),
    }
    
    return graph.invoke(initial_state)
