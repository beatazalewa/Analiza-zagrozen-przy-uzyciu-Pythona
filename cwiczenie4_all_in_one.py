"""
Ćwiczenie 4. Mini-pipeline bezpieczeństwa
Cel: parsowanie logów, walidacja IP, wykrywanie podejrzanych logowań, funkcje i generowanie alertów.
"""

import json
import ipaddress


# Dane wejściowe
log_data = """
src=203.0.113.42 user=admin action=login_failed count=12
src=10.0.0.5 user=anna action=login_ok count=0
src=198.51.100.7 user=root action=login_failed count=4
src=192.0.2.44 user=backup action=login_failed count=18
src=999.999.999.999 user=test action=login_failed count=20
src=203.0.113.15 user=service action=login_failed count=11
broken_line
"""


def parse_line(line):
    fields = {}

    for token in line.split():
        if "=" in token:
            key, value = token.split("=", 1)
            fields[key] = value

    return fields


def valid_ip(value):
    try:
        ipaddress.ip_address(value)
        return True

    except ValueError:
        return False


def is_suspicious(event):
    try:
        return (
            event.get("action") == "login_failed"
            and int(event.get("count", 0)) >= 10
        )

    except ValueError:
        return False


def create_alert(event):
    return {
        "severity": "high",
        "ip": event["src"],
        "user": event.get("user", "unknown"),
        "reason": "multiple failed logins",
        "count": int(event.get("count", 0)),
    }


alerts = []
processed = 0
skipped = 0


for line in log_data.strip().splitlines():

    event = parse_line(line)

    processed += 1

    ip = event.get("src")

    if not ip:
        print("WARNING: brak adresu IP")
        skipped += 1
        continue

    if not valid_ip(ip):
        print(f"WARNING: niepoprawny IP: {ip}")
        skipped += 1
        continue

    if is_suspicious(event):

        alert = create_alert(event)

        alerts.append(alert)

        print(
            f"ALERT: {ip} | "
            f"user={event.get('user')} | "
            f"count={event.get('count')}"
        )


print("\n--- PODSUMOWANIE ---")
print(f"Przetworzono: {processed}")
print(f"Pominięto: {skipped}")
print(f"Alerty: {len(alerts)}")


print("\n--- ALERTY JSON ---")

print(
    json.dumps(
        alerts,
        indent=2,
        ensure_ascii=False,
    )
)

# Zadanie: zmień próg z 10 na 5 i sprawdź, jak zmieni się liczba alertów.