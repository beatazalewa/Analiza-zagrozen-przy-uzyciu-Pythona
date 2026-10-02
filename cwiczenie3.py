import re
import ipaddress
from collections import Counter


pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

observed_ips = []


with open("ioc.log", "r", encoding="utf-8") as file:

    for line in file:

        candidates = re.findall(pattern, line)

        for candidate in candidates:

            try:
                ipaddress.ip_address(candidate)
                observed_ips.append(candidate)

            except ValueError:
                print(
                    f"Niepoprawny adres IP: {candidate}"
                )


counts = Counter(observed_ips)


print("\n--- IoC ---")

for ip, count in counts.most_common():
    print(f"{ip}: {count}")


print("\n--- Unikalne IoC ---")

unique_iocs = sorted(set(observed_ips))

for ip in unique_iocs:
    print(ip)