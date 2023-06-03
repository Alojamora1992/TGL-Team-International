import ui
from datetime import datetime
from tabulate import tabulate

scores = []

def add_score(name: str, trials: int, difficulty: str) -> None:
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    score = {
        "name": name,
        "trials": trials,
        "date": date_time,
        "difficulty": difficulty
    }
    scores.append(score)

def show_scores() -> None:
    sorted_scores = sorted(scores, key=lambda x: x["trials"])
    headers = ["Name", "Trials", "Date", "Difficulty"]
    table = [[score["name"], score["trials"], score["date"], score["difficulty"]] for score in sorted_scores]
    print(tabulate(table, headers, tablefmt="grid"))
    ui.show_menu()

