import os
import time
import subprocess


def update_script():
	os.system('clear')
	print("")
	print("[+] updating .....")
	print("")
	time.sleep(2)
	os.system('sudo apt update')


def remove_trash():
	print("")
	print("[+] auto cleaning ...")
	print("")
	time.sleep(2)
	os.system('sudo apt autoremove -y && sudo apt autoclean -y')

def upgrade_script():
	print("")
	print("[+] Upgrading ....")
	os.system('sudo apt upgrade -y')
	os.system('sudo apt-get upgrade -y')
	os.system('sudo apt-get dist-upgrade -y')

update_script()
remove_trash()
upgrade_script()