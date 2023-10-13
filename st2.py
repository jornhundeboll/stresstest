import subprocess
import sys

def run_stress_with_settings(setting):
    if setting == 1:
        subprocess.run(["stress", "--cpu", "2", "--io", "1", "--vm", "1", "--vm-bytes", "128M", "--timeout", "60s"])
    elif setting == 2:
        subprocess.run(["stress", "--cpu", "4", "--io", "2", "--vm", "2", "--vm-bytes", "256M", "--timeout", "120s"])
    elif setting == 3:
        subprocess.run(["stress", "--cpu", "8", "--io", "4", "--vm", "4", "--vm-bytes", "512M", "--timeout", "240s"])
    else:
        print("Invalid setting. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 program.py <setting>")
    else:
        try:
            setting = int(sys.argv[1])
            run_stress_with_settings(setting)
        except ValueError:
            print("Setting must be an integer (1, 2, or 3).")

