# selection-sort-visualizer
A visualizer of a selection sort algorithm

I chose selection sort because to me it is the most visually easy to understand and most pleasing to the eyes (bubble sort is also good looking but I feel like its too simple).

Decomposition:
 - Selection Sort part
    - take input (Unsorted Array)
    - loop through each number, seeing if the index your at is smaller than your current, setting new min if so
    - put min at start when fully looped through
    - keep looping till fully sorted
 - Snapshots
    - create a snapshot at each part where a variable changes in order to visualise steps
    - snapshots at: start of loop, whenever pointer moves, whenever minimum changes, whenever swap happens
