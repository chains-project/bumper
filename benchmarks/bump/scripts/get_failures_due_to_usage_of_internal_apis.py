import os


def main():
    directory = "./repository/reproductionLogs/successfulReproductionLogs"
    found = []

    for filename in os.scandir(directory):
        if filename.is_file():
            key = filename.name.replace(".log", "")
            path = filename.path
            with open(path) as f:
                content = f.read()
                if ".internal" in content:
                    found.append(key)
    
    for key in found:
        print(key)
    

if __name__ == "__main__":
    main()