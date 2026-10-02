# Ćwiczenie 19. Deduplikacja alertów

alerts = [
    "203.0.113.42 malware",
    "203.0.113.42 malware",
    "198.51.100.7 scan",
    "203.0.113.42 malware",
    "192.0.2.10 brute_force",
    "198.51.100.7 scan",
]


unique_alerts = set()


for alert in alerts:

    if alert not in unique_alerts:

        print(
            f"NOWY ALERT: {alert}"
        )

        unique_alerts.add(alert)

    else:

        print(
            f"DUPLIKAT: {alert}"
        )


print(
    f"\nWszystkie zdarzenia: "
    f"{len(alerts)}"
)

print(
    f"Unikalne alerty: "
    f"{len(unique_alerts)}"
)


