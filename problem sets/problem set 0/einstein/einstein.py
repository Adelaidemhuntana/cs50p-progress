def energy(mass):
  c = 300000000                 # c  stands for the speed of the light
  return mass * c**2            # it must return mass x c to the power of 2

def main():
  m = int(input("m: "))          # m is the mass
  E = energy(m)                # E stands for energy on the formula
  print(E)

main()