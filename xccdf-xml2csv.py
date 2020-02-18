"""
Importable function that accepts XCCDFs of STIG checks and returns a data structure
which can be manipulated as required.

Seeing issues with .Net STIG; recommend try/except to handle error.

Adapted by: Arron Sparks and Tyson Bradley

Adapted from:
(C) 2010 Adam Crosby
Licensed under:
http://creativecommons.org/licenses/by-nc-sa/3.0/
"""
import xml.etree.ElementTree as ET


def import_xccdf(_xccdf):
    xmlns = "http://checklists.nist.gov/xccdf/1.2"

    xml = ET.parse(_xccdf)
    benchmark = xml.getroot()
    check_list = []
    profiles = benchmark.findall(f"{{{xmlns}}}Profile")
    for profile in profiles:
        selects = profile.findall(f"{{{xmlns}}}select")
        for select_tag in selects:
            if select_tag.get("selected") == "true":
                check_list.append(select_tag.get('idref'))

    groups = benchmark.findall(f"{{{xmlns}}}Group")
    results = benchmark.findall(f"{{{xmlns}}}TestResult")
    if type(results) == "<class 'list'>":
        results = results[0]

    stigs = {}
    for group in groups:
        group_id = group.get("id")
        if group_id in check_list:
            title = group.find(f"{{{xmlns}}}title").text
            severity = group.find(f"{{{xmlns}}}Rule").get("severity")
            version = group.find(f"{{{xmlns}}}Rule/{{{xmlns}}}version").text
            rule_title = group.find(f"{{{xmlns}}}Rule/{{{xmlns}}}title").text
            desctag = f"{{{xmlns}}}Rule/{{{xmlns}}}description"
            fixtext = group.find(f"{{{xmlns}}}Rule/{{{xmlns}}}fixtext").text
            descriptiontext = group.find(desctag).text
            encodedDesc = descriptiontext.replace("&gt;", ">").replace("&lt;", "<").replace("&", "&amp;")
            innerXML = "<desc>%s</desc>" % format(encodedDesc)
            xml = ET.XML(innerXML)

            nl = '\n'
            stigs[f"{group_id.replace(nl, '##').replace('xccdf_mil.disa.stig_group_', '')}"] = {
                'Version': f"{version.replace(nl, '##')}",
                'Rule Title': f"{rule_title.replace(nl, '##')}",
                'Title': f"{title.replace(nl, '##')}",
                'Severity': f"{severity.replace(nl, '##')}",
                'Fix Text': fixtext,
            }

    for stig in stigs:
        version = stigs[stig]['Version']
        for result in results:
            if 'idref' in result.attrib and 'version' in result.attrib and version in result.attrib['version']:
                status = result.find(("{%s}result" % xmlns))
                stigs[stig]['Status'] = status.text

    return stigs


def main():
    stigs = import_xccdf(input('Provide path to XCCDF: '))


if __name__ == '__main__':
    main()
