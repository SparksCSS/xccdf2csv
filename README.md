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
As a work of the United States Government, this project is in the
public domain within the United States.

Additionally, we waive copyright and related rights in the work
worldwide through the CC0 1.0 Universal public domain dedication.

## CC0 1.0 Universal Summary

This is a human-readable summary of the [Legal Code (read the full text)](https://creativecommons.org/publicdomain/zero/1.0/legalcode).

### No Copyright

The person who associated a work with this deed has dedicated the work to
the public domain by waiving all of his or her rights to the work worldwide
under copyright law, including all related and neighboring rights, to the
extent allowed by law.

You can copy, modify, distribute and perform the work, even for commercial
purposes, all without asking permission.

### Other Information

In no way are the patent or trademark rights of any person affected by CC0,
nor are the rights that other persons may have in the work or in how the
work is used, such as publicity or privacy rights.

Unless expressly stated otherwise, the person who associated a work with
this deed makes no warranties about the work, and disclaims liability for
all uses of the work, to the fullest extent permitted by applicable law.
When using or citing the work, you should not imply endorsement by the
author or the affirmer.
