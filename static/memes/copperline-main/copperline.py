from flask import Flask, render_template, request
import pandas as pd
from lib import *
import numpy as np

app = Flask(__name__)

colors = {}
def getInvoiceColor(invoiceId):
    # Generate and store a random color for each unique invoice ID


    if invoiceId not in colors:
        # Generate a random color for the new invoice ID
        colors[invoiceId] = '#{:06x}'.format(np.random.randint(0, 256**3-1))

    return colors[invoiceId]

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/connection', methods=['GET', 'POST'])
def connection():
    return render_template('connection.html')

@app.route('/source', methods=['GET', 'POST'])  
def source():
    return render_template('source.html')

@app.route('/schedules', methods=['GET', 'POST'])
def schedules():
    return render_template('schedules.html')

@app.route('/logreport', methods=['GET', 'POST'])
def logreport():
    return render_template('logreport.html')

@app.route('/mapping', methods=['GET', 'POST'])
def mapping():
    po=get_data('PO')
    inv=get_data('Invoice')
    po_no = request.args.get('po')
    print(po_no)
    if po_no:
        add_mapping(po_no)
    pos=list(po['PO_ID'].unique())
    temp_l=[]
    for i in pos:
        l=len(inv.loc[inv['PO_ID']==i].reset_index().drop('index',axis=1)['Invoice_ID'].unique())
        temp_l+=[l]
    temp_df=pd.DataFrame([pos,temp_l]).T
    return render_template('mapping.html',df=temp_df,po_no=po_no)

# @app.route('/')
# def home():
#     return render_template('home.html', active_tab='home')

# @app.route('/products')
# def products():
#     return render_template('products.html', active_tab='products')


@app.route('/map', methods=['GET', 'POST'])
def map():
    po=get_data('PO')
    inv=get_data('Invoice')
    po_no = request.args.get('po').replace(" ", "")
    print(po_no)
    temp=inv.loc[inv['PO_ID']==po_no].reset_index().drop('index',axis=1)
    print(temp)
    temp_po=po.loc[po['PO_ID']==temp['PO_ID'][0]].reset_index().drop('index',axis=1)
    PO=Mapping(temp_po,temp)
    po_ct = np.count_nonzero(np.count_nonzero(np.array(temp_po), axis=1))
    inv_ct = np.count_nonzero(np.count_nonzero(np.array(temp), axis=1))
    return render_template('map.html',inv_ct=inv_ct, getInvoiceColor=getInvoiceColor, po_ct=po_ct,invoice_df=temp,inv_column_names=PO.columns,purchase_order_df=PO,column_names=inv.columns,po_no=po_no)



if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')

