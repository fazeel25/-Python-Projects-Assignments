"""
Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

E = m * c**2

Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

"""
C: int = 299792458 

def main():
    mass_in_kg: float = float(int(input("Enter Kils of mass: ")))

    energy_in_joules:float = mass_in_kg * (C ** 2)
    print(f"mass = {str(mass_in_kg)}kg")
    print(f"C = {str(C)}m/s")

    print(f"{str(energy_in_joules)} joules of energy!")

if __name__ == '__main__':
    main()

