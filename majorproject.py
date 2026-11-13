#IN ORDER FOR THIS CODE TO WORK MAKE SURE YOU HAVE A FILE CALLED "data.json" and "match.json"
import flet as ft
import json


class person:
    def __init__(self, n, a, g, q, p):
        self.name = n
        self.age = a
        self.gender = g
        self.preference = p
        self.questionnaire = q




quiz = False
loggedinuser = ""
current = person("", "", "", [], "")


#this literally just takes your name and makes it into initals
def gi(name):
    if not name:
        return "?"
    pieces = name.split()
    if len(pieces) == 1: #if split comes back with only one piece, (which means 1 name), itll just give it that one
        return pieces[0][0].upper()
    return (pieces[0][0] + pieces[-1][0]).upper() #else, it'll give you the first letter of the first name and the first letter of the last name
#used for pfp's
def answery(answer):
    values = {
        "Strongly Disagree": -2,
        "Disagree": -1,
        "Neutral": 0,
        "Agree": 1,
        "Strongly Agree": 2,
    }
    if answer in values:
        return values[answer]
    return 0
#this basically gets your answers and converts them to numbers




def loaddata():
    default = {"users": [], "loggedinuser": "", "quiz": False}


    try:
        with open("match.json", "r") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass


    return default #it just tries to get data, if theres nothing or its broken, itll just return a default value




def savedata():
    global loggedinuser, quiz, current


    data = loaddata()
    users = data["users"]


    if current is not None:
        preference = current.preference
        questionnaire = current.questionnaire


        if isinstance(preference, list):
            preference = preference[0] if preference else ""
        if not isinstance(questionnaire, list):
            questionnaire = [questionnaire]


        pData = {
            "name": current.name,
            "age": current.age,
            "gender": current.gender,
            "preference": preference,
            "questionnaire": questionnaire,
        }


        found = False
        for index in range(len(users)):
            if users[index]["username"] == loggedinuser:
                users[index] = {"username": loggedinuser, "quiz": quiz, "person": pData}
                found = True
                break


        if not found:
            users.append({"username": loggedinuser, "quiz": quiz, "person": pData})
            #adding a new user if the user isn't saved yet, this is for first time users
       


    data["users"] = users
    data["loggedinuser"] = loggedinuser
    data["quiz"] = quiz


    with open("match.json", "w") as f:
        json.dump(data, f, indent=4)




mdata = loaddata()
quiz = bool(mdata["quiz"])
loggedinuser = str(mdata["loggedinuser"])
prof = {}
for user in mdata["users"]:
    if user["username"] == loggedinuser:
        prof = user["person"]
        break


if prof == {}:
    current = person("", "", "", [], "")
else:
    current = person(prof["name"], prof["age"], prof["gender"], prof["questionnaire"], prof["preference"])
    #either loads the data or creates a new person object




