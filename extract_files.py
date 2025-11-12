import os

def generate_tree(repo_path):
    """Generate a 'tree -fa'-like structure for the given path."""
    lines = []
    for root, dirs, files in os.walk(repo_path):
        # Compute the depth for indentation
        level = root.replace(repo_path, '').count(os.sep)
        indent = '│   ' * level
        subdir_name = os.path.basename(root)
        if subdir_name:
            lines.append(f"{indent}├── {subdir_name}/")

        sub_indent = '│   ' * (level + 1)
        for f in files:
            lines.append(f"{sub_indent}├── {f}")
    return "\n".join(lines)


def extract_files_to_txt(
    repo_path,
    output_file,
    include_ext=None,      # e.g. ['.py', '.yml', '.json']
    exclude_dirs=None,     # e.g. ['.git', '__pycache__', 'venv']
    exclude_files=None,    # e.g. ['README.md', 'LICENSE']
    include_tree=True      # Add tree output at the top
):
    include_ext = include_ext or []      # empty means include all
    exclude_dirs = exclude_dirs or []
    exclude_files = exclude_files or []

    with open(output_file, 'w', encoding='utf-8') as txt_file:
        # Optionally write the repo tree structure
        if include_tree:
            txt_file.write(f"Repository structure for: {repo_path}\n")
            txt_file.write("=" * 80 + "\n")
            tree_str = generate_tree(repo_path)
            txt_file.write(tree_str + "\n" + "=" * 80 + "\n\n")

        # Walk through the repo and get file paths and content
        for root, dirs, files in os.walk(repo_path):
            # Exclude unwanted directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            for file in files:
                # Skip excluded files
                if file in exclude_files:
                    continue

                # Skip if file extension not in include list (if provided)
                if include_ext and not any(file.endswith(ext) for ext in include_ext):
                    continue

                file_path = os.path.join(root, file)

                # Read the content of each file
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Write file path and content to the output file
                    txt_file.write(f"{os.path.relpath(file_path, repo_path)}:\n")
                    txt_file.write(content + f"\n\n{'=' * 40}\n\n")  # separator between files
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")

if __name__ == "__main__":
    repo_directory = r"/path/to/your/project"
    output_txt_file = r"/path/to/output/project_extract.txt"

    # extract_files_to_txt(
    #     repo_directory,
    #     output_txt_file,
    #     include_ext=['.py', '.yml', '.yaml', '.json', '.sh', '.env', '.txt'],  # include only these types
    #     exclude_dirs=['.git', '__pycache__', 'venv', 'node_modules', 'dist', 'build', 'uploads', 'logs', 'certs'],
    #     exclude_files=['README.md', 'LICENSE'],
    #     include_tree=True   # set to False if you don't want the tree output
    # )

    extract_files_to_txt(
        repo_directory,
        output_txt_file,
        include_ext=[],
        exclude_dirs=['.git', '__pycache__', 'venv', 'node_modules', 'dist', 'build'],
        exclude_files=['.env'],
        include_tree=True   # set to False if you don't want the tree output
    )

    print(f"File paths, contents, and structure have been written to {output_txt_file}")
