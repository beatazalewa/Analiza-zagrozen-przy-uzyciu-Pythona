import json
import logging
import ipaddress


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    ),
)


def parse_line(line):

    fields = {}

    for token in line.split():

        if "=" not in token:
            continue

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
        "user": event.get(
            "user",
            "unknown",
        ),
        "reason": (
            "multiple failed logins"
        ),
        "count": int(
            event.get("count", 0)
        ),
    }


alerts = []

processed = 0
skipped = 0


logging.info("Analyzer started")


with open(
    "auth.log",
    "r",
    encoding="utf-8",
) as file:

    for line in file:

        line = line.strip()

        if not line:
            continue

        event = parse_line(line)

        processed += 1

        ip = event.get("src")

        if not ip:

            logging.warning(
                "Missing source IP"
            )

            skipped += 1
            continue

        if not valid_ip(ip):

            logging.warning(
                "Invalid IP: %s",
                ip,
            )

            skipped += 1
            continue

        if is_suspicious(event):

            alert = create_alert(event)

            alerts.append(alert)

            logging.warning(
                "Alert generated for %s",
                ip,
            )


with open(
    "alerts.json",
    "w",
    encoding="utf-8",
) as file:

    json.dump(
        alerts,
        file,
        indent=2,
        ensure_ascii=False,
    )


logging.info(
    "Processed records: %d",
    processed,
)

logging.info(
    "Skipped records: %d",
    skipped,
)

logging.info(
    "Generated alerts: %d",
    len(alerts),
)
