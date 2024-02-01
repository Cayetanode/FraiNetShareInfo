import win32net, argparse, colorama
from colorama import Fore, Style

description=""

parser=argparse.ArgumentParser(description='SMB logical path on Linux. - By Fraile 2024.', epilog=description)
parser.add_argument("-ip", dest="IpServer", help="Introduzca Ip Servidor SMB: 192.168.168.80", required=True)


params=parser.parse_args()
IpServer=params.IpServer



colorama.init(autoreset=True)

print ('',end="\n\n")
print ('*********************************************')
print (f"{Fore.GREEN}SMB logical path on Linux. - By Fraile 2024{Style.RESET_ALL}")
print ('*********************************************',end="\n\n")

# Definir el nombre del servidor y del recurso compartido (reemplazar con los valores reales)


try:
    # Obtener información sobre los recursos compartidos
    shares = win32net.NetShareEnum(IpServer, 2)

    # Imprimir la información de los recursos compartidos
    for share_info in shares[0]:
        share_name = share_info['netname']
        share_type = share_info['remark']
        share_path=share_info["path"]

        print(f"{Fore.GREEN}Recurso:{Style.RESET_ALL}", share_name)
        print(f"{Fore.GREEN}Tipo:{Style.RESET_ALL}",share_type)
        print(f"{Fore.GREEN}Ruta Logica:{Style.RESET_ALL}",share_path,end="\n\n")

except Exception as e:
        print(f"Error al enumerar los recursos compartidos: {e}")

