# Ćwiczenie 16. Analiza severity

log_data = """
HIGH malware 203.0.113.42
MEDIUM scan 198.51.100.7
LOW failed_login 10.0.0.5
HIGH ransomware 192.0.2.10
HIGH malware 203.0.113.50
MEDIUM brute_force 192.0.2.44
"""


from collections import Counter


severity_counter = Counter()


for line in log_data.strip().splitlines():

    parts = line.split()

    if not parts:
        continue

    severity = parts[0]

    severity_counter[severity] += 1


print("--- PODSUMOWANIE ---")


for severity, count in severity_counter.items():

    print(
        f"{severity}: {count}"
    )


if severity_counter["HIGH"] > 2:

    print(
        "\nALERT: CRITICAL STATE"
    )

