#!/usr/bin/env python3

from pyspark.sql import SparkSession
import logging
import sys

__author__ = "Alex Ciobanu"
__copyright__ = "Copyright 2019, Cloudera"
__credits__ = ["Alex ciobanu"]
__license__ = "commercial"
__version__ = "1.0"
__maintainer__ = "Everybody"
__email__ = "alex.ciobanu@cloudera.com"
__status__ = "Development"

'''
This is a sample application in pyspark 


'''

"""
This is the main function of the application it, creates the spark. hdfs and impala connections
gathers all of the tables that need compressing from the input file, 
goes through each partition and compresses the content ( if needed ) than checks everything went OK


Parameters
----------
args

Returns
-------
Return code of application

Raises
------
None
"""


def main():
    # Build the sparkSession and set application name from config file
    spark = SparkSession.builder.appName("Example").getOrCreate()
    # Setting LogLevel for the sparkContext from config file
    spark.sparkContext.setLogLevel("INFO")
    # Create variables with the table names
    table1_name = "default.sample_07"
    table2_name = "default.sample_08"
    # Pull the data into dataframes
    query1 = f"select * from {table1_name}"
    query2 = f"select * from {table2_name}"
    t1_buff = spark.sql(query1)
    t2_buff = spark.sql(query2)
    # Create alias for the tables so they can be used in joins    
    t1 = t1_buff.alias('t1')
    t2 = t2_buff.alias('t2')
    # Do a simple filter on a table     
    filtered = t1.filter("salary > 50000")
    filtered.show()
    # Do a join of two tables
    joined = t1.join(t2, t1.code == t2.code )
    joined.show()
    # Pipeline multiple functions, a join and a filter
    combined = t1.filter("salary > 50000").join(t2, t1.code == t2.code )
    combined.show()

if __name__ == "__main__":
    main()
