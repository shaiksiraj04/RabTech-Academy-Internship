from pathlib import Path
import re
import pandas as pd

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Image,
    Table,
    TableStyle,
)
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = BASE_DIR / "report"
PLOTS_DIR = BASE_DIR / "plots"
RESULTS_DIR = BASE_DIR / "results"

SOURCE_FILE = REPORT_DIR / "Research_Report.md"
OUTPUT_FILE = REPORT_DIR / "Daily_Demand_Forecasting_Research_Whitepaper.pdf"

RESULTS_FILE = RESULTS_DIR / "task6_final_report_results.csv"


# ============================================================
# LOAD MODEL RESULTS
# ============================================================

results_df = pd.read_csv(RESULTS_FILE)

results_df["MAE"] = results_df["MAE"].round(4)
results_df["RMSE"] = results_df["RMSE"].round(4)
results_df["MAPE (%)"] = results_df["MAPE (%)"].round(2)

best_row = results_df.sort_values("RMSE").iloc[0]

best_model = best_row["Model"]
best_mae = best_row["MAE"]
best_rmse = best_row["RMSE"]
best_mape = best_row["MAPE (%)"]


# ============================================================
# READ MARKDOWN
# ============================================================

markdown_text = SOURCE_FILE.read_text(encoding="utf-8")


# Replace placeholder model table with actual results
table_pattern = re.compile(
    r"\| Model \| MAE \| RMSE \| MAPE \(%\) \|.*?"
    r"\| Gradient Boosting .*?\n",
    re.DOTALL,
)

actual_table = (
    "| Model | MAE | RMSE | MAPE (%) |\n"
    "|---|---:|---:|---:|\n"
)

for _, row in results_df.iterrows():
    actual_table += (
        f"| {row['Model']} | "
        f"{row['MAE']:.4f} | "
        f"{row['RMSE']:.4f} | "
        f"{row['MAPE (%)']:.2f} |\n"
    )

markdown_text = table_pattern.sub(actual_table, markdown_text)

markdown_text = re.sub(
    r"\*\*Selected Model:\*\*.*",
    f"**Selected Model:** {best_model}",
    markdown_text,
)

markdown_text = re.sub(
    r"\*\*MAE:\*\*.*",
    f"**MAE:** {best_mae:.4f}",
    markdown_text,
)

markdown_text = re.sub(
    r"\*\*RMSE:\*\*.*",
    f"**RMSE:** {best_rmse:.4f}",
    markdown_text,
)

markdown_text = re.sub(
    r"\*\*MAPE:\*\*.*",
    f"**MAPE:** {best_mape:.2f}%",
    markdown_text,
)


# ============================================================
# PDF DOCUMENT
# ============================================================

doc = SimpleDocTemplate(
    str(OUTPUT_FILE),
    pagesize=A4,
    rightMargin=38,
    leftMargin=38,
    topMargin=42,
    bottomMargin=42,
)


# ============================================================
# STYLES
# ============================================================

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleCustom",
    parent=styles["Title"],
    fontSize=22,
    leading=28,
    alignment=TA_CENTER,
    spaceAfter=18,
)

subtitle_style = ParagraphStyle(
    "SubtitleCustom",
    parent=styles["Normal"],
    fontSize=13,
    leading=18,
    alignment=TA_CENTER,
    spaceAfter=14,
)

h1_style = ParagraphStyle(
    "H1Custom",
    parent=styles["Heading1"],
    fontSize=16,
    leading=20,
    spaceBefore=9,
    spaceAfter=7,
)

h2_style = ParagraphStyle(
    "H2Custom",
    parent=styles["Heading2"],
    fontSize=12,
    leading=15,
    spaceBefore=7,
    spaceAfter=5,
)

body_style = ParagraphStyle(
    "BodyCustom",
    parent=styles["BodyText"],
    fontSize=9,
    leading=12,
    spaceAfter=5,
)

bullet_style = ParagraphStyle(
    "BulletCustom",
    parent=body_style,
    leftIndent=16,
    firstLineIndent=-8,
    spaceAfter=4,
)

