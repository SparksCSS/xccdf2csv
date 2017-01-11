#XCCDF to CSV#
Converts XCCDF to CSV.

##Usage##
XCCDF-xml2csv converts XCCDF XML documents (such as DISA STIGs) into easier to use Comma Seperated Values (Spreadsheet).

Output files should open easily in Libreoffice or Excel.

> git clone https://github.com/opencontrol/xccdf2csv
cd xccdf2csv
python xccdf-xml2csv.py example/RHEL6/RHEL6.xml > tmp.csv

to join/convert DISA CCI to NIST 800-53 Controls use csvkit
http://csvkit.readthedocs.io/en/latest/install.html
http://csvkit.readthedocs.io/en/0.9.1/tutorial/3_power_tools.html#csvjoin-merging-related-data

`csvjoin -c CCI tmp.csv convert/NIST800.csv > joined.csv
`

###License###
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">XCCDF2TSV</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/adamcrosby/xccdf2tsv" property="cc:attributionName" rel="cc:attributionURL">Adam Crosby</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.
