from pathlib import Path
from prompts.summarization_prompts import (
    basic_summary_prompt,
    structured_summary_prompt,
    role_based_summary_prompt
)

from data.sample_summaries import (
    basic_summary,
    role_based_summary,
    structured_summary
)

from evaluation.summary_evaluator import (
    count_bullet_points,
    check_bullet_count,
    check_word_limit,
    check_required_keywords
)

def load_article():
    """Load the sample article from the data directory."""
    article_path = Path(__file__).parent / "data" / "article.txt"

    return article_path.read_text(encoding="utf-8")

def generate_prompts(article):
    """Generate three different summarization prompts."""
    return {
        "Basic Summarization": basic_summary_prompt(article),
        "Structured Summarization": structured_summary_prompt(article),
        "Role-Based Summarization": role_based_summary_prompt(article)
    }

def evaluate_summaries():
    """Evaluate sample summaries using basic quality checks."""

    summaries = {
        "Basic Summary": basic_summary,
        "Structured Summary": structured_summary,
        "Role-Based Summary": role_based_summary
    }

    required_keywords = [
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "Generative AI"
    ]

    for title, summary in summaries.items():
        bullet_count = count_bullet_points(summary)
        has_five_bullets = check_bullet_count(summary, 5)
        within_word_limit = check_word_limit(summary, 100)
        has_required_keywords = check_required_keywords(summary,required_keywords)

        print("\n" + "=" * 60)
        print(f"Evaluation: {title}")
        print("=" * 60)

        print(f"Bullet Points: {bullet_count}")
        print(f"Exactly 5 Bullets: {has_five_bullets}")
        print(f"Within 100 Words: {within_word_limit}")
        print(f"Contains Required Keywords: {has_required_keywords}")

def main():
    """Run the prompt comparison application."""
    article = load_article()
    prompts = generate_prompts(article)

    for title, prompt in prompts.items():
        print("\n" + "=" * 60)
        print(title)
        print("=" * 60)
        print(prompt)

    evaluate_summaries()

if __name__ == "__main__":
    main()
