def basic_summary_prompt(article):
    return f"""
    Summarize the following:
    {article}
"""

def structured_summary_prompt(article):
    return f"""
Summarize the following article.

Instructions:
- Write exactly 5 bullet points.
- Use simple English.
- Include the most important information.
- Avoid unnecessary details.

Article:
{article}
"""

def role_based_summary_prompt(article):
    return f"""
You are an experienced AI researcher.

Summarize the following article for a beginner
who wants to understand Artificial Intelligence.

Instructions:
- Explain the important concepts clearly.
- Include AI, Machine Learning, Deep Learning, and Generative AI.
- Mention important challenges of AI.
- Use simple English.
- Keep the summary concise.

Article:
{article}
"""