# Ćwiczenie 17. Ranking najbardziej aktywnych IP

from collections import Counter


log_data = """
203.0.113.42 10.0.0.10 22
203.0.113.42 10.0.0.10 80
198.51.100.7 10.0.0.5 443
203.0.113.42 10.0.0.20 443
192.0.2.44 10.0.0.5 22
198.51.100.7 10.0.0.10 3389
203.0.113.42 10.0.0.30 445
192.0.2.44 10.0.0.8 80
203.0.113.42 10.0.0.40 21
"""


ips = []


for line in log_data.strip().splitlines():

    parts = line.split()

    if len(parts) != 3:
        continue

    ips.append(parts[0])


counter = Counter(ips)


print("--- TOP ŹRÓDŁA ---")


for ip, count in counter.most_common(5):

    print(
        f"{ip}: {count} zdarzeń"
    )


