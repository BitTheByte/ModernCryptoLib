from CryptoLib.RSA import RSA
import platform,os
clear = ""
if "Windows" in platform.system():
	clear = "cls"
if "Linux" in platform.system():
	clear = "clear"

welcome = '''
 Welcome to [CryptoLib] RSA Automation Script
   *-----------------------------------------*
   - CryptoLib Version : 0.9 (alpha)         -
   - Automation Script Version : 0.3 (alpha) -
   - Developer : BitTheByte(Ahmed Ezzat)     -
   * ----------------------------------------*
'''
options = '''
  [1] Attacks Menu
  [2] Convert Menu
  [3] Export Menu (Soon) (API ONLY)
  [4] Utillities Menu (Soon) (API ONLY)
  [99] Back/Exit'''
chinsese_Remainer_menu = '''
 [-][1] Attack Requirments:
 [*] 0-> p 			 {0}
 [*] 1-> q 			 {1}
 [*] 2-> dp			 {2}
 [*] 3-> dq			 {3}
 [*] 4-> Chipher text {4}
 [!] USEGE : n=value'''
common_modulus_menu = '''
 [-][2] Attack Requirments:
 [*] 0-> Chipher text 1 		 {0}
 [*] 1-> Chipher text 2 		 {1}
 [*] 2-> Exponent 1			 	 {2}
 [*] 3-> Exponent 2			 	 {3}
 [*] 4-> Modulus 	 			 {4}
 [!] USEGE : n=value'''
hasted_menu = '''
 [-][4] Attack Requirments:
 [*] 0-> Exponent 1			 {0}
 [*] 1-> Exponent 2			 {1}
 [*] 2-> Exponent 3			 {2}
 [*] 3-> Chipher text 1 	 {3}
 [*] 4-> Chipher text 2 	 {4}
 [*] 5-> Chipher text 3 	 {5}
 [!] USEGE : n=value'''
fermet_menu = '''
 [-][3] Attack Requirments:
 [*] 0-> Modulus	 {0}
 [!] USEGE : n=value'''
wiener_menu = '''
 [-][5] Attack Requirments:
 [*] 0-> Modulus	 	{0}
 [*] 1-> Exponent	{1}
 [!] USEGE : n=value'''
attack_menu = '''
  [-] Available Attacks
  [1] Chinsese Remainer
  [2] Common Modulus
  [3] Fernet
  [4] Hasted
  [5] Wiener
  [6] Side Channel (Soon) (API ONLY)
  [99] Back'''
convert_menu ='''
  [-] Converts
  [*] 0-> Hex to Decimal
  [*] 1-> base64 to number
  [*] 2-> number to text
  USAGE : n=value'''
