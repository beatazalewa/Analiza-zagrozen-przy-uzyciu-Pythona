"""# Ćwiczenie 10. Wykrywanie skanowania portów"""

from collections import defaultdict


log_data = """
203.0.113.42 10.0.0.10 22
203.0.113.42 10.0.0.10 80
203.0.113.42 10.0.0.10 443
203.0.113.42 10.0.0.10 3389
203.0.113.42 10.0.0.10 445
198.51.100.7 10.0.0.5 443
203.0.113.42 10.0.0.10 21
203.0.113.42 10.0.0.10 23
"""


ports_by_ip = defaultdict(set)


for line in log_data.strip().splitlines():

    parts = line.split()

    if len(parts) != 3:
        continue

    source_ip = parts[0]
    destination_ip = parts[1]
    port = int(parts[2])

    ports_by_ip[source_ip].add(port)


for ip, ports in ports_by_ip.items():

    if len(ports) >= 5:

        print(
            "\nALERT: możliwe skanowanie portów"
        )

        print(f"Źródło: {ip}")

        print(
            f"Liczba portów: {len(ports)}"
        )

        print(
            f"Porty: {sorted(ports)}"
        )


