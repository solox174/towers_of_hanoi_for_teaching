"""
TOWERS OF HANOI: THE PHYSICAL RHYTHM RULES (the "algorithm")
------------------------------------------
1. THE SETUP:
   - Identify the "Target Order" for the smallest disk (Disk 1).
   - If N is ODD:  Move Disk 1 in a cycle: Source -> Destination -> Auxiliary -> Source and so on.
   - If N is EVEN: Move Disk 1 in a cycle: Source -> Auxiliary -> Destination -> Source and so on.

2. THE TWO-STEP LOOP (Repeat until the Destination rod is complete):

   STEP A: Move the Smallest Disk (Disk 1)
           Always move it one step forward in the Target Order

   STEP B: The "Other" Move
           Look at the two rods that do NOT have Disk 1 on them.
           There is only one legal move possible between them:
           Move the smaller available disk onto the larger one (or an empty rod).

3. THE GOLDEN CONSTRAINTS:
   - Only move one disk at a time.
   - Only take the top disk from any rod.
   - Never place a larger disk on top of a smaller disk.
"""

from collections import deque

N = int(input("How many rings: "))

# Initialize rods
source = list(range(N, 0, -1))
auxiliary = []
destination = []
destination_goal_state = source.copy()

# Parity determines rotation order per game rhythm rules
# deque creates a "circular" array of rods
if N % 2 == 0:
    d = deque([source, auxiliary, destination])
else:
    d = deque([source, destination, auxiliary])

def move_other_disks(r1, r2):
    """Moves the rod with the smallest ring onto the other"""
    # In case both rods are empty
    if not r1 and not r2: return
    # Use infinity as a placeholder for comparing to an empty rod
    d1_ring_size = r1[-1] if r1 else float('inf')
    d2_ring_size = r2[-1] if r2 else float('inf')

    if d1_ring_size < d2_ring_size:
        r2.append(r1.pop())
    else:
        r1.append(r2.pop())

print(f"Starting with Source: {source}, Auxiliary: {auxiliary}, Destination: {destination}")
# Main loop
while destination != destination_goal_state:
    # --- STEP A: Move the Smallest Disk ---
    # It is always at the top of d[0] at the start of this cycle
    ring = d[0].pop()
    d.rotate(-1)
    d[0].append(ring)

    # Check if we finished immediately after moving the smallest disk
    if destination == destination_goal_state:
        print(f"Final state: {source}, Auxiliary: {auxiliary}, Destination: {destination}")
        break

    # --- STEP B: The "Other" Move ---
    # This move happens between the two rods the smallest disk is NOT on
    # (which are d[1] and d[2] after the rotation)
    move_other_disks(d[1], d[2])
    print(f"After move: {source}, Auxiliary: {auxiliary}, Destination: {destination}")


