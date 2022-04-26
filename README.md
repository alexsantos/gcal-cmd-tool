# gcal-cmd-tool
A command line tool to manage Google Calendars

## Installation
This tool is available on PyPi. To install simply run
```bash
$ pip install gcal-cmd-tool 
```

## Authentication
Authentication to Google Calendar API is done using a service account. Instructions can be read on Google's [Authenticating as a service account ](https://cloud.google.com/docs/authentication/production).

To set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` on Linux run the following command:
```bash
$ export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```
Replace KEY_PATH with the path of the JSON file that contains your service account key.

For example:
```bash
$ export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"
```

## Resource types

### Acl
```CALENDAR``` - the Calendar ID

```EMAIL``` - the email of the user
#### list
Returns the rules in the access control list for the calendar.
```bash
$ gcal-cmd-tool acl list [OPTIONS] CALENDAR
```
#### insert
Creates an access control rule.
```bash
$ gcal-cmd-tool acl insert [OPTIONS] CALENDAR EMAIL
```
#### delete
Deletes an access control rule. 
```bash
$ gcal-cmd-tool acl delete [OPTIONS] CALENDAR EMAIL
```

### Calendars
#### get
Returns metadata for a calendar. 
```bash
$ gcal-cmd-tool calendar get [OPTIONS] CALENDAR
```

#### delete
Deletes a secondary calendar.
```bash
$ gcal-cmd-tool calendars delete [OPTIONS] CALENDAR
```