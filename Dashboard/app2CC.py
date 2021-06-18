# Flask : library utama untuk membuat API
# render_template : agar dapat memberikan respon file html
# request : untuk membaca data yang diterima saat request datang
from flask import Flask, render_template, request
# plotly dan plotly.graph_objs : membuat plot
import plotly
import plotly.graph_objs as go
# pandas : untuk membaca csv dan men-generate dataframe
import pandas as pd
import json
from sqlalchemy import create_engine

## Joblib untuk Load Model
import joblib

# untuk membuat route
app = Flask(__name__)

###################
## CATEGORY PLOT ##
###################

# IMPORT DATA USING pd.read_csv
CC = pd.read_csv('./static/CC.csv')

# # # IMPORT DATA USING pd.read_sql
# sqlengine = create_engine('mysql+pymysql://root:agdees11@127.0.0.1:3307/flaskapp', pool_recycle=3605)
# dbConnection = sqlengine.connect()
# engine = sqlengine.raw_connection()
# cursor = engine.cursor()
# CC = pd.read_sql("select * from CC", dbConnection)

# category plot function
def category_plot(
    cat_plot = 'histplot',
    cat_x = 'TENURE', cat_y = 'BALANCE',
    estimator = 'count', hue = 'SEGMENT'):

    # generate dataframe CC.csv
    # CC = pd.read_csv('./static/CC.csv')



    # jika menu yang dipilih adalah histogram
    if cat_plot == 'histplot':
        # siapkan list kosong untuk menampung konfigurasi hist
        data = []
        # generate config histogram dengan mengatur sumbu x dan sumbu y
        for val in CC[hue].unique():
            hist = go.Histogram(
                x=CC[CC[hue]==val][cat_x],
                y=CC[CC[hue]==val][cat_y],
                histfunc=estimator,
                name=str(val)
            )
            #masukkan ke dalam array
            data.append(hist)
        #tentukan title dari plot yang akan ditampilkan
        title='Histogram'
    elif cat_plot == 'boxplot':
        data = []

        for val in CC[hue].unique():
            box = go.Box(
                x=CC[CC[hue] == val][cat_x], #series
                y=CC[CC[hue] == val][cat_y],
                name = str(val)
            )
            data.append(box)
        title='Box'
    # menyiapkan config layout tempat plot akan ditampilkan
    # menentukan nama sumbu x dan sumbu y
    if cat_plot == 'histplot':
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title='person'),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )
    else:
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title=cat_y),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )
    #simpan config plot dan layout pada dictionary
    result = {'data': data, 'layout': layout}

    #json.dumps akan mengenerate plot dan menyimpan hasilnya pada graphjson
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

