import os

from omniparser.gradebook_parser import calculate_average_grade_from_csv


#
# CSV VERSION
#
#calculate average fucntin doesn't exist, to invoke function, and 

# in notes file path construction, in the directory, navigate up in hte directory and to that file, don't use slashes
def test_calculate_average_grade_from_csv():
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
    assert calculate_average_grade_from_csv(gradebook_filepath) == 90.64

    prev_gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.csv")
    assert calculate_average_grade_from_csv(prev_gradebook_filepath) == 83.64

#
# JSON VERSION
#

#def test_calculate_average_grade_from_json():
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.json")
    assert calculate_average_grade_from_json(gradebook_filepath) == 90.64

    prev_gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.json")
    assert calculate_average_grade_from_json(prev_gradebook_filepath) == 83.64
