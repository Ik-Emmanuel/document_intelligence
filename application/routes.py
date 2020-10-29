from application import app, db
from flask import render_template, request, json, jsonify, Response, redirect, flash, url_for, session
from werkzeug.utils import secure_filename
import os
from application.forms import LoginForm, RegisterForm, Contracts, Notemp2
from application.models import User, Contracts, Reviewed, Notemp2
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import requests
import json
from IPython.display import display, HTML
import urllib
import importlib
import time
import getopt
import sys
from requests import get, post
from pathlib import Path




connection_string ="DefaultEndpointsProtocol=https;AccountName=azermstorage;AccountKey=oCChxS/MC2T8OSaEFG/dcj2FniioIL8YhRFC2gsNa7Fte0SSYgw6sxovNWZbEfDnpJlXR21eB6ojNrYcd1X3JA==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_name ='ermbasic'

service_name ="az-erm-cogsearch-prod"
api_version = "2019-05-06"

headers = {
    'Content-Type' : 'application/json',
    'api-key':"B41FFAF7BD26E5416FFD3058626C4D5C"
}



datasource_name = "ermdata"
uri = f"https://az-erm-cogsearch-prod.search.windows.net/datasources?api-version=2019-05-06"

body = {
    "name": datasource_name,
    "type": "azureblob",
  "credentials": {"connectionString": connection_string},
    "container": {"name": container_name}
}
skillset_name = 'ermskillset'
uri = f"https://az-erm-cogsearch-prod.search.windows.net/skillsets/ermskillset?api-version=2019-05-06"


index_name = 'ermindex'
uri = f"https://{service_name}.search.windows.net/indexes/{index_name}?api-version={api_version}"



indexer_name = 'ermindexer'
uri = f"https://{service_name}.search.windows.net/indexers/{indexer_name}?api-version={api_version}"

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'])
 
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():
 return render_template('index.html')


@app.route('/contract')
def upload_doc():

    if not session.get('username'):
        return redirect(url_for('login'))
    
    return render_template('index2.html')


