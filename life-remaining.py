import pandas as pd
from lost_years import lost_years_who

YEAR = 2026
COUNTRY = "USA"
AGES = range(5, 86, 5)  # 5, 10, ..., 85


def compute_life_expectancy(sex: str, verbose: bool = True):
    """Compute and print WHO life expectancy for a given sex and age range.

    Args:
        sex (str): 'M' for male, 'F' for female.
        verbose (bool): If True, print full version with total lifespan.
    """
    # Build DataFrame for all ages
    df = pd.DataFrame(
        [{"age": age, "sex": sex, "year": YEAR, "country": COUNTRY} for age in AGES]
    )

    # Get WHO life expectancy
    results = lost_years_who(df)

    # Remove duplicates by averaging multiple matches for the same age
    results = results.groupby(["age", "sex"], as_index=False).mean(numeric_only=True)

    # Print nicely formatted table
    for _, row in results.iterrows():
        age = int(row["age"])
        remaining = float(row["who_life_expectancy"])
        total = age + remaining
        perc_remaining = remaining / total * 100
        perc_lived = 100 - perc_remaining

        if verbose:
            print(
                f"{sex.title()} Age {age:2}: "
                f"Expected lifespan {total:2.0f} yrs; "
                f"Years left {remaining:2.0f}; "
                f"{perc_remaining:2.0f}% life remaining, "
                f"{perc_lived:2.0f}% already lived"
            )
        else:
            print(
                f"{sex.title()} Age {age:2}: "
                f"Years left {remaining:2.0f}; "
                f"{perc_remaining:2.0f}% life remaining"
            )


def show_life_progress():
    # Validate sex input
    while True:
        sex = input("Enter sex (M/F): ").strip().upper()
        if sex in ("M", "F"):
            break
        print("Invalid input. Please enter M or F.")

    # Validate age input
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 <= age <= 120:
                break
            else:
                print("Please enter an age between 0 and 120.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    df = pd.DataFrame([{"age": age, "sex": sex, "year": YEAR, "country": COUNTRY}])

    results = lost_years_who(df)
    results = results.groupby(["age", "sex"], as_index=False).mean(numeric_only=True)

    row = results.iloc[0]

    remaining = float(row["who_life_expectancy"])
    total = age + remaining

    perc_remaining = remaining / total * 100
    perc_lived = 100 - perc_remaining

    bar_length = 40
    lived_blocks = round(bar_length * perc_lived / 100)
    remaining_blocks = bar_length - lived_blocks

    bar = "⣿" * lived_blocks + "⣀" * remaining_blocks

    sex_label = "Male" if sex == "M" else "Female"

    print()
    print(f"You are {sex_label} Age {age}.")
    print()
    print(f"Expected lifespan : {total:.0f} years ({total * 12:.0f} months)")
    print(f"Life remaining    : {remaining:.0f} years ({remaining * 12:.0f} months)")
    print(f"Life already lived: {age:.0f} years ({age * 12:.0f} months)")
    print()
    print("Life progress:")
    print()
    print(f"[{bar}]")
    print()
    print(f"{perc_lived:.0f}% already lived, {perc_remaining:.0f}% life remaining")


if __name__ == "__main__":
    print("Male life expectancy (WHO life tables, verbose):")
    compute_life_expectancy("M", verbose=True)

    print("\nFemale life expectancy (WHO life tables, verbose):")
    compute_life_expectancy("F", verbose=True)

    print("\nMale life expectancy (WHO life tables, short):")
    compute_life_expectancy("M", verbose=False)

    print("\nFemale life expectancy (WHO life tables, short):")
    compute_life_expectancy("F", verbose=False)

    print("\n--- Your Life Progress ---")
    show_life_progress()
