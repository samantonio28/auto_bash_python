import sys

file_path = sys.argv[1]

avg = 0.0
disp = 0
st_devi = 0
StrErr = 0
rse = 1
n = 0
        
with open(file_path, "r") as f:
    for line in f:
        avg += int(line)
        n += 1
    avg //= n
with open(file_path, "r") as f:
    for line in f:
        disp += (int(line) - avg) ** 2
    disp //= (n - 1)


st_devi = disp ** 0.5
StdErr = st_devi / (n ** 0.5)

rse = StdErr / avg * 100

print(f"{rse:.2f}")

if rse >= 1:
    sys.exit(1)
sys.exit(0)