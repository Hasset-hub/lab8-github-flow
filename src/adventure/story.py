from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.text import Text

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[dim]You stand still, unsure what to do. The forest swallows you.[/dim]"

def left_path(event):
    return f"[green]You walk left.[/green] [italic]{event}[/italic]"

def right_path(event):
    return f"[blue]You walk right.[/blue] [italic]{event}[/italic]"

if __name__ == "__main__":
    events = read_events_from_file("events.txt")

    console.print("[bold green]You wake up in a dark forest.[/bold green]")
    console.print("[bold yellow]You can go left or right.[/bold yellow]\n")

    while True:
        choice = console.input("[bold cyan]Which direction do you choose? (left/right/exit): [/bold cyan]")
        choice = choice.strip().lower()

        if choice == "exit":
            console.print("\n[bold magenta]You have chosen to leave the forest. Goodbye, traveler![/bold magenta]\n")
            break

        # Get the story response and print it styled
        response = step(choice, events)
        console.print(response + "\n")
