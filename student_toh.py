# The Rods (puts in list)
rod_a = [3,2,1]
rod_b = []
rod_c = []

def print_state():
    """Prints the current state of the tower."""
    print("Rod A:", rod_a[::-1])
    print("Rod B:", rod_b[::-1])
    print("Rod C:", rod_c[::-1])
    print("-" * 10)

print_state()

def move_ring( source, destination):
    """Moves the ring to the destination."""
    ring= source.pop() # lift the top ring
    destination.append(ring)  # Drops it on the new Rod
    print_state()

move_ring(rod_a, rod_c)
move_ring (rod_a, rod_b)
move_ring(rod_c, rod_b)
move_ring(rod_a, rod_c)
move_ring(rod_b, rod_a)
move_ring(rod_b, rod_c)
move_ring(rod_a, rod_c)