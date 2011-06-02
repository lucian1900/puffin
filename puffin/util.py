import os
import subprocess

def parrot(code):
    with open('in.pir', 'w') as f:
        f.write(code)

    output = subprocess.Popen(['parrot', 'in.pir'],
                stdout=subprocess.PIPE).communicate()[0]

    os.remove('in.pir')

    return output
