
import os

import pandas

import statistics

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
