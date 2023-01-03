import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, session, Response
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

# df.drop(['Lunch Break'],axis=1,inplace=True)
# df = pd.DataFrame.from_dict(records_data)
# importing the required libraries
import gspread
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import re


# define the scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\2019c\\Desktop\\program files\\sheetsapi\\cred.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)


# get the instance of the Spreadsheet
sheet = client.open('sheet database')

# get the first sheet of the Spreadsheet 0-indexed
sheet_instance = sheet.get_worksheet(3)

app = Flask(__name__)

#     print(ser[i]+1,ser[i+1]-1)
# df[df['Timings'].notna()]



def get_galaxies():
    dsa=['BM101(M5)', 'BM601(CY-1)', 'BM605(EE-1)', 'BM606(M2)',
       'BM611(CY-SH)', 'BM615(M1)', 'CE201(M1)', 'CE201/CE304 LAB',
       'CE202(M1)', 'CE304(M1)', 'CE401(M1)', 'CE401(ME1)', 'CE402(M2)',
       'CE404(M1)', 'CE501(CY-2)', 'CE502(CY-2)', 'CE503(CS-1)',
       'CE511(M1)', 'CE515(EE-3)', 'CE516(M1)', 'CE519(EE-3)',
       'CE520(M1)', 'CE521(M2)', 'CE523(EE-3)', 'CE524(M1)', 'CH201(M2)',
       'CH202(M2)', 'CH301(M2)', 'CH302(M1)', 'CH303(M2)', 'CH502(CY-2)',
       'CH503(CY-2)', 'CS(SH)', 'CS1', 'CS2', 'CS201(M6)', 'CS203(M3)',
       'CS301(M3)', 'CS301(M5)', 'CS302(M3)', 'CS303(M4)', 'CS504(CS-1)',
       'CS506(CS-1)', 'CS507(CS-SH)', 'CS510(CS-SH)', 'CS516(CS-1)',
       'CS517(M3)', 'CS518(CS-1)', 'CS522(CS-1)', 'CS526(CS-1)',
       'CS527(CS-SH)', 'CS533(CS-2)', 'CS539(M5)', 'CS550(CS-2)',
       'CS607(CS-2)', 'CS621(CS-2)', 'CS630(CS-SH)', 'CY(SH)', 'CY1',
       'CY101', 'CY2', 'CY411(CY-SH)', 'CY412(CY-SH)', 'CY414(CY-SH)',
       'CY415(CY-SH)', 'CY416(CY-1)', 'CY417(M2)', 'CY511(CY-2)',
       'CY513(CY-1)', 'CY514(CY-1)', 'CY515(CY-2)','EE(SH)', 'EE1', 'EE2',
       'EE201(M4)', 'EE201(M6)', 'EE203(M4)', 'EE204-LAB', 'EE205(CS-SH)',
       'EE205(M4)', 'EE3', 'EE301(M4)', 'EE303(CS-SH)', 'EE305(CS-SH)',
       'EE316(EE-2)', 'EE511(EE-1)', 'EE513(EE-1)', 'EE515(EE-2)',
       'EE521(EE-2)', 'EE523(EE-1)', 'EE527(EE-SH)', 'EE531(EE-1)',
       'EE533(EE-SH)', 'EE535(EE-1)', 'EE608(EE-1)', 'EE629(EE-3)',
       'Friday', 'GE103', 'GE104', 'GE107-G1', 'GE107-G2', 'GE107-G3',
       'GE107-G4', 'GE107-G5', 'GE107-G6', 'GE108(M6)', 'GE108-G10',
       'GE108-G11', 'GE108-G12', 'GE108-G7', 'GE108-G8', 'GE108-G9',
       'GE109-G10', 'GE109-G11', 'GE109-G12', 'GE109-G7', 'GE109-G8',
       'GE109-G9', 'GE111(M5)', 'GE201(M3)', 'GE201+ GE203 (M5)',
       'GE203(M1)', 'HS101', 'HS102', 'HS103', 'HS104 (M6)', 'HS201(M3)',
       'HS201(M6)', 'HS202(M6)', 'HS301(M6)', 'HS405(CY-SH)', 'HS413(M6)',
       'HS472(M3)', 'HS475(M3)', 'HS501(M4)', 'HS505(EE-SH)',
       'HS506(CY-SH)', 'HS507(CS-SH)','MA101', 'MA201(G1)(EE-1)', 'MA201(G10)(CS-1)',
       'MA201(G11)(CS-2)', 'MA201(G12+ Backloger)(M5)', 'MA201(G2)(EE-2)',
       'MA201(G3)(EE-3)', 'MA201(G4)(CS-1)', 'MA201(G5)(CS-2)',
       'MA201(G6+ Backloger)(M5)', 'MA201(G7)(EE-1)', 'MA201(G8)(EE-2)',
       'MA201(G9)(EE-3)', 'MA201(M5)', 'MA301(M4)', 'MA411(ME-1)',
       'MA412(EE-SH)', 'MA413(EE-SH)', 'MA414(ME-1)', 'MA415-(ME-2)',
       'MA511(M3)', 'MA512(EE-3)', 'MA513(ME-SH)', 'MA514(CY-SH)',
       'MA515(CY-SH)', 'MA614(M2)', 'MA615(M4)', 'ME(SH)', 'ME1',
       'ME102(ME-SH)', 'ME2', 'ME201(ME-SH)', 'ME202-LAB', 'ME206(ME-SH)',
       'ME301(M6)', 'ME302(ME-SH)', 'ME471(ME-SH)', 'ME501(ME-1)',
       'ME502(ME-1)', 'ME503(ME-1)', 'ME506(ME-SH)', 'ME507(ME-SH)',
       'ME508(ME-1)', 'ME517(ME-1)', 'ME518(ME-1)', 'ME521(ME-SH)',
       'ME547(ME-SH)', 'ME548(ME-1)', 'ME549(M2)', 'ME571(ME-1)',
       'ME579(ME-2)', 'MM201(ME-2)', 'MM202(ME-2)', 'MM203(ME-2)',
       'MM301(ME-2)', 'MM302(CY-1)', 'MM303(ME-2)', 'MM401(ME-2)',
       'MM403(ME-2)','NCC/NSO/NSS','PH101',
       'PH552(M3)', 'PH614(M3)']
    return dsa
