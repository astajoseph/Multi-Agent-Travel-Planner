"""Supabase database operations with pgvector support"""
import logging
logger = logging.getLogger(__name__)

class DatabaseManager:
    """Manages Supabase operations"""
    def __init__(self, demo_mode=True):
        self.demo_mode = demo_mode
    
    def is_connected(self):
        return not self.demo_mode
    
    def get_user_profile(self, user_id):
        return None
    
    def get_past_trips(self, user_id):
        return []