# akses halaman menuju route '/' untuk men-test
# apakah API sudah running atau belum

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def index():

    plot = category_plot()
    # dropdown menu
    # kita lihat pada halaman dashboard terdapat menu dropdown
    # terdapat lima menu dropdown, sehingga kita mengirimkan kelima variable di bawah ini
    # kita mengirimnya dalam bentuk list agar mudah mengolahnya di halaman html menggunakan looping
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('TENURE', 'Tenure'), ('BALANCE_GROUP', 'Balance Group'), ('BALANCE_FREQ_GROUP', 'Balance Frequency Group'),
    ('PURCHASES_GROUP', 'Purchases Group'), ('ONEOFF_PURCHASES_GROUP', 'One-Off Purchases Group'), ('INSTALLMENTS_PURCHASES_GROUP', 'Installment Purchases Group'),
    ('CASH_ADVANCE_GROUP', 'Cash Advance Group'), ('PURCHASES_FREQ_GROUP', 'Purchases Frequency Group'), ('ONEOFF_PURCHASES_FREQ_GROUP', 'One-Off Purchases Frequency Group'),
    ('PURCHASES_INSTALLMENTS_FREQ_GROUP', 'Purchases Installments Frequency Group'), ('CASH_ADVANCE_FREQ_GROUP', 'Cash Advance Frequency Group'),
    ('CASH_ADVANCE_TRX_GROUP', 'Cash Advance Transaction Group'), ('PURCHASES_TRX_GROUP', 'Purchases Transaction Group'),
    ('CREDIT_LIMIT_GROUP', 'Credit Limit Group'), ('PAYMENTS_GROUP', 'Payment Group'), ('MIN_PAYMENTS_GROUP', 'Minimum Payments Group'),
    ('PRC_FULL_PAYMENT_GROUP', 'Percent of Full Payment Group'), ('SEGMENT', 'Segment')]

    list_y = [('BALANCE', 'Balance'), ('BALANCE_FREQUENCY', 'Balance Frequency'), ('PURCHASES', 'Purchases'), 
    ('ONEOFF_PURCHASES', 'One-Off Purchases'), ('INSTALLMENTS_PURCHASES', 'Installment Purchases'), ('CASH_ADVANCE', 'Cash Advance'),
    ('PURCHASES_FREQUENCY', 'Purchases Frequency'), ('ONEOFF_PURCHASES_FREQUENCY', 'One-Off Purchases Frequency'),
    ('PURCHASES_INSTALLMENTS_FREQUENCY', 'Purchases Installments Frequency'), ('CASH_ADVANCE_FREQUENCY', 'Cash Advance Frequency'),
    ('CASH_ADVANCE_TRX', 'Cash Advance Transaction'), ('PURCHASES_TRX', 'Purchases Transaction'),
    ('CREDIT_LIMIT', 'Credit Limit'), ('PAYMENTS', 'Payment'), ('MINIMUM_PAYMENTS', 'Minimum Payments'),
    ('PRC_FULL_PAYMENT', 'Percent of Full Payment')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('TENURE', 'Tenure'), ('BALANCE_GROUP', 'Balance Group'), ('BALANCE_FREQ_GROUP', 'Balance Frequency Group'),
    ('PURCHASES_GROUP', 'Purchases Group'), ('ONEOFF_PURCHASES_GROUP', 'One-Off Purchases Group'), ('INSTALLMENTS_PURCHASES_GROUP', 'Installment Purchases Group'),
    ('CASH_ADVANCE_GROUP', 'Cash Advance Group'), ('PURCHASES_FREQ_GROUP', 'Purchases Frequency Group'), ('ONEOFF_PURCHASES_FREQ_GROUP', 'One-Off Purchases Frequency Group'),
    ('PURCHASES_INSTALLMENTS_FREQ_GROUP', 'Purchases Installments Frequency Group'), ('CASH_ADVANCE_FREQ_GROUP', 'Cash Advance Frequency Group'),
    ('CASH_ADVANCE_TRX_GROUP', 'Cash Advance Transaction Group'), ('PURCHASES_TRX_GROUP', 'Purchases Transaction Group'),
    ('CREDIT_LIMIT_GROUP', 'Credit Limit Group'), ('PAYMENTS_GROUP', 'Payment Group'), ('MIN_PAYMENTS_GROUP', 'Minimum Payments Group'),
    ('PRC_FULL_PAYMENT_GROUP', 'Percent of Full Payment Group'), ('SEGMENT', 'Segment')]

    return render_template(
        # file yang akan menjadi response dari API
        'category.html',
        # plot yang akan ditampilkan
        plot=plot,
        # menu yang akan tampil di dropdown 'Jenis Plot'
        focus_plot='histplot',
        # menu yang akan muncul di dropdown 'sumbu X'
        focus_x='TENURE',

        # untuk sumbu Y tidak ada, nantinya menu dropdown Y akan di disable
        # karena pada histogram, sumbu Y akan menunjukkan kuantitas data

        # menu yang akan muncul di dropdown 'Estimator'
        focus_estimator='count',
        # menu yang akan tampil di dropdown 'Hue'
        focus_hue='SEGMENT',
        # list yang akan digunakan looping untuk membuat dropdown 'Jenis Plot'
        drop_plot= list_plot,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu X'
        drop_x= list_x,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu Y'
        drop_y= list_y,
        # list yang akan digunakan looping untuk membuat dropdown 'Estimator'
        drop_estimator= list_est,
        # list yang akan digunakan looping untuk membuat dropdown 'Hue'
        drop_hue= list_hue)