@app.route('/')
def home():
    dsa=get_galaxies()
    lens=len(dsa)
    return render_template('input.html', dsa=dsa, lens=lens,header='Amazing Universe', sub_header='Our universe is quite amazing', list_header="Courses!",
                       galaxies=dsa, site_title="WaitaSecond")

@app.route('/action',methods=['POST'])
def action():
    try:
        subjects=list(map(str,request.form['text'].split(',')))
        t=request.form['text'].split(",")
        Timings={'Monday':0,'Tuesday':1,"Wednesday":2,"Thursday":3,"Friday":4}
        dic={'Timings':['Monday','Tuesday',"Wednesday","Thursday","Friday"], '8.00 - 8.50':"", '9.00 - 9.50':"", '10.00 - 10. 50':"",
                '11.00 - 11.50':"", '12.00 - 12. 50':"", '2.00 - 2.50':"", '3.00 - 3.50':"",
                '4.00 - 4.50':"", '5.00 - 5.50':"", '6.00- 6.50':""}
        df1=pd.DataFrame(data=dic)
        df1=df1.set_index('Timings')
        for i in t:
            crit=""
            crit+=i
            crit+=".*"
            criteria_re = re.compile(crit)
            cell_list = sheet_instance.findall(criteria_re)
            if(len(cell_list)>0):
                for fooind in cell_list:
                    valDay = sheet_instance.cell(fooind.row, 1).value
                    valTime = sheet_instance.cell(1, fooind.col).value
                    df1[valTime].loc[df1.index[Timings[valDay]]]=df1[valTime].loc[df1.index[Timings[valDay]]]+fooind.value
            else:
                print("no results")
        df1=df1.fillna("")
        df1=df1.T
        table= '''<!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>WaitaSecond</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <center>
            '''+df1.to_html()+'''		<br><br>
            <button type="button" onclick="tableToCSV()">
                download CSV
            </button>
            <button><a href="/">Go Back</a></button>
        </center>

        <script type="text/javascript">
            function tableToCSV() {

                // Variable to store the final csv data
                var csv_data = [];

                // Get each row data
                var rows = document.getElementsByTagName('tr');
                for (var i = 0; i < rows.length; i++) {

                    // Get each column data
                    var cols = rows[i].querySelectorAll('td,th');

                    // Stores each csv row data
                    var csvrow = [];
                    for (var j = 0; j < cols.length; j++) {

                        // Get the text data of each cell
                        // of a row and push it to csvrow
                        csvrow.push(cols[j].innerHTML);
                    }

                    // Combine each column value with comma
                    csv_data.push(csvrow.join(","));
                }

                // Combine each row data with new line character
                csv_data = csv_data.join('\\n');

                // Call this function to download csv file
                downloadCSVFile(csv_data);

            }

            function downloadCSVFile(csv_data) {

                // Create CSV file object and feed
                // our csv_data into it
                CSVFile = new Blob([csv_data], {
                    type: "text/csv"
                });

                // Create to temporary link to initiate
                // download process
                var temp_link = document.createElement('a');

                // Download csv file
                temp_link.download = "Timetable.csv";
                var url = window.URL.createObjectURL(CSVFile);
                temp_link.href = url;

                // This link should not be displayed
                temp_link.style.display = "none";
                document.body.appendChild(temp_link);

                // Automatically click the link to
                // trigger download
                temp_link.click();
                document.body.removeChild(temp_link);
            }
        </script>
        <h4>Note: Please cross check results. If you found any problems <a href="https://forms.gle/1A6T57iFpWf8k4bN9">report in this form.</a></h4>

        <footer class="page-footer orange">
    <div class="container">
        <div class="row">
            <div class="col l6 s12">
                <h5 class="white-text">Bio</h5>

                <p class="grey-text text-lighten-4">Solving little problems.</p>
            </div>
            <div class="col l3 s12">
                <h5 class="white-text">Improve this site</h5>
                <ul>
                    <li><a class="white-text" href="https://github.com/sdmadhav/IndividualTimetable">github</a></li>
                </ul>
            </div>
            <div class="col l3 s12">
                <h5 class="white-text">Connect</h5>
                <ul>
                    <li><a class="white-text" href="https://www.linkedin.com/in/madhav-deshatwad-522538226/">LinkedIn</a></li>
                </ul>
            </div>
        </div>
    </div>
</footer>
    </body>

    </html>
    '''
        return table
    except pd.errors.InvalidIndexError as e:
        return "Invalid"


if __name__ == '__main__':                          # This is a Driver code. 
    
    app.run(debug=True)

