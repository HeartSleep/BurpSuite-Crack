#!/bin/sh
#author:Waffle

echo '
    ____                      _____       _ __          ______                __  
   / __ )__  ___________     / ___/__  __(_) /____     / ____/________ ______/ /__
  / __  / / / / ___/ __ \    \__ \/ / / / / __/ _ \   / /   / ___/ __ `/ ___/ //_/
 / /_/ / /_/ / /  / /_/ /   ___/ / /_/ / / /_/  __/  / /___/ /  / /_/ / /__/ ,<   
/_____/\__,_/_/  / .___/   /____/\__,_/_/\__/\___/   \____/_/   \__,_/\___/_/|_|  
                /_/                                                               
'

UpdateFix(){
    # r start_script for start_sh
    echo "-Dfile.encoding=utf-8
    -noverify
    -javaagent:BurpSuiteLoader.jar
    -Xmx2048m"  >> /Applications/Burp\ Suite\ Professional.app/Contents/vmoptions.txt
}


Crack(){
    # cp loader for app addr
    cp BurpSuiteLoader.jar /Applications/Burp\ Suite\ Professional.app/Contents/java/app/

    # r start_script for start_sh
    echo "-Dfile.encoding=utf-8
    -noverify
    -javaagent:BurpSuiteLoader.jar
    -Xmx2048m"  >> /Applications/Burp\ Suite\ Professional.app/Contents/vmoptions.txt

    # Start Burp Loader & Burp Suite
    /Applications/Burp\ Suite\ Professional.app/Contents/PlugIns/jre.bundle/Contents/Home/bin/java -Dfile.encoding=utf-8 -noverify -javaagent:/Applications/Burp\ Suite\ Professional.app/Contents/java/app/BurpSuiteLoader.jar -Xmx2048m -jar --illegal-access=permit /Applications/Burp\ Suite\ Professional.app/Contents/java/app/burpsuite_pro.jar & /Applications/Burp\ Suite\ Professional.app/Contents/PlugIns/jre.bundle/Contents/Home/bin/java -jar /Applications/Burp\ Suite\ Professional.app/Contents/java/app/BurpSuiteLoader.jar
}

Tocn(){
    # cp BurpSuiteCnV2.0.jar fo app addr
     cp BurpSuiteCnV2.0.jar /Applications/Burp\ Suite\ Professional.app/Contents/java/app/

     #cn start script
    echo "-Dfile.encoding=utf-8
    -javaagent:BurpSuiteCnV2.0.jar
    -noverify
    -javaagent:BurpSuiteLoader.jar
    -Xmx2048m" >> /Applications/Burp\ Suite\ Professional.app/Contents/vmoptions.txt
}





# Main()
echo '输入crack类型
1.初次安装Crack
2.更新后修复Crack
3.汉化'

read -p "inputNumber:default 1" number
case $number in
    1) 
    Crack 
    ;;
    2)
    UpdateFix
    3)
    Tocn
    ;;
    *)
    crack
    ;;
esac










