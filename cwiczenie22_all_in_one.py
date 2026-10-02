# Ćwiczenie 22. Administrator z nowego IP

known_admin_ips = {
    "10.0.0.10",
    "10.0.0.11",
}


login_events = [
    ("admin", "10.0.0.10"),
    ("anna", "203.0.113.5"),
    ("admin", "203.0.113.42"),
    ("admin", "10.0.0.11"),
]


for username, login_ip in login_events:

    if (
        username == "admin"
        and login_ip not in known_admin_ips
    ):

        print(
            f"ALERT: administrator "
            f"z nowego IP: {login_ip}"
        )

    else:

        print(
            f"OK: {username} -> {login_ip}"
        )