small_style = ParagraphStyle(
    "SmallCustom",
    parent=body_style,
    fontSize=7.5,
    leading=9.5,
)


# ============================================================
# HELPERS
# ============================================================

def clean_inline(text):
    text = text.replace("`", "")
    text = text.replace("**", "")
    text = text.replace("*", "")
    return text.strip()


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.drawCentredString(
        A4[0] / 2,
        25,
        f"Page {doc.page}"
    )
    canvas.restoreState()


def add_image(path, width=6.4 * inch):
    if not path.exists():
        return []

    from PIL import Image as PILImage

    with PILImage.open(path) as img:
        img_width, img_height = img.size

    height = width * img_height / img_width

    # Prevent oversized figures
    max_height = 5.8 * inch
    if height > max_height:
        height = max_height
        width = height * img_width / img_height

    return [
        Image(str(path), width=width, height=height),
        Spacer(1, 10),
    ]


# ============================================================
# BUILD STORY
# ============================================================

story = []

# ------------------------------------------------------------
# COVER PAGE
# ------------------------------------------------------------

story.append(Spacer(1, 0.8 * inch))

story.append(
    Paragraph(
        "DATA SCIENCE RESEARCH REPORT",
        title_style,
    )
)

story.append(
    Paragraph(
        "Daily Demand Forecasting Using Statistical and Machine Learning Models",
        subtitle_style,
    )
)

story.append(Spacer(1, 0.3 * inch))

story.append(
    Paragraph(
        "<b>Research Capstone & Whitepaper</b>",
        subtitle_style,
    )
)

story.append(Spacer(1, 0.3 * inch))

story.append(
    Paragraph(
        "<b>Research Question</b><br/><br/>"
        "<i>How effectively can statistical time-series and machine learning "
        "models predict future daily demand, and which approach provides "
        "the most reliable predictive performance?</i>",
        ParagraphStyle(
            "CoverQuestion",
            parent=body_style,
            alignment=TA_CENTER,
            fontSize=11,
            leading=17,
        ),
    )
)

story.append(Spacer(1, 0.5 * inch))

story.append(
    Paragraph(
        "<b>RabTech Academy Internship</b><br/>"
        "Data Science Research Capstone<br/><br/>"
        "Python • Pandas • NumPy • Scikit-learn • Statsmodels<br/>"
        "Matplotlib • Seaborn",
        ParagraphStyle(
            "CoverInfo",
            parent=body_style,
            alignment=TA_CENTER,
            fontSize=10,
            leading=16,
        ),
    )
)

story.append(Spacer(1, 1.2 * inch))

story.append(
    Paragraph(
        "Research Type: Predictive Modeling & Forecasting",
        ParagraphStyle(
            "CoverBottom",
            parent=body_style,
            alignment=TA_CENTER,
            fontSize=10,
        ),
    )
)

story.append(PageBreak())


# ------------------------------------------------------------
# TABLE OF CONTENTS
# ------------------------------------------------------------

story.append(Paragraph("Table of Contents", h1_style))

toc_items = [
    "Abstract",
    "1. Introduction",
    "2. Research Question and Objectives",
    "3. Background and Literature Review",
    "4. Dataset and Data Methodology",
    "5. Exploratory Data Analysis",
    "6. Time-Series Analysis",
    "7. Predictive Modeling",
    "8. Model Performance and Results",
    "9. Future Demand Forecast and Business Implications",
    "10. Limitations and Future Research",
    "11. Conclusion",
    "12. References",
]

for item in toc_items:
    story.append(Paragraph(item, body_style))

story.append(PageBreak())


# ============================================================
# PARSE MARKDOWN
# ============================================================

lines = markdown_text.splitlines()

skip_cover = True
inside_table = False
table_rows = []

