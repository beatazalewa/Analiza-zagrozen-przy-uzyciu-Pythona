import re
import ipaddress
from collections import Counter

# Przykładowe logi zapisane bezpośrednio w programie
log_data = """
Connection from 203.0.113.42 detected
Malware communication with 198.51.100.7
Connection from 203.0.113.42 blocked
Invalid address 999.999.999.999 detected
Source 192.0.2.44 generated alert
203.0.113.42 attempted login
Scanner connected from 198.51.100.7
Invalid source 300.1.1.1
Connection from 10.0.0.15
"""


# Wzorzec wyszukujący kandydatów na adres IPv4
pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"


# Lista poprawnych adresów IP
observed_ips = []


# Analiza logów linia po linii
for line in log_data.strip().splitlines():

    candidates = re.findall(pattern, line)

    for candidate in candidates:

        try:
            ipaddress.ip_address(candidate)

            observed_ips.append(candidate)

        except ValueError:
            print(
                f"Niepoprawny adres IP: {candidate}"
            )


# Liczenie wystąpień adresów
counts = Counter(observed_ips)


print("\n--- IoC ---")

for ip, count in counts.most_common():

    print(f"{ip}: {count}")


# Usuwanie duplikatów
unique_iocs = sorted(set(observed_ips))


print("\n--- Unikalne IoC ---")

for ip in unique_iocs:

    print(ip)

"""
Instrukcja dla uczestnika
Uruchom program. Powinien najpierw wykryć dwa niepoprawne adresy:
Niepoprawny adres IP: 999.999.999.999
Niepoprawny adres IP: 300.1.1.1

Następnie powinien policzyć poprawne adresy:
--- IoC ---
203.0.113.42: 3
198.51.100.7: 2
192.0.2.44: 1
10.0.0.15: 1

Na końcu otrzymasz listę unikalnych adresów:
--- Unikalne IoC ---
10.0.0.15
192.0.2.44
198.51.100.7
203.0.113.42

Co właściwie robi program?
Najpierw:
re.findall(pattern, line)


wyszukuje w tekście ciągi wyglądające jak adres IPv4.
Problem polega na tym, że regex znajdzie również:
999.999.999.999

bo składniowo wygląda on jak adres IP.
Dlatego wykonujemy drugi etap:
ipaddress.ip_address(candidate)


który sprawdza, czy znaleziony adres jest rzeczywiście poprawny.
Mechanizm wygląda więc tak:
LOG
 ↓
REGEX
 ↓
kandydat na adres IP
 ↓
ipaddress.ip_address()
 ↓
poprawny IP
 ↓
Counter
 ↓
liczba wystąpień
 ↓
set()
 ↓
unikalne IoC

Zadanie dodatkowe dla uczestników
Dodaj do log_data kolejne wpisy, np.:
Attack from 192.0.2.44 detected
Connection to 203.0.113.99 blocked
Invalid source 400.500.600.700
Malware contacted 203.0.113.99

Następnie uruchom program ponownie i sprawdź:
- czy nowy adres został wykryty,
- ile razy występuje,
- czy błędny adres został odrzucony,
- czy lista unikalnych IoC zawiera duplikaty.
"""