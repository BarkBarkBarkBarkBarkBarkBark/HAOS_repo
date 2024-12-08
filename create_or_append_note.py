# create_or_append_note.py

# Retrieve data from the service call
file_name = data.get("file_name", "note.md")  # Default file name
directory = data.get("directory", "/config/notes")  # Default directory
content = data.get("content", "")  # Content to add to the file
append = data.get("append", False)  # Whether to append or overwrite

# Ensure directory ends with a slash
if not directory.endswith("/"):
    directory += "/"

# Ensure the directory exists
full_path = f"{directory}{file_name}"
try:
    # Create directory if it doesn't exist
    import os
    os.makedirs(directory, exist_ok=True)

    # Open the file in append or write mode
    mode = "a" if append else "w"
    with open(full_path, mode) as f:
        # Add a newline before appending to ensure proper formatting
        if append and content:
            f.write("\n")
        f.write(content)

    # Log success
    logger.info(f"Note updated at: {full_path}")
except Exception as e:
    logger.error(f"Error creating/updating note: {e}")
