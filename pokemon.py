#Helena
#Pokemon evolution: bulbasaur --> 16 ivysaur --> 32 venusaur
#evolve()
#train()
#battle()
#info()
#name, level, day
#init
import random
name = "Bulbasaur"
day = 1
level = 1
#functions

def main():
    print("Welcome to Pokemon Evolution, your character is Bulbasaur!")
    seePokemon = input("Would you like to see your Pokemon? (y/n):  ")
    while seePokemon != "y" and seePokemon != "n":
        seePokemon = seePokemon.lower()
        if seePokemon == "y":
            break
        elif seePokemon == "n":
            break
        else:
            seePokemon = input("Could not understand your answer, please enter it again:  ")
    if seePokemon == "y":
            stage1()
    elif seePokemon == "n":
            print("Okay then.")
    menu()
def menu():
    global day
    choice = "blank"
    while choice != "exit":
        print(" ")
        print("It is Day " + str(day) + " for your Pokemon("+ name + ")")
        choice = input("What would you like to do? (train/rest/battle/finalboss/info/exit):  ")
        choice = choice.lower()
        if choice == "train":
            train()
            evolve()
        elif choice == "rest":
             print("ZZzzzz you take a well-deserved nap.")
        elif choice == "info":
             info()
             day = day - 1
        elif choice == "exit":
             break
        elif choice == "battle":
             gymbattle()
        elif choice == "finalboss":
             finalboss()
             break
        else:
             print("Could not understand... but it is the next day now, enter a listed option.")
        day = day + 1
def train():
    global level
    level = level + 1
    print("You lift some weights and get stronger!")
    print("Level up to "+ str(level))
def info():
    if name == "Bulbasaur":
         stage1()
    elif name == "Ivysaur":
         stage2()
    else:
         stage3()
    print("Pokemon: " + name)
    print("Day: " + str(day))
    print("Level: " + str(level))
    print(" ")

def evolve():
    global name
    if level < 10:
         name = "Bulbasaur"
    elif level < 20:
         name = "Ivysaur"
    else:
         name = "Venusaur"

    if level == 10 or level == 20:
         print(" ")
         print("Wow! You evolved! Now your name is "+name)
def gymbattle():
    global level
    value = random.randint(1,10)
    if value >= 7:
        print("You win!")
        level = level + 2
    else:
        print("You lost that battle.")

def finalboss():
    global level
    winchance = level*4
    value = random.randint(1,100)
    if value <= winchance:
        fireworks()
        print("You win!!!")
        print("You defeated the final boss!!!!!")
        print("Congrats!!!")
    else:
        print("You lose :(")
        print("I guess the final boss was just better.")

def stage1():           #bulbasaur
    print((r"                                          /\n"))
    print((r"                       _,.------....___,.' ',.-.\n"))
    print((r"                    ,-'          _,.--\"        |\n"))
    print((r"                  ,'         _.-'              .\n"))
    print((r"                 /   ,     ,'                   `\n"))
    print((r"                .   /     /                     ``.\n"))
    print((r"                |  |     .                       \\.\\\n"))
    print((r"      ____      |___._.  |       __               \\ `.\n"))
    print((r"    .'    `---\"\"       ``\"-.--\"'`  \\               .  \\\n"))
    print((r"   .  ,            __               `              |   .\n"))
    print((r"   `,'         ,-\"'  .               \\             |    L\n"))
    print((r"  ,'          '    _.'                -._          /    |\n"))
    print((r" ,`-.    ,\".   `--'                      >.      ,'     |\n"))
    print((r". .'\\'   `-'       __    ,  ,-.         /  `.__.-      ,'\n"))
    print((r"||:, .           ,'  ;  /  / \\ `        `.    .      .'/\n"))
    print((r"j|:D  \\          `--'  ' ,'_  . .         `.__, \\   , /\n"))
    print(("/ L:_  |                 .  \"' :_;                `.'.'\n"))
    print((".    \"\"'                  \"\"\"\"\"'                    V\n"))
    print((r"`.                                 .    `.   _,..  `\n"))
    print((r"  `,_   .    .                _,-'/    .. `,'   __  `\n"))
    print((r"   ) \\`._        ___....----\"'  ,'   .'  \\ |   '  \\  .\n"))
    print((r"  /   `. \"`-.--\"'         _,' ,'     `---' |    `./  |\n"))
    print((r" .   _  `\"\"'--.._____..--\"   ,             '         |\n"))
    print((r" | .\" `. `-.                /-.           /          ,\n"))
    print((r" | `._.'    `,_            ;  /         ,'          .\n"))
    print((r".'          /| `-.        . ,'         ,           ,\n"))
    print((r"'-.__ __ _,','    '`-..___;-...__   ,.'\\ ____.___.'\n"))
    print((r"`\"^--'..'   '-`-^-'\"--    `-^-'`.''\"\"\"\"\"`.,^.`.--' mh\n"))
    print(("\n"))