# ada dua kondisi di mana kita akan melakukan request terhadap route ini
# pertama saat klik menu tab (Histogram & Box)
# kedua saat mengirim form (saat merubah salah satu dropdown) 
@app.route('/cat_fn/<nav>')
def cat_fn(nav):

    # saat klik menu navigasi
    if nav == 'True':
        cat_plot = 'histplot'
        cat_x = 'TENURE'
        cat_y = 'BALANCE'
        estimator = 'count'
        hue = 'SEGMENT'
    
    # saat memilih value dari form
    else:
        cat_plot = request.args.get('cat_plot')
        cat_x = request.args.get('cat_x')
        cat_y = request.args.get('cat_y')
        estimator = request.args.get('estimator')
        hue = request.args.get('hue')

    # Dari boxplot ke histogram akan None
    if estimator == None:
        estimator = 'count'
    
    # Saat estimator == 'count', dropdown menu sumbu Y menjadi disabled dan memberikan nilai None
    if cat_y == None:
        cat_y = 'BALANCE'

    # Dropdown menu
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('TENURE', 'Tenure'), ('BALANCE_GROUP', 'Balance Group'), ('BALANCE_FREQ_GROUP', 'Balance Frequency Group'),
    ('PURCHASES_GROUP', 'Purchases Group'), ('ONEOFF_PURCHASES_GROUP', 'One-Off Purchases Group'), ('INSTALLMENTS_PURCHASES_GROUP', 'Installment Purchases Group'),
    ('CASH_ADVANCE_GROUP', 'Cash Advance Group'), ('PURCHASES_FREQ_GROUP', 'Purchases Frequency Group'), ('ONEOFF_PURCHASES_FREQ_GROUP', 'One-Off Purchases Frequency Group'),
    ('PURCHASES_INSTALLMENTS_FREQ_GROUP', 'Purchases Installments Frequency Group'), ('CASH_ADVANCE_FREQ_GROUP', 'Cash Advance Frequency Group'),
    ('CASH_ADVANCE_TRX_GROUP', 'Cash Advance Transaction Group'), ('PURCHASES_TRX_GROUP', 'Purchases Transaction Group'),
    ('CREDIT_LIMIT_GROUP', 'Credit Limit Group'), ('PAYMENTS_GROUP', 'Payment Group'), ('MIN_PAYMENTS_GROUP', 'Minimum Payments Group'),
    ('PRC_FULL_PAYMENT_GROUP', 'Percent of Full Payment Group'), ('SEGMENT', 'Segment')]
    list_y = [('BALANCE', 'Balance'), ('BALANCE_FREQUENCY', 'Balance Frequency'), ('PURCHASES', 'Purchases'), 
    ('ONEOFF_PURCHASES', 'One-Off Purchases'), ('INSTALLMENTS_PURCHASES', 'Installment Purchases'), ('CASH_ADVANCE', 'Cash Advance'),
    ('PURCHASES_FREQUENCY', 'Purchases Frequency'), ('ONEOFF_PURCHASES_FREQUENCY', 'One-Off Purchases Frequency'),
    ('PURCHASES_INSTALLMENTS_FREQUENCY', 'Purchases Installments Frequency'), ('CASH_ADVANCE_FREQUENCY', 'Cash Advance Frequency'),
    ('CASH_ADVANCE_TRX', 'Cash Advance Transaction'), ('PURCHASES_TRX', 'Purchases Transaction'),
    ('CREDIT_LIMIT', 'Credit Limit'), ('PAYMENTS', 'Payment'), ('MINIMUM_PAYMENTS', 'Minimum Payments'),
    ('PRC_FULL_PAYMENT', 'Percent of Full Payment')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('TENURE', 'Tenure'), ('BALANCE_GROUP', 'Balance Group'), ('BALANCE_FREQ_GROUP', 'Balance Frequency Group'),
    ('PURCHASES_GROUP', 'Purchases Group'), ('ONEOFF_PURCHASES_GROUP', 'One-Off Purchases Group'), ('INSTALLMENTS_PURCHASES_GROUP', 'Installment Purchases Group'),
    ('CASH_ADVANCE_GROUP', 'Cash Advance Group'), ('PURCHASES_FREQ_GROUP', 'Purchases Frequency Group'), ('ONEOFF_PURCHASES_FREQ_GROUP', 'One-Off Purchases Frequency Group'),
    ('PURCHASES_INSTALLMENTS_FREQ_GROUP', 'Purchases Installments Frequency Group'), ('CASH_ADVANCE_FREQ_GROUP', 'Cash Advance Frequency Group'),
    ('CASH_ADVANCE_TRX_GROUP', 'Cash Advance Transaction Group'), ('PURCHASES_TRX_GROUP', 'Purchases Transaction Group'),
    ('CREDIT_LIMIT_GROUP', 'Credit Limit Group'), ('PAYMENTS_GROUP', 'Payment Group'), ('MIN_PAYMENTS_GROUP', 'Minimum Payments Group'),
    ('PRC_FULL_PAYMENT_GROUP', 'Percent of Full Payment Group'), ('SEGMENT', 'Segment')]

    plot = category_plot(cat_plot, cat_x, cat_y, estimator, hue)
    return render_template(
        # file yang akan menjadi response dari API
        'category.html',
        # plot yang akan ditampilkan
        plot=plot,
        # menu yang akan tampil di dropdown 'Jenis Plot'
        focus_plot=cat_plot,
        # menu yang akan muncul di dropdown 'sumbu X'
        focus_x=cat_x,
        focus_y=cat_y,

        # menu yang akan muncul di dropdown 'Estimator'
        focus_estimator=estimator,
        # menu yang akan tampil di dropdown 'Hue'
        focus_hue=hue,
        # list yang akan digunakan looping untuk membuat dropdown 'Jenis Plot'
        drop_plot= list_plot,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu X'
        drop_x= list_x,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu Y'
        drop_y= list_y,
        # list yang akan digunakan looping untuk membuat dropdown 'Estimator'
        drop_estimator= list_est,
        # list yang akan digunakan looping untuk membuat dropdown 'Hue'
        drop_hue= list_hue
    )

