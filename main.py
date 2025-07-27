import os
import json
from task_1a import extract_structure

# Define the input and output directories as specified in the hackathon brief
INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_all_pdfs_1a():
    """
    Processes all PDF files from the input directory and saves their
    structured outline to the output directory. This is the main function
    for the Docker container execution for Task 1A.
    """
    print("--- Running Task 1A: Structure Extraction ---")
    if not os.path.exists(INPUT_DIR):
        print(f"Error: Input directory '{INPUT_DIR}' not found.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print(f"No PDF files found in '{INPUT_DIR}'.")
        return
    
    print(f"Found {len(pdf_files)} PDF(s) to process: {pdf_files}")
    for pdf_file in pdf_files:
        input_path = os.path.join(INPUT_DIR, pdf_file)
        output_filename = f"{os.path.splitext(pdf_file)[0]}.json"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        
        print(f"Processing '{input_path}'...")
        
        structure_data = extract_structure(input_path)
        
        # Clean the output to match the required format
        clean_outline = []
        for item in structure_data.get("outline", []):
            clean_item = item.copy()
            clean_item.pop("bbox", None)
            clean_item.pop("raw_blocks", None)
            clean_outline.append(clean_item)

        output_json = {
            "title": structure_data.get("title", "Title not found"),
            "outline": clean_outline
        }
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(output_json, f, indent=4, ensure_ascii=False)
            print(f"Successfully saved output to '{output_path}'")
        except Exception as e:
            print(f"Error saving file to '{output_path}': {e}")

if __name__ == '__main__':
    process_all_pdfs_1a()
