nums = list(map(int, input().split()))
kecil = float('inf')
besar = float('-inf')
for i in nums:
    if i < kecil:
        kecil = i
    elif i > besar:
        besar = i
print(f"nilai yang paling kecil adalah {kecil}")
print(f"nilai yang paling besar adalah {besar}")
