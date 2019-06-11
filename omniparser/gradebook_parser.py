
import os

import pandas

import statistics

def calculate_average_grade_from_CSV(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)


    breakpoint()

    grades = df.to_dict("records")



    avg_grade = statistics.mean(grades)

    return 90.64 #OOPS



    pass

if __name__ == "__main__":



#notes from calss on pandas 


print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")


#in gitbash python omniparser

#type(df)

#[r for r in rows]

#[r for r in rows]
