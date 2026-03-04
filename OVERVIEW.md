# Advanced Calculator Application

A comprehensive, feature-rich calculator application built with Python, demonstrating advanced object-oriented programming principles, design patterns, and best practices.

## Features

### Core Arithmetic Operations
- **Basic Operations**: Addition, Subtraction, Multiplication, Division
- **Advanced Operations**: Power, Root, Modulus, Integer Division, Percentage, Absolute Difference
- All operations support decimal precision and handle edge cases gracefully

### Design Patterns Implemented
- **Factory Pattern**: `OperationFactory` for dynamic operation creation
- **Strategy Pattern**: Operation selection and execution
- **Observer Pattern**: LoggingObserver and AutoSaveObserver for calculation monitoring
- **Memento Pattern**: Undo/Redo functionality with state preservation
- **Singleton-like Pattern**: Calculator configuration management

### Key Features
- **Undo/Redo Functionality**: Revert or replay calculations using the Memento pattern
- **Comprehensive Logging**: All operations logged with configurable log levels
- **Persistent History**: Auto-save and load calculation history using pandas DataFrames
- **Input Validation**: Robust validation of user inputs with meaningful error messages
- **Configuration Management**: Environment-based configuration with `.env` file support
- **REPL Interface**: User-friendly command-line interface for interactive calculator use

## Project Structure

```
project_root/
├── app/
│   ├── __init__.py
│   ├── calculator.py              # Main Calculator class
│   ├── calculation.py             # Calculation model/value object
│   ├── calculator_config.py       # Configuration management
│   ├── calculator_memento.py      # Memento pattern for undo/redo
│   ├── calculator_repl.py         # REPL interface
│   ├── exceptions.py              # Custom exception hierarchy
│   ├── history.py                 # Observer implementations
│   ├── input_validators.py        # Input validation utilities
│   └── operations.py              # Operation implementations
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_calculation.py
│   ├── test_calculator.py
│   ├── test_calculator_memento.py
│   ├── test_config.py
│   ├── test_exceptions.py
│   ├── test_history.py
│   ├── test_operations.py
│   └── test_validators.py
├── history/                       # Calculation history storage
├── logs/                          # Application logs
├── .env                           # Environment configuration
├── .github/
│   └── workflows/
│       ├── python-app.yml         # GitHub Actions CI/CD workflow
│       └── tests.yml              # Alternative test workflow
├── requirements.txt               # Python dependencies
├── pytest.ini                     # Pytest configuration
├── main.py                        # Entry point
├── README.md                      # This file
└── LICENSE                        # Project license
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd module5_is601
```

#### 2. Create Virtual Environment
```bash
# Using venv (recommended)
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Environment
Create or update the `.env` file in the project root:

```dotenv
# Base directory for the calculator
CALCULATOR_BASE_DIR=.

# Directory paths
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_HISTORY_FILE=history/calculator_history.csv
CALCULATOR_LOG_FILE=logs/calculator.log

# History settings
CALCULATOR_MAX_HISTORY_SIZE=1000
CALCULATOR_AUTO_SAVE=true

# Calculation settings
CALCULATOR_PRECISION=10
CALCULATOR_MAX_INPUT_VALUE=1e999
CALCULATOR_DEFAULT_ENCODING=utf-8
```

## Usage

### Running the Calculator

```bash
python main.py
```

### REPL Commands

Once the calculator starts, use the following commands:

#### Arithmetic Operations
```
add <a> <b>              - Add two numbers
subtract <a> <b>         - Subtract b from a
multiply <a> <b>         - Multiply two numbers
divide <a> <b>           - Divide a by b
power <a> <b>            - Calculate a raised to power b
root <a> <b>             - Calculate the bth root of a
modulus <a> <b>          - Calculate remainder of a divided by b
int_divide <a> <b>       - Integer division of a by b
percent <a> <b>          - Calculate percentage (a/b * 100)
abs_diff <a> <b>         - Calculate absolute difference
```

#### History Management
```
history                  - Display calculation history
clear                    - Clear all calculation history
save                     - Save history to CSV file
load                     - Load history from CSV file
```

#### Undo/Redo
```
undo                     - Undo the last calculation
redo                     - Redo an undone calculation
```

#### Utility
```
help                     - Display available commands
exit                     - Exit the calculator (automatically saves history)
```

### Example Session

```
Calculator started. Type 'help' for commands.

Enter command: add

Enter numbers (or 'cancel' to abort):
First number: 10
Second number: 5

Result: 15

