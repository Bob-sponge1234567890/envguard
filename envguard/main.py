import typer
from rich.console import Console
from envguard.scanner.file_walker import walk_files

app = typer.Typer(no_args_is_help=True)

console = Console ()
@app.command()
def scan(path: str = typer.Argument(".")):
    walk_files(path)

@app.command()
def report():
    console.print("[blue]Rapport en cours...[/blue]")

if __name__ == "__main__": app()
