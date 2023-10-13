import subprocess

def run_stress_with_settings(setting):
    if setting == 1:
        # Run 'stress' with setting 1
        subprocess.run(["stress", "--cpu", "2", "--io", "1", "--vm", "1", "--vm-bytes", "128M", "--timeout", "60s"])
    elif setting == 2:
        # Run 'stress' with setting 2
        subprocess.run(["stress", "--cpu", "4", "--io", "2", "--vm", "2", "--vm-bytes", "256M", "--timeout", "120s"])
    elif setting == 3:
        # Run 'stress' with setting 3
        subprocess.run(["stress", "--cpu", "8", "--io", "4", "--vm", "4", "--vm-bytes", "512M", "--timeout", "240s"])
    else:
        print("Invalid setting. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    setting = int(input("Enter a setting (1, 2, or 3): "))
    run_stress_with_settings(setting)

