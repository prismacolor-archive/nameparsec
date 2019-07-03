# test data
names = [
    "Picard, Jean-Luc",
    "Yar, Tasha",
    "LaForge, Geordi",
    "Kirk III, James T.",
    "Kenobi, Obi-wan",
    "Wayne, Bruce",
    "Prince, Diana",
    "Queen-Monster, Mothra",
    "Kaiju Sr, Godzilla",
    "Kaiju Jr, Godzilla",
    "Grey, Gandalf",
    "Gamgee, Samwise (Sam)",
    "Menendez Garcia, Juan Carlos",
    "El Maria, Johnathan Alexander",
    "Di Marcos, Tia J.",
    "El Salvador, Taco",
    "Fancy-Woman, Grace",
    "Gonzalaz Rojo, Marcos",
    "Gonzales-Reyes, James",
    "Di Antwerp III, David",
    "Di Money, Count",
    "McRich, Richey",
    "Mac Allister, Stacy",
    "Ping, Liu-Chen",
    "Mala Wag, Something",
    "O'hara, Scarlett",
    "Day O'Connor JD, Sandra",
    "Appleseed III, John (Johnnie)",
    "Hibbert MD, James",
    "Cuyahoga B.N., Montana",
    "Frog, Michigan J.",
    "Lawyer Esq., Blue-Haired",
    "Van Gogh, Vincent",
    "Von Beethoven, Ludwig",
    "Nelson, Prince Rogers",
    "Jimenez Reyes, Elie Maria",
    "Brown, Mary Ann",
    "Flibberty Gibbet, Dan",
    "Noonien Singh, Khan"
]

# predetermined name parts
suffixes = ["JR", "JR,", "JR.", "JR.,", "II", "III", "IV", "V", "VI", "SR", "SR.", "SR,", "SR.,", "DR.", "DR.,", "DR",
            "DR,", "M.D.", "M.D.,", "MD.,", "MD.", "MD", "MD,", "PH.D", "PH.D,", "R.N.", "R.N.,", "RN", "RN,", "B.N.",
            "B.N.,", "BN", "BN,", "JD", "JD,", "ESQ", "ESQ.,", "ESQ.", "ESQ,"]
lastprefix = ["DA", "DI", "DE", "LA", "EL", "LE", "MAC", "MC", "VAN", "VON", "O", "O'"]


# function for parsing the names
def parsenames(list_of_names):
    formattednames = {"LastName": [], "Suffix": [], "FirstName": [], "PreferredName": [], "Middle": []}
    for name in list_of_names:
        basename = name.split()
        # print(basename)

        # standard names
        copyname = name.replace(",", " ")
        copyname = copyname.split()

        if len(copyname) == 2:
            formattednames["LastName"].append(copyname[0])
            formattednames["Suffix"].append(" ")
            formattednames["FirstName"].append(copyname[-1])
            formattednames["PreferredName"].append(" ")
            formattednames["Middle"].append(" ")
        elif len(copyname) == 3:
            if "," in basename[1] and basename[1].upper() not in suffixes:
                    formattednames["LastName"].append(copyname[0] + " " + copyname[1])
                    formattednames["Suffix"].append(" ")
                    formattednames["FirstName"].append(copyname[-1])
                    formattednames["PreferredName"].append(" ")
                    formattednames["Middle"].append(" ")
            elif copyname[0].upper() in lastprefix:
                formattednames["LastName"].append(copyname[0] + " " + copyname[1])
                formattednames["Suffix"].append(" ")
                formattednames["FirstName"].append(copyname[-1])
                formattednames["PreferredName"].append(" ")
                formattednames["Middle"].append(" ")
            elif copyname[1].upper() in suffixes:
                formattednames["LastName"].append(copyname[0])
                formattednames["Suffix"].append(copyname[1])
                formattednames["FirstName"].append(copyname[-1])
                formattednames["PreferredName"].append(" ")
                formattednames["Middle"].append(" ")
            elif "(" in copyname[2] or '"' in copyname[2]:
                formattednames["LastName"].append(copyname[0])
                formattednames["Suffix"].append(" ")
                formattednames["FirstName"].append(copyname[1])
                formattednames["PreferredName"].append(copyname[2])
                formattednames["Middle"].append(" ")
            else:
                formattednames["LastName"].append(copyname[0])
                formattednames["Suffix"].append(" ")
                formattednames["FirstName"].append(copyname[1])
                formattednames["PreferredName"].append(" ")
                formattednames["Middle"].append(copyname[2])
        elif len(copyname) > 3:
            if copyname[0].upper() in lastprefix:
                formattednames["LastName"].append(copyname[0] + " " + copyname[1])
                if copyname[2].upper() in suffixes:
                    formattednames["Suffix"].append(copyname[2])
                    formattednames["FirstName"].append(copyname[3])
                else:
                    formattednames["Suffix"].append(" ")
                    formattednames["FirstName"].append(copyname[2])
                if "(" in copyname[-1] or '"' in copyname[-1]:
                    formattednames["PreferredName"].append(copyname[-1])
                    formattednames["Middle"].append(" ")
                elif "." in copyname[-1]:
                    formattednames["Middle"].append(copyname[-1])
                    formattednames["PreferredName"].append(" ")
                else:
                    formattednames["Middle"].append(" ")
                    formattednames["PreferredName"].append(" ")
            elif copyname[1] in suffixes:
                formattednames["LastName"].append(copyname[0])
                formattednames["Suffix"].append(copyname[1])
                formattednames["FirstName"].append(copyname[2])
                if "(" in copyname[-1] or '"' in copyname[-1]:
                    formattednames["PreferredName"].append(copyname[-1])
                    formattednames["Middle"].append(" ")
                else:
                    formattednames["Middle"].append(copyname[-1])
                    formattednames["PreferredName"].append(" ")
            elif copyname[2] in suffixes:
                formattednames["LastName"].append(copyname[0] + " " + copyname[1])
            elif "(" in copyname[-1] or '"' in copyname[-1]:
                formattednames["LastName"].append(copyname[0] + " " + copyname[1])
                formattednames["Suffix"].append(" ")
                formattednames["FirstName"].append(copyname[2])
                formattednames["PreferredName"].append(copyname[-1])
                formattednames["Middle"].append(" ")
            else:
                formattednames["LastName"].append(copyname[0] + " " + copyname[1])
                formattednames["Suffix"].append(" ")
                formattednames["FirstName"].append(copyname[2])
                formattednames["PreferredName"].append(" ")
                formattednames["Middle"].append(copyname[-1])

    return formattednames



