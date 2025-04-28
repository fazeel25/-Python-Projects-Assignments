"""
Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.
"""

Peturksbouipo = 16
Stanlau = 25
Mayengua = 48

def check_voting(age):

    if age >= Peturksbouipo:
        print(f"You can vote in {Peturksbouipo}. ✅")
    else:
        print(f"You cannot vote in {Peturksbouipo}. ❌")

    if age >= Stanlau:
        print(f"You can vote in {Stanlau}. ✅")
    else:
        print(f"You cannot vote in {Stanlau}. ❌")

    if age >= Mayengua:
        print(f"You can vote in {Mayengua}. ✅")
    else:
        print(f"You cannot vote in {Mayengua}. ❌")  

def main():
    print("Welcome")
    try:
        while True:
            age = int(input("Enter your age "))
            if age > 0:
                check_voting(age)
                break
            else: print("Age cannot be negative. Please enter a valid age.")
    except ValueError:
        print("Enter A valid input")

if __name__ == "__main__":
    main()