try:
    badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print("tag was not found !")
else :
    if badContent == None :
        print("Tag Was none")
    else :
        print(badContent)
