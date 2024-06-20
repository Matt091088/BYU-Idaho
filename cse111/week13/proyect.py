

import questionary
from decimal import Decimal

def generate_budget(pdf_filename, costs):
    # Calculate the total cost
    total_cost = sum(costs.values())

    # Create a PDF file
    pdf = canvas.Canvas(pdf_filename)

    # Set the text format
    pdf.setFont("Helvetica", 12)

    # Add information to the PDF
    pdf.drawString(100, 800, "Budget")
    for index, (concept, cost) in enumerate(costs.items(), start=1):
        pdf.drawString(100, 780 - 20 * len(costs) + 20 * index, f"{concept.capitalize()}: ${cost}")

    pdf.drawString(100, 780 - 20 * len(costs) + 20 * (len(costs) + 1), f"Total Cost: ${total_cost}")

    # Close the PDF file
    pdf.save()

def get_costs():
    # Ask the user for costs
    questions = [
        {"type": "input", "name": "materials", "message": "Cost of Materials: "},
        {"type": "input", "name": "labor", "message": "Cost of Labor: "},
        {"type": "input", "name": "shipping", "message": "Cost of Shipping: "},
        {"type": "input", "name": "installation", "message": "Cost of Installation: "},
        {"type": "input", "name": "taxes", "message": "Taxes: "}
    ]

    answers = questionary.prompt(questions)

    # Convert answers to Decimal numbers
    costs = {key: Decimal(value) for key, value in answers.items()}

    return costs

def main():
    # Get costs from the user
    costs = get_costs()

    # Generate the budget in a PDF file
    pdf_filename = "budget.pdf"
    generate_budget(pdf_filename, costs)

    print(f"Budget generated successfully. You can find it in {pdf_filename}")

if __name__ == "__main__":
    main()
