"""
Ćwiczenie 18. Korelacja IDS + firewall
Dwa źródła danych nadal są w jednym programie:
"""

ids_data = """
203.0.113.42 scan
198.51.100.7 malware
192.0.2.10 exploit
"""


firewall_data = """
203.0.113.42 blocked
8.8.8.8 allowed
198.51.100.7 allowed
"""


ids_ips = set()
firewall_allowed = set()


for line in ids_data.strip().splitlines():

    parts = line.split()

    if len(parts) == 2:

        ids_ips.add(
            parts[0]
        )


for line in firewall_data.strip().splitlines():

    parts = line.split()

    if len(parts) != 2:
        continue

    ip, action = parts

    if action == "allowed":

        firewall_allowed.add(ip)


dangerous = (
    ids_ips
    & firewall_allowed
)


print(
    "--- KORELACJA IDS + FIREWALL ---"
)


for ip in dangerous:

    print(
        f"ALERT: {ip} został "
        f"wykryty przez IDS, "
        f"ale firewall go przepuścił"
    )


# To jest świetne ćwiczenie do pokazania bardzo uproszczonej korelacji SIEM..

