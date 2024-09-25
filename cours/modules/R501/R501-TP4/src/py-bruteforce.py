
#### Should generate a dictionary of
#### - 8 digits (only `chiffres`)
#### - No double allowed

_dict = []

x = 0

for a in range(0, 10):
  for b in range(0, 10):
    for c in range(0, 10):
      for d in range(0, 10):
        for e in range(0, 10):
          for f in range(0, 10):
            for g in range(0, 10):
              for h in range(0, 10):
                x+=1

                print("Recursion n°{x}")
                
                _dict.append(f"{a}{b}{c}{d}{e}{f}{g}{h}")

print("Recursion done")

with open("brutedict.txt", "wt", encoding="utf-8") as fout:
  fout.writelines(_dict)