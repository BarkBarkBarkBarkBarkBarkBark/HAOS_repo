import os


def generate_markdown(file_name, text, directory="markdown_files"):
    """
    Generate a Markdown (.md) file with the given text.

    :param file_name: Name of the file (with or without .md extension)
    :param text: Text content to write into the Markdown file
    :param directory: Directory to save the Markdown file
    """
    # Ensure the file name ends with .md
    if not file_name.endswith(".md"):
        file_name += ".md"

    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    # Construct the full file path
    file_path = os.path.join(directory, file_name)

    # Write the text to the Markdown file
    try:
        with open(file_path, "w") as md_file:
            md_file.write(text)
        print(f"Markdown file created at: {file_path}")
    except Exception as e:
        print(f"Error creating Markdown file: {e}")


# Example usage
if __name__ == "__main__":
    # Define the file name and content
    file_name = "example_note"
    content = "# Example Note\n\nThis is a test Markdown file generated by Python."

    # Call the function to generate the Markdown file
    generate_markdown(file_name, content)
