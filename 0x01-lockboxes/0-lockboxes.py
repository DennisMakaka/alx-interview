#!/usr/bin/python3
"""
Lockboxes - A module containing a method to determine if all lockboxes can be unlocked.

This file defines a method `canUnlockAll()` that checks if it is possible to unlock
all the boxes starting from box 0, using the keys found inside each unlocked box.

Each box contains a list of keys, where the keys correspond to other boxes. The
function works by iteratively unlocking boxes and adding their keys to the list of
available keys. The process continues until either all boxes are unlocked, or no
more boxes can be unlocked.

The function follows a simple logic of iterating over each box and unlocking all
reachable boxes using the keys inside the unlocked boxes.

Example:
    canUnlockAll([[1], [2], [3], [4], []]) -> True
    canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]) -> True
    canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]) -> False

"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    The first box (boxes[0]) is unlocked at the start, and the function iterates
    over all the boxes, unlocking the ones whose keys are available. The function
    uses a set to track the unlocked boxes and adds keys from unlocked boxes to
    continue unlocking other boxes.

    Parameters:
    boxes (list of list): A list where each element is a list representing a box,
                          and each list contains keys that correspond to other boxes.
                          Example: [[1], [2], [3], [4], []]

    Returns:
    bool: Returns True if all boxes can be unlocked, otherwise returns False.

    Example:
    canUnlockAll([[1], [2], [3], [4], []]) -> True
    canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]) -> True
    canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]) -> False
    """

    # Initialize an empty set to keep track of unlocked boxes
    unlocked = set()

    # Iterate over each box by its ID and contents (key list)
    for box_id, box in enumerate(boxes):
        # If the box is empty or it's the first box (box 0), it is unlocked
        if len(box) == 0 or box_id == 0:
            unlocked.add(box_id)

        # Iterate through the keys in the current box
        for key in box:
            # Add the key if it unlocks a valid box (not the current box itself)
            if key < len(boxes) and key != box_id:
                unlocked.add(key)

        # If the number of unlocked boxes is equal to the total number of boxes,
        # return True, indicating all boxes are unlocked
        if len(unlocked) == len(boxes):
            return True

    # If all the boxes are not unlocked, return False
    return False

