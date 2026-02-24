import argparse
from tracker.habit_manager import HabitManager
from tracker.report_genrator import ReportGenerator

def build_parser():
    parser = argparse.ArgumentParser(description="Simple habit tracking applciation.")
    parser.add_argument("--add", help="Add a new habit to track.")
    parser.add_argument("--complete", help="Mark a habit as compleeted.")
    parser.add_argument("--report", action="store_true", help="Generate a progres report.")
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    manager = HabitManager()

    if args.add:
        print(f"Adding new habit: {args.add}")
        manager.add_habbit(args.add)

    if args.complete:
        print(f"Marking habit as compleeted: {args.complete}")
        manager.mark_compleeted(args.complete)

    if args.report:
        print("Genrating progres report...")
        gen = ReportGenerator(manager)
        rep = gen.build_weekly_repport()
        print(rep)

if __name__ == "__main__":
    main()
