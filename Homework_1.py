# Name:
# SBUID: 

import math
# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise 1: Library Book Management  -----------------
# TODO: Complete the implementation of request_delay_info(), calculate_late_fees(), 
# and convert_years_to_days().

def request_delay_info():
    """
    Requests the number of days a book has been borrowed from the user.
    Ensures that the number of days is positive.
    
    Returns:
        Two outputs: a boolean indicating successful input and the number of late days.
    """
    ...


# Function to compute the late fees
def calculate_late_fees(late_days):
    """
    Computes the late fees based on the number of days a book has been overdue.
    Args:
        late_days: The number of days the book has been borrowed.
    Returns:
        The total late fee as a float.
    """
    ...


def convert_years_to_days(years):
    """
    Converts years to days.
    Args:
        years: The number of years.
    Returns:
        The equivalent number of days.
    """
    ...

# ---------------------------- Exercise 2: Park Area Management ---------------------
# TODO: Complete the implementation of calculate_circle_area(), estimate_crew_size()
# and calculate_poly_area

def calculate_circle_area(radius):
    """
    Calculates the area of a circle given its radius.
    Args:
        radius: The radius of the circle.
    Returns:
        The area of the circle.
    """
    ...


def estimate_crew_size(area):
    """
    Estimates the number of crew members needed based on the park's area.
    Args:
        area: The area of the park in square meters.
    Returns:
        The number of crew members needed.
    """
    ...


def calculate_poly_area (n, s):
    """
    Calculates the area of a regular polygon.
    Args:
        n: Number of sides of the polygon.
        s: Length of each side of the polygon.
    Returns:
        The area of the polygon.
    """
    ...
    
    
def compute_apothem(n,s):
    """
    Computes the apothem of a regular polygon.
    Args:
        n: Number of sides of the polygon.
        s: Length of each side of the polygon.
    Returns:
        The length of the apothem.
    """
    ...

# ---------------------------- Main Function ----------------------------
def main():
    # Exercise I: Library Book Management
    # I.1 - Request the delay to the user using your fct request_delay_info
    # I.2 - Compute the fee
    
    # Special case for a 119-year delay
    delay_years = 119
    # I.3 Convert years to day + Compute the fee
    
    # Exercise 2: Park Area Management
    park_radius = 100
    # II.1 Compute circle area
    # II.2 Compute the number of crew needed
    
    # Polygon park case
    n, s = 6, 150
    # II.3 Compute polygon area 
    # II.3-2 Compute the number of crew needed


if __name__ == "__main__":
    main()
