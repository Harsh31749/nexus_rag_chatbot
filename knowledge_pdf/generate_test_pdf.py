from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Project Nexus: Technical Specifications', 0, 1, 'C')
        self.ln(10)

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Specific, fictional data to test the RAG engine
content = """
1. Project Overview
Project Nexus is a next-generation quantum routing protocol designed specifically for deep-sea data transmission. The project was officially initiated on October 14th, 2024.

2. Core Components
- The primary hyper-threading matrix is coded in a proprietary language called 'Abyss-Lang'.
- The system operates at a maximum temperature threshold of 4.2 Kelvin. If this threshold is breached, the 'Aegis Protocol' automatically shuts down the mainframe.

3. Key Personnel
- Lead Architect: Dr. Aris Thorne.
- Security Director: Commander Elena Rostova.

4. Security Protocols
To access the Level 3 diagnostic terminal, engineers must use the override code: 'NEXUS-99-OMEGA'.
"""

pdf.multi_cell(0, 10, content)
pdf.output('nexus_test_document.pdf')
print("Test PDF 'nexus_test_document.pdf' generated successfully!")