import subprocess
import sys
import paho.mqtt.client as mqtt

MQTT_BROKER_HOST = "your_mqtt_broker_host"
MQTT_TOPIC = "your_mqtt_topic"

running_process = None

def on_message(client, userdata, message):
    global running_process
    try:
        setting = int(message.payload)
        if running_process:
            print("Stopping the existing stress test...")
            running_process.terminate()
            running_process.wait()
        print(f"Starting stress test with setting {setting}...")
        running_process = run_stress_with_settings(setting)
    except ValueError:
        print("Received an invalid setting from MQTT. It must be an integer (1, 2, or 3).")

def run_stress_with_settings(setting):
    if setting == 1:
        return subprocess.Popen(["stress", "--cpu", "2", "--io", "1", "--vm", "1", "--vm-bytes", "128M", "--timeout", "60s"])
    elif setting == 2:
        return subprocess.Popen(["stress", "--cpu", "4", "--io", "2", "--vm", "2", "--vm-bytes", "256M", "--timeout", "120s"])
    elif setting == 3:
        return subprocess.Popen(["stress", "--cpu", "8", "--io", "4", "--vm", "4", "--vm-bytes", "512M", "--timeout", "240s"])
    else:
        print("Invalid setting. Please choose 1, 2, or 3.")
        return None

def main():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(MQTT_BROKER_HOST)
    client.subscribe(MQTT_TOPIC)
    client.loop_forever()

if __name__ == "__main__":
    main()

