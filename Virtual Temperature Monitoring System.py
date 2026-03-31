import random
import time
import matplotlib.pyplot as plt

# Try importing notification safely
try:
    from plyer import notification
    notify_available = True
except:
    notify_available = False
    print("⚠️ Notification not working, continuing without popup...")

# -----------------------------
# SETTINGS
# -----------------------------
THRESHOLD = 35
READINGS = 20

temps = []

print("🌡️ IoT Temperature Monitoring Started...\n")

# -----------------------------
# MONITORING LOOP
# -----------------------------
for i in range(READINGS):
    temperature = random.randint(20, 45)
    temps.append(temperature)

    print(f"Reading {i+1}: {temperature} °C")

    if temperature > THRESHOLD:
        print("⚠️ High Temperature Alert!")

        # Only run if plyer works
        if notify_available:
            try:
                notification.notify(
                    title="Temperature Alert",
                    message=f"High Temp: {temperature} °C",
                    timeout=5
                )
            except:
                print("⚠️ Notification failed")

    time.sleep(1)

# -----------------------------
# GRAPH OUTPUT
# -----------------------------
plt.figure()
plt.plot(temps)
plt.title("Temperature Monitoring")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.grid()

plt.show()

print("\n✅ Monitoring Completed")
print("⚠️ High Temperature Alert!")