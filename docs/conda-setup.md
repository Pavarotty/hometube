# Quick Setup Guide for Conda Users

## Installation

```bash
# Clone the repository
git clone https://github.com/EgalitarianMonkey/hometube.git
cd hometube

# Create environment with all dependencies
conda env create -f environment.yml

# Activate environment
conda activate hometube

# Install the project in development mode
pip install -e .

# Verify installation
make test

# Start the application
streamlit run app/main.py
```

## Development Commands

```bash
# Basic testing (no coverage dependencies required)
make test

# Full testing with coverage (requires pytest-cov)
make test-coverage

# Specific test categories
make test-unit
make test-integration  
make test-performance

# Development tools
make lint
make format
make type-check
```

## Environment Updates

```bash
# Update environment when dependencies change
conda env update -f environment.yml

# Or recreate environment
conda env remove -n hometube
conda env create -f environment.yml
```

## Notes

- The `environment.yml` includes essential testing dependencies
- All make commands work with any Python environment manager
- FFmpeg is installed automatically via conda-forge channel