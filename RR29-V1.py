import os
import subprocess

RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
CYAN = '\033[36m'
RESET = '\033[0m'

def clear_screen():
    # For Linux and MacOS
    if os.name == 'posix':
        os.system('clear')
    # For Windows
    else:
        os.system('cls')

def display_logo():
    logo = f"""
    {GREEN}
       ⢀⣀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣀⣀                                                                                                        
      ⢠⣿⢿⣿⣿⣽⣯⡿⣽⢯⡿⣽⢯⡿⣽⣯⣿⣽⣟⡿⣳                                                                                                  
      ⡸⡾⢟⣓⡓⠓⠯⠿⣿⣽⡽⣯⣿⡟⠭⠚⠒⠛⠺⢯⢗             __     __  _                                                                               
      ⣞⢵⢯⢟⡿⣷⣶⢀⠈⢹⣿⡋⠄⡀⣴⣶⡿⡿⣻⢪⡪             \\ \\   / / / |                                                                              
      ⡧⡃⡓⠍⠊⠊⠊⠳⢅⣽⣿⣇⢜⠜⠙⠈⠊⠑⡑⢑⡱     _____    \\ \\ / /  | |                                                                              
      ⣿⣾⣶⣦⣶⣶⣴⣶⡯⣷⣿⡯⣟⣶⣶⣶⣶⣴⣶⣶⣷    |_____|    \\ V /   | |                                                                              
      ⢫⡻⡽⣫⢿⢽⣻⣳⢿⣽⣿⢯⣻⣞⣯⢿⢽⢯⡻⡝⡟                \\_/    |_|                                                                              
      ⢂⡊⠊⠇⢫⣑⣭⠾⢻⠾⡿⢟⠞⠷⣥⣉⡣⠣⠃⡑⢔       Why me?                                                                       
      ⠐⢱⣦⠐⢿⣿⣿⣴⡄⠑⠘⠈⢠⣦⣿⡿⣯⠂⣠⡎⠆       Instagram! @0.1exe
      ⠄ ⢈⠿⣌⢄⣀⣀⠄⠄⠠⠖⠄⠄⠄⡀⣀⠄⣰⠟⡑       Telegram: @0.1exe                                                                                     
      ⠄⠄⠑⡹⢧⡈⢉⠙⠛⠛⠛⠛⠛⢉⠉⢁⢴⠋ ⠜⠄       For tools recommendation, please DM me.
      ⠄⠄⠄⠈⠪⣳⡦⡯⣿⡄⠄⢴⣯⣖⢵⡞⡑ ⠄⠄⠄       Released date: 1/28/25 - By: Mr. RedRaccoon </>
      ⠄⠄⠄⠄⠄⠄⠻⢾⣿⡅⠄⣽⣿⠾ ⠄⠄⠄⠄⠄⠄

  ######                  ######                                                                                           
  #     #  ######  #####  #     #    ##     ####    ####    ####    ####   #    #                                          
  #     #  #       #    # #     #   #  #   #    #  #    #  #    #  #    #  ##   #                                          
  ######   #####   #    # ######   #    #  #       #       #    #  #    #  # #  #                                          
  #   #    #       #    # #   #    ######  #       #       #    #  #    #  #  # #                                          
  #    #   #       #    # #    #   #    #  #    #  #    #  #    #  #    #  #   ##                                          
  #     #  ######  #####  #     #  #    #   ####    ####    ####    ####   #    # 
                                           
                                          .--~*teu.                    .8u   
                                         dF     988Nx    .xn!~%x.     m888R- 
                                        d888b   `8888>  x888   888.    98P   
                                        ?8888>  98888F X8888   8888:   ^8    
                                         "**"  x88888~ 88888   X8888   J"    
                  Link:                       d8888*`  88888   88888> +"     
       https://0xe1i.blogspot.com/          z8**"`   : `8888  :88888X        
                 @0.1exe                  :?.....  ..F   `"**~ 88888>        
                                         <""888888888~  .xx.   88888         
                                         8:  "888888*  '8888>  8888~         
                                         ""    "**"`    888"  :88%           
                                                         ^"===""             
                                                        
    {RESET}
    """

    print(logo)


def clone_tool(tool_name, repo_url):
    tool_path = f"/home/kali/{tool_name}"
    
    if not os.path.exists(tool_path):
        print(f"Cloning {tool_name} from {repo_url}...")
        subprocess.run(["git", "clone", repo_url, tool_path])
        print(f"Download completed!\nTool is located in: {tool_path}")
    else:
        print(f"{tool_name} already exists at {tool_path}. No need to clone again.")

def select_tool(tool_name):
    tool_path = f"/home/kali/{tool_name}"

    if not os.path.exists(tool_path):
        print(f"Error: The directory for {tool_name} does not exist: {tool_path}")
        return

    files = os.listdir(tool_path)

    script_to_run = None
    for file in files:
        if file.endswith(".py"):
            script_to_run = file
            break
        elif file.endswith(".sh"):
            script_to_run = file
            break

    if script_to_run:
        script_path = os.path.join(tool_path, script_to_run)

        if script_to_run.endswith(".py"):
            print(f"Launching Python tool {script_to_run} from {script_path}...")
            subprocess.run(["python3", script_path])
        elif script_to_run.endswith(".sh"):
            print(f"Launching Bash tool {script_to_run} from {script_path}...")
            subprocess.run(["bash", script_path])
    else:
        print(f"No executable Python or Bash script found in {tool_path}.")
        