for line in lines:

    stripped = line.strip()

    # Ignore HTML cover content from markdown source
    if stripped.startswith("<div"):
        skip_cover = True
        continue

    if skip_cover and stripped.startswith("</div>"):
        skip_cover = False
        continue

    if skip_cover:
        continue

    if not stripped:
        if inside_table:
            inside_table = False

            if table_rows:
                formatted_rows = []

                for row in table_rows:
                    formatted_rows.append(
                        [
                            Paragraph(
                                clean_inline(cell),
                                small_style,
                            )
                            for cell in row
                        ]
                    )

                table = Table(
                    formatted_rows,
                    repeatRows=1,
                    hAlign="LEFT",
                )

                table.setStyle(
                    TableStyle(
                        [
                            (
                                "BACKGROUND",
                                (0, 0),
                                (-1, 0),
                                colors.HexColor("#D9EAF7"),
                            ),
                            (
                                "TEXTCOLOR",
                                (0, 0),
                                (-1, 0),
                                colors.black,
                            ),
                            (
                                "GRID",
                                (0, 0),
                                (-1, -1),
                                0.5,
                                colors.grey,
                            ),
                            (
                                "VALIGN",
                                (0, 0),
                                (-1, -1),
                                "TOP",
                            ),
                            (
                                "LEFTPADDING",
                                (0, 0),
                                (-1, -1),
                                5,
                            ),
                            (
                                "RIGHTPADDING",
                                (0, 0),
                                (-1, -1),
                                5,
                            ),
                            (
                                "TOPPADDING",
                                (0, 0),
                                (-1, -1),
                                5,
                            ),
                            (
                                "BOTTOMPADDING",
                                (0, 0),
                                (-1, -1),
                                5,
                            ),
                        ]
                    )
                )

                story.append(table)
                story.append(Spacer(1, 10))
                table_rows = []

        continue

    # Markdown table
    if stripped.startswith("|"):
        cells = [
            cell.strip()
            for cell in stripped.strip("|").split("|")
        ]

        # Ignore separator row
        if all(
            re.fullmatch(r":?-+:?", cell.replace(" ", ""))
            for cell in cells
        ):
            continue

        inside_table = True
        table_rows.append(cells)
        continue

    # Images
    image_match = re.match(
        r"!\[(.*?)\]\((.*?)\)",
        stripped,
    )

    if image_match:
        image_path = image_match.group(2)

        if image_path.startswith("../plots/"):
            full_path = BASE_DIR / image_path.replace("../", "")
        else:
            full_path = REPORT_DIR / image_path

        story.extend(add_image(full_path))
        continue

    # H1
    if stripped.startswith("# "):
        text = clean_inline(stripped[2:])
        story.append(Paragraph(text, h1_style))
        continue

    # H2
    if stripped.startswith("## "):
        text = clean_inline(stripped[3:])
        story.append(Paragraph(text, h2_style))
        continue

    # H3
    if stripped.startswith("### "):
        text = clean_inline(stripped[4:])
        story.append(
            Paragraph(
                text,
                ParagraphStyle(
                    "H3",
                    parent=h2_style,
                    fontSize=11,
                    leading=15,
                ),
            )
        )
        continue

    # Horizontal rule
    if stripped == "---":
        story.append(Spacer(1, 8))
        continue

    # Bullets
    if stripped.startswith("- "):
        text = clean_inline(stripped[2:])
        story.append(
            Paragraph(
                f"• {text}",
                bullet_style,
            )
        )
        continue

    # Numbered list
    numbered = re.match(r"^\d+\.\s+(.*)", stripped)

    if numbered:
        story.append(
            Paragraph(
                clean_inline(stripped),
                bullet_style,
            )
        )
        continue

    # Regular paragraph
    text = clean_inline(stripped)

    if text:
        story.append(
            Paragraph(
                text,
                body_style,
            )
        )


# ============================================================
# FINAL BUILD
# ============================================================

doc.build(
    story,
    onFirstPage=add_page_number,
    onLaterPages=add_page_number,
)

print("=" * 60)
print("WHITEPAPER GENERATED SUCCESSFULLY")
print("=" * 60)
print(f"PDF: {OUTPUT_FILE}")
print(f"Selected Model: {best_model}")
print(f"MAE: {best_mae:.4f}")
print(f"RMSE: {best_rmse:.4f}")
print(f"MAPE: {best_mape:.2f}%")
print("=" * 60)