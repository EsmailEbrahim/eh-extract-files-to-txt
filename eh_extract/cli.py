#!/usr/bin/env python3
import os
import argparse


def generate_tree(repo_path):
    """Generate a 'tree -fa'-like structure for the given path."""
    lines = []
    for root, dirs, files in os.walk(repo_path):
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
    include_ext=None,
    exclude_dirs=None,
    exclude_files=None,
    include_tree=True
):
    include_ext = include_ext or []
    exclude_dirs = exclude_dirs or []
    exclude_files = exclude_files or []

    with open(output_file, 'w', encoding='utf-8') as txt_file:
        if include_tree:
            txt_file.write(f"Repository structure for: {repo_path}\n")
            txt_file.write("=" * 80 + "\n")
            tree_str = generate_tree(repo_path)
            txt_file.write(tree_str + "\n" + "=" * 80 + "\n\n")

        for root, dirs, files in os.walk(repo_path):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                if file in exclude_files:
                    continue
                if include_ext and not any(file.endswith(ext) for ext in include_ext):
                    continue

                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    txt_file.write(f"{os.path.relpath(file_path, repo_path)}:\n")
                    txt_file.write(content + f"\n\n{'=' * 40}\n\n")
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract files and directory structure to a single text file."
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Path to the input repository or directory."
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Path to the output text file."
    )
    parser.add_argument(
        "--include-ext",
        nargs="*",
        default=[],
        help="List of file extensions to include (e.g. .py .yml .json). Leave empty to include all."
    )
    parser.add_argument(
        "--exclude-dirs",
        nargs="*",
        default=[".git", "__pycache__", "venv", "node_modules", "dist", "build"],
        help="List of directories to exclude."
    )
    parser.add_argument(
        "--exclude-files",
        nargs="*",
        default=[".env"],
        help="List of specific files to exclude."
    )
    parser.add_argument(
        "--no-tree",
        action="store_true",
        help="Exclude the directory tree from the output."
    )

    args = parser.parse_args()

    extract_files_to_txt(
        repo_path=args.input,
        output_file=args.output,
        include_ext=args.include_ext,
        exclude_dirs=args.exclude_dirs,
        exclude_files=args.exclude_files,
        include_tree=not args.no_tree
    )

    print(f"\n✅ File paths, contents, and structure have been written to {args.output}\n")
