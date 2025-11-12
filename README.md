# 🗂️ Extract Files to Text Utility

This Python script (`extract_files.py`) recursively extracts the contents of all files in a given directory and writes them to a single text file. It also optionally generates a “tree-like” structure (similar to the Unix `tree -fa` command) at the top of the output file.

Useful for:

-   Code auditing or review
    
-   AI context extraction (feeding codebases into LLMs)
    
-   Creating a readable snapshot of project files and structure
    

----------

## 📁 Features

-   ✅ Generates a `tree -fa`-like structure for the repository
    
-   ✅ Recursively extracts files and writes them to a single `.txt` file
    
-   ✅ Supports inclusion/exclusion by file extensions, directories, and filenames
    
-   ✅ Handles UTF-8 encoding safely with error catching
    
-   ✅ Works on Linux, macOS, and Windows
    

----------

## 🧰 Requirements

-   **Python 3.7+**
    
-   No external dependencies (only uses the standard library)
    

----------

## ⚙️ Usage

### 1. Clone or copy this script

```bash
git clone https://github.com/EsmailEbrahim/eh-extract-files-to-txt.git
cd eh-extract-files-to-txt

```

### 2. Run the script

Edit the `repo_directory` and `output_txt_file` variables in the script or pass them as arguments.

Example inside the script:

```python
if __name__ == "__main__":
    repo_directory = r"/path/to/your/project"
    output_txt_file = r"/path/to/output/project_extract.txt"

    extract_files_to_txt(
        repo_directory,
        output_txt_file,
        include_ext=['.py', '.yml', '.yaml', '.json', '.sh', '.env', '.txt'],
        exclude_dirs=['.git', '__pycache__', 'venv', 'node_modules', 'dist', 'build', 'uploads', 'logs', 'certs'],
        exclude_files=['README.md', 'LICENSE'],
        include_tree=True
    )

    print(f"File paths, contents, and structure have been written to {output_txt_file}")
```

Then run:

```bash
python extract_files.py
```

----------

## 🧩 Function Overview

### `generate_tree(repo_path)`

Generates a string representing a tree structure of the repository.

### `extract_files_to_txt(...)`

Main function that:

-   Walks the given directory
    
-   Filters files and folders based on inclusion/exclusion lists
    
-   Writes file paths and their contents to an output text file
    

----------

## Example Output

```
Repository structure for: /home/esmail/my-repo
================================================================================
├── my-repo/
│   ├── main.py
│   ├── utils/
│   │   ├── helpers.py
================================================================================

main.py:
print("Hello world")

========================================

```

----------

## 🧾 License

This project is licensed under the **MIT License**.

----------

## 👨‍💻 Author

**Esmail Ebrahim Hamza**  
- 📧 [esmailebraheem771@gmail.com](mailto:esmailebraheem771@gmail.com)
- 🌐 [GitHub: EsmailEbrahim](https://github.com/EsmailEbrahim)

----------

## 💻 Quick Install & Usage

### Install from PyPI
```bash
pip install eh-extract
```

### Or directly from GitHub

```bash
pip install git+https://github.com/EsmailEbrahim/eh-extract-files-to-txt.git
```

> 🧠 **Windows Users:**  
> If you see a warning like  
> `The script eh-extract.exe is installed in ... which is not on PATH`,  
> add that folder to your system PATH (usually `C:\Users\<User>\AppData\Roaming\Python\Python312\Scripts`).


### Usage

```bash
eh-extract -i /path/to/repo -o /path/to/output.txt --include-ext .py .yml .json
```
