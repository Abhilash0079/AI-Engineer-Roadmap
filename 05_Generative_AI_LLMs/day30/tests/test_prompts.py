from prompts.summarization_prompts import (
    basic_summary_prompt,
    structured_summary_prompt,
    role_based_summary_prompt
)

from evaluation.summary_evaluator import (
    count_bullet_points,
    check_bullet_count,
    check_word_limit,
    check_required_keywords
)


SAMPLE_ARTICLE = "Artificial Intelligence helps businesses."


def test_basic_summary_prompt():
    prompt = basic_summary_prompt(SAMPLE_ARTICLE)

    assert "Summarize" in prompt
    assert SAMPLE_ARTICLE in prompt


def test_structured_summary_prompt():
    prompt = structured_summary_prompt(SAMPLE_ARTICLE)

    assert "exactly 5 bullet points" in prompt
    assert "simple English" in prompt
    assert SAMPLE_ARTICLE in prompt


def test_role_based_summary_prompt():
    prompt = role_based_summary_prompt(SAMPLE_ARTICLE)

    assert "experienced AI researcher" in prompt
    assert "beginner" in prompt
    assert SAMPLE_ARTICLE in prompt


def test_all_prompts_are_different():
    prompts = [
        basic_summary_prompt(SAMPLE_ARTICLE),
        structured_summary_prompt(SAMPLE_ARTICLE),
        role_based_summary_prompt(SAMPLE_ARTICLE)
    ]

    assert len(set(prompts)) == 3


def test_count_bullet_points():
    summary = """
    - AI automates tasks.
    - ML learns patterns.
    - Deep Learning uses neural networks.
    """

    assert count_bullet_points(summary) == 3


def test_check_bullet_count():
    summary = """
    - First point.
    - Second point.
    - Third point.
    """

    assert check_bullet_count(summary, 3) is True
    assert check_bullet_count(summary, 5) is False


def test_check_word_limit():
    summary = "AI helps businesses improve decisions."

    assert check_word_limit(summary, 10) is True
    assert check_word_limit(summary, 4) is False


def test_count_bullet_points_with_mixed_markers():
    summary = """
    - First point.
    * Second point.
    • Third point.
    Normal paragraph.
    """

    assert count_bullet_points(summary) == 3


def test_check_required_keywords():
    summary = """
    Artificial Intelligence includes Machine Learning,
    Deep Learning, and Generative AI.
    """

    required_keywords = [
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "Generative AI"
    ]

    assert check_required_keywords(summary, required_keywords) is True

    assert check_required_keywords(
        summary,
        ["Artificial Intelligence", "Robotics"]
    ) is False