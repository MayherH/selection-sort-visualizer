from sort import selection_sort
import gradio as gr

def visualize_selection_sort(arr):
    steps = selection_sort(arr)
    visualization = []

    for step in steps: # Extracts snapshot info
        array_state = step["array"]
        i = step["i"]
        j = step["j"]
        min_idx = step["min_idx"]

        highlight = [""] * len(array_state) # Create a highlight list matching array length

        if j is not None:
            highlight[j] = "current"
        highlight[i] = "current"
        highlight[min_idx] = "min"

        visualization.append((array_state.copy(), highlight.copy()))

    return visualization # Returns all steps for visualization

def render_step(step):
    array_state, highlight = step

    tokens = []
    for value, tag in zip(array_state, highlight): # Convert each entry into a HighlightedText token
        if tag == "":
            tokens.append({"text": str(value), "entity": None})
        else:
            tokens.append({"text": str(value), "entity": tag}) # Highlighted text with entity "current" or "min"

    return tokens