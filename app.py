from sort import selection_sort
import gradio as gr

def visualize_selection_sort(arr):
    steps = selection_sort(arr)
    visualization = []

    for step in steps:
        array_state = step["array"]
        i = step["i"]
        j = step["j"]
        min_idx = step["min_idx"]

        highlight = [""] * len(array_state)

        if j is not None:
            highlight[j] = "current"
        highlight[i] = "current"
        highlight[min_idx] = "min"

        visualization.append((array_state.copy(), highlight.copy()))

    return visualization