import io
from fpdf import FPDF
from s3 import upload_to_s3  # Import the upload function from s3.py

# Define the body content for the PDF
pdf_body = '''Nepal is a beautiful country located in South Asia, nestled between China and India. 
It is known for its breathtaking landscapes, rich culture, and historical significance. Nepal is home to the majestic Himalayas, including Mount Everest, the world's highest peak.

The capital city, Kathmandu, is famous for its ancient temples, vibrant festivals, and diverse traditions. Nepalese people follow various religions, with Hinduism and Buddhism being the most prominent. The country is also known for its warm hospitality and unity in diversity.

Nepal has a rich natural heritage, with lush forests, serene lakes, and wildlife reserves. Popular tourist destinations include Pokhara, Lumbini (the birthplace of Lord Buddha), and Chitwan National Park. The country’s economy is mainly based on agriculture, tourism, and remittances.

Despite being a small country, Nepal has a strong cultural identity and a proud history. Its national flag is unique, with a triangular design symbolizing peace and bravery. The people of Nepal take pride in their traditions and work hard to build a better future.

Nepal is truly a land of natural wonders, cultural heritage, and warm-hearted people. I feel proud to be a part of this incredible nation! 🇳🇵'''

# Create a class inheriting from FPDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 15, 'My Country Nepal', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln(2)

# Create PDF in memory and upload it to S3
def create_pdf_and_upload_to_s3(pdf_body, bucket_name, s3_file_name):
    # Create a PDF instance
    pdf = PDF()
    pdf.add_page()
    pdf.chapter_body(pdf_body)
    
    # Save the PDF to a BytesIO object (in-memory)
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)  # Move to the beginning of the BytesIO buffer
    
    # Upload the PDF to S3 directly from memory
    upload_to_s3(pdf_output, bucket_name, s3_file_name)

# Example usage
bucket_name = 'my-pdf-bucket'
pdf_name = "nepal_country_info.pdf"
create_pdf_and_upload_to_s3(pdf_body, bucket_name, pdf_name)
