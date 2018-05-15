import numpy as np
import os
import csv
import json

def prepare_csv():
    with open(os.path.join( 'browsertime-data.csv'), 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = ["NodeId", "protocol", "url","browser",
                                                       "firstPaint","fullyLoaded","rumSpeedIndex","pageLoadTime","Ops","Country","roaming"], delimiter = ',')
        writer.writeheader()
   
    count1=1
    count2=2
    path_to_json = 'jsons/'
    dataRow=[]
    outfile = open("browsertime-data.csv", "a")
    writer = csv.writer(outfile)
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('json')]
    for js in json_files:
        if (os.stat(path_to_json+js).st_size!=0):
                with open(os.path.join(path_to_json, js)) as json_file:
                        try:
                                try:
                                        data=json.load(json_file)
                                except ValueError:
                                        print ("Decoding JSON failed")
				if "FIREFOX" not in data["DataId"]:
                                	dataRow=[]
                                	dataRow.append(data["NodeId"])
                                	dataRow.append(data["protocol"])
                                	dataRow.append(data["url"])
                                	dataRow.append(data["browser"])
                                	dataRow.append(float(data["firstPaint"])/1000)
                                	dataRow.append(float(data["fullyLoaded"])/1000)
                                	dataRow.append(float(data["rumSpeedIndex"])/1000)
                                	dataRow.append(float(data["pageLoadTime"])/1000)
                                	dataRow.append(data["Ops"])
                                	dataRow.append(data["Country"])
                                	if str(data["IMSIMCCMNC"])[0:3]==str(data["NWMCCMNC"])[0:3]:
                                		dataRow.append("0")
                                	else:
                                		dataRow.append("1")
                                        	writer.writerow(dataRow)
                        except KeyError:
				print json_file
                                print ("Incomple files.")

prepare_csv()
