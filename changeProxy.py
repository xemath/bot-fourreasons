import os
import subprocess

def changeProxy(zip):
    os.chdir('C:/Users/ramir/Desktop/3.35/ProxyTool')
    subprocess.run(['autoproxytool.exe', '-changeproxy/US', f'-zip={zip[0]}{zip[1]}{zip[2]}*'], shell=True)
    #print(proceso)
    print('Puerto cambiado! - Proxy changed!')

#changeProxy("13224")
