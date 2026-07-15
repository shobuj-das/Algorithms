# count full, blank, half star from rating

def start_count(rating):
    max_rating = 5.0
    full_star = int(rating)
    blank_star = int(max_rating - rating)

    print(f"Full star: {full_star}")
    print(f"Blank star: {blank_star}")

    if (full_star + blank_star) != max_rating:
        print("Half star: 1")


if __name__=="__main__":
    start_count(0.9)
