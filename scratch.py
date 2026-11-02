from pydantic import ValidationError

from readmission_risk.schemas import PatientRecord

good = PatientRecord(
    age=64, sex="F", systolic_bp=138.0, hba1c=7.2, prior_admissions=2, smoker=False
)
print(good)

try:
    PatientRecord(
        age=300, sex="F", systolic_bp=138.0, hba1c=7.2, prior_admissions=2, smoker=False
    )
except ValidationError as e:
    print("Rejected:")
    print(e)
from readmission_risk.summary import mean_age

patients = [
    PatientRecord(age=64, sex="F", systolic_bp=138, hba1c=7.2, prior_admissions=2, smoker=False),
    PatientRecord(age=52, sex="M", systolic_bp=150, hba1c=8.1, prior_admissions=0, smoker=True),
]
print(mean_age(patients))   # باید 58.0 باشد    