# Ćwiczenie 7. Podejrzane rozszerzenia plików

files = [
    "invoice.pdf",
    "report.docx",
    "update.exe",
    "photo.jpg",
    "payload.scr",
    "backup.zip",
    "malware.bat",
    "notes.txt",
]

dangerous_extensions = [
    ".exe",
    ".scr",
    ".bat",
    ".cmd",
    ".ps1",
]

detected = 0


for filename in files:

    suspicious = False

    for extension in dangerous_extensions:

        if filename.lower().endswith(extension):

            suspicious = True
            break

    if suspicious:

        print(f"ALERT: {filename}")
        detected += 1

    else:

        print(f"OK: {filename}")


print(
    f"\nPodejrzane pliki: {detected}"
)

# Zadanie: dodaj .vbs, .js i .dll.