tools_dict = {
    "OSINT Tools": {
        "Full-OSINT Ways": "https://github.com/airborne-commando/OPSEC-OSINT-Tools",
        "theHarvester": "https://github.com/laramies/theHarvester.git",
        "Sploitego": "https://github.com/allfro/sploitego",
        "Recon-ng": "https://github.com/lanmaster53/recon-ng.git",
        "FOCA": "https://github.com/ElevenPaths/FOCA",
        "Amass": "https://github.com/OWASP/Amass.git",
        "TS-OSINT": "https://github.com/trsi-sa/TS-OSINT",
        "Cr3dOv3r": "https://github.com/D4Vinci/Cr3dOv3r"
    },
    "Network Tools": {
        "Nmap": "https://github.com/nmap/nmap.git",
        "Netcat": "https://github.com/diegocr/netcat.git",
        "Wireshark": "https://github.com/wireshark/wireshark.git",
        "Aircrack-ng": "https://github.com/aircrack-ng/aircrack-ng.git",
        "Sublist3r": "https://github.com/aboul3la/Sublist3r",
        "SubnetWizard": "https://github.com/naemazam/SubnetWizard",
        "NetworkManager": "https://github.com/BornToBeRoot/NETworkManager"
    },
    "Web Hacking Tools": {
        "BadMod": "https://github.com/M4DM0e/BadMod",
        "SQLMap": "https://github.com/sqlmapproject/sqlmap.git",
        "XSStrike": "https://github.com/s0md3v/XSStrike.git",
        "XSSer": "https://github.com/epsylon/xsser",
        "Pocsuite3": "https://github.com/knownsec/pocsuite3.git",
        "NucleiScanner": "https://github.com/projectdiscovery/nuclei.git",
        "Red-Hawk": "https://github.com/Tuhinshubhra/Red_Hawk.git",
        "AngryOxide": "https://github.com/Ragnt/AngryOxide",
        "Azemux": "https://github.com/ByFragment/Azemux"
    },
    "Social-Media Phishing Tools": {
        "ZPhisher": "https://github.com/htr-tech/zphisher",
        "Black-Eye":"https://github.com/8L4NK/blackeye",
        "ADV-Phishing": "https://github.com/bhikandeshmukh/AdvPhishing",
        "Saintgram": "https://github.com/joe444-pnj/saintgram.git",
        "Hrack": "https://github.com/trsi-sa/Hrack",
        "instaloader": "https://github.com/instaloader/instaloader.git",
        "InstaHack": "https://github.com/mark0909099/instahack",
        "InstaScraper": "https://github.com/andrew/instascraper",
        "InstaBrute": "https://github.com/Ha3MrX/InstaBrute"
    },
    "Dark-Web Tools": {
        "Tor": "https://github.com/torproject/tor.git",
        "TorBot": "https://github.com/DedSecInside/TorBot",
        "TorSearcher": "https://github.com/some-man1/TorSearcher",
        "OnionShare": "https://github.com/onionshare/onionshare.git",
        "Onion-Peeler": "https://github.com/albertoscala/onion-peeler",
        "DP-Search Engine": "https://github.com/NexvisionLab/Darkweb-search-engine",
        "Dark-Science": "https://github.com/darkscience/darkweb",
        "Darkus": "https://github.com/Lucksi/Darkus"
    }
}

def show_categories():
    print(f"{GREEN}Select a category:{RESET}")
    categories = {
        "1": "OSINT Tools",
        "2": "Network Tools",
        "3": "Web Hacking Tools",
        "4": "Social-Media Phishing Tools",
        "5": "Dark-Web Tools",
        "0": "Exit the RR29-V1"
    }

    for key, value in categories.items():
        print(f"{YELLOW}{key} - {value}{RESET}")

    category = input(f"{CYAN}RR29-V1 > {RESET}")

    if category == "1":
        select_tool("OSINT Tools")
    elif category == "2":
        select_tool("Network Tools")
    elif category == "3":
        select_tool("Web Hacking Tools")
    elif category == "4":
        select_tool("Social-Media Phishing Tools")
    elif category == "5":
        select_tool("Dark-Web Tools")
    elif category == "0":
        print(f"{RED}GoodBye! CAN'T WAIT TO SEE YOU AGAIN ;){RESET}")        
        exit()
    else:
        print(f"{RED}Blind? Invalid choice!{RESET}"),
        show_categories()

def select_tool(category):
    print(f"\n{GREEN}{category}:{RESET}\n")
    tools = tools_dict[category]
    for idx, tool in enumerate(tools, start=1):
        print(f"{YELLOW}{idx} - {tool}{RESET}")
    print(f"{RED}0 - Return to Categories{RESET}\n")

    tool_choice = input(f"{CYAN}RR29-V1 > {RESET}")
    if tool_choice.isdigit() and 1 <= int(tool_choice) <= len(tools):
        tool_name = list(tools.keys())[int(tool_choice) - 1]
        clone_tool(tool_name, tools[tool_name])
    elif tool_choice == "0":
        show_categories()  
    else:
        print(f"{GREEN}Blind? Invalid choice!{RESET}")
        select_tool(category)

if __name__ == "__main__":
    clear_screen()
    display_logo()
    show_categories()
