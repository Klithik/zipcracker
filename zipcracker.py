import zipfile
import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: python3 zipcracker.py <ruta_zip> <ruta_txt>")
        return
    
    archivo_zip = zipfile.ZipFile(sys.argv[1])
    passfile = sys.argv[2]
    
    with open(passfile,"rb") as file:
        for line in file:
            line = line.strip()
            try:
                archivo_zip.extractall(pwd=line)
                print("================EXITO================")
                print("Pass: ",line)
                break
            except:
                continue

if __name__ == "__main__":
    main()
