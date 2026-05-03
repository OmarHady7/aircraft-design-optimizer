from utils import calculate_drag, calculate_lift, get_cl_from_angle

best_ld = 0

velocity = 50
Cd = 0.02
required_lift = 5000
max_wing_area = 18

best_design = None

for wing_area in range(5, 21):

    if wing_area > max_wing_area:
        continue

    for angle in range(0, 16):

        Cl = get_cl_from_angle(angle)

        lift = calculate_lift(velocity, wing_area, Cl)
        drag = calculate_drag(velocity, wing_area, Cd)

        # calculate efficiency
        ld_ratio = lift / drag if drag != 0 else 0

        # apply constraints and optimization
        if lift >= required_lift:
            if ld_ratio > best_ld:
                best_ld = ld_ratio
                best_design = (wing_area, angle, lift, drag, ld_ratio)

print("Best Design Found:")
print(f"Wing Area: {best_design[0]}")
print(f"Angle of Attack: {best_design[1]}")
print(f"Lift: {best_design[2]:.2f} N")
print(f"Drag: {best_design[3]:.2f} N")
print(f"L/D Ratio: {best_design[4]:.2f}")

print("\nInterpretation:")
print("This design meets lift requirements while maximizing aerodynamic efficiency within realistic constraints.")
