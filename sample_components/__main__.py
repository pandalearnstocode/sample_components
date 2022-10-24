import typer

from sample_components.example import hello as _hello

# README: https://github.com/tiangolo/typer/issues/233

app = typer.Typer()


@app.command()
def run_hello(name: str) -> str:
    typer.echo(f"Hello {name}")
    return _hello(name)


@app.command()
def run_bye(name: str) -> str:
    typer.echo(f"Hello {name}")
    return _hello(name)


if __name__ == "__main__":
    app()
