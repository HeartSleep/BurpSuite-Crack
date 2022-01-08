#!/bin/python3
#author:Waffle

import re,os


def PrintBanner():
    Version=0.3
    banner=f'''

    ____                      `_____       _ __          ______                __  
   / __ )__  ___________     / ___/__  __(_) /____     / ____/________ ______/ /__
  / __  / / / / ___/ __ \    \__ \/ / / / / __/ _ \   / /   / ___/ __ `/ ___/ //_/
 / /_/ / /_/ / /  / /_/ /   ___/ / /_/ / / /_/  __/  / /___/ /  / /_/ / /__/ ,<   
/_____/\__,_/_/  / .___/   /____/\__,_/_/\__/\___/   \____/_/   \__,_/\___/_/|_|  
                /_/                                                  
                                                         version:{Version}  By:Waffle             
'''
    print(banner)


class BurpCrack:
    def __init__(self) :
        self.Burpjar2021="/Applications/Burp\ Suite\ Professional.app/Contents/java/app/burpsuite_pro.jar"
        self.Burpjar2022="/Applications/Burp Suite Professional.app/Contents/Resources/app/burpsuite_pro.jar"
        self.javaPath_2021="/Applications/Burp\ Suite\ Professional.app/Contents/PlugIns/jre.bundle/Contents/Home/bin/java"
        self.javaPath_2022="/Applications/Burp\ Suite\ Professional.app/Contents/Resources/jre.bundle/Contents/Home/bin/java"
        self.infofile="/Applications/Burp Suite Professional.app/Contents/Info.plist"
        self.startfile="/Applications/Burp Suite Professional.app/Contents/vmoptions.txt"
        self.startBurpLoader2021Jar="/Applications/Burp\ Suite\ Professional.app/Contents/java/app/BurpSuiteLoader.jar"
        self.startBurpLoader2022Jar="/Applications/Burp\ Suite\ Professional.app/Contents/Resources/app/BurpSuiteLoader.jar"
        self.BurpVersion=self.DetectBurpVersion()

    def DetectBurpVersion(self):
        with open(self.infofile,'r') as f:
            data=f.read()
            rexp=r'<key>CFBundleVersion</key>\n<string>(.*)</string>'
            version=re.findall(rexp,data)[0]
            return version
    def addCrackLoader(self):
        if os.path.exists(self.Burpjar2021):
            os.system('cp BurpSuiteLoader.jar /Applications/Burp Suite Professional.app/Contents/java/app/')
            addStart='''
            -Dfile.encoding=utf-8
            -noverify
            -javaagent:BurpSuiteLoader.jar
            -Xmx2048m'''
            with open(self.startfile,'a') as f:
                f.write(addStart)
        elif os.path.exists(self.Burpjar2022):
            os.system('cp BurpSuiteLoader.jar /Applications/Burp\ Suite\ Professional.app/Contents/Resources/app')
            addStart='''
            -noverify
            -javaagent:BurpSuiteLoader.jar'''
            with open(self.startfile,'a') as f:
                f.write(addStart)


            

    def startBurpjar(self):
        if os.path.exists(self.Burpjar2021):
            cmd=r'/Applications/Burp\ Suite\ Professional.app/Contents/PlugIns/jre.bundle/Contents/Home/bin/java -Dfile.encoding=utf-8 -noverify -javaagent:/Applications/Burp\ Suite\ Professional.app/Contents/java/app/BurpSuiteLoader.jar -Xmx2048m -jar --illegal-access=permit /Applications/Burp\ Suite\ Professional.app/Contents/java/app/burpsuite_pro.jar & /Applications/Burp\ Suite\ Professional.app/Contents/PlugIns/jre.bundle/Contents/Home/bin/java -jar /Applications/Burp\ Suite\ Professional.app/Contents/java/app/BurpSuiteLoader.jar'
            os.system(cmd)
        elif os.path.exists(self.Burpjar2022):
            cmd=r'/Applications/Burp\ Suite\ Professional.app/Contents/Resources/jre.bundle/Contents/Home/bin/java  -jar -Dfile.encoding=utf-8 -noverify -javaagent:/Applications/Burp\ Suite\ Professional.app/Contents/Resources/app/BurpSuiteLoader.jar  -XX:MaxRAMPercentage=50 --illegal-access=permit  /Applications/Burp\ Suite\ Professional.app/Contents/Resources/app/burpsuite_pro.jar & /Applications/Burp\ Suite\ Professional.app/Contents/Resources/jre.bundle/Contents/Home/bin/java  -jar /Applications/Burp\ Suite\ Professional.app/Contents/Resources/app/BurpSuiteLoader.jar'
            os.system(cmd)

    def Crack(self):
        self.addCrackLoader()
        self.startBurpjar()



def main():
    PrintBanner()
    crack=BurpCrack()
    print('[+]info 当前Burp版本为',crack.BurpVersion)
    flag=int(input('输入crack类型\n1.初次安装Crack\n2.更新后修复Crack\n'))
    if flag==1:
        crack.Crack()
    elif flag==2:
        crack.addCrackLoader()





if __name__ == '__main__':
    main()