# ĆwĆwiczenie 20. Risk scoring

failed_logins = 12
known_ioc = True
suspicious_user_agent = True
malware_detected = False


score = 0


if failed_logins >= 10:

    score += 20

    print(
        "+20: wiele nieudanych logowań"
    )


if known_ioc:

    score += 50

    print(
        "+50: znany IoC"
    )


if suspicious_user_agent:

    score += 10

    print(
        "+10: podejrzany User-Agent"
    )


if malware_detected:

    score += 80

    print(
        "+80: wykryto malware"
    )


print(
    f"\nRisk score: {score}"
)


if score >= 80:

    severity = "CRITICAL"

elif score >= 50:

    severity = "HIGH"

elif score >= 20:

    severity = "MEDIUM"

else:

    severity = "LOW"


print(
    f"Severity: {severity}"
)

"""
Zadanie: ustaw:
malware_detected = True
i sprawdź wynik.
"""
