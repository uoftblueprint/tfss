# Import necessary functions and classes
from email_processing.ticket_description_generation.test_data.populate import populate_class
from description_generator import (generate_description, construct_comprehensive_delivery_prompt,
                                   construct_detailed_delivery_prompt, construct_simplified_delivery_prompt)


def try_prompts(email, output_file):
    with open(output_file, 'w') as file:
        # Write email at beginning of file
        file.write("Email Content:\n\n")
        file.write(f"To: {', '.join(email.to)}\n")
        file.write(f"From: {email.author}\n")
        file.write(f"Date: {email.date}\n")
        file.write(f"Subject: {email.subject}\n\n")
        file.write(email.body + "\n\n")

        # Test with first prompt
        detailed_description = generate_description(email, construct_detailed_delivery_prompt)
        file.write("\nDetailed Delivery Prompt Description:\n\n")
        file.write(detailed_description + "\n")

        # Test with second prompt
        simplified_description = generate_description(email, construct_simplified_delivery_prompt)
        file.write("\nSimplified Delivery Prompt Description:\n\n")
        file.write(simplified_description + "\n")

        # Test with third prompt
        comprehensive_description = generate_description(email, construct_comprehensive_delivery_prompt)
        file.write("\nComprehensive Delivery Prompt Description:\n\n")
        file.write(comprehensive_description + "\n")


if __name__ == '__main__':
    # Load emails from CSV file
    emails = populate_class('test_data/task_emails.csv')

    if emails:
        print(f"total length of emails list: {len(emails)}")
        # Prompt for index to test in emails.csv
        try:
            start_index = int(input("Enter the starting index of the emails to test (0-based index): "))
            end_index = int(input("Enter the ending index of the emails to test (0-based index): "))

            if start_index < 0 or end_index >= len(emails) or start_index > end_index:
                print("Index range invalid")
            else:
                for i in range(start_index, end_index + 1):
                    output_file = f'test_output{i + 1}.txt'
                    try_prompts(emails[i], output_file)
                    print(f"Test results for email {i} written to {output_file}")

        except ValueError:
            print("Index is invalid")
    else:
        print("No emails loaded")
