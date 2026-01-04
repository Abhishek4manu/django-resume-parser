import re

def parse_resume_data(text):
    email = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
    phone = re.findall(r"\+?\d[\d -]{8,}\d", text)

    return {
        "name": extract_name(text),
        "email": email[0] if email else None,
        "phone": phone[0] if phone else None,
        "skills": extract_section(text, "skills"),
        "education": extract_section(text, "education"),
        "experience": extract_section(text, "experience"),
    }
def extract_section(text, keyword):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    section = []
    capture = False
    SECTION_HEADERS = ["skills", "experience", "education", "projects"]


    for line in lines:
        lower = line.lower()

        if keyword.lower() == lower:
            capture = True
            continue

        if capture and lower in SECTION_HEADERS:
            break

        if capture:
            section.append(line)

    return section



def extract_name(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    candidates = []

    for idx, line in enumerate(lines[:10]): 
        lower = line.lower()

        
        if lower in {"resume", "cv", "profile","summary","curriculum vitae"}:
            continue
        if ":" in line:
            continue
        if re.search(r"\d", line):
            continue
        if re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", line):
            continue
        if re.search(r"\+?\d[\d -]{8,}\d", line):
            continue

        
        if not re.fullmatch(r"[A-Za-z ]{3,40}", line):
            continue

        words = line.split()
        if not (1 < len(words) <= 4):
            continue

        
        score = 0
        score += 5 if idx < 3 else 2           
        score += 3 if all(w[0].isupper() for w in words) else 0
        score += 2 if len(words) >= 2 else 0

        candidates.append((score, line))

    return max(candidates)[1] if candidates else None
