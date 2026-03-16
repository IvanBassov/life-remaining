# Life Remaining Calculator

**life-remaining.py** is a small Python program that displays **remaining life expectancy by age and sex** using WHO life tables.

For each age, the program calculates:

* Expected lifespan
* Years remaining
* Percentage of life remaining
* Percentage of life already lived

The program also includes an interactive mode that shows **your personal life progress** as a visual bar.

The data comes from the Python package **`lost_years`**, which provides access to **WHO life expectancy tables**.

---

## Requirements

Python 3.8 or newer.

Install dependencies:

```
pip install pandas lost-years
```

---

## Running the Program

```
python3 life-remaining.py
```

The program prints life expectancy tables for males and females and then asks for your age and sex to display a personal life progress visualization.

---

## Example Output

```
$ python3 life-remaining.py
Male life expectancy (WHO life tables, verbose):
M Age  5: Expected lifespan 77 yrs; Years left 72; 93% life remaining,  7% already lived
M Age 10: Expected lifespan 77 yrs; Years left 67; 87% life remaining, 13% already lived
M Age 15: Expected lifespan 77 yrs; Years left 62; 80% life remaining, 20% already lived
M Age 20: Expected lifespan 77 yrs; Years left 57; 74% life remaining, 26% already lived
M Age 25: Expected lifespan 77 yrs; Years left 52; 68% life remaining, 32% already lived
M Age 30: Expected lifespan 78 yrs; Years left 48; 61% life remaining, 39% already lived
M Age 35: Expected lifespan 78 yrs; Years left 43; 55% life remaining, 45% already lived
M Age 40: Expected lifespan 79 yrs; Years left 39; 49% life remaining, 51% already lived
M Age 45: Expected lifespan 79 yrs; Years left 34; 43% life remaining, 57% already lived
M Age 50: Expected lifespan 80 yrs; Years left 30; 37% life remaining, 63% already lived
M Age 55: Expected lifespan 81 yrs; Years left 26; 32% life remaining, 68% already lived
M Age 60: Expected lifespan 82 yrs; Years left 22; 27% life remaining, 73% already lived
M Age 65: Expected lifespan 83 yrs; Years left 18; 22% life remaining, 78% already lived
M Age 70: Expected lifespan 85 yrs; Years left 15; 17% life remaining, 83% already lived
M Age 75: Expected lifespan 87 yrs; Years left 12; 13% life remaining, 87% already lived
M Age 80: Expected lifespan 89 yrs; Years left  9; 10% life remaining, 90% already lived
M Age 85: Expected lifespan 91 yrs; Years left  6;  7% life remaining, 93% already lived

Female life expectancy (WHO life tables, verbose):
F Age  5: Expected lifespan 82 yrs; Years left 76; 94% life remaining,  6% already lived
F Age 10: Expected lifespan 82 yrs; Years left 72; 88% life remaining, 12% already lived
F Age 15: Expected lifespan 82 yrs; Years left 67; 82% life remaining, 18% already lived
F Age 20: Expected lifespan 82 yrs; Years left 62; 76% life remaining, 24% already lived
F Age 25: Expected lifespan 82 yrs; Years left 57; 69% life remaining, 31% already lived
F Age 30: Expected lifespan 82 yrs; Years left 52; 63% life remaining, 37% already lived
F Age 35: Expected lifespan 82 yrs; Years left 47; 57% life remaining, 43% already lived
F Age 40: Expected lifespan 83 yrs; Years left 43; 52% life remaining, 48% already lived
F Age 45: Expected lifespan 83 yrs; Years left 38; 46% life remaining, 54% already lived
F Age 50: Expected lifespan 83 yrs; Years left 33; 40% life remaining, 60% already lived
F Age 55: Expected lifespan 84 yrs; Years left 29; 35% life remaining, 65% already lived
F Age 60: Expected lifespan 85 yrs; Years left 25; 29% life remaining, 71% already lived
F Age 65: Expected lifespan 86 yrs; Years left 21; 24% life remaining, 76% already lived
F Age 70: Expected lifespan 87 yrs; Years left 17; 19% life remaining, 81% already lived
F Age 75: Expected lifespan 88 yrs; Years left 13; 15% life remaining, 85% already lived
F Age 80: Expected lifespan 90 yrs; Years left 10; 11% life remaining, 89% already lived
F Age 85: Expected lifespan 92 yrs; Years left  7;  8% life remaining, 92% already lived

Male life expectancy (WHO life tables, short):
M Age  5: Years left 72; 93% life remaining
M Age 10: Years left 67; 87% life remaining
M Age 15: Years left 62; 80% life remaining
M Age 20: Years left 57; 74% life remaining
M Age 25: Years left 52; 68% life remaining
M Age 30: Years left 48; 61% life remaining
M Age 35: Years left 43; 55% life remaining
M Age 40: Years left 39; 49% life remaining
M Age 45: Years left 34; 43% life remaining
M Age 50: Years left 30; 37% life remaining
M Age 55: Years left 26; 32% life remaining
M Age 60: Years left 22; 27% life remaining
M Age 65: Years left 18; 22% life remaining
M Age 70: Years left 15; 17% life remaining
M Age 75: Years left 12; 13% life remaining
M Age 80: Years left  9; 10% life remaining
M Age 85: Years left  6;  7% life remaining

Female life expectancy (WHO life tables, short):
F Age  5: Years left 76; 94% life remaining
F Age 10: Years left 72; 88% life remaining
F Age 15: Years left 67; 82% life remaining
F Age 20: Years left 62; 76% life remaining
F Age 25: Years left 57; 69% life remaining
F Age 30: Years left 52; 63% life remaining
F Age 35: Years left 47; 57% life remaining
F Age 40: Years left 43; 52% life remaining
F Age 45: Years left 38; 46% life remaining
F Age 50: Years left 33; 40% life remaining
F Age 55: Years left 29; 35% life remaining
F Age 60: Years left 25; 29% life remaining
F Age 65: Years left 21; 24% life remaining
F Age 70: Years left 17; 19% life remaining
F Age 75: Years left 13; 15% life remaining
F Age 80: Years left 10; 11% life remaining
F Age 85: Years left  7;  8% life remaining

--- Your Life Progress ---
Enter sex (M/F): M
Enter your age: 52

You are Male Age 52.

Expected lifespan : 82 years (982 months)
Life remaining    : 30 years (358 months)
Life already lived: 52 years (624 months)

Life progress:

[⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀]

64% already lived, 36% life remaining
```

---

## Data Notes

The WHO life tables used by the `lost_years` library are based on **WHO 2016 life expectancy data**.
The `year` parameter exists mainly for compatibility with the library interface.

---

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.
