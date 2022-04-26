import typer
from .libs import acl
from .libs import calendars

app = typer.Typer()
app.add_typer(acl.app, name="acl")
app.add_typer(calendars.app, name="calendars")
