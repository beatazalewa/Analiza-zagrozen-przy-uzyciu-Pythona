processed = 0
skipped = 0

with open("malware.log", "r", encoding="utf-8") as file:

    for line in file:

        line = line.strip()

        if not line:
            continue

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

            print(
                f"MALWARE | IP: {src} | "
                f"HASH: {file_hash}"
            )

            processed += 1

        except KeyError as error:

            print(
                f"Pominięto uszkodzony rekord. "
                f"Brak pola: {error}"
            )

            skipped += 1


print()
print(f"Poprawnie przetworzono: {processed}")
print(f"Pominięto: {skipped}")