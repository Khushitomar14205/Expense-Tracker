from project import (
    calculate_total,
    category_summary,
    budget_exceeded
)

def test_calculate_total():
    expenses=[
        {"amount": 100},
        {"amount": 200},
        {"amount":300}
    ]

    assert calculate_total(expenses) == 600

def test_category_summary():
    expenses=[
        {"category":"Food","amount":150},
        {"category":"Travel","amount":200}
    ]
    summary= category_summary(expenses)

    assert summary["Food"]== 150
    assert summary["Travel"]==200


def test_budget_exceeded_true():
    assert budget_exceeded(1500,1000) is True

def test_budget_exceeded_false():
    assert budget_exceeded(800,1000) is False
