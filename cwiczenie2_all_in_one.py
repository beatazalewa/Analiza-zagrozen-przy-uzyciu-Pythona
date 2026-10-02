log_data = """
type=MALWARE src=203.0.113.42 hash=44d88612fea8a8f36de82e1278abb02f action=blocked
type=CLEAN src=10.0.0.15 hash=abc123 action=allowed
type=MALWARE src=198.51.100.7 hash=e99a18c428cb38d5f260853678922e03 action=quarantine
type=ERROR message=scan_failed
type=MALWARE src=192.0.2.44 hash=5d41402abc4b2a76b9719d911017c592 action=blocked
type=MALWARE src=203.0.113.15 action=blocked
"""

processed = 0
skipped = 0

for line in log_data.strip().splitlines():

    line = line.strip()

    try:
        fields = {}

        for token in line.split():

            if "=" in token:
                key, value = token.split("=", 1)
                fields[key] = value

        if fields.get("type") != "MALWARE":
            continue

        src = fields["src"]
        file_hash = fields["hash"]

        print(f"MALWARE | IP: {src} | HASH: {file_hash}")

        processed += 1

    except KeyError as error:

        print(f"Pominięto rekord. Brak pola: {error}")
        skipped += 1

print()
print(f"Poprawnie przetworzono: {processed}")
print(f"Pominięto: {skipped}")