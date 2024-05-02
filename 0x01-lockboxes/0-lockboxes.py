#!/usr/bin/python3

"""
Lockboxes Problem:

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes. Write a method that determines if all the boxes can
be opened.

Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
    - boxes (list): A list of lists where each inner list represents a box containing keys.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    # Set to track opened boxes
    opened_boxes = set([0])  # Start with box 0 as it's unlocked initially

    # Queue for BFS traversal
    queue = [0]  # Start with box 0

    while queue:
        current_box = queue.pop(0)  # Get the front box from the queue
        keys = boxes[current_box]  # Get keys in the current box

        # Check each key in the current box
        for key in keys:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)  # Add the key to opened_boxes
                queue.append(key)  # Add the key to the queue for traversal

    # Check if all boxes can be opened
    return len(opened_boxes) == len(boxes)
