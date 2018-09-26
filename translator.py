def translator(phrase):
    converted = ""
    for letter in phrase:
        if letter in "dewansh":
            converted = converted + " gandu "
        else:
            converted = converted + letter
       
    return converted


print(translator(input("Enter phrase: ")))