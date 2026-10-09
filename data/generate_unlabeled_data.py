import pandas as pd
import random

countermeasure_names = [
    "Configure HTTPS securely",
    "Implement secure session management",
    "Encrypt sensitive data using latest encryption mechanisms",
    "Enable audit logging for critical events",
    "Validate all user inputs",
    "Ensure secure deletion of sensitive data",
]

statuses = ["Fixed", "In Progress", "Not Applicable"]

generic_notes = [
    "The team has implemented the control but needs verification.",
    "More clarity is required on how this control mitigates the threat.",
    "The justification seems incomplete and may need additional evidence.",
    "The control appears implemented but documentation is missing.",
    "Further review is required to confirm compliance with standards.",
]

def generate_row(i):
    title = f"U{i+1}"
    name = random.choice(countermeasure_names)
    status = random.choice(statuses)
    note = random.choice(generic_notes)

    return {
        "countermeasure_title": title,
        "countermeasure_name": name,
        "status": status,
        "note": note
    }

rows = [generate_row(i) for i in range(50)]

df = pd.DataFrame(rows)
df.to_csv("data/unlabeled_notes.csv", index=False)

print("Generated data/unlabeled_notes.csv with 50 rows.")
