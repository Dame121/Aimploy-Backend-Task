"""
Script to create a sample PDF for testing the AIMPLOY API
"""

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib import colors
    from datetime import datetime
except ImportError:
    print("Error: reportlab is not installed.")
    print("Install it using: pip install reportlab")
    exit(1)

def create_sample_pdf():
    """Create a sample PDF with text, tables, and metadata"""
    
    filename = "sample_document.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    
    # Create styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=30,
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#764ba2'),
        spaceAfter=12,
        spaceBefore=12,
    )
    
    # Build content
    content = []
    
    # Title
    content.append(Paragraph("AIMPLOY Sample Document", title_style))
    content.append(Spacer(1, 0.2*inch))
    
    # Introduction text
    content.append(Paragraph("Sample PDF for API Testing", heading_style))
    intro_text = """
    This is a sample PDF document created to test the AIMPLOY PDF Processing API. 
    It contains various types of content including text paragraphs, tables, and metadata. 
    The API should be able to extract all text and table data from this document.
    """
    content.append(Paragraph(intro_text, styles['BodyText']))
    content.append(Spacer(1, 0.2*inch))
    
    # Section 1
    content.append(Paragraph("Section 1: Company Information", heading_style))
    section1_text = """
    AIMPLOY is a leading platform for PDF processing and data extraction. 
    We provide robust APIs for handling various document types and extracting 
    valuable information from unstructured data. Our machine learning models 
    ensure accurate and efficient processing of large-scale document collections.
    """
    content.append(Paragraph(section1_text, styles['BodyText']))
    content.append(Spacer(1, 0.15*inch))
    
    # Table 1: Sample Data
    content.append(Paragraph("Sample Data Table", heading_style))
    table_data = [
        ['Product', 'Q1 Sales', 'Q2 Sales', 'Q3 Sales', 'Total'],
        ['Product A', '$50,000', '$65,000', '$72,000', '$187,000'],
        ['Product B', '$45,000', '$52,000', '$61,000', '$158,000'],
        ['Product C', '$38,000', '$42,000', '$55,000', '$135,000'],
        ['Service X', '$60,000', '$68,000', '$75,000', '$203,000'],
    ]
    
    table = Table(table_data, colWidths=[1.5*inch, 1.2*inch, 1.2*inch, 1.2*inch, 1.2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ]))
    content.append(table)
    content.append(Spacer(1, 0.2*inch))
    
    # Section 2
    content.append(Paragraph("Section 2: Features", heading_style))
    features_text = """
    <b>Text Extraction:</b> Our API can extract all text content from PDF documents while preserving the structure and formatting. 
    <br/><br/>
    <b>Table Recognition:</b> Complex tables are automatically detected and extracted in structured formats. 
    <br/><br/>
    <b>Metadata Retrieval:</b> Document metadata such as title, author, creation date, and page count are automatically extracted. 
    <br/><br/>
    <b>Error Handling:</b> The API provides comprehensive error handling and detailed error messages for troubleshooting.
    """
    content.append(Paragraph(features_text, styles['BodyText']))
    content.append(Spacer(1, 0.2*inch))
    
    # Table 2: Feature Comparison
    content.append(Paragraph("Feature Comparison", heading_style))
    comparison_data = [
        ['Feature', 'Free', 'Pro', 'Enterprise'],
        ['Text Extraction', 'Yes', 'Yes', 'Yes'],
        ['Table Detection', 'Basic', 'Advanced', 'Advanced'],
        ['API Access', 'Limited', 'Unlimited', 'Unlimited'],
        ['Support', 'Community', 'Priority', '24/7'],
        ['Price', 'Free', '$99/mo', 'Custom'],
    ]
    
    comparison_table = Table(comparison_data, colWidths=[2*inch, 1.2*inch, 1.2*inch, 1.2*inch])
    comparison_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#764ba2')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    content.append(comparison_table)
    content.append(Spacer(1, 0.2*inch))
    
    # Footer
    footer_text = f"""
    <b>Document Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    <br/>
    <b>Document Type:</b> Sample Test Document
    <br/>
    <b>Purpose:</b> API Testing and Validation
    """
    content.append(Paragraph(footer_text, styles['Normal']))
    
    # Build PDF
    doc.build(content)
    print(f"✅ Sample PDF created successfully: {filename}")
    print(f"📁 Location: {os.path.abspath(filename)}")
    print(f"📊 Size: {os.path.getsize(filename) / 1024:.2f} KB")

if __name__ == "__main__":
    import os
    create_sample_pdf()
