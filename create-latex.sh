cat <<EOF >foo.tex
\let\mypdfximage\pdfximage
\def\pdfximage{\immediate\mypdfximage}
\documentclass[12pt]{article}
\usepackage{lingmacros}
\usepackage{tree-dvips}
\usepackage{caption,subcaption}
\usepackage{graphicx}
\usepackage{pgffor}

\begin{document}

EOF

cd all_graphs
for f in *.pdf; do mv "$f" "${f// /-}"; done
rename  's/\(|\[|\]|\)//g' *
cd ..

declare -a Ops=("Telenor-SE" "Telia-SE" "Telia-NO" 
		"Tre-SE" "Telenor-NO" "ICE-NO" 
		"Yoigo-ES" "TIM-IT" "Wind-IT" 
		"Vodafone-IT" "Orange-ES")

declare -a urls=("live" "youtube" "reddit" "wikipedia" "yelp" "facebook" "microsoft" "imgur" "instagram" "coursera" "stackoverflow" "ebay" "tmall" "twitter" "kayak" "theguardian" "etsy" "flickr")

declare -a metrics=("si" "plt" "fp")


for i in "${Ops[@]}"
	do
	for j in "${urls[@]}"
		do
		for k in "${metrics[@]}"
			do
   			echo "\includegraphics[scale=0.4]{all_graphs/""$i""-""$j""-""$k"".pdf""}" >> foo.tex
			done
		done
	done
echo "\end{document}" >> foo.tex
