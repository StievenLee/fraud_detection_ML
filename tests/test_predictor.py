from app.predictor import FraudPredictor

predictor = FraudPredictor()

def test_normal_transaction():
    data = {
        "type": "PAYMENT",
        "amount": 1000,
        "oldbalanceOrg": 5000,
        "newbalanceOrig": 4000,
        "oldbalanceDest": 2000,
        "newbalanceDest": 3000
    }
    result = predictor.predict(data)

    assert result["prediction"] in [0, 1]
    assert "risk_label" in result
    assert "risk_color" in result


def test_fraud_transaction():
    data = {
        "type": "TRANSFER",
        "amount": 10000,
        "oldbalanceOrg": 10000,
        "newbalanceOrig": 0,
        "oldbalanceDest": 0,
        "newbalanceDest": 0
    }
    result = predictor.predict(data)

    assert result["prediction"] == 1


def test_flags_exist():
    data = {
        "type": "TRANSFER",
        "amount": 5000,
        "oldbalanceOrg": 8000,
        "newbalanceOrig": 3000,
        "oldbalanceDest": 0,
        "newbalanceDest": 0
    }
    result = predictor.predict(data)

    assert isinstance(result["flags"], list)


def test_no_crash_zero_amount():
    data = {
        "type": "PAYMENT",
        "amount": 0,
        "oldbalanceOrg": 1000,
        "newbalanceOrig": 1000,
        "oldbalanceDest": 500,
        "newbalanceDest": 500
    }
    result = predictor.predict(data)

    assert result["prediction"] in [0, 1]