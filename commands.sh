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

# ----------------------------------------------------------------------------

# add your changes
git add .

# commit with a version bump message
git commit -m "Bump version to 1.1.0 - add exclude-tree options"

# bump version to 1.1.0 - add exclude-tree options
git tag v1.1.0

# # push code and tag to GitHub
git push origin cli
git push origin v1.1.0

# clean previous build
rmdir /s /q dist eh_extract.egg-info  # Windows PowerShell
# or
rm -rf dist eh_extract.egg-info       # Linux/macOS

# install or upgrade build tools
python -m pip install --upgrade build

# build the package
python -m build

# install or upgrade twine
python -m pip install --upgrade twine

# upload to PyPI
python -m twine upload dist/*

# update via pip
pip install --upgrade eh-extract

# update via pipx
pipx upgrade eh-extract

# ----------------------------------------------------------------------------
