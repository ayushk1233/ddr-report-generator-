from app.services.pdf.pdf_service import PDFService

service = PDFService()

print(
    service.validate_pdf(
        "Sample Report.pdf"
    )
)