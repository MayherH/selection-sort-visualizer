# selection-sort-visualizer
A visualizer of a selection sort algorithm

I chose selection sort because to me it is the most visually easy to understand and most pleasing to the eyes (bubble sort is also good looking but I feel like its too simple).

Sort.py
   Decomposition:
   - Selection Sort part
      - take input (Unsorted Array)
      - loop through each number, seeing if the index your at is smaller than your current, setting new min if so
      - put min at start when fully looped through
      - keep looping till fully sorted
   - Snapshots
      - create a snapshot at each part where a variable changes in order to visualise steps
      - snapshots at: start of loop, whenever pointer moves, whenever minimum changes, whenever swap happens
   Pattern Recognition:
   - The algorithm repeatedly compares each element with the current minimum, and swaps elements based on the result of those comparisons
   Abstraction: 
   - specific number values dont matter, just wether its higher or lower
   Algorithmic Thinking:
   - Inputs/Output: 
   - Input: list
   - Output: list (sorted)
   - Flowchart:
      - Start
      --> Get the unsorted array 
      --> Set i to 0 (first item)
      --> Loop through the array until the end
      --> Look for the smallest number from i to the end
      --> Compare the numbers, update the min if needed
      --> Take a snapshot (show where we are in the array)
      --> When done, swap the smallest with arr[i]
      --> Take another snapshot (after the swap)
      --> Move to the next item (i++) and repeat
      --> Keep going until the whole array is sorted
      --> Final snapshot (everything is sorted now)
      --> Done

App.py 
  Decomposition:
   visualise_selection_sort(arr) Method:
    - Take input (Unsorted Array)
    - Run the selection sort algorithm to generate sorting steps
    - Loop through the steps:
        - For each step, extract the array state, current index (i), comparison index (j), and minimum index (min_idx)
        - Create a list of highlights:
            - Mark elements as "sorted" when they've already been placed correctly
            - Highlight the current minimum element and the current element being compared
        - Append the current state of the array and highlights to a visualization list
    - After the loop, add a final snapshot with all elements marked as "sorted"
    - Return the list of visual steps

- render_step(step) Method:
    - Take input (Step data: array_state, highlight)
    - For each value in the array and its corresponding highlight:
        - If no highlight, just append the value as a string
        - If there’s a highlight ("current", "min", "sorted"), append the value with the corresponding tag
    - Return the list of tokens with array elements and their respective highlights

- visualize_with_slider(arr_input) Method:
    - Take input (Comma-separated array input from user)
    - Parse the input into an integer list
    - Call visualize_selection_sort to generate the steps for the sorting process
    - Return the list of steps and the maximum step index (for the slider)

- display_step(arr_input, step_idx) Method:
    - Take input (Comma-separated array input from user and a step index)
    - Parse the input into an integer list
    - Call visualize_selection_sort to generate the sorting steps
    - If the step index is within bounds, call render_step to return the specific step
    - If the step index is out of bounds, return an empty list

- Gradio Interface (Main Gradio Block):
    - Take user input (array in Textbox, step navigation in Slider)
    - When the "Visualize" button is clicked:
        - Generate the visualization steps with visualize_with_slider
        - Update the slider to reflect the number of steps in the process
    - When the slider is moved:
        - Update the visualization based on the selected step using display_step
    - Dynamically display the array with the appropriate highlights for the selected step


   Pattern Recognition:
- visualize_selection_sort(arr):
    - Repeatedly compares each element to find the minimum and swaps it to the correct position.
    - Highlights "current", "min", and "sorted" elements at each step.

- render_step(step):
    - Generates a list of tokens with values and corresponding highlight tags ("current", "min", "sorted").

- visualize_with_slider(arr_input):
    - Parses the input array and generates the sorting steps.
    - Updates the slider to navigate through the sorting steps.

- display_step(arr_input, step_idx):
    - Retrieves a specific sorting step and displays the array state with the corresponding highlights.

- Gradio Interface:
    - User inputs an array, presses "Visualize", and navigates through the sorting steps using the slider.
    - The process of updating the array and highlights repeats with each slider change.

   Abstraction:
   - The specific values in the array are less important than the comparisons and swaps, which are visualized using highlights ("current", "min", "sorted")
   - The array state and the changes in it are the main focus of the visualization, not the exact values.

   Algorithmic Thinking:
- Inputs/Output:
    - Input: array
    - Output: A sequence of visual steps showing the array and highlighting the elements as they are compared or updated

- Flowchart:
    - Start
    --> User enters array in Textbox
    --> Press "Visualize" button
    --> visualize_with_slider(arr_input) is called
        --> arr_input is parsed into an integer array
        --> visualize_selection_sort(arr) is called
            --> Selection Sort runs on the array, generating sorting steps
            --> Snapshots of the array state are stored (highlighting "current", "min", "sorted")
        --> Return the sorting steps and the maximum index for the slider
    --> Create slider with maximum value based on the number of steps
    --> User moves the slider to navigate through the steps
    --> display_step(arr_input, step_idx) is called with the selected step index
        --> render_step(step) is called for the current step
            --> Highlights the current array state and updates the display
    --> Repeat until all steps are displayed (array fully sorted)
    --> End
