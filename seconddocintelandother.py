import base64
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
#import magic
import urllib.request
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







app = Flask(__name__)
 
UPLOAD_FOLDER = "C:/Users/Nwokochaui/Desktop/IPYTHONNOTEBOOKS/2020 Applied Machine Learning/2020 sterling work projects/Contact Intelligence/mslearn-build-ai-web-app-with-python-and-flask-master/src/starter/whole new worlds  for messing up/static/pdf/"

 
app.secret_key = "ikemmanuel"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'])
 
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
  
@app.route('/upload')
def upload_form():
 return render_template('testindex.html')


@app.route('/upload', methods=['POST'])
def upload_file():
 if request.method == 'POST':
        # check if the post request has the files part
  if 'files[]' not in request.files:
   flash('No file path')
   return redirect(request.url)
  files = request.files.getlist('files[]')

  for file in files:
   if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    flash('File(s) successfully uploaded')
    return redirect('/upload')
   

  
@app.route('/')
def upload_doc():
 return render_template('docint.html')


@app.route("/", methods=["GET", "POST"])
def upload_docy():
    if request.method == 'POST':
        endpoint = r"https://docintformrecog.cognitiveservices.azure.com/"
        apim_key = "80db2dc55adb4bd682a0064b1a827140"
        model_id = "9a4d4f7f-2d2d-4b9f-ba62-73d51abec5f6"
        post_url = endpoint + "/formrecognizer/v2.0-preview/custom/models/%s/analyze" % model_id
        params = { "includeTextDetails": True}
        headers = {'Content-Type': 'application/pdf','Ocp-Apim-Subscription-Key': apim_key,}
      
        
        mainfile = request.files['files[]'].read()
        file = request.files['files[]']
        filename = secure_filename(file.filename)
        file.save('C:/Users/Nwokochaui/Desktop/IPYTHONNOTEBOOKS/2020 Applied Machine Learning/2020 sterling work projects/Contact Intelligence/mslearn-build-ai-web-app-with-python-and-flask-master/src/starter/whole new worlds  for messing up/static/pdf/' + filename)
        file = request.files['files[]']
        
        if file and allowed_file(file.filename):
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
                    path = "C:/Users/Nwokochaui/Desktop/IPYTHONNOTEBOOKS/2020 Applied Machine Learning/2020 sterling work projects/Contact Intelligence/mslearn-build-ai-web-app-with-python-and-flask-master/src/starter/whole new worlds  for messing up/static/pdf/"
                    a = os.listdir(path)
                    a.remove(".DS_Store")
                    text = json.dumps(sorted(a))
                    return render_template('docint3.html', resp = b, contents = text) 
                                          
                                   
                if status == "failed":
                    print("Analysis failed:\n%s" % resp_json)
                    break
                time.sleep(wait_sec)
                n_try += 1
            
            except Exception as e:
                msg = "GET analyze results failed:\n%s" % str(e)
                print(msg)
                print("Analyze operation did not complete within the allocated time.")
                break
            
            
    return render_template('docint.html')       
        

        
       
    


@app.route('/search', methods=['Get', 'POST'])
def search():
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


# def index():
#     if request.method == "POST":
#         # Display the image that was uploaded
#         image = request.files["file"]
#         uri = "data:;base64," + base64.b64encode(image.read()).decode("utf-8")
    
#     else:
#         # Display a placeholder image
#         uri = "/static/placeholder.png"

#     return render_template("testindex.html", image_uri=uri )



if __name__=="__main__":
    app.run( debug=True) 