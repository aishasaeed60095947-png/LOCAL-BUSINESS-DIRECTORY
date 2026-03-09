import uuid
from datetime import datetime

class Business:
    """
    Represents a registered local business or startup.
    Encapsulates state and behavior as per OOP requirements.
    """
    def __init__(self, name, category, description=""):
        self.id = str(uuid.uuid4())
        self.name = name
        self.category = category
        self.description = description
        self.created_at = datetime.now()
        
    def get_summary(self):
        """
        Behavior method that returns a formatted string of the business details.
        """
        time_str = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.name} ({self.category}) - Added on: {time_str}"
        
    def get_formatted_time(self):
        return self.created_at.strftime("%I:%M %p, %b %d, %Y")


class BusinessStack:
    """
    Implements a Stack (LIFO) data structure using a Python list to manage
    the 'Recently Added' history.
    """
    def __init__(self):
        self._items = []
        
    def push(self, business: Business):
        """Adds a business to the top of the stack."""
        self._items.append(business)
        
    def pop(self):
        """Removes and returns the most recently added business."""
        if not self.is_empty():
            return self._items.pop()
        return None
        
    def is_empty(self):
        return len(self._items) == 0
        
    def get_latest(self):
        """Gets the item at the top of the stack without removing it."""
        if not self.is_empty():
            return self._items[-1]
        return None
        
    def get_recent(self, count=5):
        """
        Returns the most recently added businesses as a list.
        Uses slicing [::-1] to create a new list from top to bottom (LIFO).
        """
        return self._items[::-1][:count]
