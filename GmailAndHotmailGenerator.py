class Languages:
    class GMAIL:
        class English:
            englishGmailUser = "Who creating this gmail (name): "
            englishLanguageSwitch = "1 or 2 press select one/two: "

        class Turkish:
            turkishGmailUser = "Gmail oluşturan kişinin ismi: "
            turkishLanguageSwitch = "1 veya 2 bu iki rakamdan birini seçiniz: "
    class HOTMAIL:
        class English:
            englishHotmailUser = "Who creating this gmail (name): "
            englishLanguageSwitch = "1 or 2 press select one/two: "

        class Turkish:
            turkishHotmailUser = "Gmail oluşturan kişinin ismi: "
            turkishLanguageSwitch = "1 veya 2 bu iki rakamdan birini seçiniz: "


class gmail:
    gmailLogo = "@gmail.com"
    gmailFirst = "Gmail: "

class hotmail:
    hotmailLogo = "@hotmail.com"
    hotmailFirst = "Hotmail: "


langueSwitch = int(input("English / Türkçe (1 / 2): "))
mailSwitch = int(input("Gmail / Hotmail (1 / 2): "))

if langueSwitch == 1:
    if mailSwitch == 1:
        gmailUUser = input(Languages.GMAIL.English.englishGmailUser)
        gmailFFirst = input(gmail.gmailFirst)
        gmailFirstPPlus = gmailFFirst + gmail.gmailLogo
        print(f"""
----------------------------------

Gmail User Name: {gmailUUser}
-----------------------------
Gmail: {gmailFirstPPlus}

----------------------------------
        """)
    elif mailSwitch == 2:
        hotmailUUser = input(Languages.HOTMAIL.English.englishHotmailUser)
        hotmailFFirst = input(hotmail.hotmailFirst)
        hotmailFirstPPlus = hotmailFFirst + hotmail.hotmailLogo
        print(f"""
----------------------------------

Hotmail User Name: {hotmailUUser}
-----------------------------
Hotmail: {hotmailFirstPPlus}

----------------------------------
        """)

elif langueSwitch == 2:
    if mailSwitch == 1:
        gmailUser = input(Languages.GMAIL.Turkish.turkishGmailUser)
        gmailFirst = input(gmail.gmailFirst)
        gmailFirstPlus = gmailFirst + gmail.gmailLogo
        print(f"""
----------------------------------

Gmail User Name: {gmailUser}
-----------------------------
Gmail: {gmailFirstPlus}

----------------------------------
        """)
    elif mailSwitch == 2:
        hotmailUser = input(Languages.HOTMAIL.English.englishHotmailUser)
        hotmailFirst = input(hotmail.hotmailFirst)
        hotmailFirstPlus = hotmailFirst + hotmail.hotmailLogo
        print(f"""
----------------------------------

Gmail User Name: {hotmailUser}
-----------------------------
Gmail: {hotmailFirst}

----------------------------------
        """)

else:
    if langueSwitch == 1:
        if mailSwitch == 1:
            print(Languages.GMAIL.English.englishLanguageSwitch)
        elif mailSwitch == 2:
            print(Languages.HOTMAIL.English.englishLanguageSwitch)
    elif langueSwitch == 2:
        if mailSwitch == 1:
            print(Languages.GMAIL.Turkish.turkishLanguageSwitch)
        elif mailSwitch == 2:
            print(Languages.HOTMAIL.Turkish.turkishLanguageSwitch)

    else:
        print(f"{Languages.GMAIL.English.englishLanguageSwitch} | {Languages.GMAIL.Turkish.turkishLanguageSwitch}")