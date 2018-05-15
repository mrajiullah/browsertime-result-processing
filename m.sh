#!/bin/bash

( NodeId,protocol,url,browser,firstPaint,fullyLoaded,rumSpeedIndex,pageLoadTime,Ops,Country,IMSIMCCMNC, NWMCCMNC,resourceTimings)

for i in *.json; 
	do
	node=$( cat $i|jq .NodeId);
	url=$( cat $i|jq .url);
	protocol=$( cat $i|jq .protocol);
	browser=$( cat $i|jq .browser);
	fp=$( cat $i|jq .firstPaint);
	si=$( cat $i|jq .rumSpeedIndex);
	plt=$( cat $i|jq .pageLoadTime);
	ops=$( cat $i|jq .Ops);

	
	num_objects=$(cat $i|jq .resourceTimings|tr " " "\n" |grep -c "https"); 
	echo $node $ops $url $protocol $browser $num_objects $fp $si $plt 
done
