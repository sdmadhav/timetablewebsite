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
creds = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

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
    dsa=["BM101(M6)",
"BM604(M2)",
"BM607(CY-SH)",
"BM608(M1)",
"BM609(CY-SH)",
"BM610(M2)",
"BM612(CY-SH)",
"BM614(M1)",
"CE301(M2)",
"CE301(ME-1)",
"CE301(ME-2)",
"CE302(M4)",
"CE302/CE303(LAB)",
"CE303(CY-SH)",
"CE403(CY-1)",
"CE405(M2)",
"CE406(CY-2)",
"CE407(ME-1)",
"CE506(M2)",
"CE552(CY-1)",
"CE602(CY-2)",
"CH203(M1)",
"CH204(CY-2)",
"CH220(Lab)",
"CH231(Lab)",
"CH304(CY-2)",
"CH305(CY-1)",
"CH506(M2)",
"CH507A(M1)",
"CS202(M4)",
"CS204(M5)",
"CS304(M4)",
"CS305(M6)",
"CS306(M4)",
"CS503(CS-SH)",
"CS517(CS-1)",
"CS517(CS-1)(T)",
"CS531(CS-1)",
"CS533(CS-2)",
"CS535(CS-1)",
"CS536(CS-2)",
"CS539(CS-1)",
"CS546(CS-SH)",
"CS550(CS-1)",
"CS603(CS-2)",
"CS604(CS-1)",
"CS616(CS-1)",
"CS616(CS-1)(T)",
"CS712(CS-2)",
"CY001(CY-2)",
"CY101(M5)",
"CY230(CY-2)",
"CY230(M3)",
"CY421(CY-1)",
"CY422(CY-1)",
"CY423(CY-1)",
"CY424(CY-1)",
"CY427(CY-SH)",
"CY452(CY-SH)",
"CY516(CY-SH)",
"CY604(CY-2)",
"CY611(CY-1)",
"CY612(CY-2)",
"CY621(CY-2)",
"CY701(CY-SH)",
"CY704(CY-1)",
"EE206(lab)",
"EE207(M3)",
"EE207(M4)",
"EE209(M4)",
"EE307(M3)",
"EE309(M3)",
"EE510(EE-2)",
"EE512(EE-1)",
"EE514(EE-1)",
"EE514(EE-SH)",
"EE522(EE-1)",
"EE524(EE-1)",
"EE530(EE-1)",
"EE536(EE-2)",
"EE628(EE-2)",
"EE639(EE-1)",
"EE646(EE-3)",
"EE647(EE-3)",
"EE652(EE-1)",
"EE657(EE-2)",
"EE658(EE-2)",
"EE661(EE-1)",
"EE661(EE-2)",
"EE722(EE-SH)",
"GE103(M5)",
"GE104(M5)",
"GE107 LAB (G10)",
"GE107 LAB (G11)",
"GE107 LAB (G8)",
"GE107(12)",
"GE107(G7)",
"GE107(G9)",
"GE108-LAB-G1",
"GE108-LAB-G2",
"GE108-LAB-G5",
"GE108-LAB-G6",
"GE108(M5)",
"GE108(T)(M5)",
"GE109-LAB-G1",
"GE109-LAB-G2",
"GE109-LAB-G3",
"GE109-LAB-G4",
"GE109-LAB-G5GE109-LAB-G6",
"GE111(M6)",
"HS001(EE-2)",
"HS101(M5)",
"HS102(M5)",
"HS103(CS3)",
"HS103(M3)",
"HS103(M4)",
"HS103(M5)",
"HS103(M6)",
"HS104(M6)",
"HS201(M6)",
"HS202(M6)",
"HS301(M5)",
"HS405(M3)",
"HS406(M3)",
"HS463(CY-SH)",
"HS475(M4)",
"HS491(M4)",
"HS505(M4)",
"HS506(CS-SH)",
"HS507(M6)",
"MA001(CY-2)",
"MA101(CS-2)(G6)",
"MA101(G1)(CS-1)",
"MA101(G10)(EE-2)",
"MA101(G11)(EE-3)",
"MA101(G12)(EE-SH)",
"MA101(G2)(CS-SH)",
"MA101(G3)(EE-1)",
"MA101(G4)(EE-SH)",
"MA101(G5)(EE-3)",
"MA101(G7)(CS-1)",
"MA101(G8)(CS-SH)",
"MA101(G9)(EE-1)",
"MA101(M5)",
"MA202 (CE+CS+MnC)(M6)",
"MA202 (ME+MM)(M6)",
"MA203(M4)",
"MA204(M3)",
"MA205(Lab)",
"MA302(M2)",
"MA421(M1)",
"MA422(M1)",
"MA423(M2)",
"MA424(M3)",
"MA425(M1)",
"MA426(EE-1)",
"MA517(M1)",
"MA605(CS-2)",
"MA610(CS-2)",
"MA625(EE-2)",
"MA628(M3)",
"MA629(M3)",
"MA703(M2)",
"ME203(ME-SH)",
"ME204(ME-SH)",
"ME205(Lab)",
"ME304(ME-SH)",
"ME305(ME-SH)",
"ME306/ME307 LAB",
"ME306/ME307 LABGE108-LAB-G3GE108-LAB-G4",
"ME308-LAB",
"ME308-LABME205(Lab)",
"ME472(M1)",
"ME504(ME-1)",
"ME505(ME-SH)",
"ME512(ME-2)",
"ME514(ME-1)",
"ME515(ME-1)",
"ME520(ME-1)",
"ME524(ME-2)",
"ME542(ME-SH)",
"ME546(ME-1)",
"ME546(ME-SH)",
"ME549(ME-1)",
"ME559(M1)",
"ME559(ME-SH)",
"ME561(ME-1)",
"ME575(ME-2)",
"ME576(ME-SH)",
"ME580(ME-1)",
"ME624(M2)",
"ME677(ME-1)",
"ME681(ME-2)",
"ME683(ME-1)",
"MM206(ME-2)",
"MM207(M1)",
"MM306(ME-2)",
"MM307(ME-2)",
"MM308(ME-2)",
"MM309(ME-2)",
"MM431(CY-1)",
"MM531(CY-1)",
"NCC/NSO/NSS",
"PH001(CY-2)",
"PH101(G10)(EE-2)",
"PH101(G11)(EE-3)",
"PH101(G12)(CS-SH)",
"PH101(G7)(CS-1)",
"PH101(G8)(CS-SH)",
"PH101(G9)(EE-1)",
"PH101(M5)",
"PH451(M6)",
"PH457(CY-SH)",
"PH612(EE-SH)",
"PH612(EE-SH)"]
   
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
            crit+=i[0:5]
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

