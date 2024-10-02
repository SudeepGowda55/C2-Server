import pyfiglet, random, string
from .colors import ORANGE, ELECTRIC_BLUE, RESET

def startup_banner():
    banner = pyfiglet.figlet_format("C2 Server", font="slant")
    server_hash = ''.join(random.choices(string.hexdigits.lower(), k=40))
    
    print(f"{ELECTRIC_BLUE}Connecting to localhost:3000 ...\n")
    print(f"{ORANGE}{banner}")

    print(f"""{RESET}
If you can't hack humans, hack the machines. Humans are always the weakest link.

[*] Server v1.1 - {server_hash}
[*] Welcome to the custom C2 shell, please type 'help' for options
[*] Check for updates with the 'update' command
    """)