##################
## SCATTER PLOT ##
##################

# scatter plot function
def scatter_plot(cat_x, cat_y, hue):


    data = []

    for val in CC[hue].unique():
        scatt = go.Scatter(
            x = CC[CC[hue] == val][cat_x],
            y = CC[CC[hue] == val][cat_y],
            mode = 'markers',
            name = int(val)
        )
        data.append(scatt)

    layout = go.Layout(
        title= 'Scatter',
        title_x= 0.5,
        xaxis=dict(title=cat_x),
        yaxis=dict(title=cat_y)
    )

    result = {"data": data, "layout": layout}

    graphJSON = json.dumps(result,cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/scatt_fn')
def scatt_fn():
    cat_x = request.args.get('cat_x')
    cat_y = request.args.get('cat_y')
    hue = request.args.get('hue')

    # WAJIB! default value ketika scatter pertama kali dipanggil
    if cat_x == None and cat_y == None and hue == None:
        cat_x = 'BALANCE'
        cat_y = 'CREDIT_LIMIT'
        hue = 'SEGMENT'

    # Dropdown menu
    list_x = [('BALANCE', 'Balance'), ('BALANCE_FREQUENCY', 'Balance Frequency'), ('PURCHASES', 'Purchases'), 
    ('ONEOFF_PURCHASES', 'One-Off Purchases'), ('INSTALLMENTS_PURCHASES', 'Installment Purchases'), ('CASH_ADVANCE', 'Cash Advance'),
    ('PURCHASES_FREQUENCY', 'Purchases Frequency'), ('ONEOFF_PURCHASES_FREQUENCY', 'One-Off Purchases Frequency'),
    ('PURCHASES_INSTALLMENTS_FREQUENCY', 'Purchases Installments Frequency'), ('CASH_ADVANCE_FREQUENCY', 'Cash Advance Frequency'),
    ('CASH_ADVANCE_TRX', 'Cash Advance Transaction'), ('PURCHASES_TRX', 'Purchases Transaction'),
    ('CREDIT_LIMIT', 'Credit Limit'), ('PAYMENTS', 'Payment'), ('MINIMUM_PAYMENTS', 'Minimum Payments'),
    ('PRC_FULL_PAYMENT', 'Percent of Full Payment')]
    list_y = [('BALANCE', 'Balance'), ('BALANCE_FREQUENCY', 'Balance Frequency'), ('PURCHASES', 'Purchases'), 
    ('ONEOFF_PURCHASES', 'One-Off Purchases'), ('INSTALLMENTS_PURCHASES', 'Installment Purchases'), ('CASH_ADVANCE', 'Cash Advance'),
    ('PURCHASES_FREQUENCY', 'Purchases Frequency'), ('ONEOFF_PURCHASES_FREQUENCY', 'One-Off Purchases Frequency'),
    ('PURCHASES_INSTALLMENTS_FREQUENCY', 'Purchases Installments Frequency'), ('CASH_ADVANCE_FREQUENCY', 'Cash Advance Frequency'),
    ('CASH_ADVANCE_TRX', 'Cash Advance Transaction'), ('PURCHASES_TRX', 'Purchases Transaction'),
    ('CREDIT_LIMIT', 'Credit Limit'), ('PAYMENTS', 'Payment'), ('MINIMUM_PAYMENTS', 'Minimum Payments'),
    ('PRC_FULL_PAYMENT', 'Percent of Full Payment')]
    list_hue = [('SEGMENT', 'Segment')]
    # list_hue = [('TENURE', 'Tenure'), ('BALANCE_GROUP', 'Balance Group'), ('BALANCE_FREQ_GROUP', 'Balance Frequency Group'),
    # ('PURCHASES_GROUP', 'Purchases Group'), ('ONEOFF_PURCHASES_GROUP', 'One-Off Purchases Group'), ('INSTALLMENTS_PURCHASES_GROUP', 'Installment Purchases Group'),
    # ('CASH_ADVANCE_GROUP', 'Cash Advance Group'), ('PURCHASES_FREQ_GROUP', 'Purchases Frequency Group'), ('ONEOFF_PURCHASES_FREQ_GROUP', 'One-Off Purchases Frequency Group'),
    # ('PURCHASES_INSTALLMENTS_FREQ_GROUP', 'Purchases Installments Frequency Group'), ('CASH_ADVANCE_FREQ_GROUP', 'Cash Advance Frequency Group'),
    # ('CASH_ADVANCE_TRX_GROUP', 'Cash Advance Transaction Group'), ('PURCHASES_TRX_GROUP', 'Purchases Transaction Group'),
    # ('CREDIT_LIMIT_GROUP', 'Credit Limit Group'), ('PAYMENTS_GROUP', 'Payment Group'), ('MIN_PAYMENTS_GROUP', 'Minimum Payments Group'),
    # ('PRC_FULL_PAYMENT_GROUP', 'Percent of Full Payment Group'), ('SEGMENT', 'Segment')]

    plot = scatter_plot(cat_x, cat_y, hue)

    return render_template(
        'scatter.html',
        plot=plot,
        focus_x=cat_x,
        focus_y=cat_y,
        focus_hue=hue,
        drop_x= list_x,
        drop_y= list_y,
        drop_hue= list_hue
    )

##############
## PIE PLOT ##
##############

def pie_plot(hue = 'SEGMENT'):
    


    vcounts = CC[hue].value_counts()

    labels = []
    values = []

    for item in vcounts.iteritems():
        labels.append(item[0])
        values.append(item[1])
    
    data = [
        go.Pie(
            labels=labels,
            values=values
        )
    ]

    layout = go.Layout(title='Pie', title_x= 0.48)

    result = {'data': data, 'layout': layout}

    graphJSON = json.dumps(result,cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/pie_fn')
def pie_fn():
    hue = request.args.get('hue')

    if hue == None:
        hue = 'SEGMENT'

    list_hue = [('TENURE', 'Tenure'), ('BALANCE_GROUP', 'Balance Group'), ('BALANCE_FREQ_GROUP', 'Balance Frequency Group'),
    ('PURCHASES_GROUP', 'Purchases Group'), ('ONEOFF_PURCHASES_GROUP', 'One-Off Purchases Group'), ('INSTALLMENTS_PURCHASES_GROUP', 'Installment Purchases Group'),
    ('CASH_ADVANCE_GROUP', 'Cash Advance Group'), ('PURCHASES_FREQ_GROUP', 'Purchases Frequency Group'), ('ONEOFF_PURCHASES_FREQ_GROUP', 'One-Off Purchases Frequency Group'),
    ('PURCHASES_INSTALLMENTS_FREQ_GROUP', 'Purchases Installments Frequency Group'), ('CASH_ADVANCE_FREQ_GROUP', 'Cash Advance Frequency Group'),
    ('CASH_ADVANCE_TRX_GROUP', 'Cash Advance Transaction Group'), ('PURCHASES_TRX_GROUP', 'Purchases Transaction Group'),
    ('CREDIT_LIMIT_GROUP', 'Credit Limit Group'), ('PAYMENTS_GROUP', 'Payment Group'), ('MIN_PAYMENTS_GROUP', 'Minimum Payments Group'),
    ('PRC_FULL_PAYMENT_GROUP', 'Percent of Full Payment Group'), ('SEGMENT', 'Segment')]

    plot = pie_plot(hue)
    return render_template('pie.html', plot=plot, focus_hue=hue, drop_hue= list_hue)

###############
## UPDATE DB ##
###############
### Menampilkan data dari SQL
@app.route('/db_fn')
def db_fn():
    sqlengine = create_engine('mysql+pymysql://root:agdees11@127.0.0.1:3307/flaskapp', pool_recycle=3605)
    engine = sqlengine.raw_connection()
    cursor = engine.cursor()
    cursor.execute("SELECT * FROM CC")
    data = cursor.fetchall()
    return render_template('update.html', data=data)

@app.route('/update_fn', methods=['POST', 'GET'])
def update_fn():

    if request.method == 'POST':
        input = request.form
        SEGMENT = ''
        if input['SEGMENT'] == 'segment_0':
            SEGMENT = 0
        elif input['SEGMENT'] == 'segment_1':
            SEGMENT = 1
        else:
            SEGMENT = 2
        ## Memasukkan data ke Tabel SQL
        
        new_df = pd.DataFrame({
            'BALANCE' : [float(input['BALANCE'])],
            'BALANCE_FREQUENCY' : [float(input['BALANCE_FREQUENCY'])],
            'PURCHASES' : [float(input['PURCHASES'])],
            'ONEOFF_PURCHASES' : [float(input['ONEOFF_PURCHASES'])],
            'INSTALLMENTS_PURCHASES' : [float(input['INSTALLMENTS_PURCHASES'])],
            'CASH_ADVANCE' : [float(input['CASH_ADVANCE'])],
            'PURCHASES_FREQUENCY' : [float(input['PURCHASES_FREQUENCY'])],
            'ONEOFF_PURCHASES_FREQUENCY' : [float(input['ONEOFF_PURCHASES_FREQUENCY'])],
            'PURCHASES_INSTALLMENTS_FREQUENCY' : [float(input['PURCHASES_INSTALLMENTS_FREQUENCY'])],
            'CASH_ADVANCE_FREQUENCY' : [float(input['CASH_ADVANCE_FREQUENCY'])],
            'CASH_ADVANCE_TRX' : [float(input['CASH_ADVANCE_TRX'])],
            'PURCHASES_TRX' : [float(input['PURCHASES_TRX'])],
            'CREDIT_LIMIT' : [float(input['CREDIT_LIMIT'])],
            'PAYMENTS' : [float(input['PAYMENTS'])],
            'MINIMUM_PAYMENTS' : [float(input['MINIMUM_PAYMENTS'])],
            'PRC_FULL_PAYMENT' : [float(input['PRC_FULL_PAYMENT'])],
            'TENURE' : [int(input['TENURE'])],
            'SEGMENT' : [SEGMENT]
        })
        new_df.to_sql('CC', con=dbConnection, if_exists='append', index=False)
        return render_template('success.html',
            BALANCE= float(input['BALANCE']),
            BALANCE_FREQUENCY= float(input['BALANCE_FREQUENCY']),
            PURCHASES= float(input['PURCHASES']),
            ONEOFF_PURCHASES= float(input['ONEOFF_PURCHASES']),
            INSTALLMENTS_PURCHASES= float(input['INSTALLMENTS_PURCHASES']),
            CASH_ADVANCE= float(input['CASH_ADVANCE']),
            PURCHASES_FREQUENCY= float(input['PURCHASES_FREQUENCY']),
            ONEOFF_PURCHASES_FREQUENCY= float(input['ONEOFF_PURCHASES_FREQUENCY']),
            PURCHASES_INSTALLMENTS_FREQUENCY= float(input['PURCHASES_INSTALLMENTS_FREQUENCY']),
            CASH_ADVANCE_FREQUENCY= float(input['CASH_ADVANCE_FREQUENCY']),
            CASH_ADVANCE_TRX= float(input['CASH_ADVANCE_TRX']),
            PURCHASES_TRX=float(input['PURCHASES_TRX']),
            CREDIT_LIMIT= float(input['CREDIT_LIMIT']),
            PAYMENTS= float(input['PAYMENTS']),
            MINIMUM_PAYMENTS= float(input['MINIMUM_PAYMENTS']),
            PRC_FULL_PAYMENT = float(input['PRC_FULL_PAYMENT']),
            TENURE=int(input['TENURE']),
            SEGMENT= SEGMENT
            )

@app.route('/pred_lr')
## Menampilkan Dataset
def pred_lr():
    sqlengine = create_engine('mysql+pymysql://root:agdees11@127.0.0.1:3307/flaskapp', pool_recycle=3605)
    engine = sqlengine.raw_connection()
    cursor = engine.cursor()
    cursor.execute("SELECT * FROM CC")
    data = cursor.fetchall()
    return render_template('predict.html', data=data)

@app.route('/pred_result', methods=['POST', 'GET'])
def pred_result():

    if request.method == 'POST':
    ## Untuk Predict
        input = request.form
        BALANCE= float(input['BALANCE'])
        BALANCE_FREQUENCY= float(input['BALANCE_FREQUENCY'])
        PURCHASES= float(input['PURCHASES'])
        ONEOFF_PURCHASES= float(input['ONEOFF_PURCHASES'])
        INSTALLMENTS_PURCHASES= float(input['INSTALLMENTS_PURCHASES'])
        CASH_ADVANCE= float(input['CASH_ADVANCE'])
        PURCHASES_FREQUENCY= float(input['PURCHASES_FREQUENCY'])
        ONEOFF_PURCHASES_FREQUENCY= float(input['ONEOFF_PURCHASES_FREQUENCY'])
        PURCHASES_INSTALLMENTS_FREQUENCY= float(input['PURCHASES_INSTALLMENTS_FREQUENCY'])
        CASH_ADVANCE_FREQUENCY= float(input['CASH_ADVANCE_FREQUENCY'])
        CASH_ADVANCE_TRX= float(input['CASH_ADVANCE_TRX'])
        PURCHASES_TRX=float(input['PURCHASES_TRX'])
        CREDIT_LIMIT= float(input['CREDIT_LIMIT'])
        PAYMENTS= float(input['PAYMENTS'])
        MINIMUM_PAYMENTS= float(input['MINIMUM_PAYMENTS'])
        PRC_FULL_PAYMENT = float(input['PRC_FULL_PAYMENT'])
        TENURE=int(input['TENURE'])

        pred = model.predict([[BALANCE, BALANCE_FREQUENCY, PURCHASES, ONEOFF_PURCHASES, INSTALLMENTS_PURCHASES,
        CASH_ADVANCE, PURCHASES_FREQUENCY, ONEOFF_PURCHASES_FREQUENCY, PURCHASES_INSTALLMENTS_FREQUENCY, CASH_ADVANCE_FREQUENCY,
        CASH_ADVANCE_TRX, PURCHASES_TRX, CREDIT_LIMIT, PAYMENTS, MINIMUM_PAYMENTS, PRC_FULL_PAYMENT,TENURE]])[0].round(2)

        ## Untuk Isi Data
        return render_template('result.html',
            BALANCE= float(input['BALANCE']),
            BALANCE_FREQUENCY= float(input['BALANCE_FREQUENCY']),
            PURCHASES= float(input['PURCHASES']),
            ONEOFF_PURCHASES= float(input['ONEOFF_PURCHASES']),
            INSTALLMENTS_PURCHASES= float(input['INSTALLMENTS_PURCHASES']),
            CASH_ADVANCE= float(input['CASH_ADVANCE']),
            PURCHASES_FREQUENCY= float(input['PURCHASES_FREQUENCY']),
            ONEOFF_PURCHASES_FREQUENCY= float(input['ONEOFF_PURCHASES_FREQUENCY']),
            PURCHASES_INSTALLMENTS_FREQUENCY= float(input['PURCHASES_INSTALLMENTS_FREQUENCY']),
            CASH_ADVANCE_FREQUENCY= float(input['CASH_ADVANCE_FREQUENCY']),
            CASH_ADVANCE_TRX= float(input['CASH_ADVANCE_TRX']),
            PURCHASES_TRX=float(input['PURCHASES_TRX']),
            CREDIT_LIMIT= float(input['CREDIT_LIMIT']),
            PAYMENTS= float(input['PAYMENTS']),
            MINIMUM_PAYMENTS= float(input['MINIMUM_PAYMENTS']),
            PRC_FULL_PAYMENT = float(input['PRC_FULL_PAYMENT']),
            TENURE=int(input['TENURE']),
            segment_pred = pred
            )

if __name__ == '__main__':
    ## Me-Load data dari Database
    sqlengine = create_engine('mysql+pymysql://root:agdees11@127.0.0.1:3307/flaskapp', pool_recycle=3605)
    dbConnection = sqlengine.connect()
    engine = sqlengine.raw_connection()
    cursor = engine.cursor()
    # CC = pd.read_sql("select * from CC", dbConnection)
    CC = pd.read_csv('./static/CC.csv')
    ## Load Model
    model = joblib.load('ModelCreditCard')
    app.run(debug=True)