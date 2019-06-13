
import os

import pandas

import statistics

import json

def calculate_average_grade_from_CSV(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)

    #df = dataframe, from pandas package


    breakpoint()

    rows = df.to_dict("records")

    #to_dict = function convert DF to dictionary. isolating. 

    grades = [r["final_grade"] for r ]

    avg_grade = statistics.mean(grades)


    # or
    # grades = df["final_grade"].to_list
    #avg_grade = statistics.mean(grades)
    #or
    #df avg_grade = sf["Final_grade"].mean()

    

    return 90.64 #OOPS



    pass

#tests all the code below
#name is checking the main variable. 
if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE")


#constructing the file path. working on any operating system or any directory. to get rid of slashes from mac and microsoft
#__File__ references omniparser/gradebook_parser.py
#take that file and , import os module, os.path.dirname(__File__)
#os.path.join to joinh together parts of the filepath
#omniparser directory?, .. directory, data directory, gradebook directory
#os.path.isfile(gradebook_filepath), will return true if a file exists

#would be equal to gradebook_filepath = "#C:\Users\dmccollum\Documents\GitHub\omniparser-starter-py"

#gradebook_filepath = /data/gradebook_2019.csv

#

#df is a data frame from the pandas package

gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")

print(gradebook_filepath)

#C:\Users\dmccollum\Documents\GitHub\omniparser-starter-py
#cd C:/Users/dmccollum/Documents/GitHub/omniparser-starter-py




#notes from calss on pandas 


print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")


#in gitbash python omniparser

#type(df)

#[r for r in rows]

#[r for r in rows]

#JSON

# must import json

#defining a function, must be before name = main
def avg = calculate_average_grade_from_json(filepath_x):
    #breakpoint()
    # r = read, W would be right
    # print shows the type of object
    #contents within the file are string
    # use the files as variable f
    #method called read. stringer verions
    #but want to work in in dictionaryuse json.loads and get back dictionary


    with open(filepath_x, "r") as f:
        print(type(f))
        file_contents = f.read()
        print(type(file_contents = json_file.read() ==

    gradebook = json.loads(file_contents)

    print(type(gradebook))
    print(gradebook)

    students = gradebook["students"]

    #listcomprehensions start with a square bracket because its a list

    [s["finalGrade"]] for s in students]
    #import statistics
    #for eah item in our students list return a mapped attribute

    avg_grade = statistics.mean()

    return 10000
    #will return hardcoded value
    #breakpoint lies within the function

if __name__ == "__main__":
#must indent
#gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.json")
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.json")
    print(gradebook_filepath)
    print(.os.path.isfile(gradebook_filepath))
    avg = calculate_average_grade_from_json(gradebook_filepath)) #>TRUE
    print(avg)




    

# omniparser/gradebook_parser.py

import json
import os
import statistics

import pandas

def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)

    #breakpoint()
    # avg_grade = df["final_grade"].mean()

    #rows = df.to_dict("records")
    #grades = [r["final_grade"] for r in rows] #> [86.7, 95.1, 60.3, 99.8, 97.4, 85.5, 97.2, 98.0, 93.9, 92.5]
    #avg_grade = statistics.mean(grades)

    #grades =  df["final_grade"].to_list()
    #avg_grade = statistics.mean(grades)

    avg_grade = df["final_grade"].mean()

    return avg_grade #90.64 #"OOPS"

def calculate_average_grade_from_json(x):
    with open(x, "r") as f:
        #print(type(f)) #> Text IO
        file_contents = f.read()
        #print(type(file_contents)) #> str

    gradebook = json.loads(file_contents)
    #print(type(gradebook))
    #print(gradebook)

    #breakpoint()
    students = gradebook["students"]
    grades = [s["finalGrade"] for s in students]
    avg_grade = statistics.mean(grades)
    return avg_grade


if __name__ == "__main__":
    #print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
    #gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
    ##gradebook_filepath = "C:/Users/Mike/Documents/GitHub/omniparser-starter-py/data/gradebook_2019.csv"
    ##gradebook_filepath = "data/gradebook_2019.csv"
    #print(gradebook_filepath)
    #avg = calculate_average_grade_from_csv(gradebook_filepath)
    #print(avg)

    print("PARSING SOME JSON GRADEBOOK FILES HERE...")
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.json")
    print(gradebook_filepath) #>  c:\users\mike\documents\github\omniparser-starter-py\omniparser\gradebook_parser.py
    print(os.path.isfile(gradebook_filepath)) #> True
    avg = calculate_average_grade_from_json(gradebook_filepath)
    print(avg)
