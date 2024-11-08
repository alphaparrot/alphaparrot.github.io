import os, time

def imgplate(filename,alt,description,png,pdf):
    text = ('\t\t\t\t<div class="image full">                               \n'+
            '\t\t\t\t    <a target="_blank" href="%s"><img src="%s" alt="%s"></a>                    \n'+
            '\t\t\t\t    <div class="description">                          \n'+
            '\t\t\t\t    <p style="text-align:left" class="description content"> %s <br/>           \n'+
            '\t\t\t\t    <a href="%s" target="_blank">PNG</a> | <a href="%s" target="_blank">PDF</a></p> \n'+
            '\t\t\t\t    </div>                                \n '+
            '\t\t\t\t</div> ')%(filename,filename,alt,description,png,pdf)
    return text

def img2plate(file1,alt1,file2,alt2,description,png1,pdf1,png2,pdf2):
    text  = ('\t\t\t\t<div class="image full">                              \n'+
            '\t\t\t\t    <div class="flex-container">                       \n'+
            '\t\t\t\t    <div class="column"><a target="_blank" href="%s"><img src="%s" alt="%s"></a></div> \n'+
            '\t\t\t\t    <div class="column"><a target="_blank" href="%s"><img src="%s" alt="%s"></a></div> \n'+
            '\t\t\t\t    </div>                                             \n'+
            '\t\t\t\t    <div class="description">                          \n'+
            '\t\t\t\t    <p style="text-align:left" class="description content"> %s <br/>           \n'+
            '\t\t\t\t    Left: <a href="%s" target="_blank">PNG</a> | <a href="%s" target="_blank">PDF</a><br/> \n'+
            '\t\t\t\t    Right: <a href="%s" target="_blank">PNG</a> | <a href="%s" target="_blank">PDF</a></p> \n'+
            '\t\t\t\t    </div>                                             \n'+
            '\t\t\t\t</div>  ')%(file1,file1,alt1,file2,file2,alt2,description,png1,pdf1,png2,pdf2)
    return text
#imgplate(filepath,alttext,description,pdflink,pnglink)
#imgplate(filepath1,alttext1,filepath2,alttext2,description,pdflink1,pnglink1,pdflink2,pnglink2)

par = "<p>%s</p>"

section = '<p style="font-size:25px"><a name="%s">%s</a></p>'
#section%(name,sectiontitle)

def makeneighborhood(neighborhood,pathdir,deathratio):
    with open("template.html","r") as templatef:
        template = templatef.read().split('\n')
    filename = neighborhood.replace("/","_").replace(" ","_").replace("-","_")+".html"
    title = "\t\t<title>%s | COVID-19 Dashboard</title>"%neighborhood
    navlink = '\t\t\t\t\t\t\t<li class="active"><a href="%s">%s, Toronto</a></li>'%(filename,neighborhood)
    header = '\t\t\t\t\t<h2><a name="current">%s COVID-19 Data</a></h2>'%neighborhood
    
    if deathratio>0:
        deathplate = "<br> \n<p>1 in %d people have died in %s, Toronto.</p>\n<br>\n"%(deathratio,neighborhood)
    else:
        deathplate = "<br> \n<p>No people have died in %s, Toronto.</p>\n<br>\n"%neighborhood
    
    body = ("<header><h2>%s Plots</h2></header>    \n"%neighborhood+
            deathplate+
            imgplate("%s_rawcases.png"%pathdir,"%s cases per day"%neighborhood,
                      "New COVID-19 cases per day in %s, Toronto. These data "%neighborhood+
                      "have not had a rolling average applied.","%s_rawcases.png"%pathdir,
                      "%s_rawcases.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_avgcases.png"%pathdir,
                      "%s average cases per day, linear scale"%neighborhood,
                      "%s_avgcases_log.png"%pathdir,
                      "%s_average cases per day, logarithmic scale"%neighborhood,
                      "7-day average of new COVID-19 cases per day in %s, Toronto."%neighborhood+
                      "These data have had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_avgcases.png"%pathdir,"%s_avgcases.pdf"%pathdir,
                      "%s_avgcases_log.png"%pathdir,"%s_avgcases_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_breakdown.png"%pathdir,
                      "%s case breakdown, linear scale"%neighborhood,
                      "%s_breakdown_log.png"%pathdir,
                      "%s_case breakdown, logarithmic scale"%neighborhood,
                      "Breakdown of daily COVID-19 cases per day in %s, Toronto by status--"%neighborhood+
                      "active, recovered, ever hospitalized, or dead. Note that 'hospitalized' is a status that applies to any of the other 3 categories. These data have not had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_breakdown.png"%pathdir,"%s_breakdown.pdf"%pathdir,
                      "%s_breakdown_log.png"%pathdir,"%s_breakdown_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            imgplate("%s_Rt.png"%pathdir,"Historical %s effective reproductive number"%neighborhood,
                      "Raw and 2-week average of %s and Toronto's effective reproductive numbers. This is the average number of people a sick person will infect. If this is increasing, then transmission is increasing, even if cases are still declining. If this is above 1, then cases are increasing. If it is decreasing, then transmission is declining, even if cases are still rising. Note that due to the existence of super-spreaders, this metric is not the same as the number of people the average sick person will infect (i.e. a person selected at random from the cohort of infected people will typically infect fewer people than would be implied by R<sub>t</sub>, but a small fraction will infect many more."%neighborhood,"%s_Rt.png"%pathdir,
                      "%s_Rt.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_relcases.png"%pathdir,
                      "%s average cases per day per 100k, linear scale"%neighborhood,
                      "%s_relcases_log.png"%pathdir,
                      "%s_average cases per day per 100k, logarithmic scale"%neighborhood,
                      "7-day average of new COVID-19 cases per day per 100k in %s, Toronto."%neighborhood+
                      "These data have had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_relcases.png"%pathdir,"%s_relcases.pdf"%pathdir,
                      "%s_relcases_log.png"%pathdir,"%s_relcases_log.pdf"%pathdir)+"\n"+
            "<br >\n"+
            "<p>Last updated %s</p>"%(time.asctime(time.localtime())))
            
    html = []
    for line in template:
        html.append(line)
        if "<!-- TITLE -->" in line:
            html.append(title)
        elif "<!-- NAVBAR -->" in line:
            html.append(navlink)
        elif "<!-- HEADER -->" in line:
            html.append(header)
        elif "<!-- BODY -->" in line:
            html.append(body)
            
    with open("%s"%filename,"w") as htmlf:
        htmlf.write('\n'.join(html))
        
