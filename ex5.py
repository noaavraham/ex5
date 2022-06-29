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

    for value in students_dict.values():
        for element in value[registered_courses_key]:
            if course_name in element:
                students_in_the_course.append(value[student_name_key])

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

    for value in students_dict.values():
        for element in value[registered_courses_key]:
            if element in students_in_course_dict:
                students_in_course_dict[element] += 1
            else:
                students_in_course_dict[element] = 1

    with open(output_file_path, 'w') as f:
        for key, value in sorted(students_in_course_dict.items()):
            temp = '"{}" {}\n'.format(key, value)
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

            for value in courses_dict.values():
                for element in value[lecturers_key]:
                    if element in lecturers_courses:
                        if value[course_name_key] not in lecturers_courses[element]:
                            lecturers_courses[element].append(value[course_name_key])

                    else:
                        lecturers_courses[element] = [value[course_name_key]]

    with open(output_json_path, 'w') as f:
        json.dump(lecturers_courses, f, indent=4)
