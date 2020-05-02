#!/usr/local/Python-3.7/bin/python
import cgi
import pymysql



# retrieve form data, if any
form = cgi.FieldStorage()

#check if form data is returned
if form:

    # Connect to the database.
    connection = pymysql.connect(host='bioed.bu.edu',database='cwill96',user='cwill96',password='cwill96',port=4253)
    cursor = connection.cursor()


    # check if submit button was clicked
    submit = form.getvalue("submit")
    if submit:
        #get the pathway
        path_name = form.getvalue("path_name")
        gene_name = form.getvalue("gene_name")
        
        #specify the query for the interacting proteins
        query = """
        select name, quantity, price
        from Products natural join Categories
        where category = '%s' and name ='%s'
 
        """%(gene_name,path_name)
        
        #execute the query
        cursor.execute(query)
        rows=cursor.fetchall()

        #start http return 
        print("Content-type: text/html\n")
        #print the rows of the response
        for row in rows:
            print(row[0],row[1],row[2])

 
        
    #otherwise, one of the drop down menus was clicked
    else:
        table = form.getvalue("table")

        #specify the query for the gene table
        if (table == "Categories"):
            query = """
            select category
            from Categories
            """
        else: 
            #specify the query for the pathway table
            #note that the gene_name was sent from the form to be included in the query
            if (table == "Products"):
                cate_name = form.getvalue("cate_name")      
                query = """
                select name
				from Products natural join Categories
				where category = '%s'

                """%(cate_name)
            else: 
            #specify the query for the pathway table
            #note that the gene_name was sent from the form to be included in the query
                table1=form.getvalue("table1")
    
                if (table1 == "Categories1"):
                    gene_name = form.getvalue("gene_name") 
                    path_name = form.getvalue("path_name")     
                    query = """
                    select quantity
                    from Products natural join Categories
                    where category = '%s' and name ='%s'

                    """%(gene_name,path_name)

        #execute the query
        cursor.execute(query)
        rows=cursor.fetchall()
                
        #start http return 
        print("Content-type: text/html\n")
        #print the rows of the response
        for row in rows:
            print(row[0])
   
else:
    #no form data, just print an empty http header
    print("working")




