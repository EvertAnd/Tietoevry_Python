# 1. Song class
# define a class Song
# The class constructor needs to have three additional 3 parameters (self and 3 more!)
# title defaults to empty string
# author defaults to empty string
# lyrics by default empty tuple
# inside constructor method:
# set/store these three parameters inside objects variables of the same name (remember to use self!)
#  print on the screen "New Song made" - (try also printing here author and title!)
# Minimum:
# Write a method sing that prints the song line by line on the screen, first printing the author and title, if any.
# Write a method yell that prints the song in capital letters line by line on the screen, first printing the author and title, if any.
# Bonus: make the above sing and chain methods chainable, so we can call them several times (chained)
# Bonus: create an additional parameter max_lines that prints only a certain number of lines for both sing and yell.
# Better do with some default value e.g. -1, at which all rows are then printed.
# Create multiple songs with lyrics
# Example:
# ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
# ziemelmeita.sing(1).yell()
# Outputs:
# Ziemeļmeita - Jumprava
# Gāju meklēt ziemeļmeitu
# Ziemeļmeita - Jumprava
# GĀJU MEKLĒT ZIEMEĻMEITU
# GARU, TĀLU CEĻU VEICU
# 1a
class Song:
    def __init__(self, title, author, lyrics=tuple()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f" Song: {title} by {author}- Lyrics:{lyrics}")

    def sing(self):
        self: max_lines = max_lines
        print(f" Singing {self.title} - {self.author}")
        self._print_lyrics(self.lyrics, max_lines)
        return self

    def yell(self):
        cap_lyrics = [line.upper() for line in self.lyrics]
        print(f"YELL{self.title} - {self.title}")
        self._print_lyrics(cap_lyrics.lyrics, max_lines)
        return self


ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
print(ziemelmeita.title)
print(ziemelmeita.lyrics)

# ziemelmeita.sing().yell()
ziemelmeita.yell()

# 2a
class Song1:
    def _print_lyrics(self, lyrics, max_lines=-1):
        if max_lines == -1:
            max_lines = len(lyrics)
        for i in lyrics[:max_lines]:
            print(i)
            return self

    def sing(self, max_lines=-1):
       # self: max_lines = max_lines
        print(f"Singing {self.title} - {self.title}")
        self._print_lyrics(sing.lyrics, max_lines)
        return self

    def yell(self, max_lines: object = -1) -> object:
        cap_lyrics = [line.upper() for line in self.lyrics]
        print(f"YELL: {self.title} - {self.title}")
        self._print_lyrics(cap_lyrics.lyrics, max_lines)
        return self
#
#
#
#
# vairogi = Song1("Vairogi", "Līvi", ["Mūsu dziesmas ir vairogi seni", "Mēs tās par pagalvjiem liksim",
#                                    "Daudzu likteņu pilni mēs elposim", "Kā pakalni Daugavas krastos"])
#
# vairogi.sing(2).yell(1)
#
# vairogi.sing().sing().sing()


# 2. Rap class
# For those feeling comfortable with class syntax, create a Rap class that inherits from Song
# # no new constructor method is necessary (you can if you want)
#  add a new method break_it with two default parameters max_lines=-1 and drop equal to "yeah", which is similar to sing, but adds a drop after each word .
# Example:
# zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","
# Garu, tālu ceļu veicu"])
# zrap.break_it(1, "yah")
# Ziemeļmeita - Jumprava
# Gāju YAH meklēt YAH ziemeļmeitu YAH
