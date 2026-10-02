"""
Ćwiczenie 12. Threat Intelligence lookup
Zamiast threat_intel.json mamy słownik Pythona:
"""

threat_intel = {

    "203.0.113.42": {
        "type": "C2",
        "malware": "ExampleRAT",
        "severity": "high",
    },

    "198.51.100.99": {
        "type": "scanner",
        "malware": None,
        "severity": "medium",
    },
}


ip = input(
    "Podaj adres IP: "
)


if ip in threat_intel:

    info = threat_intel[ip]

    print("\nIoC znaleziony!")

    print(
        f"Typ: {info['type']}"
    )

    print(
        f"Malware: {info['malware']}"
    )

    print(
        f"Severity: {info['severity']}"
    )

else:

    print(
        "\nBrak adresu w bazie IoC"
    )

"""
Do testu wpisz np.:
203.0.113.42
"""