def makephu(phu,pathdir,deathratio):
    with open("template.html","r") as templatef:
        template = templatef.read().split('\n')
    filename = "ontario_%s"%phu.replace('"','').replace('&','and').replace(",","").replace("/","_").replace(" ","_").replace("-","_")+".html"
    print(filename)
    title = "\t\t<title>%s, ON | COVID-19 Dashboard</title>"%phu
    navlink = '\t\t\t\t\t\t\t<li class="active"><a href="%s">%s, ON</a></li>'%(filename,phu)
    header = '\t\t\t\t\t<h2><a name="current">%s, ON COVID-19 Data</a></h2>'%phu
    
    if deathratio>0:
        deathplate = "<br> \n<p>1 in %d people have died in %s, Ontario.</p>\n<br>\n"%(deathratio,phu)
    else:
        deathplate = "<br> \n<p>No people have died in %s, Ontario.</p>\n<br>\n"%phu
    
    body = ("<header><h2>%s Plots</h2></header>    \n"%phu+
            img2plate("%s_rawdaily.png"%pathdir,
                      "%s raw cases per day, linear scale"%phu,
                      "%s_rawdaily_log.png"%pathdir,
                      "%s_raw cases per day, logarithmic scale"%phu,
                      "New COVID-19 cases per day in %s, ON."%phu+
                      "These data have not had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_rawdaily.png"%pathdir,"%s_rawdaily.pdf"%pathdir,
                      "%s_rawdaily_log.png"%pathdir,"%s_rawdaily_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_avgdaily.png"%pathdir,
                      "%s average cases per day, linear scale"%phu,
                      "%s_avgdaily_log.png"%pathdir,
                      "%s_average cases per day, logarithmic scale"%phu,
                      "7-day average of new COVID-19 cases per day in %s, ON."%phu+
                      "These data have had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_avgdaily.png"%pathdir,"%s_avgdaily.pdf"%pathdir,
                      "%s_avgdaily_log.png"%pathdir,"%s_avgdaily_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_active.png"%pathdir,
                      "%s, ON active cases, linear scale"%phu,
                      "%s_active_log.png"%pathdir,
                      "%s, ON_active cases, logarithmic scale"%phu,
                      "Active COVID-19 cases each day in %s, ON."%phu+
                      "  These data have not had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_active.png"%pathdir,"%s_active.pdf"%pathdir,
                      "%s_active_log.png"%pathdir,"%s_active_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            imgplate("%s_Rt.png"%pathdir,"Historical %s effective reproductive number"%phu,
                      "Raw and 2-week average of %s and ON's effective reproductive numbers. This is the average number of people a sick person will infect. If this is increasing, then transmission is increasing, even if cases are still declining. If this is above 1, then cases are increasing. If it is decreasing, then transmission is declining, even if cases are still rising. Note that due to the existence of super-spreaders, this metric is not the same as the number of people the average sick person will infect (i.e. a person selected at random from the cohort of infected people will typically infect fewer people than would be implied by R<sub>t</sub>, but a small fraction will infect many more."%phu,
                      "%s_Rt.png"%pathdir,"%s_Rt.pdf"%pathdir)+"\n"+
            "<br> \n"+
            imgplate("%s_deaths.png"%pathdir,
                      "%s, ON average deaths per day"%phu,
                      "7-day average of COVID-19 deaths per day in %s, ON."%phu+
                      "These data have had a rolling average applied.",
                      "%s_deaths.png"%pathdir,"%s_deaths.pdf"%pathdir)+"\n"+
            deathplate+
            "<p>Last updated %s</p>"%(time.asctime(time.localtime())))
    
    html = []
    for line in template:
        html.append(line)
        if "<!-- TITLE -->" in line:
            html.append(title)
        elif "<!-- NAVBAR -->" in line:
            html.append(navlink)
        elif "<!-- HEADER -->" in line:
            html.append(header)
        elif "<!-- BODY -->" in line:
            html.append(body)
            
    with open("%s"%filename,"w") as htmlf:
        htmlf.write('\n'.join(html))
    

