# Text Extractor from PDF

This repository contains a Flask web application that allows users to upload a PDF file and converts its text content to a CSV file. The text content is extracted page by page, preserving the format.

## Features

- Upload a PDF file
- Extract text content from each page
- Save the extracted content in a CSV file
- Download the CSV file automatically

## Requirements

- Python 3.x
- Flask
- PyMuPDF (fitz)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sahilkumar19/pdf-to-csv-converter.git
   cd pdf-to-csv-converter
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate
3. **Install the required packages:**
   ```bash
   pip install Flask PyMuPDF

## Usage

1. **Run the Flask application:**
   ````bash
   python app.py
2. **Open a web browser and navigate to:**
   ````bash
   http://127.0.0.1:5000/



