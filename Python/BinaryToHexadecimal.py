# Convert Binary to Hexadecimal

print("Enter '0' for exit.");
binary = input("Enter a number in Binary Format: ");
if binary == 0:
    exit();
else:
    st = int(binary, 2);
    print(binary,"in Hexadecimal =",hex(st));