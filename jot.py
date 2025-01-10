def parse_disk_map(disk_map):
    """
    Parse the dense disk map into a list of file and free space blocks.
    """
    blocks = []
    for i in range(0, len(disk_map), 2):
        file_size = int(disk_map[i])
        free_space = int(disk_map[i + 1])
        if file_size > 0:
            blocks.extend([len(blocks) // 2] * file_size)  # Assign file ID
        if free_space > 0:
            blocks.extend(['.'] * free_space)
    return blocks

def compact_disk(blocks):
    """
    Simulate the compaction process by moving file blocks to the leftmost free space.
    """
    n = len(blocks)
    write_pointer = 0

    for read_pointer in range(n):
        if blocks[read_pointer] != '.':
            blocks[write_pointer] = blocks[read_pointer]
            write_pointer += 1

    # Fill remaining blocks with free space ('.')
    for i in range(write_pointer, n):
        blocks[i] = '. '

    return blocks

def calculate_checksum(blocks):
    """
    Calculate the filesystem checksum.
    """
    checksum = 0
    for position, block in enumerate(blocks):
        if block != '.':
            checksum += position * int(block)
    return checksum

def main():
    # Input: The disk map as a string
    disk_map = "2333133121414131402"  # Replace with your actual input

    # Step 1: Parse the disk map
    blocks = parse_disk_map(disk_map)
    print("Initial disk blocks:", ''.join(map(str, blocks)))

    # Step 2: Compact the disk
    compacted_blocks = compact_disk(blocks)
    print("Compacted disk blocks:", ''.join(map(str, compacted_blocks)))

    # Step 3: Calculate the checksum
    checksum = calculate_checksum(compacted_blocks)
    print("Filesystem checksum:", checksum)

if __name__ == "__main__":
    main()






# with open('jot.txt') as f:
#     disk_map = [int(x) for x in [line.rstrip() for line in f][0]]

# print(disk_map)

# part1 = True

# if part1:
#     current_id = len(disk_map)//2
#     front_id = 0
#     compact = [front_id, disk_map.pop(0)]  # Compact will be file id, length, file id, length, etc.
#     front_id += 1

#     # The approach here is to consume file_map character by character from the back and the front
#     # We'll put the first full file into the compact list, then fill the free space with files from
#     # the back, and go back and forth.
#     while disk_map:
#         # We've already moved the first file over, so the first character at this point represents
#         # the length of free space. Get the last character, which should be a file with file ID
#         # current_id
#         current_file = disk_map[-1]
#         if len(disk_map) == 2:  # Last file, just move it over and stop
#             compact += [current_id, current_file]
#             break

#         # Can the file fit entirely into the free space we have available, with room to spare?
#         if current_file < disk_map[0]:
#             # Update the free space in the front of disk_map
#             disk_map[0] -= current_file
#             # Add current_file to compact
#             compact += [current_id, current_file]
#             # Update the current_id
#             current_id -= 1
#             # Clean up the file and extra free space at the end of disk_map
#             disk_map.pop()  # File
#             disk_map.pop()  # Free space
#         # Can the file fit exactly into the free space, with no room to spare?
#         elif current_file == disk_map[0]:
#             # Remove the free space in the front of disk_map
#             disk_map.pop(0)
#             # Add current_file to compact and update the current_id
#             compact += [current_id, current_file]
#             current_id -= 1
#             # Clean up the file and extra free space at the end of disk_map
#             disk_map.pop()  # File
#             disk_map.pop()  # Free space
#             # Move the front file into compact and update the front_id
#             compact += [front_id, disk_map.pop(0)]
#             front_id += 1
#         # Else, the file needs to be split up
#         else:
#             # Add part of the current_file to compact. Do not update current_id
#             compact += [current_id, disk_map[0]]
#             # Update current_file to reflect its remaining length
#             current_file = current_file - disk_map[0]
#             # Remove the free space in the front of disk_map
#             disk_map.pop(0)
#             # Move the front file into compact and update the front_id
#             compact += [front_id, disk_map.pop(0)]
#             front_id += 1
#             # Update the current_file length in disk_map for the next iteration
#             disk_map[-1] = current_file

#     counter = 0  # Keeps track of the overall index
#     check_sum = 0
#     for i in range(len(compact)//2):  # Going through compact in groups of 2
#         file_id = compact[i*2]
#         count = compact[i*2 + 1]
#         for c in range(count):
#             check_sum += file_id * counter
#             counter += 1
#     print(f"Part 1: {check_sum}")

