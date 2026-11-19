import json, os

REPO = r"C:\Users\Alexander\.gemini\antigravity\scratch\leets"
Q_PATH = os.path.join(REPO, "questions.json")

with open(Q_PATH, "r", encoding="utf-8") as f:
    d = json.load(f)

# Metadata mappings
TOPIC_SKILL_MAP = {
    # 2023-summer-01
    "2023-h404-01-q1a": (["5.2", "5.1"], ["technical"]),
    "2023-h404-01-q1b": (["6.2"], ["technical"]),
    "2023-h404-01-q1c": (["1.3", "6.4"], ["design"]),
    "2023-h404-01-q1di": (["6.4", "3.6"], ["maths"]),
    "2023-h404-01-q1dii": (["6.4", "3.5"], ["technical"]),
    "2023-h404-01-q1diii": (["6.4"], ["technical"]),
    "2023-h404-01-q1div": (["6.4"], ["technical"]),
    "2023-h404-01-q1dv": (["6.4", "6.5"], ["technical"]),
    "2023-h404-01-q1e": (["3.4", "2.4"], ["design"]),
    "2023-h404-01-q2a": (["3.6", "4.1"], ["maths"]),
    "2023-h404-01-q2bi": (["7.3"], ["practical"]),
    "2023-h404-01-q2bii": (["3.6", "3.3"], ["maths"]),
    "2023-h404-01-q2biii": (["3.6", "5.3"], ["maths"]),
    "2023-h404-01-q2biv": (["3.6", "5.3"], ["maths"]),
    "2023-h404-01-q2bv": (["3.5", "3.6"], ["maths", "technical"]),
    "2023-h404-01-q3ai": (["1.3"], ["design"]),
    "2023-h404-01-q3aii": (["7.2", "7.3"], ["practical"]),
    "2023-h404-01-q3b": (["2.3"], ["design"]),
    "2023-h404-01-q4a": (["3.2"], ["design"]),
    "2023-h404-01-q4bi": (["6.2", "3.6"], ["maths"]),
    "2023-h404-01-q4bii": (["6.2", "3.6"], ["maths"]),
    "2023-h404-01-q4ci": (["6.4", "6.5"], ["technical"]),
    "2023-h404-01-q4cii": (["6.5"], ["technical"]),
    "2023-h404-01-q4ciii": (["6.5"], ["technical"]),
    "2023-h404-01-q4civ": (["6.5"], ["technical"]),

    # 2023-summer-02
    "2023-h404-02-q1": (["3.1", "3.5"], ["design"]),
    "2023-h404-02-q2": (["3.2", "7.4"], ["design", "technical"]),
    "2023-h404-02-q3ai": (["3.6"], ["maths"]),
    "2023-h404-02-q3aii": (["3.6"], ["maths"]),
    "2023-h404-02-q3bi": (["6.4"], ["technical"]),
    "2023-h404-02-q3bii": (["6.4", "3.6"], ["maths"]),
    "2023-h404-02-q4": (["4.1", "6.1", "7.2"], ["practical", "design"]),
    "2023-h404-02-q5": (["6.4", "6.5"], ["technical", "design"]),

    # 2024-summer-01
    "2024-h404-01-q1ai": (["1.3", "9.2"], ["design"]),
    "2024-h404-01-q1aii": (["1.3"], ["design"]),
    "2024-h404-01-q1bi": (["6.2", "3.6"], ["maths"]),
    "2024-h404-01-q1bii": (["6.2"], ["technical"]),
    "2024-h404-01-q1biii": (["5.2", "5.1"], ["technical"]),
    "2024-h404-01-q1ci": (["2.4"], ["design"]),
    "2024-h404-01-q1cii": (["2.4"], ["design"]),
    "2024-h404-01-q2ai": (["3.6", "3.3"], ["maths"]),
    "2024-h404-01-q2aii": (["3.6", "5.3"], ["maths"]),
    "2024-h404-01-q2aiii": (["7.2", "7.3"], ["practical"]),
    "2024-h404-01-q2bi": (["6.4", "3.6"], ["maths"]),
    "2024-h404-01-q2bii": (["6.4", "3.6"], ["maths"]),
    "2024-h404-01-q2biii": (["6.4"], ["technical"]),
    "2024-h404-01-q3a": (["2.4", "3.1"], ["design"]),
    "2024-h404-01-q3b": (["7.5"], ["technical"]),
    "2024-h404-01-q4a": (["1.3", "3.2"], ["design"]),
    "2024-h404-01-q4bi": (["3.6"], ["maths"]),
    "2024-h404-01-q4bii": (["3.6"], ["maths"]),
    "2024-h404-01-q4ci": (["6.5", "4.3"], ["technical"]),
    "2024-h404-01-q4cii": (["6.4", "6.5"], ["technical", "design"]),
    "2024-h404-01-q4d": (["3.4"], ["design"]),

    # 2024-summer-02
    "2024-h404-02-q1": (["9.2", "7.5"], ["technical"]),
    "2024-h404-02-q2": (["3.2", "7.4"], ["design"]),
    "2024-h404-02-q3ai": (["3.6", "6.3"], ["maths"]),
    "2024-h404-02-q3aii": (["6.3", "3.6"], ["maths"]),
    "2024-h404-02-q3aiii": (["6.3", "3.6"], ["maths"]),
    "2024-h404-02-q3b": (["7.2", "3.6"], ["maths", "practical"]),
    "2024-h404-02-q4": (["6.4", "6.2"], ["technical", "design"]),
    "2024-h404-02-q5": (["3.1", "3.2"], ["design"]),
}

for q in d["questions"]:
    qid = q["id"]
    if qid in TOPIC_SKILL_MAP:
        topics, skills = TOPIC_SKILL_MAP[qid]
        q["topics"] = topics
        q["skills"] = skills

        # Ensure question has clean number
        if "question_number" in q and q["question_number"]:
            raw_prompt = q.get("question", "")
            q["prompt"] = raw_prompt
            q["question"] = q["question_number"]
            # Generate clean summary
            clean_text = raw_prompt.replace("\n", " ").strip()
            if len(clean_text) > 130:
                q["summary"] = clean_text[:127] + "..."
            else:
                q["summary"] = clean_text

    # Ensure all questions have list for figures
    if "figures" not in q or q["figures"] is None:
        q["figures"] = []
    # Ensure all questions have list for topics and skills
    if "topics" not in q or q["topics"] is None:
        q["topics"] = []
    if "skills" not in q or q["skills"] is None:
        q["skills"] = []

with open(Q_PATH, "w", encoding="utf-8") as f:
    json.dump(d, f, indent=2)

print(f"Successfully normalized schema for all questions in questions.json!")