@app.route("/contract", methods=["GET", "POST"])
def upload_docy():
    if request.method == 'POST':
        doctype = request.form.get("doctype")
        if doctype == "notemp":
            mainfile = request.files['files[]'].read()
            file = request.files['files[]']
            filename = secure_filename(file.filename)
            # file.save('C:/Users/Nwokochaui/Desktop/IPYTHONNOTEBOOKS/2020 Applied Machine Learning/2020 sterling work projects/Contact Intelligence/mslearn-build-ai-web-app-with-python-and-flask-master/src/starter/whole new worlds  for messing up/static/pdf/' + filename)
            file = request.files['files[]']
            path = "C:/Users/Nwokochaui/Desktop/FLASK DEMO AND WEBDEV/whole new flask/application/static/pdf/"
                        
            a = os.listdir(path)
            a.remove(".DS_Store")
            text = json.dumps(sorted(a))
            flash("File successfully uploaded!", "success")
            return render_template('docresult2.html', contents = text, filename=secure_filename(file.filename)) 
                                            
            # endpoint = r"https://docintelligence.cognitiveservices.azure.com/"
            # apim_key = "d358df492d5f4e6583f28e842ad27aee"
            # model_id = "d89b811b-d391-497e-a346-e6b3de90f811"
            # post_url = endpoint + "/formrecognizer/v2.0-preview/custom/models/%s/analyze" % model_id
            # params = { "includeTextDetails": True}
            # headers = {'Content-Type': 'application/pdf','Ocp-Apim-Subscription-Key': apim_key,}
        
            
            # mainfile = request.files['files[]'].read()
            # file = request.files['files[]']
            # filename = secure_filename(file.filename)
            # file.save('C:/Users/Nwokochaui/Desktop/IPYTHONNOTEBOOKS/2020 Applied Machine Learning/2020 sterling work projects/Contact Intelligence/mslearn-build-ai-web-app-with-python-and-flask-master/src/starter/whole new worlds  for messing up/static/pdf/' + filename)
            # file = request.files['files[]']
            
            # if file and allowed_file(file.filename):
            #     filename = secure_filename(file.filename)
            #     file.save(secure_filename(file.filename))
                
            #     # file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            
        

            
            
                    
            # new_path = os.path.abspath(filename)
        
            # new_path = os.path.dirname(os.path.abspath(file))
            
            
            # print(files)
            # filename = secure_filename(files.filename)
            # source = new_path
            # # # source = r"C:\Users\Nwokochaui\Desktop\Forms\cont4.PDF"
            # with open (new_path, "rb" ) as f:
            #     data_bytes = f.read()
            # try:
            #     resp = post(url = post_url, data = mainfile, headers = headers, params = params)
            #     if resp.status_code != 202:
            #         print("POST analyze failed:\n%s" % json.dumps(resp.json()))
            #         quit()
            #     print("POST analyze succeeded:\n%s" % resp.headers)
            #     get_url = resp.headers["operation-location"]
            # except Exception as e:
            #     print("POST analyze failed:\n%s" % str(e))
            #     quit()
            # n_tries = 15
            # n_try = 0
            # wait_sec = 5
            # max_wait_sec = 60
            # resp_json = " "
            # while n_try < n_tries:
            
            #     try:
            #         resp = get(url = get_url, headers = {"Ocp-Apim-Subscription-Key": apim_key})
            #         resp_json = json.loads(resp.text)
            #         print ("Running")
            #         if resp.status_code != 200:
            #             print("GET analyze results failed:\n%s" % resp_json)
            #             break
            #         status = resp_json["status"]
            #         if status == "succeeded":
            #             print("Analysis succeeded" ) #% json.dumps(resp_json, indent=2, sort_keys=True))
            #         if resp_json:
            #             print("jason gotten")
            #         status = resp_json["status"]
            #         if status == "succeeded": 
                        
            #             b = dict(resp_json['analyzeResult']['documentResults'][0])
            #             path = "C:/Users/Nwokochaui/Desktop/FLASK DEMO AND WEBDEV/whole new flask/application/static/pdf/"
                        
            #             a = os.listdir(path)
            #             a.remove(".DS_Store")
            #             text = json.dumps(sorted(a))
            #             return render_template('docresult2.html', resp = b, contents = text, filename=secure_filename(file.filename)) 
                                            
                                    
            #         if status == "failed":
            #             print("Analysis failed:\n%s" % resp_json)
            #             break
            #         time.sleep(wait_sec)
            #         n_try += 1
                
            #     except Exception as e:
            #         msg = "GET analyze results failed:\n%s" % str(e)
            #         print(msg)
            #         print("Analyze operation did not complete within the allocated time.")
            #         break
        else:
                   
            endpoint = r"https://docintelligence.cognitiveservices.azure.com/"
            apim_key = "d358df492d5f4e6583f28e842ad27aee"
            model_id = "d89b811b-d391-497e-a346-e6b3de90f811"
            post_url = endpoint + "/formrecognizer/v2.0-preview/custom/models/%s/analyze" % model_id
            params = { "includeTextDetails": True}
            headers = {'Content-Type': 'application/pdf','Ocp-Apim-Subscription-Key': apim_key,}
        
            
            mainfile = request.files['files[]'].read()
            file = request.files['files[]']
            filename = secure_filename(file.filename)
            file.save('C:/Users/Nwokochaui/Desktop/IPYTHONNOTEBOOKS/2020 Applied Machine Learning/2020 sterling work projects/Contact Intelligence/mslearn-build-ai-web-app-with-python-and-flask-master/src/starter/whole new worlds  for messing up/static/pdf/' + filename)
            file = request.files['files[]']
            
            if file and allowed_file(file.filename):
                flash("File successfully analysed!", "success")
                filename = secure_filename(file.filename)
                file.save(secure_filename(file.filename))
                
                # file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            
        

            
            
                    
            # new_path = os.path.abspath(filename)
        
            # new_path = os.path.dirname(os.path.abspath(file))
            
            
            # print(files)
            # filename = secure_filename(files.filename)
            # source = new_path
            # # # source = r"C:\Users\Nwokochaui\Desktop\Forms\cont4.PDF"
            # with open (new_path, "rb" ) as f:
            #     data_bytes = f.read()
            try:
                resp = post(url = post_url, data = mainfile, headers = headers, params = params)
                if resp.status_code != 202:
                    print("POST analyze failed:\n%s" % json.dumps(resp.json()))
                    quit()
                print("POST analyze succeeded:\n%s" % resp.headers)
                get_url = resp.headers["operation-location"]
            except Exception as e:
                print("POST analyze failed:\n%s" % str(e))
                quit()
            n_tries = 15
            n_try = 0
            wait_sec = 5
            max_wait_sec = 60
            resp_json = " "
            while n_try < n_tries:
            
                try:
                    resp = get(url = get_url, headers = {"Ocp-Apim-Subscription-Key": apim_key})
                    resp_json = json.loads(resp.text)
                    print ("Running")
                    if resp.status_code != 200:
                        print("GET analyze results failed:\n%s" % resp_json)
                        break
                    status = resp_json["status"]
                    if status == "succeeded":
                        print("Analysis succeeded" ) #% json.dumps(resp_json, indent=2, sort_keys=True))
                    if resp_json:
                        print("jason gotten")
                    status = resp_json["status"]
                    if status == "succeeded": 
                        
                        b = dict(resp_json['analyzeResult']['documentResults'][0])
                        path = "C:/Users/Nwokochaui/Desktop/FLASK DEMO AND WEBDEV/whole new flask/application/static/pdf/"
                        
                        a = os.listdir(path)
                        a.remove(".DS_Store")
                        text = json.dumps(sorted(a))
                        return render_template('docresult.html', resp = b, contents = text, filename=secure_filename(file.filename)) 
                                            
                                    
                    if status == "failed":
                        flash("Analysis failed!. Please select file of the right type and try again", "danger")
                        return render_template ("index2.html")

                        print("Analysis failed:\n%s" % resp_json)
                        break
                    time.sleep(wait_sec)
                    n_try += 1
                
                except Exception as e:
                    msg = "GET analyze results failed:\n%s" % str(e)
                    print(msg)
                    print("Analyze operation did not complete within the allocated time.")
                    flash("Analysis failed!. Please select file of the right type and try again", "danger")
                    
                    break
            
            
    return render_template('index2.html')       
        

