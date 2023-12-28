# Python script to replace all semicolons (';') with commas (',') in a file.

def replace_semicolons_with_commas(file_path):
    """
    Replaces all semicolons in a file with commas.

    Parameters:
    file_path (str): Path to the file to be modified.
    """
    try:
        # Read the original content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Replace all semicolons with commas
        modified_content = content.replace(';', ',')

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)

        print(f"Semicolons in '{file_path}' have been successfully replaced with commas.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
replace_semicolons_with_commas('./winequality-red.data')

# Note: Replace 'path/to/your/file.txt' with the actual path to the file you want to modify.

