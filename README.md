# gcal-cmd-tool
A command line tool to manage Google Calendars

## Authentication
Authentication to Google Calendar API is done using a service account. Instructions can be read on Google's [Authenticating as a service account ](https://cloud.google.com/docs/authentication/production).

To set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` on Linux run the following command:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```
Replace KEY_PATH with the path of the JSON file that contains your service account key.

For example:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"
```

## Resource types

### Acl
#### list
Returns the rules in the access control list for the calendar.
```bash
$ python3 gcal-cmd-tool.py acl list [OPTIONS] CALENDAR
```
#### insert
Creates an access control rule.
#### delete
Deletes an access control rule. 

### Calendars
#### get
Returns metadata for a calendar. 
#### delete
Deletes a secondary calendar.