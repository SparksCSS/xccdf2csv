# XCCDF to CSV
Converts XCCDF format (used by [DISA STIGs](http://iase.disa.mil/stigs/cci/Pages/index.aspx) and [OpenSCAP](https://github.com/openscap)) to Comma Seperated Value (CSV) table.

## Usage
XCCDF-xml2csv converts XCCDF XML documents into easier to use Comma Seperated Values (Spreadsheet).

Output files should open easily in Libreoffice or Excel.

```
git clone https://github.com/opencontrol/xccdf2csv
cd xccdf2csv
python xccdf-xml2csv.py example/RHEL6/RHEL6.xml > tmp.csv
```

to join/convert DISA CCI to NIST 800-53 Controls use [csvkit](http://csvkit.readthedocs.io/en/latest/install.html) specifically [csvjoin](http://csvkit.readthedocs.io/en/0.9.1/tutorial/3_power_tools.html#csvjoin-merging-related-data)

```
csvjoin -c CCI tmp.csv convert/NIST800.csv > joined.csv
```

## License 
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">XCCDF2TSV</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/adamcrosby/xccdf2tsv" property="cc:attributionName" rel="cc:attributionURL">Adam Crosby</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.

### Other Information

In no way are the patent or trademark rights of any person affected by CC0,
nor are the rights that other persons may have in the work or in how the
work is used, such as publicity or privacy rights.

Unless expressly stated otherwise, the person who associated a work with
this deed makes no warranties about the work, and disclaims liability for
all uses of the work, to the fullest extent permitted by applicable law.
When using or citing the work, you should not imply endorsement by the
author or the affirmer.
