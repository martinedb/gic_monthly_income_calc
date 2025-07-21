from datetime import datetime, timedelta

# Function for calculating simple interest income per month
def simple_interest_monthly(principal, annual_rate, term_years):
    total_interest = principal * annual_rate * term_years
    monthly_income = total_interest / (term_years * 12)
    return monthly_income

# Function for calculating compound interest income per month
def compound_interest_monthly(principal, annual_rate, term_years, months_elapsed):
    # Check if months_elapsed is greater than 0 before performing the calculation
    if months_elapsed <= 0:
        return 0  # No income generated if months_elapsed is 0 or negative

    monthly_rate = annual_rate / 12
    amount = principal * (1 + monthly_rate) ** months_elapsed
    total_interest = amount - principal
    monthly_income = total_interest / months_elapsed
    return monthly_income

# GIC Investment data
gics = [
    {"amount": 2000, "rate": 0.042, "term_years": 2, "interest_type": "simple", "start_date": "2023-05-08", "end_date": "2025-05-08", "current_value": 2019.10},
    {"amount": 5000, "rate": 0.043, "term_years": 1, "interest_type": "simple", "start_date": "2024-09-23", "end_date": "2025-09-23", "current_value": 5075.99},
    {"amount": 5000, "rate": 0.0355, "term_years": 1, "interest_type": "simple", "start_date": "2025-01-14", "end_date": "2026-01-14", "current_value": 5008.27},
    {"amount": 6000, "rate": 0.0425, "term_years": 3, "interest_type": "simple", "start_date": "2024-08-14", "end_date": "2027-08-14", "current_value": 6118.07},
    {"amount": 10000, "rate": 0.0485, "term_years": 2, "interest_type": "compound", "start_date": "2024-01-05", "end_date": "2026-01-05", "current_value": 10521.22},
    {"amount": 5000, "rate": 0.0425, "term_years": 3, "interest_type": "compound", "start_date": "2024-08-20", "end_date": "2027-08-20", "current_value": 5094.90},
]

# Function to calculate monthly income for each GIC by month end
def calculate_monthly_income_by_end_dates(gics, start_year, end_year):
    monthly_incomes = []

    # Iterate over all the months from start_year to end_year
    for year in range(start_year, end_year + 1):
        # Find the last day of each month
        for month in range(1, 13):
            # Get the last day of the current month
            last_day_of_month = datetime(year, month, 1) + timedelta(days=32)
            last_day_of_month = last_day_of_month.replace(day=1) - timedelta(days=1)

            # Calculate the monthly income for each GIC for this specific month
            total_income_for_month = 0
            for gic in gics:
                start_date = datetime.strptime(gic["start_date"], "%Y-%m-%d")
                term_years = gic["term_years"]
                interest_type = gic["interest_type"]

                # Calculate months elapsed since the GIC start date
                months_elapsed = (last_day_of_month.year - start_date.year) * 12 + last_day_of_month.month - start_date.month

                if months_elapsed >= 0:  # The GIC must have been started before the current month
                    if interest_type == "simple":
                        monthly_income = simple_interest_monthly(gic["amount"], gic["rate"], term_years)
                    elif interest_type == "compound":
                        monthly_income = compound_interest_monthly(gic["amount"], gic["rate"], term_years, months_elapsed)
                    total_income_for_month += monthly_income

            monthly_incomes.append((last_day_of_month, total_income_for_month))

    return monthly_incomes

# Calculate monthly income for each month between 2024 and 2025
monthly_incomes = calculate_monthly_income_by_end_dates(gics, 2024, 2025)

# Output the monthly income report
for month_end, income in monthly_incomes:
    print(f"Month Ending {month_end.strftime('%B %d, %Y')}: ${income:.2f}")
