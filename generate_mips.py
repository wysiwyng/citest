import random
import json

def main():
    mips = random.uniform(70, 100)

    outdict = {
        'mips': mips,
        'cputime': 22.1903,
        'simtime': 20.7443,
        'cpucycles': 7.10091e8
    }

    with open('run_results.json', 'w') as f:
        json.dump(outdict, f)

if __name__ == '__main__':
    main()
