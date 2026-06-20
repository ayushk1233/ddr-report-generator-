# DDR Report Generator

AI-powered Diagnostic Damage Report (DDR) Generator that transforms inspection reports and thermal imaging reports into structured, evidence-backed property diagnostic reports.

## Assignment Context

This project was developed as part of a technical assessment with an intended completion window of approximately 24 hours.

Given the time constraint, the primary focus was placed on:

* Building a complete end-to-end working pipeline
* Ensuring extraction accuracy and traceability
* Generating structured diagnostic reports
* Correlating inspection evidence with thermal evidence
* Producing a professional PDF report suitable for review

The goal was to prioritize correctness, explainability, and maintainability over extensive feature expansion.

---

## Features

### PDF Processing

* Inspection PDF ingestion
* Thermal PDF ingestion
* Multi-page document processing
* Image extraction and preservation

### Observation Extraction

* Detection of impacted areas
* Issue identification
* Observation structuring
* Area-level grouping

### Thermal Analysis

* Hotspot extraction
* Coldspot extraction
* Thermal anomaly detection
* Thermal image association
* Visible image association

### Evidence Correlation

* Inspection image mapping
* Thermal image mapping
* Area-based evidence bundling
* Evidence traceability

### AI Intelligence Layer

* Executive summary generation
* Root cause analysis
* Severity assessment
* Repair recommendations
* Missing information detection

### Report Generation

* Professional HTML rendering
* PDF export
* Area-wise diagnostic sections
* Embedded inspection images
* Embedded thermal images

---

## Project Structure

```text
├── app/
│   ├── api/
│   ├── core/
│   ├── outputs/
│   ├── schemas/
│   ├── services/
│   │   ├── evidence/
│   │   ├── extraction/
│   │   ├── image/
│   │   ├── llm/
│   │   ├── pipeline/
│   │   ├── reasoning/
│   │   ├── reports/
│   │   └── rules/
│   ├── storage/
│   ├── templates/
│   └── tests/
├── scripts/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## Pipeline Flow

```text
Inspection PDF
        │
        ▼
Observation Extraction
        │
        ▼
Evidence Correlation
        │
        ▼
Thermal Analysis
        │
        ▼
AI Intelligence Layer
        │
        ▼
DDR Report Generation
        │
        ▼
PDF Output
```

---

## Running the Project

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Environment

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_key_here
```

### 5. Run Streamlit Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Example Workflow

1. Upload Inspection Report PDF
2. Upload Thermal Report PDF
3. Start Analysis
4. Pipeline extracts observations and thermal evidence
5. AI generates diagnostics and recommendations
6. Download generated DDR PDF report

---

## Current Limitations

Due to the assessment time constraints, several enhancements were intentionally deferred:

### Thermal Correlation

Current implementation uses area-level thermal attribution.

Future versions would include:

* Automatic thermal-to-observation matching
* Thermal anomaly clustering
* Cross-page thermal reasoning

### Image Attribution

Current image mapping is deterministic and area-based.

Future versions would include:

* Semantic image-to-observation matching
* Vision-language verification
* Confidence-weighted image attribution

### Confidence Scoring

The current report contains confidence indicators but does not yet compute a fully evidence-driven confidence score.

Future versions would calculate confidence using:

* Observation quality
* Evidence completeness
* Thermal validation
* Cross-source consistency

### Report Intelligence

Future improvements:

* Cause-effect correlation matrix
* Source-area identification
* Repair cost estimation
* Risk progression forecasting
* Historical trend tracking

---

## What I Would Build With More Time

If this project were extended beyond the assessment timeline, the next development priorities would be:

### Phase 1

* Automatic thermal area attribution
* Advanced evidence confidence scoring
* Improved diagnostic correlation

### Phase 2

* Vision-language image validation
* Enhanced root cause reasoning
* Structured summary matrix generation

### Phase 3

* Historical inspection comparison
* Retrieval-Augmented Knowledge Base (RAG)
* Multi-property benchmarking

### Phase 4

* Multi-agent diagnostic workflow
* Human-in-the-loop review system
* SaaS deployment and monitoring

---

## Engineering Priorities

The project was intentionally designed around:

* Modularity
* Explainability
* Traceable evidence
* Incremental development
* Production-ready architecture patterns

Every generated conclusion in the report is linked back to extracted observations, images, or thermal findings, allowing reviewers to verify the reasoning process.

---

## Output

The final output is a structured Diagnostic Damage Report (DDR) containing:

* Executive Summary
* Area-wise Findings
* Inspection Evidence
* Thermal Evidence
* Root Cause Analysis
* Recommendations
* Missing Information Summary

Generated as a downloadable PDF report.
