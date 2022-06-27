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

    with open(input_json_path, 'r') as f:
        students_dict = json.load(f)

    for v in students_dict.values():
        for ele in v["registered_courses"]:
            if course_name in ele:
                students_in_the_course.append(v["student_name"])


    return students_in_the_course


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    students_in_course_dict = {}
    # sort = True
    # separator = " "

    with open(input_json_path, 'r') as f:
        students_dict = json.load(f)

    for v in students_dict.values():
        for ele in v["registered_courses"]:
            if ele in students_in_course_dict:
                students_in_course_dict[ele] += 1
            else:
                students_in_course_dict[ele] = 1

    with open(output_file_path, 'w') as f:
        for k, v in sorted(students_in_course_dict.items()):
            temp = '"{}" {}\n'.format(k, v)
            f.write(temp)

    #    json.dump(students_in_course_dict, f, separators=("\n", " "), sort_keys=sort)



def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    pass



