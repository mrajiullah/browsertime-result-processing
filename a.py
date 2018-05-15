

import glob
import json

for fn in glob.glob('*HEADLESS*'):
    with open(fn,'r') as f:
       j=json.loads(f.read())

       #print j['NodeId'], j['Ops'], j['Timestamp'], j['url'], j['pageLoadTime'], len(json.loads(j['resourceTimings'].replace("u'", "'").replace("'", '"')))
       l=j['resourceTimings'].count("u'name'")
       print "{};{};{};{};{}".format(j['url'], j['protocol'], j['browser'], j['Ops'], l)

       #echo $node $ops $url $protocol $browser $num_objects $fp $si $plt 
       #echo  $url $protocol $browser $num_objects 

