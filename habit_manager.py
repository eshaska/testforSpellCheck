from datetime import datetime

class HabitManager:
    """Manages habbits and stores completetion history."""

    def __init__(self):
        self.habits = {}
        self.history = {}

    def add_habbit(self, name: str):
        """Adds a new habbit to the internal colleciton."""
        if name in self.habits:
            print("Habit alredy exists, skiping add.")
            return
        self.habits[name] = {
            "created_at": datetime.now(),
            "streak": 0
        }
        print(f"Habbit '{name}' succesfully added.")

    def mark_compleeted(self, name: str):
        """Marks a habbit as done for today and updates strek."""
        if name not in self.habits:
            print("Habbit not foudn in system.")
            return

        today = datetime.now().date()
        if name not in self.history:
            self.history[name] = []

        self.history[name].append(today)
        self.habits[name]["streak"] += 1
        print(f"Habbit '{name}' compleeted for {today}.")

    def get_all_habits(self):
        """Returns all habbits currenty being tracked."""
        return self.habits
