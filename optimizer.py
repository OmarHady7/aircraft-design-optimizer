from utils import calculate_drag, calculate_lift, get_cl_from_angle

rho = 1.225

velocity = 50
Cd = 0.02
required_lift = 5000

best_design = None
min_drag = float("inf")

for wing_area in range(5, 21):
    for angle in range(0, 16):

        Cl = get_cl_from_angle(angle)

        lift = calculate_lift(velocity, wing_area, Cl)
        drag = calculate_drag(velocity, wing_area, Cd)

        if lift >= required_lift:
            if drag < min_drag:
                min_drag = drag
                best_design = (wing_area, angle, lift, drag)

print("Best Design Found:")
print(f"Wing Area: {best_design[0]}")
print(f"Angle of Attack: {best_design[1]}")
print(f"Lift: {best_design[2]:.2f} N")
print(f"Drag: {best_design[3]:.2f} N")
