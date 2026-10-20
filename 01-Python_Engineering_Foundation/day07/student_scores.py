def calculate_average(scores: list[float]) -> float:
    """Calculate the average of a list of scores"""
    if not scores:
        raise ValueError("Scores cannot be empty.")

    if any(not isinstance(score, (int, float)) or isinstance(score, bool) for score in scores):
        raise ValueError("All scores must be numbers.")

    return sum(scores) / len(scores)