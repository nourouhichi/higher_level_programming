#!/usr/bin/python3
import os
import sys
def usage_err():
    print('Usage: read_write_heap.py pid search_string replace_string')
    exit(1)
if len(sys.argv) != 4:
    usage_err()

maps_file = "/proc/{}/maps".format(sys.argv[1])
mem_file = "/proc/{}/mem".format(sys.argv[1])
string = sys.argv[2]
replace = sys.argv[3]

with open(maps_file, 'r') as maps:
    for line in maps:
        if ("[heap]") in line:
            heap_found = line
            break
"""splitting the address space """
heap_found = heap_found.split()
"""converting to base 16""" 
starting_at = int(heap_found[0].split("-")[0], 16)
ending_at = int(heap_found[0].split("-")[1], 16)

with open(mem_file, 'rb+') as memory:
    memory.seek(starting_at)
    heap = memory.read(ending_at - starting_at)
    index = heap.index(bytes(string, "ASCII"))
    memory.seek(index + starting_at)
    memory.write(bytes(replace, "ASCII"))
memory.close()
maps.close()
