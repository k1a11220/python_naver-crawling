from urllib.request import urlopen
from bs4 import BeautifulSoup

mechDesign = 20207
productDesign = 20102
circuitDesign = 20106
electricDesign = 20108
mec = 20205


html = urlopen("http://api.saramin.co.kr/job-search?ind_cd=20102&edu_lv=1")  

bsObject = BeautifulSoup(html, "html.parser") 


print(bsObject.job.keyword)