"""
Ćwiczenie 5. Symulacja ciągłego monitorowania
W środowisku online lepiej nie używać nieskończonej:
while True:


Zamiast tego zasymulujemy kolejne cykle monitorowania.
"""

import time


log_batches = [
    """
    src=10.0.0.5 action=login_ok count=0
    src=203.0.113.42 action=login_failed count=3
    """,

    """
    src=203.0.113.42 action=login_failed count=7
    src=198.51.100.7 action=login_failed count=2
    """,

    """
    src=203.0.113.42 action=login_failed count=12
    src=192.0.2.44 action=login_failed count=15
    """,
]


for cycle, log_data in enumerate(log_batches, start=1):

    print(f"\n=== CYKL {cycle} ===")

    for line in log_data.strip().splitlines():

        fields = {}

        for token in line.split():

            if "=" in token:
                key, value = token.split("=", 1)
                fields[key] = value

        count = int(fields.get("count", 0))

        if (
            fields.get("action") == "login_failed"
            and count >= 10
        ):

            print(
                f"ALERT: {fields.get('src')} "
                f"-> {count} nieudanych logowań"
            )

        else:

            print(
                f"INFO: {fields.get('src')} "
                f"-> brak alertu"
            )

    time.sleep(1)


print("\nMonitoring zakończony.")

# Zadanie: zmień time.sleep(1) na time.sleep(3) i obserwuj kolejne cykle.