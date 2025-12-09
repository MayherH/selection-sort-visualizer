from sort import selection_sort
import gradio as gr

def visualize_selection_sort(arr):
    steps = selection_sort(arr)
    visualization = []
    n = len(arr)

    for step in steps: # Extracts snapshot info
        array_state = step["array"]
        i = step["i"]
        j = step["j"]
        min_idx = step["min_idx"]

        highlight = [""] * len(array_state) # Create a highlight list matching array length
        
        for idx in range(i): # Mark sorted elements (elements that are in their final position)
            highlight[idx] = "sorted"

        if j is not None: # Highlight current and min only if j is not None
            highlight[j] = "current"
            highlight[min_idx] = "min"

        visualization.append((array_state.copy(), highlight.copy()))

    final_highlight = ["sorted"] * n # Add final step with all elements marked as sorted (Because otherwise, it wont show everything as sorted at the end, making it look a little yucky)
    visualization.append((arr.copy(), final_highlight))

    return visualization # Returns all steps for visualization

def render_step(step):
    array_state, highlight = step

    tokens = []
    for value, tag in zip(array_state, highlight): # Convert each entry into a HighlightedText token
        if tag == "":
            tokens.append((str(value), None))
        else:
            tokens.append((str(value), tag)) # Highlighted text with label "current" or "min"

    return tokens

def visualize_with_slider(arr_input): # Generate all sorting steps from input array
    try:
        arr = [int(x.strip()) for x in arr_input.split(",")]
        steps = visualize_selection_sort(arr)
        return steps, len(steps) - 1
    except:
        return [], 0

def display_step(arr_input, step_idx): # Get the visualization for a specific step
    try:
        arr = [int(x.strip()) for x in arr_input.split(",")]
        steps = visualize_selection_sort(arr)
        if step_idx < len(steps):
            return render_step(steps[step_idx])
        return []
    except:
        return []

with gr.Blocks() as demo:
    gr.Markdown("# Selection Sort Visualizer")
    
    with gr.Row():
        arr_input = gr.Textbox(
            label="Enter numbers (comma-separated)",
            placeholder="3,1,4,1,5,9,2,6",
            value="5,2,8,1,9"
        )
        visualize_btn = gr.Button("Visualize")
    
    step_slider = gr.Slider(
        minimum=0,
        maximum=100,
        step=1,
        label="Sort Step",
        interactive=True
    )
    
    visualization = gr.HighlightedText(
        label="Array State",
        color_map={"current": "yellow", "min": "red", "sorted": "green"}
    )
    
    def update_visualization(arr_input):
        steps, max_idx = visualize_with_slider(arr_input)
        return gr.update(maximum=max_idx)
    
    visualize_btn.click(
        fn=update_visualization,
        inputs=arr_input,
        outputs=[step_slider]
    )
    
    step_slider.change(
        fn=display_step,
        inputs=[arr_input, step_slider],
        outputs=visualization
    )

if __name__ == "__main__":
    demo.launch()