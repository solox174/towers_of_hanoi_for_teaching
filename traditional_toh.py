N = int(input("How many rings: "))

def recursive_hanoi(n, source, auxiliary, target):
    """
    TRADITIONAL RECURSIVE SOLUTION
    Logic: Move n-1 disks to a spare rod, move the base disk,
           then move those n-1 disks back on top.
    """
    if n > 0:
        # 1. Move n-1 disks from Source to Auxiliary
        recursive_hanoi(n - 1, source, target, auxiliary)

        # 2. Move the actual disk (the base)
        disk = source.pop()
        target.append(disk)
        print(f"Move disk {disk} to {target}")

        # 3. Move those n-1 disks from Auxiliary to Target
        recursive_hanoi(n - 1, auxiliary, source, target)

recursive_hanoi(N, list(range(N, 0, -1)), [], [])
