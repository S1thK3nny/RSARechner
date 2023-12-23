from gooey import Gooey, GooeyParser, Events
from prime_utils import *
from rsa_utils import *
import os

save_steps = []
dir = os.path.dirname(os.path.abspath(__file__))

@Gooey(auto_start = True,
       use_events = [Events.VALIDATE_FORM],
       show_preview_warning = False,
       program_name = "RSA Rechner",
       image_dir = dir + "\images", #Screw their built in local path, it doesn't work. This, however, does!
       show_success_modal = False,
       show_restart_button = False,
       clear_before_run = True,
       language = "German",
       default_size = (650, 580),
       menu = [{
        'name': 'Info',
        'items': [{
                'type': 'MessageDialog',
                'menuTitle': 'Was ist RSA?',
                'caption': 'Was ist RSA?',
                'message': 'RSA ist ein asymmetrisches Kryptoverfahren, das zum Verschlüsseln und Signieren verwendet wird. Es wurde 1977 von Rivest, Shamir und Adleman entwickelt.'
            }, {
                'type': 'MessageDialog',
                'menuTitle': 'Ver- und Entschlüsselung',
                'caption': 'Ver- und Entschlüsselung',
                'message': "Verschlüsselung:\nWenn man eine Nachricht m mit dem öffentlichen Schlüssel (n, e) verschlüsseln möchte, berechnet man m' = m^e mod n. Hierbei ist m' die verschlüsselte Nachricht. Das bedeutet, man nimmt die Nachricht m, erhebt sie zur Potenz e und nimmt dann den Rest bei Division durch n.\n\nEntschlüsselung:\nWenn man die verschlüsselte Nachricht m' mit dem privaten Schlüssel (n, d) entschlüsseln möchte, berechnet man m = (m')^d mod n. Hierbei ist m die ursprüngliche Nachricht. Das bedeutet, man nimmt die verschlüsselte Nachricht m', erhebt sie zur Potenz d und nimmt dann den Rest bei Division durch n."
            }, {
                'type': 'Link',
                'menuTitle': 'GitHub Repository',
                'url': 'https://github.com/S1thK3nny/RSARechner/'
            }]
        }])
def main():
    parser = GooeyParser(description="Dieses Programm ermöglicht die einfache Berechnung von öffentlichen und privaten\nSchlüsseln für das RSA-Verschlüsselungsverfahren.")
    parser.add_argument("P", action = "store", help = "Geben Sie Ihr gewähltes P ein", type = must_be_prime)
    parser.add_argument("Q", action = "store", help = "Geben Sie Ihr gewähltes Q ein", type = must_be_prime)
    parser.add_argument("E", action = "store", help = "Geben Sie Ihr gewähltes E ein", type = must_be_prime)
    parser.add_argument("--saveTXT", action = "store_true", metavar = "Als Text-Datei speichern", help = "Speichert den Console-Output als RSA_output.txt ab")
    parser.add_argument("--appendTXT", action = "store_true", metavar = "An die Datei anhängen anstatt ersetzen", help = "Schreibt zur Datei anstatt sie zu ersetzen.\nBenötigt 'Als Text-Datei speichern'")

    args = parser.parse_args()

    n, phi = base_calculations(args.P, args.Q, save_steps)
    GCD(phi, args.E, save_steps)
    _, d = print_extended_GCD(args.E, phi, save_steps)
    print_keys(n, args.E, d, save_steps)

    if args.saveTXT:
        file_path = 'RSA_output.txt' # needs to be like this for the exe
        mode = 'a' if args.appendTXT else 'w'
        
        try:
            with open(file_path, mode) as file:
                for step in save_steps:
                    file.write(str(step) + '\n')
                file.write("\n\n")
        except Exception as e:
            raise TypeError("Konnte die Datei nicht speichern!")



if __name__ == '__main__':
    main()