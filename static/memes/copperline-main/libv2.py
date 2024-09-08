def trim_float(number):
    return float(f'{number:.2f}')

def add_mapping(id):
    import pyodbc
    import pandas as pd
    # Define the connection string
    server = 'copperlinesql.database.windows.net'
    database = 'mycopperline'
    username = 'Copperadmin'
    password = 'HelpMe=0'
    conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    # Connect to the database
    conn = pyodbc.connect(conn_str)

    # Define the query
    query1 = f'insert into mapping values({id})'

    cursor = conn.cursor()
    cursor.execute(query1)

    cursor.commit()
    conn.close()
    
def get_data(data):
    import pyodbc
    import pandas as pd
    # Define the connection string
    server = 'copperlinesql.database.windows.net'
    database = 'mycopperline'
    username = 'Copperadmin'
    password = 'HelpMe=0'
    # server = 'LAPTOP-O1482QPD\SQLEXPRESS'
    # database = 'copperline'
    # username = 'kousa'
    # password = 'koushikKP1'
    conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    # Connect to the database
    conn = pyodbc.connect(conn_str)

    # Define the query
    query1 = 'SELECT * FROM '+data

    query2 = '''UPDATE Invoice
SET Quantity = (
  SELECT Quantity FROM Invoice AS I2
  WHERE I2.Invoice_Date = Invoice.Invoice_Date
  AND I2.PO_ID = Invoice.PO_ID
  AND I2.Item_name IS NULL AND I2.Unit_cost IS NULL AND I2.Amount IS NULL
)
WHERE Quantity IS NULL AND Item_name IS NOT NULL AND Unit_cost IS NOT NULL AND Amount IS NOT NULL AND Invoice_ID IS NOT NULL AND Invoice_Date IS NOT NULL AND PO_ID IS NOT NULL;

DELETE FROM Invoice WHERE Invoice_Date = Invoice_Date
  AND PO_ID = Invoice.PO_ID
  AND Item_name IS NULL AND Unit_cost IS NULL AND Amount IS NULL
  
DELETE FROM Invoice WHERE Quantity IS NULL AND Item_name IS NULL;

  '''
    # Execute the query and fetch the results
    cursor = conn.cursor()
    cursor.execute(query2)
    cursor.commit()
    cursor.execute(query1)
    results = cursor.fetchall()

    rows=[]
    # Print the results
    for row in results:

        rows+=[list(row)]
    if data=='PO':
        df = pd.DataFrame(rows,columns=['Quantity','Item Name','Unit Cost','Amount','PO_ID'])
    elif data=='Invoice':
        df= pd.DataFrame(rows,columns=['Quantity','Item Name','Unit Cost','Amount','Invoice_ID','Invoice_Date','PO_ID'])
        
    # Close the connection
    conn.close()
    return df

def Mapping(po,df):
    
    import numpy as np
    import pandas as pd
    import json
    import spacy
    nlp = spacy.load("en_core_web_sm")
    with open("embeddings.json", "r") as infile:
        embeds = json.load(infile)
    d1=po['Unit Cost']
    d2=df['Unit Cost']
    # Apply the function to a column
    d1 = d1.apply(trim_float)
    # Apply the function to a column
    d2 = d2.apply(trim_float)
    item=[]
    qty=[]
    cost=[]
    for i in range(len(d2)):#d2 df
        it=[]
        q=[]
        c=[]
        for j in range(len(d1)):#d1 po
            try:
                a=embeds[po.iloc[j]['Item Name']]

            except:
                a=nlp(po.iloc[j]['Item Name']).vector.tolist()
                embeds[po.iloc[j]['Item Name']]=a

            try:
                b=embeds[df.iloc[i]['Item Name']]
            except:
                b=nlp(df.iloc[i]['Item Name']).vector.tolist()
                embeds[df.iloc[i]['Item Name']]=b
            similarity = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
            if d2[i]==d1[j] and similarity>0:
                it+=[po.iloc[j]['Item Name']]
                q+=[str(po.iloc[j]['Quantity'])]
                c+=[str(po.iloc[j]['Unit Cost'])]
        if it==[]:
            it+=['']
            q+=['']
            c+=['']
        item+=it
        qty+=q
        cost+=c
        temp=pd.DataFrame({'PO Quantity':qty,'PO Item Name':item,'PO Unit Cost':cost})
    with open("embeddings.json", "w") as outfile:
        json.dump(embeds, outfile)
    return temp
