import pytest
from datetime import datetime
from decimal import Decimal
from app.calculator_memento import CalculatorMemento
from app.calculation import Calculation


def test_memento_to_dict():
    """Test the to_dict method of CalculatorMemento."""
    # Create a calculation
    calc = Calculation(operation="Addition", operand1=Decimal("2"), operand2=Decimal("3"))
    
    # Create a memento with the calculation
    memento = CalculatorMemento(history=[calc])
    
    # Convert to dict
    memento_dict = memento.to_dict()
    
    # Assert
    assert 'history' in memento_dict
    assert 'timestamp' in memento_dict
    assert len(memento_dict['history']) == 1
    assert memento_dict['history'][0]['operation'] == 'Addition'


def test_memento_from_dict():
    """Test the from_dict method of CalculatorMemento."""
    # Create sample data
    data = {
        'history': [
            {
                'operation': 'Multiplication',
                'operand1': '4',
                'operand2': '5',
                'result': '20',
                'timestamp': datetime.now().isoformat()
            }
        ],
        'timestamp': datetime.now().isoformat()
    }
    
    # Create memento from dict
    memento = CalculatorMemento.from_dict(data)
    
    # Assert
    assert len(memento.history) == 1
    assert memento.history[0].operation == 'Multiplication'
    assert memento.history[0].operand1 == Decimal('4')
    assert memento.history[0].operand2 == Decimal('5')
    assert memento.history[0].result == Decimal('20')
