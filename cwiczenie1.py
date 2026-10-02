print("***** Failed logins *****")
print()
failed_logins = [2, 5, 12, 3, 18, 7, 10, 1]

alert_count = 0

for value in failed_logins:

    if value >= 10:
        print(f"ALERT: {value} nieudanych logowań")
        alert_count += 1

    elif value >= 5:
        print(f"WARNING: {value} nieudanych logowań")

    else:
        print(f"OK: {value} nieudanych logowań")

print()
print(f"Liczba alertów: {alert_count}"
)
print()
print("***** Accounts *****")
print()
accounts = {
    "admin": 12,
    "anna": 3,
    "backup": 18,
    "pawel": 7,
    "service": 11,
}

for username, failed_logins in accounts.items():

    if failed_logins >= 10:
        print(f"ALERT: {username} -> {failed_logins}")

    elif failed_logins >= 5:
        print(f"WARNING: {username} -> {failed_logins}")

    else:
        print(f"OK: {username} -> {failed_logins}")