"""
Ćwiczenie 26. Mini SOC Analyzer — jednoplikowy projekt końcowy
Tutaj połączymy kilka wcześniejszych ćwiczeń.
"""

import ipaddress

from collections import Counter


log_data = """
203.0.113.42 admin login_failed 12
10.0.0.5 anna login_ok 0
198.51.100.7 root login_failed 3
192.0.2.44 backup login_failed 18
203.0.113.42 admin login_failed 15
999.999.999.999 test login_failed 20
198.51.100.99 service login_failed 11
"""


known_iocs = {
    "203.0.113.42",
    "198.51.100.99",
}


def valid_ip(ip):

    try:
        ipaddress.ip_address(ip)
        return True

    except ValueError:
        return False


def calculate_risk(
    failed_count,
    known_ioc,
):

    score = 0

    if failed_count >= 10:
        score += 30

    if failed_count >= 15:
        score += 20

    if known_ioc:
        score += 50

    return score


def get_severity(score):

    if score >= 80:
        return "CRITICAL"

    elif score >= 50:
        return "HIGH"

    elif score >= 30:
        return "MEDIUM"

    else:
        return "LOW"


alerts = []

ip_counter = Counter()


for line in log_data.strip().splitlines():

    parts = line.split()

    if len(parts) != 4:
        continue

    ip = parts[0]
    username = parts[1]
    action = parts[2]

    try:
        count = int(parts[3])

    except ValueError:
        continue

    if not valid_ip(ip):

        print(
            f"WARNING: niepoprawny IP: {ip}"
        )

        continue

    ip_counter[ip] += 1

    is_ioc = ip in known_iocs

    score = calculate_risk(
        count,
        is_ioc,
    )

    severity = get_severity(score)

    if (
        action == "login_failed"
        and score >= 30
    ):

        alert = {
            "ip": ip,
            "user": username,
            "count": count,
            "ioc": is_ioc,
            "score": score,
            "severity": severity,
        }

        alerts.append(alert)


print("\n=== ALERTY SOC ===")


for alert in alerts:

    print(
        f"\n[{alert['severity']}] "
        f"{alert['ip']}"
    )

    print(
        f"User: {alert['user']}"
    )

    print(
        f"Failed logins: {alert['count']}"
    )

    print(
        f"Known IOC: {alert['ioc']}"
    )

    print(
        f"Risk score: {alert['score']}"
    )


print(
    "\n=== NAJAKTYWNIEJSZE IP ==="
)


for ip, count in ip_counter.most_common():

    print(
        f"{ip}: {count}"
    )


print(
    "\n=== PODSUMOWANIE ==="
)

print(
    f"Liczba alertów: {len(alerts)}"
)

"""
Zadanie dla uczestniczek
Po uruchomieniu gotowej wersji należy kolejno:
1. zmienić próg login_failed,
2. dodać nowy IOC do known_iocs,
3. zmienić punktację,
4. dodać nowy poziom severity,
5. dodać kolejne zdarzenia do log_data,
6. spróboować wywołać błąd niepoprawnym IP,
7. dodać informację o tym, dlaczego alert dostał określoną liczbę punktów.
"""


