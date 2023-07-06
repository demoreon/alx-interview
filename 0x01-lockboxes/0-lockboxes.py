#!/usr/bin/python3
"""
Function to scan boxes if they can be unlocked
"""


def canUnlockAll(boxes):
    """
    This cans a boxes using multiple loops.
    The time complexity is quadratic O(n)
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
