def count_bullet_points(summary):
    """Counts bullet points in a summary"""
    bullet_markers = ("- ", "* ", "• ")
    return sum(
        1 for line in summary.splitlines()
        if line.strip().startswith(bullet_markers)
    )

def check_bullet_count(summary, expected_count):
    """Check whether the summary has the expected bullet count."""
    actual_count = count_bullet_points(summary)

    return actual_count == expected_count

def check_word_limit(summary, max_words):
    """Chek whether the summary stays within a word limit."""
    return len(summary.split()) <= max_words

def check_required_keywords(summary, required_keywords):
    """Check whether all required keywords appear in a summary."""
    summary_lower = summary.lower()

    return all(
        keyword.lower() in summary_lower
        for keyword in required_keywords
    )