for i in range(99, 0, -1):
    if i == 1:
        print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
        print("Take it down and pass it around, no more bottles of beer on the wall.")
    elif i == 2:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i-1} bottle of beer on the wall.")
    else:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
    
    print()