def makeStateorProvince(name,pathdir,deathratio):
    with open("template.html","r") as templatef:
        template = templatef.read().split('\n')
    filename = name.replace('"','').replace('&','and').replace(",","").replace("/","_").replace(" ","_").replace("-","_")+".html"
    print(filename)
    title = "\t\t<title>%s | COVID-19 Dashboard</title>"%name
    navlink = '\t\t\t\t\t\t\t<li class="active"><a href="%s">%s</a></li>'%(filename,name)
    header = '\t\t\t\t\t<h2><a name="current">%s COVID-19 Data</a></h2>'%name
    
    if deathratio>0:
        deathplate = "<br> \n<p>1 in %d people have died in %s.</p>\n<br>\n"%(deathratio,name)
    else:
        deathplate = "<br> \n<p>No people have died in %s.</p>\n<br>\n"%(name)
    
    body = ("<header><h2>%s Plots</h2></header>    \n"%name+
            img2plate("%s_rawdaily.png"%pathdir,
                      "%s raw cases per day"%name,
                      "%s_avgdaily.png"%pathdir,
                      "%s_average cases per day"%name,
                      "New COVID-19 cases per day in %s"%name+
                      " These data have not had a rolling average applied. The first plot gives raw cases per day, while the second gives the 7-day moving average.",
                      "%s_rawdaily.png"%pathdir,"%s_rawdaily.pdf"%pathdir,
                      "%s_avgdaily.png"%pathdir,"%s_avgdaily.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_relrawdaily.png"%pathdir,
                      "%s cases per 100k per day, linear scale"%name,
                      "%s_relrawdaily_log.png"%pathdir,
                      "%s_cases per 100k per day, logarithmic scale"%name,
                      "New COVID-19 cases per 100k per day in %s,"%name+
                      " compared to the national average. These data have not had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_relrawdaily.png"%pathdir,"%s_relrawdaily.pdf"%pathdir,
                      "%s_relrawdaily_log.png"%pathdir,"%s_relrawdaily_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_relavgdaily.png"%pathdir,
                      "%s average cases per 100k per day, linear scale"%name,
                      "%s_relavgdaily_log.png"%pathdir,
                      "%s_average cases per 100k per day, logarithmic scale"%name,
                      "7-day average of new COVID-19 cases per 100k per day in %s,"%name+
                      " compared to the national average. These data have had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_relavgdaily.png"%pathdir,"%s_relavgdaily.pdf"%pathdir,
                      "%s_relavgdaily_log.png"%pathdir,"%s_relavgdaily_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_3wk.png"%pathdir,
                      "%s active cases, linear scale"%name,
                      "%s_3wk_log.png"%pathdir,
                      "%s_active cases, logarithmic scale"%name,
                      "3-week running sum of COVID-19 cases each day in %s."%name+
                      " These data have not had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_3wk.png"%pathdir,"%s_3wk.pdf"%pathdir,
                      "%s_3wk_log.png"%pathdir,"%s_3wk_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_rel3wk.png"%pathdir,
                      "%s active cases per 1000, linear scale"%name,
                      "%s_rel3wk_log.png"%pathdir,
                      "%s_active cases per 1000, logarithmic scale"%name,
                      "3-week running sum of COVID-19 cases per 1000 each day in %s."%name+
                      " These data have not had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_rel3wk.png"%pathdir,"%s_rel3wk.pdf"%pathdir,
                      "%s_rel3wk_log.png"%pathdir,"%s_rel3wk_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            imgplate("%s_Rt.png"%pathdir,"Historical %s effective reproductive number"%name,
                      "Raw and 2-week average of the effective reproductive number in %s. This is the average number of people a sick person will infect. If this is increasing, then transmission is increasing, even if cases are still declining. If this is above 1, then cases are increasing. If it is decreasing, then transmission is declining, even if cases are still rising. Note that due to the existence of super-spreaders, this metric is not the same as the number of people the average sick person will infect (i.e. a person selected at random from the cohort of infected people will typically infect fewer people than would be implied by R<sub>t</sub>, but a small fraction will infect many more."%name,
                      "%s_Rt.png"%pathdir,"%s_Rt.pdf"%pathdir)+"\n"+
            deathplate+
            img2plate("%s_rawdeaths.png"%pathdir,
                      "%s raw deaths per day"%name,
                      "%s_relavgdeaths.png"%pathdir,
                      "%s average deaths per 1M per day"%name,
                      "Raw COVID-19 deaths per day in %s, and the 7-day average of deaths per million per day in the same compared to the national average."%name,
                      "%s_rawdeaths.png"%pathdir,"%s_rawdeaths.pdf"%pathdir,
                      "%s_relavgdeaths.png"%pathdir,"%s_relavgdeaths.pdf"%pathdir)+"\n"+
            "<br >\n"+
            "<p>Last updated %s</p>"%(time.asctime(time.localtime())))
    
    html = []
    for line in template:
        html.append(line)
        if "<!-- TITLE -->" in line:
            html.append(title)
        elif "<!-- NAVBAR -->" in line:
            html.append(navlink)
        elif "<!-- HEADER -->" in line:
            html.append(header)
        elif "<!-- BODY -->" in line:
            html.append(body)
            
    with open("%s"%filename,"w") as htmlf:
        htmlf.write('\n'.join(html))
        
        
