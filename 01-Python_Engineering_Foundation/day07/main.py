from student_scores import calculate_average

def main()-> None:
    """Run the test score utility"""
    scores = [80, 90, 100]
    # scores = []
    try:
        average = calculate_average(scores)
        print(f"Student scores: {scores}")
        print(f"Average score: {average}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__=='__main__':
    main()