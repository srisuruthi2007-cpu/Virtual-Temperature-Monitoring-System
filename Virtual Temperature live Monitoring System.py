import random
import time
import matplotlib.pyplot as plt

temps = []

plt.ion()  # Turn ON live plotting

print("🌡️ Live Temperature Monitoring Started...\n")

for i in range(50):  # number of updates
    temp = random.randint(20, 45)
    temps.append(temp)

    print(f"Reading {i+1}: {temp} °C")

    # Clear previous graph
    plt.clf()

    # Plot updated data
    plt.plot(temps, marker='o')
    plt.title("Live Temperature Monitoring")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.grid()

    # Pause to update graph
    plt.pause(0.5)

    time.sleep(0.5)

plt.ioff()  # Turn OFF live plotting
plt.show()

print("\n✅ Monitoring Completed")