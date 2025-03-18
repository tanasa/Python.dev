import os
import sys

def process_file(filename):
    """
    Processes the file : it extracts the names of the courses.
    Parameters:
        filename (str)

    Returns:
        list: list of courses.
    """

    with open(filename, 'r') as fin:
        content = fin.read()

    lines = content.splitlines()
    courses = []

    for line in lines:
        # Strip extra whitespace
        if line.strip().endswith(('unit', 'units')):
            # Find the index of the last comma
            last_comma_index = line.rindex(',')
            # Extract the course name from the beginning to the last comma
            courseName = line[:last_comma_index]
            # Strip any '*' characters from the course name
            courseName = courseName.replace('*', '')
            courses.append(courseName)

    return courses

if __name__ == "__main__":
    courses1 = process_file("course-list1.txt")
    courses2 = process_file("course-list2.txt")
    courses3 = process_file("course-list3.txt")

    common_courses = list(set(courses1) & set(courses2) & set(courses3))
    print("common core classes :", common_courses)

