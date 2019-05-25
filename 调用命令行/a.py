import subprocess
from subprocess import Popen, PIPE, STDOUT

if __name__ == '__main__':
    for i in range(1,4):
        cmd = "python b.py " + str(i)
        with Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT) as res:
            out = res.stdout.read()
            out = bytes.decode(out,encoding = "utf-8")
            print(out)