def makeCounty(county,state,pathdir,deathratio):
    with open("template.html","r") as templatef:
        template = templatef.read().split('\n')
    filename1 = "%s_%s"%(state,
                county.replace('"','').replace('&','and').replace(",","").replace("/","_").replace(" ","_").replace("-","_"))+".html"
    filename = "%s_%s"%(state.replace(" ","_"),
                county.replace('"','').replace('&','and').replace(",","").replace("/","_").replace(" ","_").replace("-","_"))+".html"
    os.system('rm -rf "%s"'%filename1)
    #print(filename)
    title = "\t\t<title>%s County, %s | COVID-19 Dashboard</title>"%(county,state)
    navlink = '\t\t\t\t\t\t\t<li class="active"><a href="%s">%s County, %s</a></li>'%(filename,county,state)
    header = '\t\t\t\t\t<h2><a name="current">%s County, %s COVID-19 Data</a></h2>'%(county,state)
    
    if deathratio>0:
        deathplate = "<br> \n<p>1 in %d people have died in %s County, %s.</p>\n<br>\n"%(deathratio,county,state)
    else:
        deathplate = "<br> \n<p>No people have died in %s County, %s.</p>\n<br>\n"%(county,state)
    
    body = ("<header><h2>%s Plots</h2></header>    \n"%county+
            deathplate+
            img2plate("%s_rawdaily.png"%pathdir,
                      "%s County raw cases per day"%county,
                      "%s_avgdaily.png"%pathdir,
                      "%s_County average cases per day"%county,
                      "New COVID-19 cases per day in %s County"%county+
                      " These data have not had a rolling average applied. The first plot gives raw cases per day, while the second gives the 7-day moving average.",
                      "%s_rawdaily.png"%pathdir,"%s_rawdaily.pdf"%pathdir,
                      "%s_avgdaily.png"%pathdir,"%s_avgdaily.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_relrawdaily.png"%pathdir,
                      "%s County cases per 100k per day, linear scale"%county,
                      "%s_relrawdaily_log.png"%pathdir,
                      "%s_County cases per 100k per day, logarithmic scale"%county,
                      "New COVID-19 cases per 100k per day in %s County,"%county+
                      " compared to the national average. These data have not had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_relrawdaily.png"%pathdir,"%s_relrawdaily.pdf"%pathdir,
                      "%s_relrawdaily_log.png"%pathdir,"%s_relrawdaily_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_relavgdaily.png"%pathdir,
                      "%s County average cases per 100k per day, linear scale"%county,
                      "%s_relavgdaily_log.png"%pathdir,
                      "%s_County average cases per 100k per day, logarithmic scale"%county,
                      "7-day average of new COVID-19 cases per 100k per day in %s County,"%county+
                      " compared to the national average. These data have had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_relavgdaily.png"%pathdir,"%s_relavgdaily.pdf"%pathdir,
                      "%s_relavgdaily_log.png"%pathdir,"%s_relavgdaily_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_3wk.png"%pathdir,
                      "%s County active cases, linear scale"%county,
                      "%s_3wk_log.png"%pathdir,
                      "%s_County active cases, logarithmic scale"%county,
                      "3-week running sum of COVID-19 cases each day in %s County."%county+
                      " These data have not had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_3wk.png"%pathdir,"%s_3wk.pdf"%pathdir,
                      "%s_3wk_log.png"%pathdir,"%s_3wk_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            img2plate("%s_rel3wk.png"%pathdir,
                      "%s County active cases per 1000, linear scale"%county,
                      "%s_rel3wk_log.png"%pathdir,
                      "%s_County active cases per 1000, logarithmic scale"%county,
                      "3-week running sum of COVID-19 cases per 1000 each day in %s County."%county+
                      " These data have not had a rolling average applied. The first plot gives the data on a linear vertical scale, while the second gives the data on a logarithmic vertical scale, which better shows different exponentials.",
                      "%s_rel3wk.png"%pathdir,"%s_rel3wk.pdf"%pathdir,
                      "%s_rel3wk_log.png"%pathdir,"%s_rel3wk_log.pdf"%pathdir)+"\n"+
            "<br> \n"+
            imgplate("%s_Rt.png"%pathdir,"Historical %s County effective reproductive number"%county,
                      "Raw and 2-week average of the effective reproductive number in %s County, compared to the state average. This is the average number of people a sick person will infect. If this is increasing, then transmission is increasing, even if cases are still declining. If this is above 1, then cases are increasing. If it is decreasing, then transmission is declining, even if cases are still rising. Note that due to the existence of super-spreaders, this metric is not the same as the number of people the average sick person will infect (i.e. a person selected at random from the cohort of infected people will typically infect fewer people than would be implied by R<sub>t</sub>, but a small fraction will infect many more."%county,
                      "%s_Rt.png"%pathdir,"%s_Rt.pdf"%pathdir)+"\n"+
            "<br >\n"+
            "<p>Last updated %s</p>"%(time.asctime(time.localtime())))
    
    html = []
    for line in template:
        html.append(line)
        if "<!-- TITLE -->" in line:
            html.append(title)
        elif "<!-- NAVBAR -->" in line:
            html.append(navlink)
        elif "<!-- HEADER -->" in line:
            html.append(header)
        elif "<!-- BODY -->" in line:
            html.append(body)
            
    with open("%s"%filename,"w") as htmlf:
        htmlf.write('\n'.join(html))
        
        