def main(page: ft.Page):
    page.title = "Kelebogile"
    page.window.width = 400
    page.window.height = 600
    page.window.resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    def pref():
        page.controls.clear()
        page.floating_action_button = None
        page.scroll = ft.ScrollMode.AUTO


        title = ft.SafeArea(
            content=ft.Text(
                spans=[
                    ft.TextSpan(
                        text="Welcome to Kelebogile!",
                        style=ft.TextStyle(size=25, weight=ft.FontWeight.BOLD),
                    )
                ]
            )
        )


        def submitdef(e):
            global current, quiz
            num = [
                answery(quiz3.value),
                answery(quiz4.value),
                answery(quiz5.value),
                answery(quiz6.value),
                answery(quiz7.value),
                answery(quiz8.value),
                answery(quiz9.value),
                answery(quiz10.value),
                answery(quiz11.value),
                answery(quiz12.value),
            ]
            current = person(name.value, age.value, quiz1.value, num, quiz2.value)
            quiz = True
            savedata()
            mainer()


        submit = ft.Button(content="Submit", on_click=submitdef)
        subtext = ft.Text(spans=[ft.TextSpan(text="In order to use Kelebogile, you'll have to answer a couple of questions.")])
        name = ft.TextField(label="Name", hint_text="Please enter your REAL name (First, Last).")
        age = ft.TextField(label="Age", hint_text="Please enter your REAL age.")
        quiz1 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Male", label="Male"),
                ft.Radio(value="Female", label="Female"),
                ft.Radio(value="Non-Binary", label="Non-Binary"),
                ft.Radio(value="Other", label="Other"),
            ])
        )
        quiz2 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Male", label="Male"),
                ft.Radio(value="Female", label="Female"),
                ft.Radio(value="Non-Binary", label="Non-Binary"),
                ft.Radio(value="Other", label="Other"),
                ft.Radio(value="All", label="All"),
            ])
        )
        quiz3 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Strongly Agree", label="Strongly Agree"),
                ft.Radio(value="Agree", label="Agree"),
                ft.Radio(value="Neutral", label="Neutral"),
                ft.Radio(value="Disagree", label="Disagree"),
                ft.Radio(value="Strongly Disagree", label="Strongly Disagree"),
            ])
        )
        quiz4 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Strongly Agree", label="Strongly Agree"),
                ft.Radio(value="Agree", label="Agree"),
                ft.Radio(value="Neutral", label="Neutral"),
                ft.Radio(value="Disagree", label="Disagree"),
                ft.Radio(value="Strongly Disagree", label="Strongly Disagree"),
            ])
        )
        quiz5 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Strongly Agree", label="Strongly Agree"),
                ft.Radio(value="Agree", label="Agree"),
                ft.Radio(value="Neutral", label="Neutral"),
                ft.Radio(value="Disagree", label="Disagree"),
                ft.Radio(value="Strongly Disagree", label="Strongly Disagree"),
            ])
        )
        quiz6 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Strongly Agree", label="Strongly Agree"),
                ft.Radio(value="Agree", label="Agree"),
                ft.Radio(value="Neutral", label="Neutral"),
                ft.Radio(value="Disagree", label="Disagree"),
                ft.Radio(value="Strongly Disagree", label="Strongly Disagree"),
            ])
        )
        quiz7 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Strongly Agree", label="Strongly Agree"),
                ft.Radio(value="Agree", label="Agree"),
                ft.Radio(value="Neutral", label="Neutral"),
                ft.Radio(value="Disagree", label="Disagree"),
                ft.Radio(value="Strongly Disagree", label="Strongly Disagree"),
            ])
        )
        quiz8 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Strongly Agree", label="Strongly Agree"),
                ft.Radio(value="Agree", label="Agree"),
                ft.Radio(value="Neutral", label="Neutral"),
                ft.Radio(value="Disagree", label="Disagree"),
                ft.Radio(value="Strongly Disagree", label="Strongly Disagree"),
            ])
        )
        quiz9 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Strongly Agree", label="Strongly Agree"),
                ft.Radio(value="Agree", label="Agree"),
                ft.Radio(value="Neutral", label="Neutral"),
                ft.Radio(value="Disagree", label="Disagree"),
                ft.Radio(value="Strongly Disagree", label="Strongly Disagree"),
            ])
        )
        quiz10 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Strongly Agree", label="Strongly Agree"),
                ft.Radio(value="Agree", label="Agree"),
                ft.Radio(value="Neutral", label="Neutral"),
                ft.Radio(value="Disagree", label="Disagree"),
                ft.Radio(value="Strongly Disagree", label="Strongly Disagree"),
            ])
        )
        quiz11 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Strongly Agree", label="Strongly Agree"),
                ft.Radio(value="Agree", label="Agree"),
                ft.Radio(value="Neutral", label="Neutral"),
                ft.Radio(value="Disagree", label="Disagree"),
                ft.Radio(value="Strongly Disagree", label="Strongly Disagree"),
            ])
        )
        quiz12 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Strongly Agree", label="Strongly Agree"),
                ft.Radio(value="Agree", label="Agree"),
                ft.Radio(value="Neutral", label="Neutral"),
                ft.Radio(value="Disagree", label="Disagree"),
                ft.Radio(value="Strongly Disagree", label="Strongly Disagree"),
            ])
        )


        qtext = [
            "I feel energized after hanging out with a large group of people.",
            "I am deeply affected by other peoples emotions and misfortunes.",
            "I worry frequently about things that might go wrong.",
            "I spend a lot of time daydreaming or exploring abstract concepts",
            "I have a deep appreciation for art, music, or literature.",
            "I keep my living and working spaces organized.",
            "I am rarely late for appointments or scheduled meetings.",
            "I find it easy to start conversations with strangers.",
            "I enjoy being the center of attention at social gatherings.",
            "I often second-guess the decisions I have made."
        ]


        page.add(
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    title,
                    subtext,
                    name,
                    age,
                    ft.Text("What gender are you?"),
                    quiz1,
                    ft.Text("What gender would you like to see?"),
                    quiz2,
                ],
            )
        )


        page.add(
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(value=qtext[0]), quiz3,
                    ft.Text(value=qtext[1]), quiz4,
                    ft.Text(value=qtext[2]), quiz5,
                    ft.Text(value=qtext[3]), quiz6,
                    ft.Text(value=qtext[4]), quiz7,
                    ft.Text(value=qtext[5]), quiz8,
                    ft.Text(value=qtext[6]), quiz9,
                    ft.Text(value=qtext[7]), quiz10,
                    ft.Text(value=qtext[8]), quiz11,
                    ft.Text(value=qtext[9]), quiz12,
                ],
            )
        )
        page.add(submit)
        page.update()


    def matches():
        page.controls.clear()
        page.floating_action_button = None
        page.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.PALETTE),
            leading_width=40,
            title=ft.Text("Kelebogile"),
            center_title=False,
            bgcolor=ft.Colors.BLUE_GREY_400,
            actions=[
                ft.IconButton(ft.CircleAvatar(content=ft.Text(gi(loggedinuser or "U")), bgcolor=ft.Colors.PRIMARY, color=ft.Colors.ON_PRIMARY)),
                ft.PopupMenuButton(
                    key="popup",
                    items=[
                        ft.PopupMenuItem(content="Generate Matches", on_click=matches),
                        ft.PopupMenuItem(content="Answer Questions", on_click=pref),
                        ft.PopupMenuItem(content="Main Page", on_click=mainer),
                        ft.PopupMenuItem(content="Quit", on_click=quit),
                    ],
                ),
            ],
        )


        all_data = loaddata()


        currentUser = None
        for user in all_data["users"]:
            if user["username"] == loggedinuser:
                currentUser = user
                break


        if currentUser is None or "person" not in currentUser:
            page.add(ft.Text("No user profile found."))
            page.update()
            return


        currentData = currentUser["person"]
        currentQ = currentData["questionnaire"]
        currentGender = currentData["gender"]
        currentPref = currentData["preference"]


        matchesList = []
        for user in all_data["users"]:
            if user["username"] == loggedinuser or not user["quiz"]:
                continue
            pData = user["person"]
            if not pData:
                continue


            otherGender = pData["gender"]
            otherPref = pData["preference"]


            currentOk = False
            if currentPref == "All":
                currentOk = True
            elif currentPref == "Male":
                currentOk = otherGender == "Male" or otherGender == "All"
            elif currentPref == "Female":
                currentOk = otherGender == "Female" or otherGender == "All"
            elif currentPref == "Non-Binary":
                currentOk = otherGender == "Non-Binary" or otherGender == "All"
            elif currentPref == "Other":
                currentOk = otherGender == "Other" or otherGender == "All"


            otherOk = False
            if otherPref == "All":
                otherOk = True
            elif otherPref == "Male":
                otherOk = currentGender == "Male"
            elif otherPref == "Female":
                otherOk = currentGender == "Female"
            elif otherPref == "Non-Binary":
                otherOk = currentGender == "Non-Binary"
            elif otherPref == "Other":
                otherOk = currentGender == "Other"


            if not currentOk or not otherOk:
                continue


            if currentGender == "Male" and currentPref == "Male":
                currentOk = otherGender == "Male" or otherGender == "All"
            if currentGender == "Female" and currentPref == "Female":
                currentOk = otherGender == "Female" or otherGender == "All"


            if not currentOk or not otherOk:
                continue


            otherQ = pData["questionnaire"]
            score = 0
            for i in range(min(len(currentQ), len(otherQ))):
                score += abs(currentQ[i] - otherQ[i])


            matchesList.append((score, user["username"], pData))


        matchesList.sort(key=lambda x: x[0])


        if not matchesList:
            page.add(ft.Text("No compatible matches yet."))
            page.update()
            return


        cards = []
        for score, username, pData in matchesList[:3]:
            name = pData["name"]
            cards.append(
                ft.Column(
                    controls=[
                        ft.CircleAvatar(content=ft.Text(gi(name)), bgcolor=ft.Colors.PRIMARY, color=ft.Colors.ON_PRIMARY),
                        ft.Text(name),
                        ft.Text(f"Score: {score}"),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )


        page.add(ft.Column(controls=cards, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER))
        page.update()


    def mainer():
        page.controls.clear()
        page.floating_action_button = None
        page.appbar = ft.AppBar(  # ts creates a little bar at the top
            leading=ft.Icon(ft.Icons.PALETTE),  # this is just making a palette at the far left i didnt mean to keep this but it grew on me
            leading_width=40,
            title=ft.Text("Kelebogile"),
            center_title=False,
            bgcolor=ft.Colors.BLUE_GREY_400,
            actions=[
                ft.IconButton(ft.CircleAvatar(content=ft.Text("DT"), bgcolor=ft.Colors.PRIMARY, color=ft.Colors.ON_PRIMARY)),
                ft.PopupMenuButton(
                    key="popup",
                    items=[
                        ft.PopupMenuItem(content="Generate Matches", on_click=matches),
                        ft.PopupMenuItem(content="Answer Questions", on_click=pref),
                        ft.PopupMenuItem(content="Main Page", on_click=mainer),
                        ft.PopupMenuItem(content="Quit", on_click=quit),
                    ],
                ),
            ],
        )
        # safearea is used to make sure nothing interlaps with the window, for example avoiding the status bar
        page.add(ft.SafeArea(content=ft.Column(controls=[ft.Text("Seems pretty empty.. Maybe you should match with some people.", size=12, color=ft.Colors.GREY)])))
        page.update()


    def start():
        page.controls.clear()
        page.floating_action_button = None


        title = ft.SafeArea(
            content=ft.Text(
                spans=[
                    ft.TextSpan(
                        text="Kelebogile",
                        style=ft.TextStyle(
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            foreground=ft.Paint(
                                gradient=ft.PaintLinearGradient(
                                    begin=(0, 25),
                                    end=(150, 25),
                                    colors=[ft.Colors.PINK, ft.Colors.RED],
                                )
                            ),
                        ),
                    )
                ]
            )
        )


        username = ft.TextField(label="Name", hint_text="Please enter your username")
        password = ft.TextField(label="Password", hint_text="Please enter your password.", password=True, can_reveal_password=True)
        message_text = ft.Text(value="", color=ft.Colors.RED)


        def login(e):
            global loggedinuser


            with open("data.json", "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {}


            if username.value in data:
                if data[username.value] == password.value:
                    loggedinuser = username.value
                    savedata()
                    message_text.value = "Login success!"
                    message_text.color = ft.Colors.GREEN
                    mainer()
                else:
                    message_text.value = "Incorrect password."
                    message_text.color = ft.Colors.RED
            else:
                message_text.value = "Username not found."
                message_text.color = ft.Colors.RED


            page.update()


        def register(e):
            if not username.value or not password.value:
                message_text.value = "Username and password cannot be empty!"
                message_text.color = ft.Colors.RED
                page.update()
                return


            data = {}
            with open("data.json", "r") as f:
                try:
                    loaded_data = json.load(f)
                    if isinstance(loaded_data, dict):
                        data = loaded_data
                    else:
                        data = {}
                except (json.JSONDecodeError, FileNotFoundError):
                    data = {}


            data[username.value] = password.value
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
            message_text.value = f"Registered {username.value} successfully!"
            message_text.color = ft.Colors.GREEN
            page.update()


        LB = ft.Button(content="Login", on_click=login)
        RB = ft.Button(content="Register", on_click=register)


        page.add(
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    title,
                    username,
                    password,
                    ft.Row(controls=[LB, RB], alignment=ft.MainAxisAlignment.CENTER),
                    message_text,
                ],
            )
        )
        page.update()


    start()




if __name__ == "__main__":
    ft.run(main)

