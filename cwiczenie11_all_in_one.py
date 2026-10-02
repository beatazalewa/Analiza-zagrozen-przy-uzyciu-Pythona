"""
Ćwiczenie 11. Komunikacja ze znanym IoC
Zamiast bad_ips.txt i connections.log mamy dwie zmienne.
"""

bad_ips = {
    "203.0.113.42",
    "198.51.100.99",
    "192.0.2.77",
}


log_data = """
10.0.0.5 -> 8.8.8.8
10.0.0.10 -> 203.0.113.42
10.0.0.15 -> 1.1.1.1
10.0.0.20 -> 198.51.100.99
"""


for line in log_data.strip().splitlines():

    parts = line.split(" -> ")

    if len(parts) != 2:
        continue

    source = parts[0]
    destination = parts[1]

    if destination in bad_ips:

        print(
            f"ALERT: {source} "
            f"połączył się z IOC "
            f"{destination}"
        )

    else:

        print(
            f"OK: {source} -> {destination}"
        )


