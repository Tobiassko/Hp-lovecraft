import autoit
import pyautogui
import time
import subprocess
import sys

# Add Swedish character mapping
SWEDISH_CHARS = {
    'å': '{ASC 0229}',
    'ä': '{ASC 0228}',
    'ö': '{ASC 0246}',
    'Å': '{ASC 0197}',
    'Ä': '{ASC 0196}',
    'Ö': '{ASC 0214}'
}

def check_autoit():
    """Verify AutoIt is working properly"""
    try:
        pos = autoit.mouse_get_pos()
        return True
    except Exception as e:
        print(f"AutoIt initialization failed: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

def type_text(text, interval=0.04):
    """Type text with specified interval between keystrokes"""
    for char in text:
        if char in SWEDISH_CHARS:
            autoit.send(SWEDISH_CHARS[char])
        elif char == '\n':
            autoit.send("{ENTER}")
        elif char in '!@#$%^&*()_+{}|:"<>?':
            autoit.send('{' + char + '}')
        else:
            autoit.send(char)
        time.sleep(interval)

def open_window(program_path):
    """Open a program or window using the specified path"""
    try:
        subprocess.Popen(program_path)
        time.sleep(1)  # Wait for window to open
        return True
    except Exception as e:
        print(f"Error opening window: {e}")
        return False
def open_notepad():
    """Open Windows Notepad"""
    notepad_path = "notepad.exe"
    return open_window(notepad_path)

def move_notepad(x, y):
    """Move the Notepad window to specified coordinates"""
    title = "Untitled - Notepad"
    window = pyautogui.getWindowsWithTitle(title)
    if window:
        window[0].moveTo(x, y)
    else:
        print("Notepad window not found")

def scale_notepad(width, height):
    """Resize the Notepad window to specified dimensions"""
    title = "Untitled - Notepad"
    window = pyautogui.getWindowsWithTitle(title)
    if window:
        window[0].resizeTo(width, height)
    else:
        print("Notepad window not found")

def click_position(x, y):
    """Click at specified coordinates"""
    autoit.mouse_click("left", x, y)

def get_mouse_position():
    """Get current mouse position"""
    return autoit.mouse_get_pos()

def delete_text():
    """Delete text using Ctrl+A and Delete"""
    autoit.send("^a")  # Select all text
    autoit.send("{DELETE}")  # Delete selected text

def copy_text():
    """Copy text using Ctrl+C"""
    autoit.send("^a")  # Select all text
    autoit.send("^c")  # Copy selected text
    backspace_text()  # Clear selection

def show_warning(warning, title, button):
    """Display a Windows warning message"""
    autoit.message_box(warning, title)

def backspace_text(amount=1):
    autoit.send("{BACKSPACE " + str(amount) + "}")

def present_slide(content, title="H.P. Lovecraft Presentation"): 
    """Display a slide with content and wait for user interaction"""
    delete_text()  # Clear previous content
    type_text(content)
    pyautogui.alert("", title)

# Main presentation execution
if __name__ == "__main__":
    check_autoit()
    open_notepad()
    copy_text()
    time.sleep(0.5)
    move_notepad(100, 100)
    scale_notepad(800, 800)
    
    
    
    
    
    




    
    # Title Slide
    present_slide("""H.P. LOVECRAFT: EN LITTERÄR LEGEND
================================
En berättelse om skräckmästaren som förändrade horror-genren.""")

    # Introduction and Early Life
    present_slide("""BARNDOM OCH UPPVÄXT
==================
Howard Phillips Lovecraft föddes den 20 augusti 1890 i Providence, 
Rhode Island. Hans tidiga år präglades av tragedi. När Lovecraft var 
tre år gammal drabbades hans far av en psykisk sjukdom och togs in 
på mentalsjukhus, där han senare dog 1898.

Efter faderns bortgång växte Lovecraft upp i sin morfars stora 
hus, omgiven av böcker och uppmuntrad att utforska 
litteraturen. Hans mor, Sarah, och hans två mostrar tog hand 
om honom, men familjens välstånd skulle snart förändras.""")

    # Youth and Development
    present_slide("""UNGDOM OCH UTVECKLING
===================
Som ung visade Lovecraft en enastående intellektuell förmåga. 
Redan vid sex års ålder skrev han sina första berättelser, 
starkt påverkad av de klassiska sagor och myter han fann i 
morfaderns bibliotek.
""")

    # Career and Writing
    present_slide("""FÖRFATTARSKAP OCH KARRIÄR
=======================
Trots sin begränsade formella utbildning utvecklade Lovecraft 
en unik litterär stil. Hans genombrott kom 1923 med publiceringen 
i tidskriften Weird Tales. Samma år träffade han Sonia Greene, 
som han senare gifte sig med och flyttade till New York med.

Tiden i New York blev dock svår för Lovecraft. Storstadslivet 
och äktenskapet tärde på honom, och 1926 återvände han till sitt 
älskade Providence. Där började hans mest produktiva period som 
författare.""")

    # Major Works
    present_slide("""MÄSTERVERK OCH MYTOLOGI
=====================
Under sent 1920-tal skrev Lovecraft sina mest inflytelserika verk. 
"The Call of Cthulhu" (1926) introducerade den berömda Cthulhu-
mytologin - ett omfattande fiktivt universum befolkat av uråldriga, 
kosmiska varelser bortom mänsklig förståelse.

"The Colour Out of Space" (1927) blandade skräck med science fiction 
på ett sätt som ingen gjort förut. I "The Shadow over Innsmouth" (1931) 
och "At the Mountains of Madness" (1931) utvecklade han sina teman om 
människans litenhet i ett vast och likgiltigt universum.""")

    # Philosophy and Themes
    present_slide("""VÄRLDSSYN OCH TEMATIK
===================
Lovecrafts berättelser återspeglar en djup filosofisk pessimism. 
Hans verk kretsar kring tanken att människan är betydelselös i 
universums stora sammanhang. Denna "kosmiska skräck" skiljer sig 
från traditionella spökhistorier genom sitt fokus på existentiell 
ångest snarare än fysisk fara.

I Lovecrafts värld är kunskap ofta en förbannelse. Ju mer hans 
karaktärer upptäcker om universums sanna natur, desto närmare 
kommer de vansinnet. Detta tema återspeglar hans egen konflikt 
mellan vetenskaplig rationalism och fascination för det okända.

En av de mest intressanta aspekterna i Lovecrafts verk, enligt mig, 
är hur han ofta beskriver det ofattbara och ineffabla. Många av hans 
monster och händelser går inte att helt förstå eller beskriva med 
mänskliga ord, vilket skapar en känsla av mystik och skräck som går 
djupare än det vi kan se eller förklara.""")

    # Legacy and Influence
    present_slide("""INFLYTANDE OCH ARV
==================
Lovecraft dog i fattigdom 1937, endast 46 år gammal. Under sin 
livstid var han relativt okänd utanför en liten krets av beundrare. 
Men hans inflytande växte stadigt efter hans död.

Idag ses Lovecraft som en av de mest inflytelserika författarna 
inom fantastik och skräck. Hans verk har inspirerat otaliga 
författare, från Stephen King till Neil Gaiman, och hans 
inflytande sträcker sig långt utanför litteraturen till film, 
spel, musik och konst.""")

    # Final Thoughts
    present_slide('''EFTERMÄLE
=========
Lovecrafts största bedrift var kanske att han förändrade 
skräckgenren i grunden. Han flyttade fokus från gotiska spöken 
och monster till något mycket större och mer skrämmande: 
insikten om vår egen obetydlighet i ett oändligt universum.

"Den äldsta och starkaste känslan hos människan är rädsla,
och den djupaste rädslan är rädslan för det okända."

- H.P. Lovecraft (1890-1937)

Gjord av: Tobias Olofsson

"troligtvis en av de bästa presentationerna någonsin"
-Chatgpt


Om det fans något i notepad innan så kan du få tillbaka det genom att trycka på ctrl-a och ctrl+v''')