def stage2():           #ivysaur
    print((r"                              ,'\"`.,./.\n"))
    print((r"                            ,'        Y',\"..\n"))
    print((r"                          ,'           \\  | \\\n"))
    print((r"                         /              . |  `\n"))
    print((r"                        /               | |   \\\n"))
    print((r"           __          .                | |    .\n"))
    print((r"      _   \\  `. ---.   |                | j    |\n"))
    print((r"     / `-._\\   `Y   \\  |                |.     |\n"))
    print((r"    _`.    ``    \\   \\ |..              '      |,-'\"\"7,....\n"))
    print((r"    l     '-.     . , `|  | , |`. , ,  /,     ,'    '/   ,'_,.-.\n"))
    print((r"    `-..     `-.  : :     |/ `   ' \"\\,' | _  /          '-'    /___\n"))
    print((r"     \\\"\"' __.,.-`.: :        /   /._    l'.,'\n"))
    print((r"      `--,   _.-' `\".           /__ `'-.' '         .\n"))
    print((r"      ,---..._,.--\"\"\"\"\"\"\"--.__..----,-.'   .  /    .'   ,.--\n"))
    print((r"      |                          ,':| /    | /     ;.,-'--      ,.-\n"))
    print((r"      |     .---.              .'  :|'     |/ ,.-='\"-.`\"`' _   -.'\n"))
    print((r"      /    \\    /               `. :|--.  _L,\"---.._        \"----'\n"))
    print((r"    ,' `.   \\ ,'           _,     `''   ``.-'       `-  -..___,'\n"))
    print((r"   . ,.  .   `   __     .-'  _.-           `.     .__    \\\n"))
    print((r"   |. |`        \"  ;   !   ,.  |             `.    `.`'---'\n"))
    print((r"   ,| |C\\       ` /    | ,' |(]|            -. |-..--`\n"))
    print((r"  /  \"'--'       '      /___|__]        `.  `- |`.\n"))
    print((r" .       ,'                   ,   /       .    `. \\\n"))
    print((r"   \\                      .,-'  ,'         .     `-.\n"))
    print((r"    x---..`.  -'  __..--'\"/\"\"\"\"\"  ,-.      |   |   |\n"))
    print((r"   / \\--._'-.,.--'     _`-    _. ' /       |     -.|\n"))
    print((r"  ,   .   `-..__ ...--'  _,.-' | `   ,.-.  ;   /  '|\n"))
    print((r" .  _,'         '\"-----\"\"      |    `   | /  ,'    ;\n"))
    print((r" |-'  .-.    `._               |     `._// ,'     /\n"))
    print((r"_|    `-'   _,' \"`--.._________|        `,'    _ /.\n"))
    print(("//\\   ,-._.'\"/\\__,.   _,\"     /_\\__/`. /'.-.'.-/_,`-' mh\n"))
    print(("`-\"`\"' v'    `\"  `-`-\"              `-'`-`  `'\n"))
