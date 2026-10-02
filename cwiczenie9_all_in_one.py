# Ćwiczenie 9. Password spraying

from collections import defaultdict


log_data = """
203.0.113.50 anna failed
203.0.113.50 pawel failed
203.0.113.50 admin failed
203.0.113.50 backup failed
203.0.113.50 service failed
198.51.100.10 anna failed
198.51.100.10 pawel success
"""


accounts_by_ip = defaultdict(set)


for line in log_data.strip().splitlines():

    parts = line.split()

    if len(parts) != 3:
        continue

    ip, username, status = parts

    if status == "failed":

        accounts_by_ip[ip].add(username)


for ip, accounts in accounts_by_ip.items():

    if len(accounts) >= 4:

        print(
            "\nALERT: możliwy password spraying"
        )

        print(f"IP: {ip}")

        print(
            f"Liczba kont: {len(accounts)}"
        )

        print(
            f"Konta: {sorted(accounts)}"
        )

# Zadanie: zmień próg z 4 kont na 3.

