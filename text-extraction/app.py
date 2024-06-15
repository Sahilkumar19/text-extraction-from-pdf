from flask import Flask, render_template, request, redirect, url_for, send_file
import fitz  # PyMuPDF
import csv
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

def extract_text_from_pdf(pdf_path, csv_path):
    pdf_document = fitz.open(pdf_path)
    with open(csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Page Number', 'Content'])
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            text = page.get_text("text")
            csv_writer.writerow([page_number + 1, text])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'pdf_file' not in request.files:
            return redirect(request.url)
        file = request.files['pdf_file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(pdf_path)
            csv_path = os.path.splitext(pdf_path)[0] + '.csv'
            extract_text_from_pdf(pdf_path, csv_path)
            return send_file(csv_path, as_attachment=True)
    return render_template('index.html')

if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)