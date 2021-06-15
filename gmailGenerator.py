class Languages:
    class English:
        englishGmailUser = "Who creating this gmail (name): "
        englishLanguageSwitch = "1 or 2 press select one/two: "
    
    class Turkish:
        turkishGmailUser = "Gmail oluşturan kişinin ismi: "
        turkishLanguageSwitch = "1 veya 2 bu iki rakamdan birini seçiniz: "

class gmail:
    gmailLogo = "@gmail.com"
    gmailFirst = "Gmail: "



langueSwitch = int(input("English / Türkçe (1 / 2): "))

if langueSwitch == 1:
    gmailUUser = input(Languages.English.englishGmailUser)
    gmailFFirst = input(gmail.gmailFirst)
    gmailFirstPPlus = gmailFFirst + gmail.gmailLogo
    print(f"""
----------------------------------

Gmail User Name: {gmailUUser}
-----------------------------
Gmail: {gmailFirstPPlus}

----------------------------------
    """)

elif langueSwitch == 2:
    gmailUser = input(Languages.Turkish.turkishGmailUser)
    gmailFirst = input(gmail.gmailFirst)
    gmailFirstPlus = gmailFirst + gmail.gmailLogo
    print(f"""
----------------------------------

Gmail User Name: {gmailUser}
-----------------------------
Gmail: {gmailFirstPlus}

----------------------------------
    """)

else:
    if langueSwitch == 1:
         print(Languages.English.englishLanguageSwitch)
    elif langueSwitch == 2:
         print(Languages.Turkish.turkishLanguageSwitch)