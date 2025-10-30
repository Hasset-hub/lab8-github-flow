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
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("[bold cyan]You wake up in a dark forest. You can go left or right.[/bold cyan]")

    while True:
        choice = console.input("[bold green]Which direction do you choose? (left/right/exit): [/bold green]")
        choice = choice.strip().lower()

        if choice == 'exit':
            console.print("[bold red]You decide to leave the forest. Goodbye adventurer![/bold red]")
            break
        
        result = step(choice, events)
        console.print(f"[yellow]{result}[/yellow]")