def makeCountry(country,deathratio):
    with open("template.html","r") as templatef:
        template = templatef.read().split('\n')
    filename = "%s_country"%(country.replace('"','').replace('&','and').replace(",","").replace("/","_").replace(" ","_").replace("-","_"))+".html"
    #print(filename)
    title = "\t\t<title>%s | COVID-19 Dashboard</title>"%country
    navlink = '\t\t\t\t\t\t\t<li class="active"><a href="%s">%s</a></li>'%(filename,country)
    header = '\t\t\t\t\t<h2><a name="current">%s COVID-19 Data</a></h2>'%country
    
    if deathratio>0:
        deathplate = "<br> \n<p>1 in %d people have died in %s.</p>\n<br>\n"%(deathratio,country)
    else:
        deathplate = "<br> \n<p>No people have died in %s.</p>\n<br>\n"%country
    
    body = (imgplate("%s_summary.png"%country,
                     "COVID-19 summary for %s"%country,
                     "7-day average of daily cases, 2-week average of the effective reproductive number, 7-day average of daily deaths per million, and total cumulative cases as a percent of the population for %s."%country,
                      "%s_summary.png"%country,"%s_summary.pdf"%country)+"\n"+
            deathplate+
            "<p>Last updated %s</p>"%(time.asctime(time.localtime())))
    
    html = []
    for line in template:
        html.append(line)
        if "<!-- TITLE -->" in line:
            html.append(title)
        elif "<!-- NAVBAR -->" in line:
            html.append(navlink)
        elif "<!-- HEADER -->" in line:
            html.append(header)
        elif "<!-- BODY -->" in line:
            html.append(body)
            
    with open("%s"%filename,"w") as htmlf:
        htmlf.write('\n'.join(html))
    
    