def stage3():           #venusaur
    print((r"                          _._       _,._\n"))
    print((r"                       _.'   `. ' .'   _`.\n"))
    print((r"               ,\"\"\"/`\"\"-.-.,/. ` V'\\-,`.,--/\"\"\".\"-..\n"))
    print((r"             ,'    `...,' . ,\\-----._|     `.   /   \\\n"))
    print((r"            `.            .`  -'`\"\" .._   :> `-'   `.\n"))
    print((r"           ,'  ,-.  _,.-'| `..___ ,'   |'-..__   .._ L\n"))
    print((r"          .    \\_ -'   `-'     ..      `.-' `.`-.'_ .|\n"))
    print((r"          |   ,',-,--..  ,--../  `.  .-.    , `-.  ``.\n"))
    print((r"          `.,' ,  |   |  `.  /'/,,.\\/  |    \\|   |\n"))
    print((r"               `  `---'    `j   .   \\  .     '   j\n"))
    print((r"             ,__`\"        ,'|`'\\_/`.'\\'        |\\-'-, _,.\n"))
    print((r"      .--...`-. `-`. /    '- ..      _,    /\\ ,' .--\"'  ,'\".\n"))
    print((r"    _'-\"\"-    --  _`'-.../ __ '.'`-^,_`-\"\"\"\"---....__  ' _,-`\n"))
    print((r"  _.----`  _..--.'        |  \"`-..-\" __|'\"'         .\"\"-. \"\"'--.._\n"))
    print((r" /        '    /     ,  _.+-.'  ||._'   \"\"\"\". .          `     .__\\\n"))
    print((r"`---    /        /  / j'       _/|..`  -. `-`\\ \\   \\  \\   `.  \\ `-..\n"))
    print((",\" _.-' /    /` ./  /`_|_,-\"   ','|       `. | -'`._,   L  \\ .  `.   |\n"))
    print(("`\"' /  /  / ,__...-----| _.,  ,'            `|----.._`-.|' |. .` ..  .\n"))
    print((r"  /  '| /.,/   \\--.._ `-,' ,          .  '`.'  __,., '  ''``._ \\ \\`,'\n"))
    print((r" /_,'---  ,     \\`._,-` \\ //  / . \\    `._,  -`,  / / _   |   `-L -\n"))
    print((r"  /       `.     ,  ..._ ' `_/ '| |\\ `._'       '-.'   `.,'     |\n"))
    print((r" '         /    /  ..   `.  `./ | ; `.'    ,\"\" ,.  `.    \\      |\n"))
    print((r"  `.     ,'   ,'   | |\\  |       \"        |  ,'\\ |   \\    `    ,L\n"))
    print((r"  /|`.  /    '     | `-| '                  /`-' |    L    `._/  \\\n"))
    print((r" / | .`|    |  .   `._.'                   `.__,'   .  |     |  (`\n"))
    print((r"'-\"\"-'_|    `. `.__,._____     .    _,        ____ ,-  j     \".-'\"'\n"))
    print((r"       \\      `-.  \\/.    `\"--.._    _,.---'\"\"\\/  \"_,.'     /-'\n"))
    print((r"        )        `-._ '-.        `--\"      _.-'.-\"\"        `.\n"))
    print((r"       ./            `,. `\".._________...\"\"_.-\"`.          _j\n"))
    print((r"      /_\\.__,\"\".   ,.'  \"`-...________.---\"     .\".   ,.  / \\\n"))
    print((r"             \\_/\"\"\"-'                           `-'--(_,`\"`-` mh\n"))
def fireworks():
    print((r"                        *    *                             "))
    print((r"    *         '       *       .  *   '     .           * *"))
    print((r"                                                                '"))
    print((r"        *                *'          *          *        '"))
    print((r"    .           *               |               /"))
    print((r"                '.         |    |      '       |   '     *"))
    print((r"                    \*        \   \             /"))
    print((r"        '          \     '* |    |  *        |*                *  *"))
    print((r"                *      `.       \   |     *     /    *      '"))
    print((r"    .                  \      |   \          /               *"))
    print((r"        *'  *     '      \      \   '.       |"))
    print((r"            -._            `                  /         *"))
    print((r"    ' '      ``._   *                           '          .      '"))
    print((r"    *           *\*          * .   .      *"))
    print((r"    *  '        *    `-._                       .         _..:='        *"))
    print((r"                .  '      *       *    *   .       _.:--'"))
    print((r"            *           .     .     *         .-'         *"))
    print((r"   .               '             . '   *           *         ."))
    print((r"    *       ___.-=--..-._     *                '               '"))
    print((r"                                    *       *"))
    print((r"                    *        _.'  .'       `.        '  *             *"))
    print((r"        *              *_.-'   .'            `.               *"))
    print((r"                    .'                       `._             *  '"))
    print((r"    '       '                        .       .  `.     ."))
    print((r"        .                      *                  `"))
    print((r"                *        '             '                          ."))
    print((r"        .                          *        .           *  *"))
    print((r"                *        .                                    '"))
#main
main()
