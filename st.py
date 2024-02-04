import sys
print(sys.version)
print(sys.version_info)

m=int(input("Enter your marks: "))
if m<90:
    # SystemExit("Not Selected")
    sys.exit("Not Selected")
else:
    print("Selected")