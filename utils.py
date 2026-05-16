from skills import SKILLS

def extract_skills(text):

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))


def missing_skills(found_skills):

    missing = []

    for skill in SKILLS:
        if skill not in found_skills:
            missing.append(skill)

    return missing