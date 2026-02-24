class ReportGenerator:
    """Generates statisitcal repports for habit progres."""

    def __init__(self, manager):
        self.manager = manager

    def build_weekly_repport(self):
        """Creates a weekly summery of habbit completetions."""
        habits = self.manager.get_all_habits()
        lines = []
        lines.append("Weekly Habit Repport")
        lines.append("====================")

        if not habits:
            return "No habbits found. Try addding some first."

        for name, data in habits.items():
            streak = data["streak"]
            lines.append(f"Habbit: {name} | Curent streak: {streak}")

        lines.append("\nKeep up the consistancy and good work!")
        return "\n".join(lines)
