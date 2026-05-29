# Build a configurable risk scoring system for loan applications

def score_credit(credit_score=0, **_) -> float:
    if credit_score >= 750: return 100
    elif credit_score >= 700: return 80
    elif credit_score >= 650: return 60
    elif credit_score >= 600: return 40
    else: return 10

def score_income(monthly_income=0, loan_amount=1, **_) -> float:
    # Monthly repayment assumed 1/36 of loan (3 year term)
    repayment = loan_amount / 36
    ratio = repayment / monthly_income if monthly_income > 0 else 1
    if ratio < 0.2:  return 100
    elif ratio < 0.3: return 75
    elif ratio < 0.4: return 50
    else: return 20

def score_employment(years_employed=0, **_) -> float:
    return min(100, years_employed * 10)

def score_debt_ratio(total_debt=0, monthly_income=1, **_) -> float:
    ratio = total_debt / (monthly_income * 12) if monthly_income > 0 else 99
    if ratio < 0.2:  return 100
    elif ratio < 0.4: return 70
    elif ratio < 0.6: return 40
    else: return 10

def calculate_risk(*scorer_fns, weights=None, **applicant_data):
    n = len(scorer_fns)
    weights = weights or [1/n] * n
    if len(weights) != n:
        raise ValueError("Weights must match number of scorers")

    breakdown = {}
    composite = 0
    for fn, w in zip(scorer_fns, weights):
        score = fn(**applicant_data)
        breakdown[fn.__name__] = round(score, 1)
        composite += score * w

    return {"composite": round(composite, 1), "breakdown": breakdown}

def make_decision(composite: float) -> str:
    if composite >= 70: return "✅ Approve"
    elif composite >= 50: return "⚠️  Review"
    else: return "❌ Decline"

# Test applicants
scorers = (score_credit, score_income, score_employment, score_debt_ratio)
w = [0.35, 0.30, 0.15, 0.20]

applicants = [
    {"name": "Ana",   "credit_score": 780, "monthly_income": 8000,  "loan_amount": 50000, "years_employed": 8,  "total_debt": 5000},
    {"name": "Ben",   "credit_score": 620, "monthly_income": 4000,  "loan_amount": 30000, "years_employed": 2,  "total_debt": 12000},
    {"name": "Cara",  "credit_score": 550, "monthly_income": 2500,  "loan_amount": 20000, "years_employed": 1,  "total_debt": 18000},
]
for a in applicants:
    name = a.pop("name")
    result = calculate_risk(*scorers, weights=w, **a)
    decision = make_decision(result["composite"])
    print(f"\n{name}: composite={result['composite']} → {decision}")
    for k, v in result["breakdown"].items():
        print(f"  {k}: {v}")