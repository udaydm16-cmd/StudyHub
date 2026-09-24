from data import students


def get_student_by_id(student_id):
    """Find a student using their unique ID."""

    for student in students:
        if student["id"] == student_id:
            return student

    return None


def search_students(name=None, class_name=None):
    """Search students by name or class."""

    results = students

    if name:
        results = [
            student
            for student in results
            if name.lower() in student["name"].lower()
        ]

    if class_name:
        results = [
            student
            for student in results
            if student["class"].lower() == class_name.lower()
        ]

    return results


def get_student_progress(student_id):
    """Return a student's current learning levels."""

    student = get_student_by_id(student_id)

    if not student:
        return None

    return {
        "student_id": student["id"],
        "name": student["name"],
        "class": student["class"],
        "skills": student["skills"]
    }


def get_class_students(class_name):
    """Return all students in a class."""

    return [
        student
        for student in students
        if student["class"].lower() == class_name.lower()
    ]


def find_students_needing_support(subject=None, skill=None):
    """Find students whose scores indicate they may need support."""

    results = []

    for student in students:

        weak_skills = []

        for subject_name, skills in student["skills"].items():

            if subject and subject_name.lower() != subject.lower():
                continue

            for skill_name, score in skills.items():

                if skill and skill_name.lower() != skill.lower():
                    continue

                if score < 50:
                    weak_skills.append({
                        "subject": subject_name,
                        "skill": skill_name,
                        "score": score
                    })

        if weak_skills:

            results.append({
                "student_id": student["id"],
                "name": student["name"],
                "class": student["class"],
                "weak_skills": weak_skills
            })

    return results


def find_improving_students():
    """
    Placeholder for future trajectory analysis.

    This will use historical assessment data once
    the real backend is connected.
    """

    return []