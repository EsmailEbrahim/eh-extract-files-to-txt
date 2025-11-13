#!/usr/bin/env python3
import os
import argparse
from eh_extract import __version__


version = __version__


def generate_tree(repo_path, exclude_dirs=None, exclude_files=None):
    """Generate a 'tree -fa'-like structure for the given path."""
    exclude_dirs = exclude_dirs or []
    exclude_files = exclude_files or []

    lines = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        level = root.replace(repo_path, '').count(os.sep)
        indent = '│   ' * level
        subdir_name = os.path.basename(root)
        if subdir_name:
            lines.append(f"{indent}├── {subdir_name}/")

        sub_indent = '│   ' * (level + 1)
        for f in files:
            if f in exclude_files:
                continue
            lines.append(f"{sub_indent}├── {f}")
    return "\n".join(lines)


def extract_files_to_txt(
    repo_path,
    output_file,
    include_ext=None,
    exclude_dirs=None,
    exclude_files=None,
    include_tree=True,
    exclude_tree_dirs=None,
    exclude_tree_files=None
):
    include_ext = include_ext or []
    exclude_dirs = exclude_dirs or []
    exclude_files = exclude_files or []
    exclude_tree_dirs = exclude_tree_dirs or exclude_dirs
    exclude_tree_files = exclude_tree_files or exclude_files

    with open(output_file, 'w', encoding='utf-8') as txt_file:
        if include_tree:
            txt_file.write(f"Repository structure for: {repo_path}\n")
            txt_file.write("=" * 80 + "\n")
            tree_str = generate_tree(repo_path, exclude_tree_dirs, exclude_tree_files)
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
        help="List of directories to exclude from file extraction."
    )
    parser.add_argument(
        "--exclude-files",
        nargs="*",
        default=[".env"],
        help="List of specific files to exclude from file extraction."
    )
    parser.add_argument(
        "--exclude-tree-dirs",
        nargs="*",
        default=None,
        help="List of directories to exclude from the tree structure. Defaults to --exclude-dirs."
    )
    parser.add_argument(
        "--exclude-tree-files",
        nargs="*",
        default=None,
        help="List of files to exclude from the tree structure. Defaults to --exclude-files."
    )
    parser.add_argument(
        "--no-tree",
        action="store_true",
        help="Exclude the directory tree from the output."
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"eh-extract {version}"
    )

    args = parser.parse_args()

    extract_files_to_txt(
        repo_path=args.input,
        output_file=args.output,
        include_ext=args.include_ext,
        exclude_dirs=args.exclude_dirs,
        exclude_files=args.exclude_files,
        include_tree=not args.no_tree,
        exclude_tree_dirs=args.exclude_tree_dirs,
        exclude_tree_files=args.exclude_tree_files
    )

    print(f"\n✅ File paths, contents, and structure have been written to {args.output}\n")
