import typer
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = typer.Typer()


@app.command("get", help="Returns metadata for a calendar.")
def get_calendar(calendar_id: str = typer.Argument("primary", metavar="calendarId")):
    service = build(serviceName='calendar', version='v3')
    try:
        result = service.calendars().get(calendarId=calendar_id).execute()
        print(result)
    except HttpError as error:
        print(error)


@app.command("delete", help="Deletes a secondary calendar.")
def delete_calendar(calendar_id: str = typer.Argument(..., metavar="calendarId")):
    service = build(serviceName='calendar', version='v3')
    try:
        result = service.calendars().delete(calendarId=calendar_id).execute()
        print(result)
    except HttpError as error:
        print(error)