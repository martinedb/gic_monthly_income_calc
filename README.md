# GIC Monthly Income Calculator

This Python script helps you estimate your monthly income from Guaranteed Investment Certificates (GICs). It's designed for simplicity and easy customization, so you can adapt it to your own financial circumstances.

---

## Getting Started

### Quick Start: Copy-Paste Method

The easiest way to use this script is to **copy the code** from the repository (or from below) and **paste it into your favorite code editor** (for example, Windsurf, Anaconda, or Visual Studio Code):

1. Open your code editor.
2. Copy the Python script from this repository.
3. Paste it into a new file (e.g., `gic_monthly_income_calc.py`).
4. Edit the input variables to reflect your own GIC details.
5. Run the script.

This method is perfect for quick calculations and small scripts like this one!

---

### Alternative: Cloning the Repository

If you’d like to keep the script up to date or prefer working with Git, you can clone the repository:

```bash
git clone https://github.com/martinedb/gic_monthly_income_calc.git
```
Then open the script file in your code editor and follow the instructions above.

---

## Walkthrough of the Code

Below is a section-by-section guide to help you understand and adapt the script:

### 1. Input Variables

Set your GIC details here:
- **Principal:** The amount you invest.
- **Interest Rate:** The annual interest rate (as a decimal, e.g., 0.05 for 5%).
- **Term:** The number of years the GIC lasts.

Edit these values to match your investment.

```python
principal = 10000   # Your GIC amount
interest_rate = 0.05 # Annual interest rate (5%)
term_years = 1       # Term in years
```

### 2. Monthly Income Calculation

Calculates your monthly income:

```python
monthly_income = (principal * interest_rate) / 12
```

The script may account for compounding if applicable.

### 3. Output

Prints your estimated monthly income:

```python
print(f"Estimated monthly income: ${monthly_income:.2f}")
```

---

## Customizing for Your Needs

- **Adjust the input variables** for your principal, rate, and term.
- **Expand the script:** Add more GICs or change the compounding frequency as needed.

---

## Example Use Case

Suppose you invest $20,000 at a 4% annual rate for 2 years:

```python
principal = 20000
interest_rate = 0.04
term_years = 2
```

Run the script to see your monthly income.

---

## Troubleshooting

- Make sure you have Python 3 installed.
- Check that variable values are numbers.
- Review the calculation logic if results look off.

---

## License

This script is provided as-is, for educational and personal finance planning purposes.

---

For any questions, open an issue in the repository.

Happy calculating!
