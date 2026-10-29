import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt


def simulate_landing_roll(
    mass=60_000,          # kg
    initial_speed=70,     # m/s
    friction=0.35,        # illustrative effective coefficient
    max_brake_force=250_000,  # N
    air_density=1.225,    # kg/m^3
    drag_coefficient=0.8,
    frontal_area=100,     # m^2
    dt=0.01,              # seconds
):
    g = 9.81

    # Initial state
    t = 0.0
    x = 0.0
    v = initial_speed

    times = [t]
    distances = [x]
    speeds = [v]
    decelerations = [0.0]

    while v > 0:
        # Simplified vertical force balance:
        # lift is neglected, so normal force is approximately m*g.
        normal_force = mass * g

        # Wheel braking: limited by both brakes and tire grip.
        brake_force = min(
            max_brake_force,
            friction * normal_force
        )

        # Aerodynamic drag, opposite to the motion.
        drag_force = (
            0.5
            * air_density
            * drag_coefficient
            * frontal_area
            * v**2
        )

        # Total deceleration magnitude.
        acceleration = -(brake_force + drag_force) / mass

        # Integrate motion using a simple time step.
        old_v = v
        v = max(0.0, v + acceleration * dt)

        # Trapezoidal integration for distance.
        x += (old_v + v) * 0.5 * dt
        t += dt

        times.append(t)
        distances.append(x)
        speeds.append(v)
        decelerations.append(-acceleration)

    print(f"Stopping distance: {x:.1f} m")
    print(f"Stopping time: {t:.2f} s")

    # Plot results.
    fig, axes = plt.subplots(3, 1, figsize=(9, 9))

    axes[0].plot(times, speeds)
    axes[0].set_ylabel("Speed (m/s)")
    axes[0].grid(True)

    axes[1].plot(times, distances)
    axes[1].set_ylabel("Distance (m)")
    axes[1].grid(True)

    axes[2].plot(times, decelerations)
    axes[2].set_ylabel("Deceleration (m/s²)")
    axes[2].set_xlabel("Time (s)")
    axes[2].grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    simulate_landing_roll()