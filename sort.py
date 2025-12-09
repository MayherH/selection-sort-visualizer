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