import subprocess

# Configure your Perforce details
P4PORT = "105.112.xxx.xx:xxxx"  # Replace with your server address
P4USER = "your_username"        # Replace with your username
P4PASSWD = "your_password"      # Replace with your password (optional)

def p4_login():
    try:
        # Set the P4 environment variables
        subprocess.run(["p4", "set", f"P4PORT={P4PORT}"], check=True)
        subprocess.run(["p4", "set", f"P4USER={P4USER}"], check=True)

        # Login using the password
        login_process = subprocess.run(["p4", "login"], input=P4PASSWD.encode(), capture_output=True, text=True)

        # Check login result
        if "Login succeeded" in login_process.stdout:
            print("[✅] Login successful!")
        else:
            print("[❌] Login failed!")
            print(login_process.stdout, login_process.stderr)

    except subprocess.CalledProcessError as e:
        print("[❌] Error executing Perforce commands:", e)

if __name__ == "__main__":
    p4_login()
