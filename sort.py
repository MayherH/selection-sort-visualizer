def selection_sort(arr): # Standard selection sort algorithm, with snapshots for visualization
    
    steps = []
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps.append({"array": arr.copy(), "i": i, "j": j, "min_idx": min_idx}) # snapshot
            if arr[j] < arr[min_idx]:
                min_idx = j
                steps.append({"array": arr.copy(), "i": i, "j": j, "min_idx": min_idx}) # snapshot
        steps.append({"array": arr.copy(), "i": i, "j": None, "min_idx": min_idx}) # snapshot
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append({"array": arr.copy(), "i": i, "j": None, "min_idx": min_idx}) # snapshot
    return steps

def bubble_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        swap_count = 0
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
        if swap_count == 0:
            return arr
    return arr