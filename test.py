import random
import json

mips = random.randrange(10, 100)

outdict = {
    'mips': mips,
    'cputime': 22.1903,
    'simtime': 20.7443,
    'cpucycles': 7.10091e8
}

with open('run_results.json', 'w') as f:
    json.dump(outdict, f)
