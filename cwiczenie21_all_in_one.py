# Ćwiczenie 21. Logowanie poza godzinami pracy

from datetime import datetime


log_data = """
2026-10-02 08:15 admin login
2026-10-02 12:30 anna login
2026-10-02 23:48 backup login
2026-10-02 03:15 admin login
2026-10-02 17:20 pawel login
"""


for line in log_data.strip().splitlines():

    parts = line.split()

    if len(parts) != 4:
        continue

    date_value = parts[0]
    time_value = parts[1]
    username = parts[2]

    timestamp = datetime.strptime(
        f"{date_value} {time_value}",
        "%Y-%m-%d %H:%M",
    )

    hour = timestamp.hour

    if hour < 6 or hour >= 22:

        print(
            f"ALERT: {username} "
            f"zalogował się o "
            f"{timestamp.strftime('%H:%M')}"
        )

    else:

        print(
            f"OK: {username} "
            f"-> {timestamp.strftime('%H:%M')}"
        )