Enter command: multiply

Enter numbers (or 'cancel' to abort):
First number: 3.5
Second number: 2

Result: 7

Enter command: history

Calculation History:
1. Addition(10, 5) = 15
2. Multiplication(3.5, 2) = 7

Enter command: exit
History saved successfully.
Goodbye!
```

## Configuration

### Environment Variables

All configuration is managed through environment variables, which can be set in the `.env` file:

| Variable | Default | Description |
|----------|---------|-------------|
| `CALCULATOR_BASE_DIR` | `.` | Project root directory |
| `CALCULATOR_LOG_DIR` | `logs` | Directory for log files |
| `CALCULATOR_HISTORY_DIR` | `history` | Directory for history files |
| `CALCULATOR_HISTORY_FILE` | `history/calculator_history.csv` | History CSV file path |
| `CALCULATOR_LOG_FILE` | `logs/calculator.log` | Log file path |
| `CALCULATOR_MAX_HISTORY_SIZE` | `1000` | Maximum history entries |
| `CALCULATOR_AUTO_SAVE` | `true` | Auto-save history after each calculation |
| `CALCULATOR_PRECISION` | `10` | Decimal precision for calculations |
| `CALCULATOR_MAX_INPUT_VALUE` | `1e999` | Maximum allowed input value |
| `CALCULATOR_DEFAULT_ENCODING` | `utf-8` | File encoding |

## Testing

### Running Tests

```bash
# Run all tests with coverage report
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_operations.py -v

# Run tests matching a pattern
pytest tests/test_calc* -v

# Run with detailed output
pytest -v --tb=short
```

### Coverage Report

View the HTML coverage report in `htmlcov/index.html`:

```bash
# Generate coverage report
pytest --cov=app --cov-report=html

# Open in browser (Linux/macOS)
open htmlcov/index.html
```

**Current Coverage**: 100% across all modules

### Test Files

- `test_calculation.py` - Calculation model tests
- `test_calculator.py` - Main Calculator class tests
- `test_calculator_memento.py` - Memento/undo-redo tests
- `test_config.py` - Configuration management tests
- `test_exceptions.py` - Exception hierarchy tests
- `test_history.py` - Observer pattern tests
- `test_operations.py` - Operation implementation tests
- `test_validators.py` - Input validation tests

## CI/CD Pipeline

The project includes GitHub Actions workflows for continuous integration:

### Workflow: `python-app.yml`

Triggers on:
- Push to `main` branch
- Pull requests to `main` branch

Steps:
1. Checkout code
2. Set up Python 3.x
3. Install dependencies
4. Run tests with pytest
5. Enforce 90% code coverage

View workflow status in the GitHub Actions tab of the repository.

## Architecture & Design Patterns

### Factory Pattern
The `OperationFactory` class provides a centralized way to create operation instances:

```python
operation = OperationFactory.create_operation('add')
result = operation.execute(Decimal('5'), Decimal('3'))
```

Register custom operations:
```python
OperationFactory.register_operation('custom', CustomOperation)
```

### Observer Pattern
Observes calculations and performs actions:

```python
class CustomObserver(HistoryObserver):
    def update(self, calculation: Calculation):
        # Handle calculation event
        pass

calc.add_observer(CustomObserver())
```

### Memento Pattern
Preserves and restores calculator state for undo/redo:

```python
# Undo operations
calc.undo()  # Reverts to previous state
calc.redo()  # Restores undone state
```

## Error Handling

The application uses a custom exception hierarchy for precise error handling:

```
CalculatorError (Base)
├── ValidationError - Input validation failures
├── OperationError - Calculation failures
└── ConfigurationError - Configuration issues
```

Example:
```python
try:
    result = calc.perform_operation('invalid', 5)
except ValidationError as e:
    print(f"Input error: {e}")
except OperationError as e:
    print(f"Calculation error: {e}")
