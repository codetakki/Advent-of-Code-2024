def is_safe_report(report):
    """Check if a report is safe based on the original rules."""
    increasing = True
    decreasing = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not (1 <= abs(diff) <= 3):  # Rule 2: Difference must be 1 to 3
            return False
        if diff > 0:
            decreasing = False  # Not decreasing
        if diff < 0:
            increasing = False  # Not increasing

    return increasing or decreasing  # Rule 1: Must be either all increasing or all decreasing

def is_safe_with_dampener(report):
    """Check if a report is safe after removing at most one level."""
    if is_safe_report(report):  # If already safe, no need for the dampener
        return True

    # Check if removing a single level makes it safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Remove the i-th level
        if is_safe_report(modified_report):
            return True

    return False

def count_safe_reports_with_dampener(reports):
    """Count the number of safe reports considering the Problem Dampener."""
    safe_count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count

# Example data
with open('2/input.txt', 'r') as file:
    lines = file.readlines()

# Process each line to convert it into an array of integers
array_of_arrays = [list(map(int, line.split())) for line in lines]

data = array_of_arrays

def run():
  # Count safe reports considering the Problem Dampener
  safe_reports_count_with_dampener = count_safe_reports_with_dampener(data)
  # print(f"Number of safe reports with dampener: {safe_reports_count_with_dampener}")

from utils import takeTime 
takeTime(run, 1000)