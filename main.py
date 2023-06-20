import flet as ft
import random
from time import sleep

planets_dict = {
    "Sun": ["Sun", "Mercury", "Saturn", "Mars"],
    "Mercury": ["Mercury", "Mars", "Uranus", "Jupiter"],
    "Venus": ["Venus", "Jupiter", "Earth", "Saturn"],
    "Earth": ["Earth", "Mars", "Jupiter", "Neptune"],
    "Mars": ["Mars", "Neptune", "Earth", "Venus"],
    "Jupiter": ["Jupiter", "Saturn", "Mars", "Sun"],
    "Saturn": ["Saturn", "Mercury", "Venus", "Uranus"],
    "Uranus": ["Uranus", "Neptune", "Sun", "Venus"],
    "Neptune": ["Neptune", "Saturn", "Earth", "Uranus"],
}
planet = ""
points = 0
times = 1


def main(page: ft.Page):
    page.title = "System Solar Game"
    page.window_width = 1024
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#4a1760"
    page.padding = 0

    def check_option(e):
        global planet
        global points
        global times
        
        if planet == e.control.data:
            e.control.bgcolor = "green"
            show_result.content.value = f"Is {planet}"
            show_result.content.color = "green"
            points = points + 1
        else:
            e.control.bgcolor = "red"
            show_result.content.value = f"Is {planet}"
            show_result.content.color = "red"

        e.control.update()
        show_result.update()
        sleep(1)
        e.control.bgcolor = "pink600"
        show_result.content.value = ""

        for i in range(0, 9):
            row_planets.controls[i].color = None
        if times == 10:
            page.dialog = dlg_endgame
            dlg_endgame.title.value = f"Score: {points}/10"
            dlg_endgame.open = True
            page.update()
            return
        times = times + 1
        new_question()

    def new_question():
        global planet
        global planets_dict
        planet = random.choice(
            [
                "Sun",
                "Mercury",
                "Venus",
                "Earth",
                "Mars",
                "Jupiter",
                "Saturn",
                "Uranus",
                "Neptune",
            ]
        )
        
        options_list = planets_dict.get(planet)
        random.shuffle(options_list)
        # I put in gray those who are not the planet
        for i in range(0, 9):
            if not row_planets.controls[i].data == planet:
                row_planets.controls[i].color = "white10"
        page.update()
        # Put the options buttons
        for i in range(0, 4):
            row_buttons.controls[i].content.value = options_list[i]
            row_buttons.controls[i].data = options_list[i]
        page.update()

    def play_game(e):
        page.controls.clear()
        page.dialog = dlg_startgame
        dlg_startgame.open = True
        page.add(title)
        page.add(show_result)
        page.add(row_planets)
        page.add(ft.Container(height=50))
        page.add(row_buttons)
        page.update()
        new_question()

    def new_game(e):
        global points
        global times
        points = 0
        times = 1
        dlg_endgame.open = False
        page.update()
        new_question()

    def close_dlg(e):
        dlg_startgame.open = False
        dlg_startgame.update()

    row_planets = ft.Row(
        width=1024,
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        controls=[
            ft.Image(
                src="assets/Sun.png",
                data="Sun",
                width=180,
                height=180,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Image(
                src="assets/Mercury.png",
                data="Mercury",
                width=30,
                height=30,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Image(
                src="assets/Venus.png",
                data="Venus",
                width=50,
                height=50,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Image(
                src="assets/Earth.png",
                data="Earth",
                width=80,
                height=80,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Image(
                src="assets/Mars.png",
                data="Mars",
                width=50,
                height=50,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Image(
                src="assets/Jupiter.png",
                data="Jupiter",
                width=130,
                height=130,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Image(
                src="assets/Saturn.png",
                data="Saturn",
                width=180,
                height=130,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Image(
                src="assets/Uranus.png",
                data="Uranus",
                width=80,
                height=80,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Image(
                src="assets/Neptune.png",
                data="Neptune",
                width=100,
                height=100,
                fit=ft.ImageFit.CONTAIN,
            ),
        ],
    )

    row_buttons = ft.Row(
        width=1024,
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        controls=[
            ft.Container(
                on_click=check_option,
                data="Mercury",
                width=100,
                height=100,
                border_radius=50,
                border=ft.border.all(3, "white54"),
                bgcolor=ft.colors.PINK_600,
                content=ft.Text("Mercury", size=20, weight=ft.FontWeight.BOLD),
                alignment=ft.alignment.center,
            ),
            ft.Container(
                on_click=check_option,
                data="Jupiter",
                width=100,
                height=100,
                border_radius=50,
                border=ft.border.all(3, "white54"),
                bgcolor=ft.colors.PINK_600,
                content=ft.Text("Jupiter", size=20, weight=ft.FontWeight.BOLD),
                alignment=ft.alignment.center,
            ),
            ft.Container(
                on_click=check_option,
                data="Mars",
                width=100,
                height=100,
                border_radius=50,
                border=ft.border.all(3, "white54"),
                bgcolor=ft.colors.PINK_600,
                content=ft.Text("Mars", size=20, weight=ft.FontWeight.BOLD),
                alignment=ft.alignment.center,
            ),
            ft.Container(
                on_click=check_option,
                data="Earth",
                width=100,
                height=100,
                border_radius=50,
                border=ft.border.all(3, "white54"),
                bgcolor=ft.colors.PINK_600,
                content=ft.Text("Earth", size=20, weight=ft.FontWeight.BOLD),
                alignment=ft.alignment.center,
            ),
        ],
    )

    title = ft.Row(
        width=1024,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                "What planet is?",
                size=30,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
            )
        ],
    )

    show_result = ft.Container(
        height=50,
        width=1024,
        content=ft.Text(value="", size=30, weight=ft.FontWeight.BOLD),
        alignment=ft.alignment.center,
    )

    dlg_startgame = ft.AlertDialog(
        modal=True,
        title=ft.Text(value="How to play", text_align=ft.TextAlign.CENTER),
        content=ft.Image(src="assets/Tutorial.png",width=300,height=200),
        actions=[
            ft.TextButton("Ok", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )
    dlg_endgame = ft.AlertDialog(
        modal=True,
        title=ft.Text(value="", text_align=ft.TextAlign.CENTER),
        actions=[
            ft.TextButton("New Game", on_click=new_game),
            ft.TextButton("Exit", on_click=lambda e: page.window_destroy()),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Load Home
    page.add(
        ft.Container(
            width=1024,
            height=600,
            image_src="assets/background.png",
            image_fit=ft.ImageFit.FILL,
            content=ft.Column(
                [
                    ft.Text("SOLAR", size=60, weight=ft.FontWeight.BOLD),
                    ft.Text("SYSTEM", size=60, weight=ft.FontWeight.BOLD),
                    ft.Container(height=50),
                    ft.Container(
                        on_click=play_game,
                        content=ft.Text("Play", size=30, weight=ft.FontWeight.BOLD),
                        width=150,
                        height=80,
                        bgcolor=ft.colors.PINK,
                        border_radius=20,
                        border=ft.border.all(3, "white54"),
                        alignment=ft.alignment.center,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
