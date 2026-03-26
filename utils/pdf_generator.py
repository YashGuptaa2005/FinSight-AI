from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(filename="report.pdf", content="Sample Report"):
    """
    Generate a simple PDF report
    """
    c = canvas.Canvas(filename, pagesize=letter)
    
    width, height = letter

    c.setFont("Helvetica", 12)

    # Add content
    text = c.beginText(40, height - 50)
    text.textLines(content)

    c.drawText(text)

    c.save()

    print(f"PDF saved as {filename}")


# Test
if __name__ == "__main__":
    sample_text = "This is a test report for FinSight AI."
    generate_pdf_report("test_report.pdf", sample_text)