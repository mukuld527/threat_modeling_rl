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

# Application Team Notes (why/how Fixed or Not Applicable)
app_fixed_notes = [
    "The control is fully implemented following enterprise guidelines.",
    "The team applied the required configurations and validated the behavior in QA.",
    "Implementation aligns with the architecture design and passed all security checks.",
    "The feature was updated to meet compliance requirements and verified by testing.",
    "The control was implemented using recommended libraries and validated end-to-end."
]

app_not_applicable_notes = [
    "This control is not applicable because the application does not store sensitive data.",
    "The feature is internal-only and does not expose external endpoints.",
    "The application does not handle user authentication, making this control irrelevant.",
    "The system architecture does not include components requiring this control.",
    "The control is not applicable due to the application's read-only data flow."
]

app_in_progress_notes = [
    "The team is currently implementing this control and expects completion next sprint.",
    "Development is underway, and partial functionality is already in place.",
    "The control is being integrated into the service layer and requires additional testing.",
    "Implementation has started but dependencies are still pending.",
    "The team is working on this control and will provide updates after integration testing."
]

# Security Architect Notes (agree/disagree)
architect_agree_notes = [
    "Security architect agrees with the justification provided by the application team.",
    "The explanation is valid and aligns with enterprise security standards.",
    "The justification is acceptable and meets the required security criteria.",
    "Architect concurs with the team's assessment and rationale.",
    "The provided reasoning is sound and approved by the security architect."
]

architect_disagree_notes = [
    "Security architect disagrees with the justification and requests additional evidence.",
    "The explanation is insufficient; further clarification is required.",
    "Architect does not accept the justification and recommends implementing the control.",
    "The rationale is incomplete and does not meet security expectations.",
    "Architect rejects the justification and requires corrective action."
]

def generate_row(i):
    title = f"T{i+1}"
    name = random.choice(countermeasure_names)
    status = random.choice(statuses)

    # Application team note based on status
    if status == "Fixed":
        app_note = random.choice(app_fixed_notes)
    elif status == "Not Applicable":
        app_note = random.choice(app_not_applicable_notes)
    else:
        app_note = random.choice(app_in_progress_notes)

    # Architect agreement or disagreement
    architect_agrees = random.choice([True, False])
    if architect_agrees:
        architect_note = random.choice(architect_agree_notes)
        label = 0  # valid
    else:
        architect_note = random.choice(architect_disagree_notes)
        label = random.choice([1, 2, 3])  # invalid, clarification, feedback

    return {
        "countermeasure_title": title,
        "countermeasure_name": name,
        "status": status,
        "application_team_note": app_note,
        "security_architect_note": architect_note,
        "label": label
    }

# Generate 1000 rows
rows = [generate_row(i) for i in range(1000)]

df = pd.DataFrame(rows)
df.to_csv("data/notes.csv", index=False)

print("Generated data/notes.csv with 1000 rows.")
