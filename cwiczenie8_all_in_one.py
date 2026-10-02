# Ćwiczenie 8. Wykrywanie brute force

from collections import Counter


log_data = """
203.0.113.42 admin failed
203.0.113.42 admin failed
203.0.113.42 admin failed
198.51.100.7 anna success
203.0.113.42 root failed
192.0.2.10 admin failed
203.0.113.42 backup failed
192.0.2.10 admin failed
203.0.113.42 admin failed
203.0.113.42 admin failed
"""


BRUTE_FORCE_THRESHOLD = 5

failed_ips = []


for line in log_data.strip().splitlines():

    parts = line.split()

    if len(parts) != 3:
        continue

    ip, username, status = parts

    if status == "failed":
        failed_ips.append(ip)


counts = Counter(failed_ips)


print("--- ANALIZA LOGOWAŃ ---")


for ip, count in counts.items():

    if count >= BRUTE_FORCE_THRESHOLD:

        print(
            f"ALERT: możliwy brute force "
            f"{ip} -> {count} prób"
        )

    else:

        print(
            f"INFO: {ip} -> {count} prób"
        )

# Zadanie: zmień próg z 5 na 3.

