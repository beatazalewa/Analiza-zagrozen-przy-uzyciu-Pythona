# Ćwiczenie 13. Analiza User-Agent

log_data = """
10.0.0.5 | Mozilla/5.0
10.0.0.10 | curl/8.0
10.0.0.11 | python-requests/2.31
10.0.0.12 | Mozilla/5.0
10.0.0.13 | sqlmap/1.7
10.0.0.14 | Nikto/2.1
"""


suspicious_agents = [
    "curl",
    "python-requests",
    "sqlmap",
    "nikto",
]


for line in log_data.strip().splitlines():

    parts = line.split(" | ")

    if len(parts) != 2:
        continue

    ip = parts[0]
    user_agent = parts[1]

    ua_lower = user_agent.lower()

    detected = False

    for suspicious in suspicious_agents:

        if suspicious in ua_lower:

            print(
                f"WARNING: {ip} -> "
                f"{user_agent}"
            )

            detected = True
            break

    if not detected:

        print(
            f"OK: {ip} -> {user_agent}"
        )

# Czy curl automatycznie oznacza atak? Oczywiście nie — to sygnał do dalszej analizy.

