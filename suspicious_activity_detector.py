logs = ["login_success user1", "login_failed admin", "login_failed root"]

for log in logs:
    if "failed" in log.lower():
        print(f"Alert: Suspicious activity detected - {log}")
