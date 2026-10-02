# Ćwiczenie 15. Analiza hashy

known_hashes = {
    "44d88612fea8a8f36de82e1278abb02f",
    "e99a18c428cb38d5f260853678922e03",
    "5d41402abc4b2a76b9719d911017c592",
}


files = [
    (
        "invoice.pdf",
        "abc123",
    ),
    (
        "payload.exe",
        "44d88612fea8a8f36de82e1278abb02f",
    ),
    (
        "photo.jpg",
        "def456",
    ),
    (
        "update.exe",
        "e99a18c428cb38d5f260853678922e03",
    ),
]


for filename, file_hash in files:

    if file_hash in known_hashes:

        print(
            f"ALERT: {filename}"
        )

        print(
            f"Znany hash malware: {file_hash}"
        )

    else:

        print(
            f"OK: {filename}"
        )


