import typer
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = typer.Typer()


@app.command("list")
def list_acl(calendar: str):
    service = build(serviceName='calendar', version='v3')
    try:
        acl = service.acl().list(calendarId=calendar).execute()

        for rule in acl['items']:
            print(f"{rule['scope']['value']}: {rule['role']}")
    except HttpError as error:
        print(error)


@app.command("insert")
def insert_acl(calendar: str, email: str):
    service = build(serviceName='calendar', version='v3')
    try:
        service.acl().get(calendarId=calendar, ruleId=f"user:{email}").execute()
        print(f"{email} already exists as reader for calendar: {calendar}")
    except HttpError as error:
        if error.status_code == 404:
            rule = {
                'scope': {
                    'type': 'user',
                    'value': email,
                },
                'role': 'reader'
            }
            insert = service.acl().insert(calendarId=calendar, body=rule).execute()
            print(f"{insert['id']} inserted as reader on calendar: {calendar}")
            return 0
        else:
            print(error)


@app.command("delete")
def delete_acl(calendar: str, email: str):
    service = build(serviceName='calendar', version='v3')
    try:
        service.acl().delete(calendarId=calendar, ruleId=f"user:{email}").execute()
        print(f"{email} deleted from calendar: {calendar}")
    except HttpError as error:
        print(error)