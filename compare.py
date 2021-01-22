import json
import sys

TOLERANCE = 0.7

f1_name = sys.argv[1]
f2_name = sys.argv[2]

with open(f1_name, 'r') as f1, open(f2_name, 'r') as f2:
    f1_dict = json.load(f1)
    f2_dict = json.load(f2)

f1_mips = f1_dict['mips']
f2_mips = f2_dict['mips']

lower_bound = f1_mips * TOLERANCE
upper_bound = f1_mips * (2 - TOLERANCE)

print(f'f1 mips: {f1_mips}')
print(f'f2 mips: {f2_mips}')

if f2_mips < lower_bound:
    sys.exit(2)
elif f2_mips > upper_bound:
    sys.exit(1)
else:
    sys.exit(0)