```

## Logging

The application logs all important events and calculations:

**Log Levels**:
- `INFO` - Operation summaries, state changes
- `WARNING` - Unusual conditions, recovery actions
- `ERROR` - Calculation failures, exceptions

**Log Location**: `logs/calculator.log`

**Log Format**:
```
2026-03-03 10:30:45,123 - INFO - Calculation performed: Addition (5, 3) = 8
2026-03-03 10:30:50,456 - ERROR - Division by zero is not allowed
```

## Data Persistence

### History Storage

Calculations are persisted to CSV using pandas:

**File Location**: `history/calculator_history.csv`

**Format**:
```csv
operation,operand1,operand2,result,timestamp
Addition,10,5,15,2026-03-03T10:30:45.123456
Multiplication,3.5,2,7,2026-03-03T10:30:50.654321
```

### Auto-Save

Enabled by default (`CALCULATOR_AUTO_SAVE=true`). Automatically saves history after each calculation.

## Dependencies

### Core Dependencies
- `python-dotenv` - Environment variable management
- `pandas` - Data persistence and analysis
- `pytest` - Testing framework
- `pytest-cov` - Code coverage reporting

### Development Dependencies
- `pylint` - Code quality analysis
- `coverage` - Coverage measurement

See `requirements.txt` for complete version information.

## Performance Considerations

- **Decimal Arithmetic**: Uses `Decimal` type for precise calculations
- **Lazy Loading**: Configuration loaded on demand
- **Efficient Storage**: Pandas DataFrames for memory-efficient history storage
- **Limited History**: Max 1000 entries (configurable) prevents memory bloat

## Troubleshooting

### Issue: History not saving
**Solution**: 
- Verify `CALCULATOR_LOG_DIR` and `CALCULATOR_HISTORY_DIR` exist
- Check file permissions on directories
- Ensure `CALCULATOR_AUTO_SAVE=true` in `.env`

### Issue: Colors not showing in terminal
**Solution**: Terminal must support ANSI colors. Most modern terminals do.

### Issue: Test failures
**Solution**:
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` to install all dependencies
- Delete `.pytest_cache` and `htmlcov` directories, then retry

## Contributing

To extend the calculator with new operations:

1. Subclass `Operation` in `app/operations.py`
2. Implement the `execute()` method
3. Override `validate_operands()` if needed
4. Register with `OperationFactory.register_operation()`
5. Add tests in `tests/test_operations.py`
6. Update documentation

Example:
```python
class SquareRoot(Operation):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Calculate square root (ignores b)."""
        if a < 0:
            raise ValidationError("Cannot calculate root of negative number")
        return Decimal(a ** Decimal('0.5'))

OperationFactory.register_operation('sqrt', SquareRoot)
```

## Testing Before Deployment

### Pre-Push Checklist

- [ ] Run `pytest --cov=app` - all tests pass, 100% coverage
- [ ] Verify `.env` file is configured correctly
- [ ] Test each arithmetic operation manually
- [ ] Test undo/redo functionality
- [ ] Test history save/load
- [ ] Test with various input types (integers, decimals, negative numbers)
- [ ] Test error cases (division by zero, invalid input, etc.)
- [ ] Check log file is being created and populated
- [ ] Verify GitHub Actions workflow passes

### Operations to Test Manually

1. **Add**: `2 + 3` → 5, `2.5 + 1.5` → 4
2. **Subtract**: `10 - 3` → 7, `-5 - 3` → -8
3. **Multiply**: `4 * 5` → 20, `-2 * 3` → -6
4. **Divide**: `10 / 2` → 5, `10 / 3` → 3.333...
5. **Power**: `2 ^ 3` → 8, `5 ^ 2` → 25
6. **Root**: `sqrt(9, 2)` → 3, `root(8, 3)` → 2
7. **Modulus**: `10 % 3` → 1, `-10 % 3` → -1
8. **Integer Division**: `10 // 3` → 3, `-10 // 3` → -3
9. **Percentage**: `(50 / 100) * 100` → 50, `(33.33 / 100) * 100` → 33.33
10. **Absolute Difference**: `abs(10 - 3)` → 7, `abs(3 - 10)` → 7

### Edge Cases to Test

```
# Division by zero
divide 10 0  → Error: "Division by zero not allowed"

# Large numbers
add 1e308 1e308  → Result

# Negative exponents (should fail)
power 2 -1  → Error: "Negative exponents not supported"

# Root of negative (should fail)
root -9 2  → Error: "Cannot calculate root of negative number"

# Zero root (should fail)
root 9 0  → Error: "Zero root is undefined"

# Empty history
history  → "No calculations in history"

# Undo with no history
undo  → "Nothing to undo"
```

## Licenses & Attribution

This project demonstrates OOP principles and design patterns in Python.
See LICENSE file for details.

## Support & Questions

For issues, questions, or suggestions:
1. Check the README for common solutions
2. Review test files for usage examples
3. Check GitHub Issues for related problems
4. Review code comments and docstrings

---

**Last Updated**: March 3, 2026  
**Version**: 1.0.0  
**Python**: 3.8+  
**Test Coverage**: 100%
