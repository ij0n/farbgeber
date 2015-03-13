#!/usr/bin/python
# coding=utf-8

import time
from time import gmtime, strftime

from colour import Color

# zentraler zeitgeber, sollte immer <3600 und >0 sein und integer raustun


def generate_html_palette(timevalue=0.0, baseSaturation=1.0, baseLuminance=0.4, huemodifier=0.03, lummodifier=0.07,
                          satmodifier=0.2, programmcycles=0):

    print "zentrale Farbgebeeinheit"

    while programmcycles < 3600:

        timevalue = int(strftime("%M", gmtime())) * 60 + int(strftime("%S", gmtime()))
        timevalue = float(timevalue)

        baseHue = timevalue / 3600
        baseColor = Color(hsl=(baseHue, baseSaturation, baseLuminance))

        baseColorVar1 = Color(hsl=(baseColor.hue + huemodifier, baseSaturation - satmodifier, baseLuminance))
        baseColorVar2 = Color(hsl=(baseColor.hue - huemodifier, baseSaturation - satmodifier, baseLuminance))
        baseColorVar3 = Color(hsl=(baseColor.hue, baseSaturation, baseLuminance + lummodifier))
        baseColorVar4 = Color(hsl=(baseColor.hue, baseSaturation, baseLuminance - lummodifier))

        base_degree = baseHue * 360
        if base_degree < 180:
            ContrastHue = base_degree + 180
        elif base_degree >= 180:
            ContrastHue = base_degree - 180
        ContrastHue = ContrastHue / 360

        ContrastColor = Color(hsl=(ContrastHue, baseSaturation - satmodifier, (baseLuminance + 0.2)))

        # Terminaloutput

        # print timevalue
        # print "baseColor ", baseColor.hex
        # print "baseColorVariant1 ", baseColorVar1
        # print "baseColorVariant2 ", baseColorVar2
        # print "baseColorVariant3 ", baseColorVar3
        # print "baseColorVariant4 ", baseColorVar4
        # print "ContrastColor ", ContrastColor.hex
        # print "###################################"

        # Weboutput

        htmlpreface = """<html><head><title>visuelle Ausgabeeinheit des zentralen Farbgebers</title><meta http-equiv="refresh" content="1" />
<style type="text/css">
"""
        htmlcontent = """</style></head><body><h1>visuelle Ausgabeeinheit des zentralen Farbgebers</h1>
<div>BaseColor """ + baseColor.hex + """</div></ br>
<div class="baseColorVar1">baseColorVariant1 """ + baseColorVar1.hex + """</div>
<div class="baseColorVar2">baseColorVariant2 """ + baseColorVar2.hex + """</div>
<div class="baseColorVar3">baseColorVariant3 """ + baseColorVar3.hex + """</div>
<div class="baseColorVar4">baseColorVariant4 """ + baseColorVar4.hex + """</div>
<div class="Contrastcolor">Contrastcolor """ + ContrastColor.hex + """</div>"""
        zeitzeile = "<h3>Color-Seed " + str(timevalue) + " " + strftime("%H:%M:%S", gmtime()) + "Uhr</h3>"
        htmlclosing = """</body></html>"""

        css1 = "body { font-size:20px; background-color:" + baseColor.hex + "; color:" + ContrastColor.hex + "; }"
        css2 = ".baseColorVar1 { background-color:" + baseColorVar1.hex + "; width:100%; height:40px; padding: 40px; font-size:20px; } \n\r"
        css3 = ".baseColorVar2 { background-color:" + baseColorVar2.hex + "; width:50%; height:40px; padding: 40px; font-size:20px; } \n\r"
        css4 = ".baseColorVar3 { background-color:" + baseColorVar3.hex + "; width:100%; height:40px; padding: 40px; font-size:20px; } \n\r"
        css5 = ".baseColorVar4 { background-color:" + baseColorVar4.hex + "; width:50%; height:40px; padding: 40px; font-size:20px; } \n\r"
        css6 = ".Contrastcolor { background-color:" + ContrastColor.hex + "; width:10%; height:900px; position:absolute; right:300px; top:0px; color:" + baseColor.hex + "; padding: 40px; font-size:20px; } \n"

        f = open('output1.html', 'w')
        outputtxt = str(htmlpreface) + str(css1) + str(css2) + str(css3) + str(css4) + str(css5) + str(css6) + str(
            htmlcontent) + str(zeitzeile) + str(htmlclosing)
        f.write(outputtxt)
        f.close()

        programmcycles += 1
        time.sleep(1)

if __name__ == "__main__":
    generate_html_palette()