## MAIN LOOP ##
while(1):
	os.system(clear)
	print welcome
	print options
	curser = ">>>"
	choose = raw_input(curser)
	if choose == "99":
		print "[~] GOOD BYE ^_^"
		break
	if choose == "1":
		os.system(clear)
		while(1):
			os.system(clear)
			print attack_menu
			choose = raw_input(curser)
			if choose == "99":
				break
			if choose == "1":
				os.system(clear)
				print chinsese_Remainer_menu.format('','','','','')
				args = [0,0,0,0,0]
				while(1):
					try:
						user_change_value = raw_input(curser)
						if user_change_value == "99":
							break

						if user_change_value.lower() == "run plain":
							try:
								print "[#] Solution(Plain Text) : " + str(RSA.convert.number_to_text(RSA.attacks.Chinese_remainder_theorem(long(args[0]),long(args[1]),long(args[2]),long(args[3]),long(args[4]))))
							except Exception as e:
								print "[~] {}".format(e)
						if user_change_value.lower() == "run hex":
							try:
								print "[#] Solution(hex) : " + hex(RSA.attacks.Chinese_remainder_theorem(long(args[0]),long(args[1]),long(args[2]),long(args[3]),long(args[4])))
							except Exception as e:
								print "[~] {}".format(e)
						if user_change_value.lower() == "info":
							os.system(clear)
							print chinsese_Remainer_menu.format(args[0],args[1],args[2],args[3],args[4])
						if "=" in user_change_value:
							user_change_value = user_change_value.replace("{","").replace("}","").split("=")
							args[ int(user_change_value[0]) ] = int(user_change_value[1])
					except Exception as e:
						print "[~] {}".format(e)
						pass
			if choose == "2":
				os.system(clear)
				print common_modulus_menu.format('','','','','')
				args = [0,0,0,0,0]
				while(1):
					try:
						user_change_value = raw_input(curser)
						if user_change_value == "99":
							break
						if user_change_value.lower() == "run plain":
							try:
								print "[#] Solution(Plain Text) : " + str(RSA.convert.number_to_text(RSA.attacks.Common_modulus(long(args[0]),long(args[1]),long(args[2]),long(args[3]),long(args[4]))))
							except Exception as e:
								print "[~] {}".format(e)
						if user_change_value.lower() == "run hex":
							try:
								print "[#] Solution(hex) : " + hex(RSA.attacks.Common_modulus(long(args[0]),long(args[1]),long(args[2]),long(args[3]),long(args[4])))
							except Exception as e:
								print "[~] {}".format(e)
						if user_change_value.lower() == "info":
							os.system(clear)
							print common_modulus_menu.format(args[0],args[1],args[2],args[3],args[4])
						if "=" in user_change_value:
							user_change_value = user_change_value.replace("{","").replace("}","").split("=")
							args[ int(user_change_value[0]) ] = int(user_change_value[1])
					except Exception as e:
						print "[~] {}".format(e)
						pass
			if choose == "3":
				os.system(clear)
				print fermet_menu.format('')
				args = [0]
				while(1):
					try:
						user_change_value = raw_input(curser)
						if user_change_value == "99":
							break
						if  "run" in user_change_value.lower():
							try:
								print "[#] Solution(p,q) : " + str(RSA.attacks.Fermat(long(args[0])))
							except Exception as e:
								print "[~] {}".format(e)
						if user_change_value.lower() == "info":
							os.system(clear)
							print fermet_menu.format(args[0])
						if "=" in user_change_value:
							user_change_value = user_change_value.replace("{","").replace("}","").split("=")
							args[ int(user_change_value[0]) ] = int(user_change_value[1])
					except Exception as e:
						print "[~] {}".format(e)
						pass
			if choose == "4":
				os.system(clear)
				print hasted_menu.format('','','','','','')
				args = [0,0,0,0,0,0]
				while(1):
					try:
						user_change_value = raw_input(curser)
						if user_change_value == "99":
							break
						if user_change_value.lower() == "run plain":
							try:
								print "[#] Solution(Plain Text) : " + str(RSA.convert.number_to_text(RSA.attacks.hasted(long(args[0]),long(args[1]),long(args[2]),long(args[3]),long(args[4]),long(args[5]))))
							except Exception as e:
								print "[~] {}".format(e)
						if user_change_value.lower() == "run hex":
							try:
								print "[#] Solution(hex) : " + hex(RSA.attacks.hasted(long(args[0]),long(args[1]),long(args[2]),long(args[3]),long(args[4]),long(args[5])))
							except Exception as e:
								print "[~] {}".format(e)
						if user_change_value.lower() == "info":
							os.system(clear)
							print hasted_menu.format(args[0],args[1],args[2],args[3],args[4],args[5])
						if "=" in user_change_value:
							user_change_value = user_change_value.replace("{","").replace("}","").split("=")
							args[ int(user_change_value[0]) ] = int(user_change_value[1])
					except Exception as e:
						print "[~] {}".format(e)
						pass
			if choose == "5":
				os.system(clear)
				print wiener_menu.format('','')
				args = [0,0]
				while(1):
					try:
						user_change_value = raw_input(curser)
						if user_change_value == "99":
							break
						if  "run" in user_change_value.lower():
							try:
								print "[#] Solution(p,q,d) : " + str(RSA.attacks.Wiener(long(args[0]),long(args[1])))
							except Exception as e:
								print "[~] {}".format(e)
						if user_change_value.lower() == "info":
							os.system(clear)
							print wiener_menu.format(args[0],long(args[1]))
						if "=" in user_change_value:
							user_change_value = user_change_value.replace("{","").replace("}","").split("=")
							args[ int(user_change_value[0]) ] = int(user_change_value[1])
					except Exception as e:
						print "[~] {}".format(e)
						pass
	if choose == "2":
			os.system(clear)
			print convert_menu
			while(1):
				user_change_value = raw_input(curser)
				if user_change_value == "99":
					break
				if "=" in user_change_value:
					user_change_value = user_change_value.replace("{","").replace("}","").split("=")
					if user_change_value[0] == '0':
						print "[#] Solution (DEC.):"  + str(RSA.convert.bytes_to_number( (user_change_value[1]) ))
					if user_change_value[0] == '1':
						print "[#] Solution (BASE64):"  + str(RSA.convert.base64_to_number( (user_change_value[1]) ))
					if user_change_value[0] == '2':
						print "[#] Solution (Plain):"  + str(RSA.convert.number_to_text( (user_change_value[1]) ))