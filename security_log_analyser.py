file = open("login_log.txt", "r")
logs = file.readlines()
failed_attempts = {}
for log in logs:
    if "FAILED" in log:
        parts = log.split()
        ip_address = parts[2]

        if ip_address in failed_attempts:
            failed_attempts[ip_address]=failed_attempts[ip_address] +1
        else:
            failed_attempts[ip_address] = 1

        
print("\n===== SECURITY LOG REPORT=====\n")
print("Failed login report:")
for ip_address in failed_attempts:
    print(ip_address, "had" ,failed_attempts[ip_address], "failed login attempts")
    if failed_attempts[ip_address] >= 3:
        print(ip_address, "is suspicious!")

print("\n===============================\n")
print("Analysis Complete.\n")
file.close()