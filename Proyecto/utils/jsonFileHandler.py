from json import dumps, load

def readFile(fileName):
    try:
        with open(fileName) as f:
            fileData = load(f)
            f.close()
        return fileData    
    except:
        return []
    

def saveFile(fileName, data):
    jsonFile = open(fileName, "w", encoding='utf-8')
    jsonFile.write(dumps(data, indent = 4, ensure_ascii=False)) # Acomoda
    jsonFile.close()

