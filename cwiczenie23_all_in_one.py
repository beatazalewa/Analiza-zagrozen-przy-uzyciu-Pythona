# Ćwiczenie 23. Analiza domen

domains = [
    "example.com",
    "google.com",
    "update-system-security.xyz",
    "office.com",
    "free-money-now.top",
    "microsoft.com",
    "secure-login-account.click",
]


suspicious_tlds = [
    ".xyz",
    ".top",
    ".click",
]


for domain in domains:

    suspicious = False

    for tld in suspicious_tlds:

        if domain.lower().endswith(tld):

            suspicious = True
            break

    if suspicious:

        print(
            f"WARNING: {domain}"
        )

    else:

        print(
            f"OK: {domain}"
        )

# Tutaj koniecznie warto podkreślić: podejrzane TLD nie oznacza automatycznie złośliwej domeny.
