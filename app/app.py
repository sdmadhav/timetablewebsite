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
    dsa=["MA101(G7)(CS-1)",
"GE104(M5)",
"MA101(M5)",
"PH101(M5)",
"GE108(M5)",
"HS102(M5)",
"CY516(CY-SH)",
"HS301(M5)",
"CS712(CS-2)",
"MA101(G8)(CS-SH)",
"HS202(M6)",
"MA202 (CE+CS+MnC)(M6)",
"CH203(M1)",
"HS201(M6)",
"MM309(ME-2)",
"GE111(M6)",
"CY452(CY-SH)",
"EE209(M4)",
"MA101(G9)(EE-1)",
"EE209(M4)",
"MA203(M4)",
"BM101(M6)",
"CS503(CS-SH)",
"MA302(M2)",
"ME683(ME-1)",
"CS604(CS-1)",
"ME204(ME-SH)",
"MA101(G10)(EE-2)",
"ME204(ME-SH)",
"CY230(M3)",
"CE301(ME-1)",
"CS550(CS-1)",
"CE406(CY-2)",
"ME559(ME-SH)",
"CS535(CS-1)",
"MA101(G11)(EE-3)",
"CS535(CS-1)",
"ME203(ME-SH)",
"CS202(M4)",
"ME677(ME-1)",
"MA628(M3)",
"HS475(M4)",
"MA101(G12)(EE-SH)",
"ME561(ME-1)",
"MM206(ME-2)",
"MA204(M3)",
"MA629(M3)",
"HS491(M4)",
"ME559(M1)",
"HS405(M3)",
"MA703(M2)",
"MA703(M2)",
"CS533(CS-2)",
"CS539(CS-1)",
"ME524(ME-2)",
"ME549(ME-1)",
"MA517(M1)",
"MA421(M1)",
"MA421(M1)",
"CS531(CS-1)",
"ME681(ME-2)",
"MA422(M1)",
"EE510(EE-2)",
"EE658(EE-2)",
"PH451(M6)",
"ME514(ME-1)",
"ME546(ME-SH)",
"CY701(CY-SH)",
"EE524(EE-1)",
"EE639(EE-1)",
"ME515(ME-1)",
"CY421(CY-1)",
"CY421(CY-1)",
"BM612(CY-SH)",
"MA424(M3)",
"CY427(CY-SH)",
"CH507A(M1)",
"ME575(ME-2)",
"BM607(CY-SH)",
"MA423(M2)",
"CY604(CY-2)",
"CY704(CY-1)",
"EE514(EE-1)",
"CY423(CY-1)",
"CY611(CY-1)",
"EE657(EE-2)",
"CY422(CY-1)",
"BM610(M2)",
"EE722(EE-SH)",
"BM608(M1)",
"BM609(CY-SH)",
"EE646(EE-3)",
"EE661(EE-1)",
"CE552(CY-1)",
"EE522(EE-1)",
"PH001(CY-2)",
"CY001(CY-2)",
"HS001(EE-2)",
"MA001(CY-2)",
"HS301(M5)",
"ME308-LABME205(Lab)",
"GE111(M6)",
"GE107(G7)",
"NCC/NSO/NSS",
"ME306/ME307 LABGE108-LAB-G3GE108-LAB-G4",
"CE302/CE303(LAB)",
"GE109-LAB-G5GE109-LAB-G6",
"EE206(lab)",
"GE104(M5)",
"MA101(M5)",
"PH101(M5)",
"GE108(M5)",
"HS102(M5)",
"MM307(ME-2)",
"HS104(M6)",
"CS712(CS-2)",
"CS304(M4)",
"PH101(G7)(CS-1)",
"HS202(M6)",
"MA202 (CE+CS+MnC)(M6)",
"CH203(M1)",
"HS201(M6)",
"HS103(M6)",
"ME305(ME-SH)",
"ME504(ME-1)",
"CY452(CY-SH)",
"MA425(M1)",
"PH101(G8)(CS-SH)",
"EE209(M4)",
"MA203(M4)",
"BM101(M6)",
"CS503(CS-SH)",
"ME512(ME-2)",
"CS604(CS-1)",
"PH101(G9)(EE-1)",
"ME204(ME-SH)",
"CY230(M3)",
"CE301(M2)",
"CS550(CS-1)",
"EE307(M3)",
"ME542(ME-SH)",
"PH101(G10)(EE-2)",
"CS535(CS-1)",
"ME203(ME-SH)",
"CS202(M4)",
"ME677(ME-1)",
"CS306(M4)",
"CS304(M4)",
"HS475(M4)",
"PH101(G11)(EE-3)",
"ME561(ME-1)",
"MM206(ME-2)",
"MA204(M3)",
"MA629(M3)",
"CE405(M2)",
"HS406(M3)",
"HS405(M3)",
"PH101(G12)(CS-SH)",
"MA703(M2)",
"CS533(CS-2)",
"CS539(CS-1)",
"ME524(ME-2)",
"CH305(CY-1)",
"HS463(CY-SH)",
"MA517(M1)",
"MA202 (CE+CS+MnC)(M6)",
"MA421(M1)",
"CS531(CS-1)",
"ME681(ME-2)",
"MA422(M1)",
"MA605(CS-2)",
"PH451(M6)",
"MA203(M4)",
"ME514(ME-1)",
"ME546(ME-1)",
"CY701(CY-SH)",
"MA610(CS-2)",
"MA425(M1)",
"ME515(ME-1)",
"CY230(CY-2)",
"CY421(CY-1)",
"BM612(CY-SH)",
"MA424(M3)",
"CY427(CY-SH)",
"ME520(ME-1)",
"CS546(CS-SH)",
"ME575(ME-2)",
"ME203(ME-SH)",
"BM607(CY-SH)",
"MA423(M2)",
"CY604(CY-2)",
"ME472(M1)",
"PH612(EE-SH)",
"EE514(EE-1)",
"MM206(ME-2)",
"CY423(CY-1)",
"CY611(CY-1)",
"EE530(EE-1)",
"EE512(EE-1)",
"EE657(EE-2)",
"MA423(M2)",
"CY422(CY-1)",
"BM610(M2)",
"EE536(EE-2)",
"EE647(EE-3)",
"EE722(EE-SH)",
"BM608(M1)",
"BM609(CY-SH)",
"CH506(M2)",
"EE646(EE-3)",
"EE661(EE-2)",
"CE602(CY-2)",
"CE552(CY-1)",
"EE522(EE-1)",
"MM431(CY-1)",
"EE514(EE-SH)",
"PH001(CY-2)",
"CY001(CY-2)",
"HS001(EE-2)",
"MM531(CY-1)",
"MA001(CY-2)",
"EE206(lab)",
"ME308-LABME205(Lab)",
"GE108-LAB-G5",
"GE108-LAB-G6",
"ME306/ME307 LAB",
"GE109-LAB-G4",
"GE109-LAB-G3",
"CE302/CE303(LAB)",
"GE107(12)",
"MM307(ME-2)",
"HS101(M5)",
"MA101(M5)",
"PH101(M5)",
"GE108(T)(M5)",
"HS102(M5)",
"MA202 (ME+MM)(M6)",
"GE103(M5)",
"CY101(M5)",
"MA101(CS-2)(G6)",
"CY101(M5)",
"ME305(ME-SH)",
"HS202(M6)",
"MA202 (CE+CS+MnC)(M6)",
"CH203(M1)",
"HS201(M6)",
"HS103(M6)",
"CE302(M4)",
"CE303(CY-SH)",
"CS517(CS-1)",
"MA101(G1)(CS-1)",
"CH203(M1)",
"EE209(M4)",
"MA203(M4)",
"BM101(M6)",
"CS503(CS-SH)",
"CS204(M5)",
"CH204(CY-2)",
"MM306(ME-2)",
"MA101(G2)(CS-SH)",
"BM101(M6)",
"EE307(M3)",
"ME204(ME-SH)",
"CY230(M3)",
"CE301(M2)",
"CS550(CS-1)",
"CS616(CS-1)",
"MA426(EE-1)",
"ME304(ME-SH)",
"MA101(G3)(EE-1)",
"CE301(ME-2)",
"CS306(M4)",
"CS535(CS-1)",
"ME203(ME-SH)",
"CS202(M4)",
"ME677(ME-1)",
"BM614(M1)",
"EE207(M3)",
"EE309(M3)",
"MA101(G4)(EE-SH)",
"CS202(M4)",
"CE405(M2)",
"ME561(ME-1)",
"MM206(ME-2)",
"MA204(M3)",
"MA629(M3)",
"ME580(ME-1)",
"MM207(M1)",
"HS507(M6)",
"MA101(G5)(EE-3)",
"MA204(M3)",
"CH305(CY-1)",
"MA703(M2)",
"CS533(CS-2)",
"CS539(CS-1)",
"ME524(ME-2)",
"ME505(ME-SH)",
"MM308(ME-2)",
"CE403(CY-1)",
"MA424(M3)",
"MA421(M1)",
"CS531(CS-1)",
"ME681(ME-2)",
"MA422(M1)",
"MA625(EE-2)",
"CS305(M6)",
"CH304(CY-2)",
"CY423(CY-1)",
"ME514(ME-1)",
"ME546(ME-1)",
"CY701(CY-SH)",
"CY424(CY-1)",
"CE407(ME-1)",
"HS505(M4)",
"CY421(CY-1)",
"BM612(CY-SH)",
"MA424(M3)",
"CY427(CY-SH)",
"CY621(CY-2)",
"ME576(ME-SH)",
"HS506(CS-SH)",
"BM607(CY-SH)",
"MA423(M2)",
"CY604(CY-2)",
"CS603(CS-2)",
"PH457(CY-SH)",
"CY423(CY-1)",
"CY611(CY-1)",
"CY612(CY-2)",
"CS536(CS-2)",
"CY422(CY-1)",
"BM610(M2)",
"CE506(M2)",
"ME624(M2)",
"BM608(M1)",
"BM609(CY-SH)",
"EE652(EE-1)",
"MM309(ME-2)",
"EE661(EE-2)",
"EE628(EE-2)",
"MA302(M2)",
"EE522(EE-1)",
"CE406(CY-2)",
"PH001(CY-2)",
"CY001(CY-2)",
"HS001(EE-2)",
"ME308-LAB",
"ME306/ME307 LAB",
"GE107 LAB (G10)",
"HS301(M5)",
"HS101(M5)",
"MM307(ME-2)",
"HS104(M6)",
"MA202 (ME+MM)(M6)",
"GE103(M5)",
"CY101(M5)",
"MA101(M5)",
"GE103(M5)",
"HS201(M6)",
"GE111(M6)",
"CY516(CY-SH)",
"ME305(ME-SH)",
"ME504(ME-1)",
"HS103(CS3)",
"CE302(M4)",
"CE303(CY-SH)",
"CS517(CS-1)",
"ME683(ME-1)",
"MM309(ME-2)",
"ME512(ME-2)",
"CS204(M5)",
"CH204(CY-2)",
"MM306(ME-2)",
"MM306(ME-2)",
"ME559(ME-SH)",
"MA302(M2)",
"EE307(M3)",
"ME542(ME-SH)",
"CS616(CS-1)",
"MA426(EE-1)",
"ME304(ME-SH)",
"ME304(ME-SH)",
"MA628(M3)",
"CE406(CY-2)",
"CS306(M4)",
"CS304(M4)",
"BM614(M1)",
"EE207(M3)",
"EE309(M3)",
"EE309(M3)",
"ME559(M1)",
"CE405(M2)",
"HS406(M3)",
"ME580(ME-1)",
"MM207(M1)",
"HS507(M6)",
"CE403(CY-1)",
"HS491(M4)",
"CH305(CY-1)",
"HS463(CY-SH)",
"ME505(ME-SH)",
"MM308(ME-2)",
"CE403(CY-1)",
"CH304(CY-2)",
"MA422(M1)",
"EE658(EE-2)",
"ME549(ME-1)",
"MA605(CS-2)",
"MA625(EE-2)",
"CS305(M6)",
"CH304(CY-2)",
"EE639(EE-1)",
"EE510(EE-2)",
"MA610(CS-2)",
"MA425(M1)",
"CY424(CY-1)",
"CE407(ME-1)",
"HS505(M4)",
"CY427(CY-SH)",
"EE524(EE-1)",
"ME520(ME-1)",
"CS546(CS-SH)",
"CY621(CY-2)",
"ME576(ME-SH)",
"HS506(CS-SH)",
"CH507A(M1)",
"ME472(M1)",
"PH612(EE-SH)",
"BM604(M2)",
"CS603(CS-2)",
"PH457(CY-SH)",
"EE207(M4)",
"CY704(CY-1)",
"EE530(EE-1)",
"EE512(EE-1)",
"CY612(CY-2)",
"CS536(CS-2)",
"EE536(EE-2)",
"EE647(EE-3)",
"CE506(M2)",
"ME624(M2)",
"CH506(M2)",
"EE652(EE-1)",
"CE602(CY-2)",
"EE628(EE-2)",
"HS001(EE-2)",
"MM431(CY-1)",
"MM531(CY-1)",
"NCC/NSO/NSS",
"GE107 LAB (G8)",
"GE107 LAB (G11)",
"CH231(Lab)",
"MA205(Lab)",
"GE108-LAB-G1",
"GE109-LAB-G2",
"GE104(M5)",
"HS301(M5)",
"CY516(CY-SH)",
"MM307(ME-2)",
"HS104(M6)",
"MA202 (ME+MM)(M6)",
"GE103(M5)",
"CY101(M5)",
"MA101(M5)",
"MA202 (ME+MM)(M6)",
"CE303(CY-SH)",
"GE111(M6)",
"MM309(ME-2)",
"ME305(ME-SH)",
"ME504(ME-1)",
"CE302(M4)",
"CE303(CY-SH)",
"CS517(CS-1)(T)",
"CS712(CS-2)",
"CE302(M4)",
"CH204(CY-2)",
"ME683(ME-1)",
"MA302(M2)",
"ME512(ME-2)",
"CS204(M5)",
"CH204(CY-2)",
"MM306(ME-2)",
"CY452(CY-SH)",
"CS204(M5)",
"MA426(EE-1)",
"ME559(ME-SH)",
"CE406(CY-2)",
"EE307(M3)",
"ME542(ME-SH)",
"HS103(M3)",
"CS616(CS-1)(T)",
"MA426(EE-1)",
"ME304(ME-SH)",
"CS604(CS-1)",
"CY424(CY-1)",
"MA628(M3)",
"CS306(M4)",
"CS304(M4)",
"HS103(M4)",
"BM614(M1)",
"EE207(M3)",
"EE309(M3)",
"MM207(M1)",
"ME559(M1)",
"HS491(M4)",
"CE405(M2)",
"HS406(M3)",
"HS103(M5)",
"ME580(ME-1)",
"MM207(M1)",
"HS507(M6)",
"HS475(M4)",
"MM308(ME-2)",
"ME549(ME-1)",
"CH305(CY-1)",
"HS463(CY-SH)",
"ME505(ME-SH)",
"MM308(ME-2)",
"CE403(CY-1)",
"HS405(M3)",
"CS305(M6)",
"EE658(EE-2)",
"EE510(EE-2)",
"MA605(CS-2)",
"MA625(EE-2)",
"CS305(M6)",
"CH304(CY-2)",
"MA517(M1)",
"CE407(ME-1)",
"EE639(EE-1)",
"EE524(EE-1)",
"MA610(CS-2)",
"MA425(M1)",
"CY424(CY-1)",
"CE407(ME-1)",
"HS505(M4)",
"PH451(M6)",
"CH507A(M1)",
"ME520(ME-1)",
"CS546(CS-SH)",
"CY621(CY-2)",
"ME576(ME-SH)",
"HS506(CS-SH)",
"ME515(ME-1)",
"CY704(CY-1)",
"ME472(M1)",
"PH612(EE-SH)",
"BM604(M2)",
"CS603(CS-2)",
"PH457(CY-SH)",
"ME575(ME-2)",
"EE530(EE-1)",
"EE512(EE-1)",
"CY612(CY-2)",
"CS536(CS-2)",
"EE514(EE-1)",
"EE536(EE-2)",
"EE647(EE-3)",
"CE506(M2)",
"ME624(M2)",
"EE657(EE-2)",
"CH506(M2)",
"EE652(EE-1)",
"EE722(EE-SH)",
"CE602(CY-2)",
"EE628(EE-2)",
"EE646(EE-3)",
"MM431(CY-1)",
"CE552(CY-1)",
"MM531(CY-1)",
"MA001(CY-2)",
"ME205(Lab)",
"GE107(G9)",
"GE108-LAB-G2",
"CH220(Lab)",
"GE109-LAB-G1",
"EE206(lab)",
"NCC/NSO/NSS"]
   
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

