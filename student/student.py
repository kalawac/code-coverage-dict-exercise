def create_student(name, level, courses):
    if not courses:
        courses = []

    return {
        "name": name,
        "level": level,
        "courses": courses,
    }

def add_class(student, course_name):
    student["courses"].append(course_name)

def get_num_classes(student):
    return len(student["courses"])

def summary(student):
    return (
        f"{student['name']} is a {student['level']} enrolled in "
        f"{get_num_classes(student)} classes"
    )

def get_student_with_more_classes(student_a, student_b):
    if get_num_classes(student_a) > get_num_classes(student_b):
        return student_a
    return student_b
