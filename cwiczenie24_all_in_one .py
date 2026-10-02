# Ćwiczenie 24. Długie subdomeny

domains = [
    "www.example.com",
    "api.company.pl",
    (
        "a8d7f6a8d7f6a8d7f6a8d7f6"
        ".example.com"
    ),
    (
        "dGVzdC1kYXRhLWV4ZmlsdHJhdGlvbg"
        ".example.net"
    ),
]


MAX_LENGTH = 20


for domain in domains:

    first_part = domain.split(".")[0]

    length = len(first_part)

    if length > MAX_LENGTH:

        print(
            f"WARNING: {domain}"
        )

        print(
            f"Długość subdomeny: {length}"
        )

    else:

        print(
            f"OK: {domain}"
        )

# Może to być DNS tunneling, ale sama długa subdomena nie dowodzi tunelowania.

