import subprocess


try:
    result = subprocess.run("sleep 10 && echo ciao", timeout=1, shell=True, stdout=subprocess.PIPE)
    print(f"let's go: {result}")
except subprocess.TimeoutExpired:
    # insert code here
    print("Timeout")