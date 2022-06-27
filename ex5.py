import json
import os


def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    students_in_the_course = []
    registered_courses_key = "registered_courses"
    student_name_key = "student_name"

    with open(input_json_path, 'r') as f:
        students_dict = json.load(f)

    for v in students_dict.values():
        for ele in v[registered_courses_key]:
            if course_name in ele:
                students_in_the_course.append(v[student_name_key])

    return students_in_the_course


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    students_in_course_dict = {}
    registered_courses_key = "registered_courses"

    with open(input_json_path, 'r') as f:
        students_dict = json.load(f)

    for v in students_dict.values():
        for ele in v[registered_courses_key]:
            if ele in students_in_course_dict:
                students_in_course_dict[ele] += 1
            else:
                students_in_course_dict[ele] = 1

    with open(output_file_path, 'w') as f:
        for k, v in sorted(students_in_course_dict.items()):
            temp = '"{}" {}\n'.format(k, v)
            f.write(temp)


def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    lecturers_courses = {}
    lecturers_key = "lecturers"
    course_name_key = "course_name"

    for json_file in os.listdir(json_directory_path):
        if json_file.endswith('.json'):
            json_file_path = os.path.join(json_directory_path, json_file)

            with open(json_file_path, 'r') as f:
                courses_dict = json.load(f)

            for v in courses_dict.values():
                for ele in v[lecturers_key]:
                    if ele in lecturers_courses:
                        if v[course_name_key] not in lecturers_courses[ele]:
                            lecturers_courses[ele].append(v[course_name_key])

                    else:
                        lecturers_courses[ele] = [v[course_name_key]]

    with open(output_json_path, 'w') as f:
        json.dump(lecturers_courses, f, indent=4)
