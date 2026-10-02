# Ćwiczenie 6. Threat Log Analyzer

import json
import ipaddress

from collections import Counter


log_data = """
type=AUTH src=203.0.113.42 user=admin action=login_failed count=14
type=MALWARE src=198.51.100.7 hash=44d88612fea8a8f36de82e1278abb02f action=blocked
type=AUTH src=10.0.0.5 user=anna action=login_ok count=0
type=MALWARE src=203.0.113.42 hash=e99a18c428cb38d5f260853678922e03 action=quarantine
type=AUTH src=192.0.2.44 user=root action=login_failed count=18
type=MALWARE src=999.999.999.999 hash=abc123 action=blocked
type=AUTH src=198.51.100.7 user=backup action=login_failed count=3
broken_record
"""


def parse_line(line):

    event = {}

    for token in line.split():

        if "=" in token:
            key, value = token.split("=", 1)
            event[key] = value

    return event


def valid_ip(value):

    try:
        ipaddress.ip_address(value)
        return True

    except ValueError:
        return False


def detect_alert(event):

    if event.get("type") == "MALWARE":

        return {
            "severity": "high",
            "type": "malware",
            "ip": event.get("src"),
            "reason": "malware detected",
        }

    if event.get("type") == "AUTH":

        try:
            count = int(event.get("count", 0))

        except ValueError:
            return None

        if (
            event.get("action") == "login_failed"
            and count >= 10
        ):

            return {
                "severity": "high",
                "type": "authentication",
                "ip": event.get("src"),
                "user": event.get("user"),
                "count": count,
                "reason": "multiple failed logins",
            }

    return None


alerts = []
observed_ips = []

processed = 0
skipped = 0


for line in log_data.strip().splitlines():

    event = parse_line(line)

    if not event.get("type"):

        print(
            f"WARNING: błędny rekord: {line}"
        )

        skipped += 1
        continue

    processed += 1

    ip = event.get("src")

    if ip:

        if valid_ip(ip):

            observed_ips.append(ip)

        else:

            print(
                f"WARNING: niepoprawny IP: {ip}"
            )

            skipped += 1
            continue

    alert = detect_alert(event)

    if alert:

        alerts.append(alert)

        print(
            f"ALERT: {alert['reason']} "
            f"| IP: {alert['ip']}"
        )


ioc_counts = Counter(observed_ips)


print("\n--- ALERTY ---")

print(
    json.dumps(
        alerts,
        indent=2,
        ensure_ascii=False,
    )
)


print("\n--- IoC ---")

for ip, count in ioc_counts.most_common():

    print(f"{ip}: {count}")


print("\n--- PODSUMOWANIE ---")

print(f"Przetworzono: {processed}")
print(f"Pominięto: {skipped}")
print(f"Alerty: {len(alerts)}")
print(f"Unikalne IoC: {len(ioc_counts)}")
