# Task 1A: High-Accuracy Structure Extraction

    This project extracts structured outlines (Title, H1, H2, H3) from PDF documents.

    ## Methodology
    The solution uses a multi-heuristic scoring engine that analyzes each line of a PDF based on font size, weight, and textual patterns to identify headings. It uses statistical analysis on these scores to classify heading levels, making it robust to different document layouts.

    ## How to Build and Run
    1.  **Build the Docker Image:**
        ```bash
        docker build --platform linux/amd64 -t adobe-task1a .
        ```
    2.  **Run the Container:**
        Create `input` and `output` folders. Place PDFs in the `input` folder.
        ```bash
        docker run --rm -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" --network none adobe-task1a
        ```