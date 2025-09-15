# Scripts Utilities

This directory contains utility scripts for the HomeTube project.

## Available Scripts

### `check_tests.py`
Comprehensive test verification and execution script.

**Usage:**
```bash
# Run from project root
python scripts/check_tests.py

# Or make it executable
chmod +x scripts/check_tests.py
./scripts/check_tests.py
```

**Features:**
- Verifies test file structure
- Executes all test categories
- Provides detailed summary report
- Validates project integrity

**Output:**
- ✅ SUCCESS indicators for passing tests
- ❌ FAILED indicators with error codes
- 📈 Summary score and statistics
- 🎉 Celebration message when all tests pass

This script is particularly useful for:
- CI/CD pipeline validation
- Pre-commit testing
- Development environment verification
- Test refactoring validation