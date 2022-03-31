import typer
from libs import acl
from libs import calendars

#  export GOOGLE_APPLICATION_CREDENTIALS=~/helios-prod-jms-14370ea47159.json

app = typer.Typer()
app.add_typer(acl.app, name="acl")
app.add_typer(calendars.app, name="calendars")

if __name__ == "__main__":
    app()
