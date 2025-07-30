import urequests
import time
import network

# Wi-Fi credentials
ssid = '...'
password = '...'

# Connect to Wi-Fi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    time.sleep(1)
    print("Connecting to WiFi...")

print("Connected to WiFi:", station.ifconfig())

# Google Form details
form_url = "..."
field_name = "..."

# Replace this with dynamic sensor reading
value_to_send = "object detected"

# Loop to send data every 10 seconds
while True:
    payload = field_name + "=" + value_to_send
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        response = urequests.post(form_url, data=payload, headers=headers)
        print("Form submitted:", response.status_code)
        response.close()
    except Exception as e:
        print("Failed to submit:", e)

    time.sleep(3)

