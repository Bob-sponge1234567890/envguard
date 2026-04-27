import typer

app = typer.Typer(no_args_is_help=True)

from rich.console import Console

console = Console ()
@app.command()
def scan(path: str = typer.Argument(".")):
    console.print(f"[green]Scan de : {path}[/green]")

@app.command()
def report():
    console.print("[blue]Rapport en cours...[/blue]")

if __name__ == "__main__": app()
