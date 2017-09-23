import re

def getcontent(listurl):
    i=0
    for i in range(0,len(listurl)):
        for j in range(0,len(listurl[i])):
            try:
                url=listurl[i][j]
                url=url.replace("amp;""")
                #open the url
                data =
                titlepat = "<title>(.*?)</title>"
                contentpat='id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(titlepat).findall(data)
                content=re.compile(contentpat).findall(data)
                thistitle = "此次没有获取到"
                thiscontent = "此次没有获取到"
                if(title!=[])
                    thistitle=title[0]
                dataall="<p>标题为："+thistitle+"</p><p>内容为："+thiscontent+"</p><br>"
                fh.write(dataall).encode("utf-8")
                print("di ")


