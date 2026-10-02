"""
Ćwiczenie 25. Raport dzienny SOC
W wersji online zamiast zapisywania daily_report.txt wyświetlamy gotowy raport.
"""

report = {
    "processed_events": 1250,
    "alerts": 23,
    "high": 5,
    "medium": 11,
    "low": 7,
    "unique_iocs": 14,
}


print(
    "=== SOC DAILY REPORT ==="
)

print(
    f"Zdarzenia: "
    f"{report['processed_events']}"
)

print(
    f"Alerty: "
    f"{report['alerts']}"
)

print(
    f"HIGH: "
    f"{report['high']}"
)

print(
    f"MEDIUM: "
    f"{report['medium']}"
)

print(
    f"LOW: "
    f"{report['low']}"
)

print(
    f"IOC: "
    f"{report['unique_iocs']}"
)


if report["high"] >= 5:

    print(
        "\nUWAGA: podwyższona liczba "
        "alertów HIGH"
    )


