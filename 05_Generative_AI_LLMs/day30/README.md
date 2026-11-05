# Day 30 — Prompt Design

## Project Overview

This project demonstrates how different prompt engineering techniques affect the instructions given to a Large Language Model (LLM).

It builds a modular prompt comparison application that generates three different summarization prompts and evaluates sample summaries using rule-based evaluation functions.

## Learning Objectives

- Understand prompt engineering fundamentals.
- Learn zero-shot, one-shot, and few-shot prompting.
- Understand role-based prompting.
- Learn how instructions, context, examples, and output constraints improve prompts.
- Compare basic, structured, and role-based summarization prompts.
- Implement simple rule-based summary evaluation.
- Understand the limitations of automated evaluation.

## Project Features

### 1. Prompt Generation

Three summarization prompt styles:

- **Basic Summarization:** A simple summarization instruction.
- **Structured Summarization:** Specifies five bullet points, simple English, and important information.
- **Role-Based Summarization:** Assigns an AI researcher role and provides audience and content requirements.

### 2. Summary Evaluation

The evaluation module checks:

- Number of bullet points.
- Whether the summary contains exactly five bullet points.
- Whether the summary stays within a specified word limit.
- Whether all required keywords appear in the summary.

### 3. Sample Summaries

Three predefined sample summaries are used to demonstrate how the evaluation functions work.

**Note:** The application currently generates prompts and evaluates predefined summaries. It does not call an external LLM API or generate actual LLM responses.

## Project Structure

```text
day30/
│
├── data/
│   ├── article.txt
│   └── sample_summaries.py
│
├── evaluation/
│   ├── __init__.py
│   └── summary_evaluator.py
│
├── prompts/
│   ├── __init__.py
│   └── summarization_prompts.py
│
├── tests/
│   └── test_prompts.py
│
├── main.py
├── README.md
└── INTERVIEW_NOTES.md
```

## Technologies Used

- Python
- Pytest
- pathlib
- Python modules and packages

No external LLM API or additional third-party dependency is required.

## Setup and Installation

Activate the existing project virtual environment from the roadmap root:

```powershell
.\venv\Scripts\Activate.ps1
```

Navigate to the Day 30 directory:

```powershell
cd 05_Generative_AI_LLMs\day30
```

## Run the Application

```powershell
python main.py
```

The application displays the three prompt designs and evaluates the predefined sample summaries.

## Run Tests

```powershell
python -m pytest tests/test_prompts.py -v
```

The test suite verifies prompt generation, prompt differences, bullet-point counting, word limits, and required-keyword checks.

## Evaluation Limitations

The current evaluator uses simple rule-based checks.

It does not determine:

- Whether the summary is factually correct.
- Whether important information has been omitted.
- Whether the summary preserves the article's meaning.
- Whether the summary is readable or useful.
- Whether the LLM has hallucinated information.

Keyword matching checks exact phrases and does not understand synonyms or semantic similarity.

A more advanced evaluation system could include factual consistency, semantic similarity, completeness, and human review.

## Key Learning

Effective prompts clearly communicate the task, provide relevant context, define constraints, and specify the expected output.

Prompt evaluation is important because a prompt that produces a correctly formatted response may still produce inaccurate or incomplete information.
