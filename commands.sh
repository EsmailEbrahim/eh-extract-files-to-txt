# ----------------------------------------------------------------------------

# install build tool
python -m pip install --upgrade build

# build
python -m build

# install locally
pip install dist/eh_extract-1.0.0-py3-none-any.whl

# run (once PATH is fixed)
eh-extract -i C:\path\to\repo -o C:\path\to\output.txt

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# install directly from GitHub
pip install git+https://github.com/EsmailEbrahim/eh-extract-files-to-txt.git

# run
eh-extract -i C:\path\to\repo -o C:\path\to\output.txt

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# upload to PyPI
# install twine and build
python -m pip install --upgrade build twine

# build
python -m build

# upload to PyPI
python -m twine upload dist/*

# install from PyPI
pip install eh-extract

# run
eh-extract -i C:\path\to\repo -o C:\path\to\output.txt

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# install via pipx
sudo apt install pipx

# ensure pipx path is added to shell profile
pipx ensurepath

# install eh-extract
pipx install eh-extract

# run
eh-extract -i /path/to/repo -o /path/to/output.txt

# ----------------------------------------------------------------------------
