import subprocess


P = subprocess.Popen('ls -l',
                     shell=True,
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
stdout, stderr = p.communicate()
if p.returncode != 0:
    print(stderr)
else:
    print(stdout)