@app.route("/login", methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data
        

        user = User.objects(email=email).first()
        # if request.form.get("email") =="test@docint.com":
        #     flash("You are successfully logged in!", "success")
        #     return redirect("/index")
        if user and password == user.password:
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            session['isadmin'] =user.isadmin
            return redirect("/index")
        else:
            flash("Sorry, something went wrong. Confirm your login details and try again","danger")
    return render_template("login.html", title="Login", form=form, login=True )

@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id   = User.objects.count()
        user_id   += 1
        email   =  form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        branch = form.branch.data 
        isadmin = form.isadmin.data

        user = User(user_id=user_id, email=email,  password=password, first_name=first_name, last_name=last_name, branch=branch, isadmin=isadmin)
        user.save()
        flash("You have successfully registered a new user!", "success")
        return redirect (url_for('upload_doc'))

    return render_template("register.html", form=form, title="Register New User" )

@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username', None)
    return redirect(url_for('index'))


# @app.route('/upload')
# def upload_form():
#     if not session.get('username'):
#         return redirect(url_for('login'))
#     return render_template('testindex.html')


# @app.route('/upload', methods=['POST'])
# def upload_file():
    
#     if not session.get('username'):
#         return redirect(url_for('login'))
#     if request.method == 'POST':
#             # check if the post request has the files part
#         if 'files[]' not in request.files:

#             flash('No file path')
#             return redirect(request.url)
#             files = request.files.getlist('files[]')

#     for file in files:
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
#             flash('File(s) successfully uploaded')
#             return redirect('/upload')

            
   
@app.route('/search', methods=['Get', 'POST'])
def search():
    if not session.get('username'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        search_term = request.form['search_term']
        service_name ="az-erm-cogsearch-prod"
        index_name = 'ermindex'
        api_version = "2019-05-06"
        headers = {'Content-Type' : 'application/json', 'api-key':"B41FFAF7BD26E5416FFD3058626C4D5C"}
        url = 'https://{}.search.windows.net/indexes/{}/docs'.format(service_name, index_name) 
        url += '?api-version={}'.format(api_version)
        url += '&search="{}"'.format(search_term )
        url += '&$count=true'
        # url += '&$top=1'
        url += '&highlight=translated_text'
        url += '&highlightPreTag=' + urllib.parse.quote('<span style="background-color: #a3f71d">', safe='')
        url += '&highlightPostTag=' + urllib.parse.quote('</span>', safe='')

        resp = requests.get(url, headers=headers)
        search_results = resp.json()

        for result in search_results['value']:
            view1= HTML('<h4>' + str(result['metadata_storage_name']) + '</h4>')
            for highlight in result['@search.highlights']['translated_text'][:]:
                view2 = HTML(highlight)
        return render_template('testindexsearch2.html', search_term = search_term,  search_results = search_results)

    return render_template('testindexsearch.html')



@app.route("/review")
def review():
    return render_template("review.html")






@app.route("/user")
def user():
    # User(user_id= 2, first_name="John", last_name="obibi", email="john.obibi@gmail.com", password="abc123", branch="CBD - Abuja").save()
    users = User.objects.all()
    return render_template("user.html", users=users)

@app.route("/upload1", methods=['POST', 'GET'])
def upload1():
    if request.method == 'POST':

        
        
            form = Contracts()
            cont_id = Contracts.objects.count()
            cont_id += 1
            user_id  = session['user_id']
            file_name = request.form['filename']
            contract_owner = request.form['contract_owner']
            contract_number = request.form['contract_number']
            counterparty = request.form['counterparty']
            entitlement = request.form['entitlement']
            status = request.form['status']
            final_price = request.form['final_price']
            termination_clause = request.form['termination_clause']
            expiry_date=  request.form['expiry_date']
            signatory = request.form['signatory']
            role = request.form['role']
            date= request.form['date']
            representative = request.form['representative']
            date_recieved = request.form['date_recieved']
            comment1 = request.form['comment1']
            comment2 = request.form['comment2']
            comment3 = request.form['comment3']
            department = request.form['department']
            date_of_review = request.form['date_of_review']

            contracts = Contracts(cont_id=cont_id, user_id=user_id, file_name=file_name, contract_owner=contract_owner,
            counterparty=counterparty, entitlement=entitlement, status=status, final_price=final_price, termination_clause=termination_clause,
            expiry_date=expiry_date, signatory=signatory, role=role, date=date, representative=representative,
            date_recieved=date_recieved, comment1=comment1, comment2=comment2, comment3=comment3, department=department, date_of_review=date_of_review)
            contracts.save()
            flash("You have successfully uploaded a file!", "success")
            return redirect (url_for('upload_doc'))
    return render_template("index2.html", form=form ) 


@app.route("/upload2", methods=['POST', 'GET'])
def upload2():
    if request.method == 'POST':

        
        
            form = Notemp2()
            cont_id = Notemp2.objects.count()
            cont_id += 1
            user_id  = session['user_id']
            file_name = request.form['filename']
            contract_title = request.form['contract_title']
            date_of_review = request.form['date_of_review']
            department = request.form['department']
            comment1 = request.form['comment1']
            comment2 = request.form['comment2']
            comment3 = request.form['comment3']
            comment4 = request.form['comment4']


            notemp = Notemp2(cont_id=cont_id, user_id=user_id, file_name=file_name, contract_title=contract_title,date_of_review=date_of_review,
            department=department, comment1=comment1, comment2=comment2, comment3=comment3, comment4=comment4 )
            notemp.save()
            flash("You have successfully uploaded a file!", "success")
            return redirect (url_for('upload_doc'))
    return render_template("index2.html", form=form )
      
