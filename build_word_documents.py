"""
Build 5 separate, simple, clean Word documents (CO1 to CO5).
Style: Simple, black-and-white, no colors.
Contains:
  - Header block with Student Name: SASIVARNAN SJ and Register Number: 1912260058
  - Course Outcome Title
  - For each task/question:
      - Title / Objective
      - Complete Source Code
      - Pasted Output Screenshot
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

BASE_DIR = r"c:\Users\Admin\OneDrive\Documents\PYTHON"

STUDENT_NAME = "SASIVARNAN SJ"
REGISTER_NO = "1912260058"
COURSE_NAME = "CSA08 – Python Programming"

CO_METADATA = [
    {
        "co_id": "CO1",
        "doc_filename": "CSA08_CO1_Assignment.docx",
        "title": "COURSE OUTCOME 1 (CO1)",
        "subtitle": "Interactive and Script Modes, Values, Types, Variables, Expressions, Functions and Modules",
        "folder": "CO1_Programs",
        "items": [
            {
                "num": "Task 1",
                "title": "Understand the Problem and Identify the Data",
                "script": "CO1_Task1_UnderstandProblemData.py",
                "screenshot": "screenshot_co1_task1_understand_problem_data.png",
                "desc": "Identifies and categorizes all data elements (inputs, outputs, constants, rate card parameters), specifies type constraints and ranges, and evaluates storage models (parallel lists vs composite delivery records) for 300 village farmers."
            },
            {
                "num": "Task 2",
                "title": "Explore Values, Types, and Decimal Precision",
                "script": "CO1_Task2_ValuesTypes.py",
                "screenshot": "screenshot_co1_task2_values_types.png",
                "desc": "Demonstrates Python type inspection, integer vs float division behaviors, IEEE-754 floating-point inaccuracies, and exact monetary calculations using the Decimal module."
            },
            {
                "num": "Task 4",
                "title": "Milk Rate Card Expressions & Step Formulations",
                "script": "CO1_Task4_RateExpressions.py",
                "screenshot": "screenshot_co1_task4_rate_expressions.png",
                "desc": "Implements arithmetic expressions for calculating Fat and SNF steps relative to base parameters and computes per-litre rates with proper operator precedence."
            },
            {
                "num": "Task 7",
                "title": "Reusable Module Architecture (milkrate.py)",
                "script": "CO1_Task7_MilkrateModule.py",
                "screenshot": "screenshot_co1_task7_milkrate_module.png",
                "desc": "Modularizes milk rate evaluation and payout logic into reusable standalone functions with an automated self-test routine."
            },
            {
                "num": "Task 9",
                "title": "Village Milk Co-operative Payment Calculator & Validation",
                "script": "CO1_Task9_PaymentCalculator.py",
                "screenshot": "screenshot_co1_task9_payment_calculator.png",
                "desc": "Implements boundary validation for milk deliveries (litres, fat%, SNF%), generates formatted shift payout slips, and totals 10-day settlement balances."
            },
            {
                "num": "Task 10",
                "title": "Performance and Cumulative Rounding Analysis (Float vs Decimal)",
                "script": "CO1_Task10_FloatVsDecimal.py",
                "screenshot": "screenshot_co1_task10_float_vs_decimal.png",
                "desc": "Compares execution times and cumulative financial deviations between float and Decimal types across scales of 300, 6,000, and 150,000 transactions."
            }
        ]
    },
    {
        "co_id": "CO2",
        "doc_filename": "CSA08_CO2_Assignment.docx",
        "title": "COURSE OUTCOME 2 (CO2)",
        "subtitle": "Control Flow Constructs, String Manipulations, Functions, Scope and Recursion",
        "folder": "CO2_Programs",
        "items": [
            {
                "num": "Question 1",
                "title": "Decisions with Many Boundaries: Electricity Subsidy Eligibility",
                "script": "CO2_Q1_ElectricitySubsidy.py",
                "screenshot": "screenshot_co2_q1_electricity_subsidy.png",
                "desc": "Evaluates household electricity subsidy tiers using chained conditional comparisons across multiple threshold boundaries and senior citizen exemptions."
            },
            {
                "num": "Question 2",
                "title": "Loops that Count Attempts: Bank Kiosk OTP Verification",
                "script": "CO2_Q2_BankOTPAttempts.py",
                "screenshot": "screenshot_co2_q2_bank_otp_attempts.png",
                "desc": "Simulates bank kiosk authentication allowing 3 attempts, ignoring blank inputs without consuming tries, and triggering an account lock upon failure."
            },
            {
                "num": "Question 3",
                "title": "Vehicle Registration Number Validator (Pure String Methods)",
                "script": "CO2_Q3_VehiclePlateValidator.py",
                "screenshot": "screenshot_co2_q3_vehicle_plate_validator.png",
                "desc": "Validates state, district, series, and number plate formats using string slicing and character classification methods without regular expressions."
            },
            {
                "num": "Question 4",
                "title": "Building Long Text Performance Benchmark ('+=' vs 'str.join()')",
                "script": "CO2_Q4_StringConcatBenchmark.py",
                "screenshot": "screenshot_co2_q4_string_concat_benchmark.png",
                "desc": "Benchmarks string concatenation algorithms over 100,000 billing statement lines to demonstrate O(n) vs O(n^2) time complexity caused by string immutability."
            },
            {
                "num": "Question 5",
                "title": "Functions, Parameters and Scope: Mutable Default Argument Trap",
                "script": "CO2_Q5_CanteenMutableDefault.py",
                "screenshot": "screenshot_co2_q5_canteen_mutable_default.png",
                "desc": "Demonstrates the persistent default mutable argument trap in Python function definitions and implements the idiomatic None default sentinel fix."
            },
            {
                "num": "Question 6",
                "title": "Recursion and Its Limits: Temple Steps Climbing with Memoisation",
                "script": "CO2_Q6_ClimbingStepsRecursion.py",
                "screenshot": "screenshot_co2_q6_climbing_steps_recursion.png",
                "desc": "Analyzes recursive call trees and function call overhead, demonstrating dramatic performance optimization and stack safety using functools.lru_cache."
            }
        ]
    },
    {
        "co_id": "CO3",
        "doc_filename": "CSA08_CO3_Assignment.docx",
        "title": "COURSE OUTCOME 3 (CO3)",
        "subtitle": "Python Data Structures: Lists, Tuples, Dictionaries, Sets and Comprehensions",
        "folder": "CO3_Programs",
        "items": [
            {
                "num": "Question 1",
                "title": "Lists and Slicing: 365-Day Daily Rainfall Records",
                "script": "CO3_Q1_RainfallSlicing.py",
                "screenshot": "screenshot_co3_q1_rainfall_slicing.png",
                "desc": "Applies list slicing to compute weekly totals, identify wettest and driest weeks, calculate 7-day moving averages, and extract zero-rainfall dry days."
            },
            {
                "num": "Question 2",
                "title": "Tuples, Mutability and Copying: GPS Stops & Grid Aliasing Trap",
                "script": "CO3_Q2_GridAliasingAndCopying.py",
                "screenshot": "screenshot_co3_q2_grid_aliasing_and_copying.png",
                "desc": "Uses immutable tuples as dictionary coordinates, diagnoses the [[0]*cols]*rows list repetition aliasing bug, and contrasts shallow vs deep copying."
            },
            {
                "num": "Question 3",
                "title": "Dictionaries: Kisan Call Centre Complaint Word Frequencies",
                "script": "CO3_Q3_KisanWordFrequencies.py",
                "screenshot": "screenshot_co3_q3_kisan_word_frequencies.png",
                "desc": "Counts complaint keyword occurrences using dictionaries, filters out language stop-words using a set, and identifies the top-k most frequent grievances."
            },
            {
                "num": "Question 4",
                "title": "Sets: Elective Course Registration Clash Detection",
                "script": "CO3_Q4_ElectiveClashSets.py",
                "screenshot": "screenshot_co3_q4_elective_clash_sets.png",
                "desc": "Identifies scheduling clashes and enrollment categories between AI and IoT elective courses using set intersection (&), symmetric difference (^), and difference (-)."
            },
            {
                "num": "Question 5",
                "title": "List Comprehensions: Cold-Storage Vaccine Temperature Monitor",
                "script": "CO3_Q5_VaccineTempComprehensions.py",
                "screenshot": "screenshot_co3_q5_vaccine_temp_comprehensions.png",
                "desc": "Cleans sensor readings streams with conditional list comprehensions, converts units to Fahrenheit, and extracts alarm timestamps outside the 2–8°C safe window."
            },
            {
                "num": "Question 6",
                "title": "Nested Data: Railway Timetable Inverted Station Index",
                "script": "CO3_Q6_RailwayTimetableIndex.py",
                "screenshot": "screenshot_co3_q6_railway_timetable_index.png",
                "desc": "Constructs an inverted multi-level index from nested train timetable dictionaries to provide O(1) station departure enquiries and weekly schedules."
            },
            {
                "num": "Question 7",
                "title": "Contact-Merging Program from First Principles",
                "script": "CO3_Q7_ContactMerging.py",
                "screenshot": "screenshot_co3_q7_contact_merging.png",
                "desc": "Normalizes multi-device phone numbers, resolves duplicates across SIM and phone stores, and consolidates email addresses using set unions."
            }
        ]
    },
    {
        "co_id": "CO4",
        "doc_filename": "CSA08_CO4_Assignment.docx",
        "title": "COURSE OUTCOME 4 (CO4)",
        "subtitle": "File Handling, Custom Exceptions, Modules and Package Architectures",
        "folder": "CO4_Programs",
        "items": [
            {
                "num": "Task 1",
                "title": "File-Processing Design Review: Hostel Mess Bill Totaling",
                "script": "CO4_Task1_MessBillsReview.py",
                "screenshot": "screenshot_co4_task1_mess_bills_review.png",
                "desc": "Refactors legacy file processing into safe context-managed stream processing, validating each record line-by-line and generating an audit log of rejected entries."
            },
            {
                "num": "Task 2 & 3",
                "title": "Biometric Attendance Processing & Custom InvalidRecord Exception",
                "script": "CO4_Task2_BiometricAttendance.py",
                "screenshot": "screenshot_co4_task2_biometric_attendance.png",
                "desc": "Defines custom user exceptions for damaged telemetry lines, calculates percentage attendance, and flags students below the mandatory 75% attendance threshold."
            },
            {
                "num": "Task 4",
                "title": "File Forensics: Overwrite ('w') vs Append ('a') Mode Trap",
                "script": "CO4_Task4_FileForensics.py",
                "screenshot": "screenshot_co4_task4_file_forensics.png",
                "desc": "Investigates file corruption in library logging caused by overwrite mode and proves data preservation using append mode."
            },
            {
                "num": "Task 6",
                "title": "College Fest Multi-Department Registration Pipeline",
                "script": "CO4_Task6_FestRegistration.py",
                "screenshot": "screenshot_co4_task6_fest_registration.png",
                "desc": "Ingests registration files across multiple departments, eliminates duplicate participant records, validates emails without regex, and generates clean master files."
            }
        ]
    },
    {
        "co_id": "CO5",
        "doc_filename": "CSA08_CO5_Assignment.docx",
        "title": "COURSE OUTCOME 5 (CO5)",
        "subtitle": "Data Acquisition, Cleaning, SQLite Database, Visualisation and AI Applications",
        "folder": "CO5_Programs",
        "items": [
            {
                "num": "Task B1",
                "title": "Air Quality Data Acquisition, Cleaning & Min-Max Normalisation",
                "script": "CO5_B1_AirQualityCleaning.py",
                "screenshot": "screenshot_co5_b1_air_quality_cleaning.png",
                "desc": "Parses environmental CSV files, removes sensor anomalies and missing values, converts Fahrenheit to Celsius, and normalizes PM2.5 readings into [0.0, 1.0]."
            },
            {
                "num": "Task B2",
                "title": "SQLite Storage with Parameterized Queries & SQL Injection Defense",
                "script": "CO5_B2_SQLiteDatabase.py",
                "screenshot": "screenshot_co5_b2_sqlite_database.png",
                "desc": "Creates relational tables in SQLite, executes parameterized aggregations with '?' placeholders, and proves immunity against SQL injection payloads."
            },
            {
                "num": "Task B3",
                "title": "Environmental Telemetry Multi-Panel Visualizations (Matplotlib)",
                "script": "CO5_B3_Visualizations.py",
                "screenshot": "screenshot_co5_b3_visualizations.png",
                "extra_image": "co5_air_quality_charts.png",
                "desc": "Generates a 4-panel dashboard containing a daily PM2.5 trend line chart, station mean bar chart, temperature scatter plot, and distribution histogram."
            },
            {
                "num": "Task B4",
                "title": "AI Applications: Sentiment Analysis with Negation & Summarizer",
                "script": "CO5_B4_SentimentAnalysis.py",
                "screenshot": "screenshot_co5_b4_sentiment_analysis.png",
                "desc": "Classifies citizen complaint sentiment using lexicon scoring with negation look-behind and extracts top actionable grievance sentences for municipal review."
            },
            {
                "num": "Task B5",
                "title": "Rule-Based Environmental Telemetry Query Assistant Chatbot",
                "script": "CO5_B5_AirQualityChatbot.py",
                "screenshot": "screenshot_co5_b5_air_quality_chatbot.png",
                "desc": "Implements a domain-specific conversational bot that parses natural language queries and queries station air quality records."
            }
        ]
    }
]

def format_run_black(run, font_name="Calibri", font_size=11, bold=False, italic=False):
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(0, 0, 0)

def add_header_block(doc, co_title, co_subtitle):
    """Simple, clean academic title block (Strictly Black & White, No Colors)."""
    table = doc.add_table(rows=5, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    data = [
        ("Course Name & Code:", COURSE_NAME),
        ("Student Name:", STUDENT_NAME),
        ("Register Number:", REGISTER_NO),
        ("Course Outcome:", co_title),
        ("Focus Areas:", co_subtitle)
    ]

    for i, (k, v) in enumerate(data):
        row = table.rows[i]
        
        # Left cell (Key)
        c0 = row.cells[0]
        c0.width = Inches(2.2)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(2)
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(k)
        format_run_black(r0, font_name="Calibri", font_size=11, bold=True)

        # Right cell (Value)
        c1 = row.cells[1]
        c1.width = Inches(4.3)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(v)
        format_run_black(r1, font_name="Calibri", font_size=11, bold=(i == 1 or i == 2))

    # Add divider line
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_before = Pt(6)
    p_div.paragraph_format.space_after = Pt(14)
    r_div = p_div.add_run("─" * 68)
    format_run_black(r_div, font_name="Calibri", font_size=11, bold=False)

def build_document_for_co(co_spec):
    doc = Document()

    # Page Margins: Standard 1 inch all around
    sections = doc.sections
    for sec in sections:
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.left_margin = Inches(1.0)
        sec.right_margin = Inches(1.0)

    # 1. Header Block
    add_header_block(doc, co_spec["title"], co_spec["subtitle"])

    # 2. Iterate through each task/question
    folder_path = os.path.join(BASE_DIR, co_spec["folder"])
    screenshots_dir = os.path.join(BASE_DIR, "Screenshots")

    for idx, item in enumerate(co_spec["items"]):
        # Task Heading
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(4)
        h.paragraph_format.keep_with_next = True
        r_h = h.add_run(f"{item['num']}: {item['title']}")
        format_run_black(r_h, font_name="Calibri", font_size=13, bold=True)

        # Description
        p_desc = doc.add_paragraph()
        p_desc.paragraph_format.space_before = Pt(0)
        p_desc.paragraph_format.space_after = Pt(6)
        r_desc = p_desc.add_run(f"Description: {item['desc']}")
        format_run_black(r_desc, font_name="Calibri", font_size=10.5, italic=True)

        # Code Subheading
        p_code_lbl = doc.add_paragraph()
        p_code_lbl.paragraph_format.space_before = Pt(4)
        p_code_lbl.paragraph_format.space_after = Pt(2)
        p_code_lbl.paragraph_format.keep_with_next = True
        r_c_lbl = p_code_lbl.add_run(f"Python Source Code ({item['script']}):")
        format_run_black(r_c_lbl, font_name="Calibri", font_size=11, bold=True)

        # Read source code from file
        script_full_path = os.path.join(folder_path, item["script"])
        code_text = ""
        if os.path.exists(script_full_path):
            with open(script_full_path, "r", encoding="utf-8") as f:
                code_text = f.read()
        else:
            code_text = f"# File {item['script']} not found."

        # Insert code block into simple single-cell table for neat formatting
        code_table = doc.add_table(rows=1, cols=1)
        code_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        code_cell = code_table.cell(0, 0)
        code_cell.width = Inches(6.5)

        # Format code text paragraph
        p_code = code_cell.paragraphs[0]
        p_code.paragraph_format.space_before = Pt(2)
        p_code.paragraph_format.space_after = Pt(2)
        p_code.paragraph_format.line_spacing = 1.05
        r_code = p_code.add_run(code_text.strip())
        format_run_black(r_code, font_name="Consolas", font_size=8.5, bold=False)

        # Output Heading
        p_out_lbl = doc.add_paragraph()
        p_out_lbl.paragraph_format.space_before = Pt(10)
        p_out_lbl.paragraph_format.space_after = Pt(4)
        p_out_lbl.paragraph_format.keep_with_next = True
        r_out_lbl = p_out_lbl.add_run("Execution Output Screenshot:")
        format_run_black(r_out_lbl, font_name="Calibri", font_size=11, bold=True)

        # Paste Output Screenshot Image
        img_path = os.path.join(screenshots_dir, item["screenshot"])
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(2)
            p_img.paragraph_format.space_after = Pt(10)
            doc.add_picture(img_path, width=Inches(6.3))
        else:
            p_err = doc.add_paragraph(f"[Screenshot {item['screenshot']} not found]")
            format_run_black(p_err.runs[0], font_name="Calibri", font_size=10, italic=True)

        # If there's an extra visualization image (like CO5 Matplotlib chart)
        if "extra_image" in item:
            extra_img_path = os.path.join(BASE_DIR, item["extra_image"])
            if os.path.exists(extra_img_path):
                p_chart_lbl = doc.add_paragraph()
                p_chart_lbl.paragraph_format.space_before = Pt(6)
                p_chart_lbl.paragraph_format.space_after = Pt(2)
                r_chart_lbl = p_chart_lbl.add_run("Generated Multi-Panel Environmental Dashboard:")
                format_run_black(r_chart_lbl, font_name="Calibri", font_size=11, bold=True)

                p_chart = doc.add_paragraph()
                p_chart.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_chart.paragraph_format.space_before = Pt(2)
                p_chart.paragraph_format.space_after = Pt(10)
                doc.add_picture(extra_img_path, width=Inches(6.3))

        # Add horizontal separator or page break
        if idx < len(co_spec["items"]) - 1:
            p_sep = doc.add_paragraph()
            p_sep.paragraph_format.space_before = Pt(8)
            p_sep.paragraph_format.space_after = Pt(12)
            r_sep = p_sep.add_run("─" * 68)
            format_run_black(r_sep, font_name="Calibri", font_size=11)

    # Save document in root directory
    doc_path = os.path.join(BASE_DIR, co_spec["doc_filename"])
    doc.save(doc_path)
    print(f"Created Word Document: {doc_path} ({os.path.getsize(doc_path):,} bytes)")

    # Also copy to artifact directory
    art_dir = r"C:\Users\Admin\.gemini\antigravity\brain\e9202e20-2e2c-4aeb-91f6-e707a8e7894b"
    if os.path.exists(art_dir):
        import shutil
        shutil.copyfile(doc_path, os.path.join(art_dir, co_spec["doc_filename"]))

def main():
    print(f"Generating 5 simple Word documents for {STUDENT_NAME} ({REGISTER_NO})...")
    for co in CO_METADATA:
        build_document_for_co(co)
    print("\nAll 5 Course Outcome Word documents built successfully!")

if __name__ == "__main__":
    main()
