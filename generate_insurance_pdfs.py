#!/usr/bin/env python3
"""
Generate 10 realistic insurance claim PDFs with structured and unstructured data
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from datetime import datetime, timedelta
import random
import os

# ============================================================================
# CREATE OUTPUT DIRECTORY AT START (before any generators run)
# ============================================================================
os.makedirs("insurance_claims", exist_ok=True)

# Style for table cell values that may be too long to fit in their column
# (plain strings don't wrap in reportlab Tables and bleed into the next cell)
_wrap_style = ParagraphStyle('WrapCell', fontName='Helvetica', fontSize=9, leading=11)

def generate_auto_claim():
    """Auto Insurance Claim - Vehicle Collision"""
    doc = SimpleDocTemplate("insurance_claims/01_auto_collision_claim.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Header
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'],
                                  fontSize=16, textColor=colors.HexColor('#1e40af'),
                                  spaceAfter=12, alignment=TA_CENTER)
    story.append(Paragraph("AUTO INSURANCE CLAIM FORM", title_style))
    story.append(Spacer(1, 0.2*inch))

    # Structured data
    data = [
        ['Claim Number:', 'CLM-2026-89234', 'Date of Loss:', '2026-09-15'],
        ['Policyholder:', 'James Mitchell', 'Policy #:', 'AUTO-456782-B'],
        ['Vehicle:', '2021 Honda Civic (Blue)', 'Mileage:', '42,340 miles'],
        ['Accident Location:', Paragraph('2847 Maple Drive, Seattle WA 98101', _wrap_style), 'Date Reported:', '2026-09-16'],
        ['Estimated Damage:', '$8,450', 'Status:', 'Under Investigation'],
    ]

    t = Table(data, colWidths=[1.8*inch, 2.2*inch, 1.8*inch, 2.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e0e7ff')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.3*inch))

    # Unstructured notes
    story.append(Paragraph("INCIDENT DETAILS & NOTES", styles['Heading2']))
    story.append(Spacer(1, 0.1*inch))

    unstructured_text = """
    <b>Incident Description:</b><br/>
    Vehicle was traveling northbound on Maple Drive at approximately 2:45 PM when it
    was struck on the driver's side by a 2019 Toyota Camry that ran a red light at the
    intersection with Pine Street. Claimant reports immediate pain in left shoulder and
    neck. Police were called and report number 2026-89234-SPD was filed. Officer
    James Rodriguez was first responder.<br/><br/>

    <b>Witness Information:</b><br/>
    Two witnesses present at scene:<br/>
    - Sarah Chen (passenger in claimant's vehicle): Phone 206-555-0142<br/>
    - Robert Williams (bystander): States he saw other vehicle run the light, available
    for statement<br/><br/>

    <b>Damage Assessment (preliminary):</b><br/>
    - Driver's side door: severe dent, door frame damage<br/>
    - Quarter panel: crease and paint damage<br/>
    - Rocker panel: bent, needs replacement<br/>
    - Vehicle safety systems: airbags deployed, frame checking required<br/>
    - Interior: damage to door panel trim, seat fabric torn on driver's seat
    """

    story.append(Paragraph(unstructured_text, styles['Normal']))

    doc.build(story)
    print("Generated: 01_auto_collision_claim.pdf")

def generate_health_claim():
    """Health Insurance Claim - Hospital Visit"""
    doc = SimpleDocTemplate("insurance_claims/02_health_hospital_claim.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("HEALTH INSURANCE CLAIM FORM",
                          ParagraphStyle('Title', parent=styles['Heading1'], fontSize=16,
                                       textColor=colors.HexColor('#1e40af'), alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))

    # Structured data
    data = [
        ['Member ID:', 'HLT-987234-A', 'Date of Service:', '2026-09-10'],
        ['Member Name:', 'Robert Martinez', 'DOB:', '1975-03-22'],
        ['Provider:', 'Seattle General Hospital', 'Facility Type:', 'Hospital - Inpatient'],
        ['Admission Date:', '2026-09-10 14:32', 'Discharge Date:', '2026-09-12 09:15'],
        ['Primary Diagnosis:', 'Pneumonia (J18.9)', 'Secondary:', 'Hypertension (I10)'],
        ['Total Billed Amount:', '$14,235.67', 'Insurance Responsibility:', '$9,847.23'],
    ]

    t = Table(data, colWidths=[1.8*inch, 2.2*inch, 1.8*inch, 2.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e0e7ff')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.3*inch))

    # Detailed clinical notes
    story.append(Paragraph("CLINICAL DOCUMENTATION & PROVIDER NOTES", styles['Heading2']))
    story.append(Spacer(1, 0.1*inch))

    clinical_text = """
    <b>Chief Complaint:</b><br/>
    Patient presented to ED with persistent cough, fever up to 103.2°F, shortness of breath
    for 4 days. Patient reports general malaise and loss of appetite.<br/><br/>

    <b>Diagnosis & Treatment:</b><br/>
    Bilateral infiltrates on chest X-ray consistent with pneumonia. Started on antibiotics.
    Oxygen therapy initiated. Patient improving after 48 hours of treatment.
    """

    story.append(Paragraph(clinical_text, styles['Normal']))

    doc.build(story)
    print("Generated: 02_health_hospital_claim.pdf")

def generate_home_damage_claim():
    """Home Insurance Claim - Water Damage"""
    doc = SimpleDocTemplate("insurance_claims/03_home_water_damage_claim.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("HOME INSURANCE CLAIM - WATER DAMAGE",
                          ParagraphStyle('Title', parent=styles['Heading1'], fontSize=16,
                                       textColor=colors.HexColor('#1e40af'), alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))

    # Structured data
    data = [
        ['Claim Number:', 'HOM-2026-45612', 'Date of Loss:', '2026-09-12'],
        ['Policyholder:', 'Michelle Johnson', 'Policy #:', 'HOME-789234-C'],
        ['Property Address:', Paragraph('4521 Evergreen Lane, Portland OR 97201', _wrap_style), 'Sq Footage:', '2,450 sq ft'],
        ['Year Built:', '1998', 'Type of Loss:', 'Water Damage - Plumbing'],
        ['Date Reported:', '2026-09-12', 'Estimated Damage:', '$23,500'],
    ]

    t = Table(data, colWidths=[1.8*inch, 2.2*inch, 1.8*inch, 2.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e0e7ff')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("LOSS DESCRIPTION & ASSESSMENT", styles['Heading2']))
    story.append(Spacer(1, 0.1*inch))

    damage_text = """
    <b>Incident Summary:</b><br/>
    Toilet supply line ruptured causing water damage to master bedroom and guest bedroom.
    Estimated water flow for 4-6 hours before discovery. Drywall saturation, carpet water
    damage, and laminate flooring warped.<br/><br/>

    <b>Affected Areas:</b><br/>
    Master Bedroom: ceiling damage, crown molding water damage, carpet padding destroyed.
    Guest Bedroom: secondary water intrusion, drywall staining. Bathroom: toilet assembly
    damage, tile grout degradation.
    """

    story.append(Paragraph(damage_text, styles['Normal']))

    doc.build(story)
    print("Generated: 03_home_water_damage_claim.pdf")

def generate_workers_comp_claim():
    """Workers Compensation Claim - Workplace Injury"""
    doc = SimpleDocTemplate("insurance_claims/04_workers_comp_injury_claim.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("WORKERS' COMPENSATION CLAIM FORM",
                          ParagraphStyle('Title', parent=styles['Heading1'], fontSize=16,
                                       textColor=colors.HexColor('#1e40af'), alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))

    # Structured data
    data = [
        ['Claim Number:', 'WC-2026-56789', 'Date of Injury:', '2026-09-08'],
        ['Employee:', 'David Thompson', 'Employee ID:', 'EMP-87654'],
        ['Employer:', 'Pacific Manufacturing LLC', 'Industry:', 'Manufacturing'],
        ['Injury Type:', 'Back Strain - Lifting', 'Body Part:', 'Lower Back (L4-L5)'],
        ['Date Reported:', '2026-09-08 16:45', 'Time Off Work:', '8 days (and counting)'],
        ['Medical Provider:', 'Dr. Sarah Chen MD', 'Facility:', 'Orthopedic Care Clinic'],
    ]

    t = Table(data, colWidths=[1.8*inch, 2.2*inch, 1.8*inch, 2.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e0e7ff')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("INCIDENT & MEDICAL DETAILS", styles['Heading2']))
    story.append(Spacer(1, 0.1*inch))

    injury_text = """
    <b>Incident Description:</b><br/>
    Employee lifting 45-50 lbs box from lower shelf to upper shelf without assistance.
    Experienced sharp pain in lower back. Felt something "pop" in back. Unable to continue working.<br/><br/>

    <b>Medical Evaluation:</b><br/>
    Muscle guarding in lumbar region, positive straight leg raise test, limited ROM.
    MRI pending. Initial diagnosis: acute lumbar strain with possible disc herniation.
    """

    story.append(Paragraph(injury_text, styles['Normal']))

    doc.build(story)
    print("Generated: 04_workers_comp_injury_claim.pdf")

def generate_liability_claim():
    """Liability Insurance Claim - Property Damage"""
    doc = SimpleDocTemplate("insurance_claims/05_liability_property_claim.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("LIABILITY INSURANCE CLAIM FORM",
                          ParagraphStyle('Title', parent=styles['Heading1'], fontSize=16,
                                       textColor=colors.HexColor('#1e40af'), alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))

    # Structured data
    data = [
        ['Claim Number:', 'LIB-2026-33456', 'Date of Incident:', '2026-09-14'],
        ['Insured:', 'Thomas Builders Inc.', 'Policy #:', 'COM-LIA-567234'],
        ['Claimant:', 'Patricia Reynolds', 'Claim Type:', 'Property Damage - Negligence'],
        ['Loss Location:', Paragraph('2301 Oak Street, Apartment 4B, Portland OR', _wrap_style), 'Date Reported:', '2026-09-14'],
        ['Estimated Liability:', '$5,300', 'Status:', 'Liability Acknowledged'],
    ]

    t = Table(data, colWidths=[1.8*inch, 2.2*inch, 1.8*inch, 2.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e0e7ff')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("LIABILITY & DAMAGES DOCUMENTATION", styles['Heading2']))
    story.append(Spacer(1, 0.1*inch))

    liability_text = """
    <b>Incident Description:</b><br/>
    Construction crew removing aluminum siding fell from 4th floor scaffolding, damaging
    patio awning and furniture below. No personal injury but significant property damage.<br/><br/>

    <b>Damage Assessment:</b><br/>
    Retractable awning: 4-foot tear through fabric canopy. Replacement: $4,200<br/>
    Patio furniture: 2 chairs damaged. Replacement: $1,100<br/>
    Total claimed: $5,300
    """

    story.append(Paragraph(liability_text, styles['Normal']))

    doc.build(story)
    print("Generated: 05_liability_property_claim.pdf")

def generate_remaining_claims():
    """Generate remaining 5 claims (simplified for brevity)"""
    # Rental damage claim
    doc = SimpleDocTemplate("insurance_claims/06_rental_damage_claim.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    story.append(Paragraph("RENTAL PROPERTY DAMAGE CLAIM",
                          ParagraphStyle('Title', parent=styles['Heading1'], fontSize=16,
                                       textColor=colors.HexColor('#1e40af'), alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))
    data = [
        ['Claim #:', 'REN-2026-22145', 'Property:', '1823 Riverside Apt 201'],
        ['Landlord:', 'Cascade Property Mgmt', 'Tenant:', 'Marcus Williams'],
        ['Move-Out:', '2026-09-13', 'Damage Type:', 'Excessive Wear'],
        ['Claim Amount:', '$6,850', 'Deposit Held:', '$2,000'],
    ]
    t = Table(data, colWidths=[1.75*inch, 1.75*inch, 1.75*inch, 1.75*inch])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e0e7ff')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)]))
    story.append(t)
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Damage includes: carpet stains, burn marks, wall damage, cabinet damage. Kitchen countertop stained beyond repair.", styles['Normal']))
    doc.build(story)
    print("Generated: 06_rental_damage_claim.pdf")

    # Travel insurance claim
    doc = SimpleDocTemplate("insurance_claims/07_travel_trip_claim.pdf", pagesize=letter)
    story = []
    story.append(Paragraph("TRAVEL INSURANCE CLAIM",
                          ParagraphStyle('Title', parent=styles['Heading1'], fontSize=16,
                                       textColor=colors.HexColor('#1e40af'), alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))
    data = [
        ['Claim #:', 'TRV-2026-44789', 'Insured:', 'Jennifer Lopez'],
        ['Trip:', 'Japan 09/12-09/26', 'Trip Cost:', '$4,200'],
        ['Trigger:', 'Family Medical Emergency', 'Father Status:', 'Stroke - ICU'],
        ['Cancellation Date:', '2026-09-11', 'Days Before Trip:', '1 day'],
    ]
    t = Table(data, colWidths=[1.75*inch, 1.75*inch, 1.75*inch, 1.75*inch])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e0e7ff')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)]))
    story.append(t)
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Father suffered severe stroke. Medical certification provided. All documentation included.", styles['Normal']))
    doc.build(story)
    print("Generated: 07_travel_trip_claim.pdf")

    # Dental claim
    doc = SimpleDocTemplate("insurance_claims/08_dental_major_claim.pdf", pagesize=letter)
    story = []
    story.append(Paragraph("DENTAL INSURANCE CLAIM",
                          ParagraphStyle('Title', parent=styles['Heading1'], fontSize=16,
                                       textColor=colors.HexColor('#1e40af'), alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))
    data = [
        ['Claim #:', 'DEN-2026-67234', 'Member:', 'Karen Anderson'],
        ['Treatment:', 'Crown & Root Canal', 'Tooth:', '#14 Upper Right Molar'],
        ['Total Charges:', '$1,890', 'Est. Insurance:', '$1,103'],
        ['Status:', 'Completed', 'Member Copay:', '$795'],
    ]
    t = Table(data, colWidths=[1.75*inch, 1.75*inch, 1.75*inch, 1.75*inch])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e0e7ff')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)]))
    story.append(t)
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Root canal therapy 09/10/26, permanent ceramic crown 09/17/26. Successful treatment with good prognosis.", styles['Normal']))
    doc.build(story)
    print("Generated: 08_dental_major_claim.pdf")

    # Life insurance claim
    doc = SimpleDocTemplate("insurance_claims/09_life_death_claim.pdf", pagesize=letter)
    story = []
    story.append(Paragraph("LIFE INSURANCE CLAIM - DEATH BENEFIT",
                          ParagraphStyle('Title', parent=styles['Heading1'], fontSize=16,
                                       textColor=colors.HexColor('#1e40af'), alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))
    data = [
        ['Claim #:', 'LIF-2026-89012', 'Policy #:', 'LIFE-678901-L'],
        ['Deceased:', 'William Peterson', 'DOD:', '2026-09-06'],
        ['Beneficiary:', 'Susan Peterson (Spouse)', 'Relationship:', 'Spouse (28 yrs)'],
        ['Death Benefit:', '$500,000', 'Cause:', 'Heart Attack (STEMI)'],
    ]
    t = Table(data, colWidths=[1.75*inch, 1.75*inch, 1.75*inch, 1.75*inch])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e0e7ff')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)]))
    story.append(t)
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Natural death from acute MI. Full autopsy. No policy exclusions apply. Beneficiary verified.", styles['Normal']))
    doc.build(story)
    print("Generated: 09_life_death_claim.pdf")

    # Pet insurance claim
    doc = SimpleDocTemplate("insurance_claims/10_pet_vet_claim.pdf", pagesize=letter)
    story = []
    story.append(Paragraph("PET INSURANCE CLAIM - VETERINARY CARE",
                          ParagraphStyle('Title', parent=styles['Heading1'], fontSize=16,
                                       textColor=colors.HexColor('#1e40af'), alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))
    data = [
        ['Claim #:', 'PET-2026-55678', 'Pet:', 'Maximus (Golden Retriever)'],
        ['Age:', '8 years old', 'DOB:', '2018-05-12'],
        ['Condition:', 'ACL Repair (Orthopedic)', 'Facility:', 'Riverside Vet Hospital'],
        ['Total Charges:', '$4,320', 'Deductible:', '$250'],
    ]
    t = Table(data, colWidths=[1.75*inch, 1.75*inch, 1.75*inch, 1.75*inch])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e0e7ff')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)]))
    story.append(t)
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("TPLO surgical repair for torn ACL. Surgery 09/01/26. Recovery progressing well. Full recovery expected in 6-8 weeks.", styles['Normal']))
    doc.build(story)
    print("Generated: 10_pet_vet_claim.pdf")

print("\nGenerating 10 Insurance Claims PDFs...\n")
generate_auto_claim()
generate_health_claim()
generate_home_damage_claim()
generate_workers_comp_claim()
generate_liability_claim()
generate_remaining_claims()

print("\nAll 10 PDFs generated successfully!")
print("Location: insurance_claims/")
