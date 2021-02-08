import pathlib
import random
import shutil
import string
import sys
import json

import compare
import generate_mips


def make_hash(l=6, c=string.ascii_lowercase + string.digits):
    return ''.join(random.choices(c, k=l))

shutil.move('new/run_results.json', 'old/run_results.json')

with open('run_results.json', 'w') as f:
    json.dump({'mips': int(sys.argv[1])}, f)

shutil.move('run_results.json', 'new')
compare.main('new/run_results.json', 'old/run_results.json', make_hash(), 0.1, False)
