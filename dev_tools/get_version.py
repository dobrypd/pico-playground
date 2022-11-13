import subprocess
import shlex

if __name__ == "__main__":
    subprocess.run(shlex.split("git tag -l 1"), check=True)
