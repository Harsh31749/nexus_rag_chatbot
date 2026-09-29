from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        pass

def create_pdf(title, filename, content):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 15)
    pdf.cell(0, 10, title, 0, 1, 'C')
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, content)
    pdf.output(filename)
    print(f"Generated: {filename}")

content1 = """
1. Mission Objective
The Artemis-V mission aims to establish the first permanent habitat on the Martian surface by 2038.

2. Habitat Specifications
The primary habitat, known as 'Ares Base', is constructed using 3D-printed regolith composite material. It can withstand external temperatures dropping to -100 degrees Celsius and local sandstorms with winds up to 150 km/h.

3. Key Personnel
- Mission Commander: Captain Sarah Jenkins
- Chief Engineer: Dr. Elias Vance
- Lead Botanist: Dr. Maya Lin

4. Emergency Protocols
In the event of a depressurization alarm, all crew must immediately dawn their Mark-IV suits and proceed to the central airlock bunker. The lockdown override code is 'ARES-LOCK-44'.
"""

content2 = """
1. Introduction to Quantum Processing
The Q-Core Processor utilizes 256 interconnected qubits to perform calculations in parallel, achieving speeds up to 10,000 times faster than classical silicon chips for specific optimization algorithms.

2. Operating Environment
To maintain quantum coherence, the Q-Core must be submerged in liquid helium and kept at a temperature of 15 milliKelvin. Any fluctuation above 20 milliKelvin will cause instantaneous decoherence and data loss.

3. System Architecture
- Qubit Type: Superconducting Transmon
- Error Correction: Surface Code Protocol
- Coherence Time (T2): 150 microseconds

4. Maintenance
Only Level 5 certified technicians are permitted to access the dilution refrigerator. Maintenance logs must be digitally signed using the cryptographic key 'Q-SYNC-909'.
"""

create_pdf('Artemis-V Mars Mission Manual', 'mars_mission_manual.pdf', content1)
create_pdf('Q-Core Quantum Processing Guide', 'quantum_computing_guide.pdf', content2)
