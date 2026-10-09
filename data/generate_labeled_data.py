import pandas as pd
import random

# Countermeasure names
countermeasure_names = [
    "Configure HTTPS securely",
    "Implement secure session management",
    "Encrypt sensitive data using latest encryption mechanisms",
    "Implement secure password storage",
    "Enable audit logging for critical events",
    "Validate all user inputs",
    "Implement secure key rotation",
    "Ensure secure deletion of sensitive data",
    "Protect API endpoints with authentication",
    "Implement rate limiting for brute-force protection"
]

# Status options
statuses = ["Fixed", "In Progress", "Not Applicable"]

# Notes for each label
valid_notes = [
    "The control is implemented as described and meets all requirements.",
    "Encryption is applied to data in transit and at rest.",
    "Audit logging is configured according to enterprise standards.",
    "Input validation is enforced on all user-facing fields.",
    "HTTPS is configured with TLS 1.3 and strong cipher suites."
]

invalid_notes = [
    "We think this control is implemented but are not fully sure.",
    "The team will add this later, so marking complete for now.",
    "This is not needed because our app is internal only.",
    "We skipped this control due to time constraints.",
    "The control is not applicable but no justification provided."
]

clarification_notes = [
    "Need more details on how encryption keys are rotated.",
    "Clarify how access is revoked for terminated employees.",
    "Explain how input validation handles nested JSON payloads.",
    "More information needed on session timeout configuration.",
    "Clarify how audit logs are protected from tampering."
]

feedback_notes = [
    "Please update the justification to include specific evidence.",
    "Add screenshots showing where the control is implemented.",
    "Rewrite the explanation to align with enterprise standards.",
    "Provide more detail on how this control mitigates the threat.",
    "Add references to the architecture diagram for clarity."
]

def generate_row(i):
    title = f"T{i+1}"
    name = random.choice(countermeasure_names)
    status = random.choice(statuses)

    label = random.choice([0, 1, 2, 3])

    if label == 0:
        note = random.choice(valid_notes)
    elif label == 1:
        note = random.choice(invalid_notes)
    elif label == 2:
        note = random.choice(clarification_notes)
    else:
        note = random.choice(feedback_notes)

    return {
        "countermeasure_title": title,
        "countermeasure_name": name,
        "status": status,
        "note": note,
        "label": label
    }

# Generate 1000 rows
rows = [generate_row(i) for i in range(1000)]

df = pd.DataFrame(rows)
df.to_csv("data/notes.csv", index=False)

print("Generated data/notes.csv with 1000 rows.")
