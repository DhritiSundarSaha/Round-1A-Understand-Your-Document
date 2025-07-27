import fitz  # PyMuPDF
import os

def create_sample_pdf_1a():
    """Generates a sample PDF for Task 1A testing if it doesn't exist."""
    pdf_path = "sample_document.pdf"
    if os.path.exists(pdf_path):
        return
    
    print(f"Generating sample PDF: '{pdf_path}'...")
    try:
        doc = fitz.open()
        page = doc.new_page()
        # --- FIX: Using standard base font names for guaranteed compatibility ---
        page.insert_text((72, 72), "Advanced AI Systems", fontsize=24, fontname="helvetica-bold")
        page.insert_text((72, 120), "1. Introduction to AI", fontsize=18, fontname="helvetica-bold")
        page.insert_text((72, 140), "Artificial intelligence is a transformative technology. This document explores the core concepts and their applications across various industries.", fontsize=12, fontname="helvetica")
        page.insert_text((72, 200), "1.1 Core Concepts", fontsize=14, fontname="helvetica-bold")
        page.insert_text((72, 220), "Machine learning and deep learning are subsets of AI. Natural Language Processing (NLP) is another key area.", fontsize=12, fontname="helvetica")
        doc.save(pdf_path)
        doc.close()
        print("Sample PDF created successfully.")
    except Exception as e:
        print(f"Error creating sample PDF: {e}")
