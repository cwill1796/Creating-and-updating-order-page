#!/usr/local/Python-3.7/bin/python
import pymysql
import sys
import cgi
import mysql.connector
import cgitb
cgitb.enable()

myuser = "cwill96"
mypassword = "cwill96"



form = cgi.FieldStorage()

if form:

    # Connect to the database.
    connection = mysql.connector.connect(host='bioed.bu.edu', user=myuser, password=mypassword, database='cwill96', port='4253')
    cursor = connection.cursor()

    # check if submit button was clicked
    submit = form.getvalue("submit")
    if submit:
        path_name = form.getvalue("path_name")
        #specify the query for the interacting proteins
        query = """
        select category
        from Categories = '%s' 
        """%(path_name)
        
        #execute the query
        cursor.execute(query)
        rows=cursor.fetchall()

        #start http return 
        print("Content-type: text/html\n")
        #print the rows of the response
        for row in rows:
            print(row[0],row[1])
                    
    #otherwise, one of the drop down menus was clicked
    else:
        table = form.getvalue("table")

        #specify the query for the gene table
        if (table == "Catergoies"):
            query = """
            select category
            from Categories
            """
        else: 
            #specify the query for the pathway table
            #note that the gene_name was sent from the form to be included in the query
            if (table == "Products"):
                Categories = form.getvalue("Categories")      
                query = """
                select name
                from Products natural join Categories
                where category = '%s'

                """%(Categories)

        #execute the query
        cursor.execute(query)
        rows=cursor.fetchall()

        #start http return 
        print("Content-type: text/html\n")
        #print the rows of the response
        for row in rows:
            print(row[0])

