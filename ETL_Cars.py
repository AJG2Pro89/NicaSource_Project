# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:39:44 2023

@author: alberto.garcia
"""
import psycopg2

conn = psycopg2.connect(
    host= "us-east.connect.psdb.cloud",
    user= "2apdlsldndll6j6k9aqh",
    password= "pscale_pw_sgroSPwIl1d7AC9yTQtxTJMJJC4Uml1n8gritmXF4r",
    database="nicasource",
    port='5432'
)

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()