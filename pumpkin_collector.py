
import random
import arcade

PLAYER_SCALING = 0.5
PUMPKIN_SCALING = 0.2
PUMPKIN_COUNT = 50

WIDTH = 800
HEIGHT = 600
TITLE = "Spooky Collection"

current_screen = "menu"


def on_draw():
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "play":
        draw_play()


def on_key_press(key, modifiers):
    global current_screen

    if current_screen == "menu":
        menu_keybinds(key, modifiers)
    elif current_screen == "instructions":
        instructions_keybinds(key, modifiers)
    elif current_screen == "play":
        play_keybinds(key, modifiers)


def menu_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.I:
        current_screen = "instructions"
    elif key == arcade.key.P:
        current_screen = "play"
    elif key == arcade.key.ESCAPE:
        exit()


def instructions_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ESCAPE:
        current_screen = "menu"


def play_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ESCAPE:
        current_screen = "menu"

def draw_menu():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("Main Menu", WIDTH/2, HEIGHT/2,
                     arcade.color.SKY_BLUE, font_size=30, anchor_x="center")
    arcade.draw_text("I for Instructions", WIDTH/2, HEIGHT/2-60,
                     arcade.color.SKY_BLUE, font_size=20, anchor_x="center")
    arcade.draw_text("P to Play", WIDTH/2, HEIGHT/2-90,
                     arcade.color.SKY_BLUE, font_size=20, anchor_x="center")


def draw_instructions():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("Instructions", WIDTH/2, HEIGHT/2,
                     arcade.color.SKY_BLUE, font_size=30, anchor_x="center")
    arcade.draw_text("Use the mouse to move", WIDTH/2, HEIGHT/2-60,
                     arcade.color.SKY_BLUE, font_size=20, anchor_x="center")



def draw_play():
    def __init__(self):


        super().__init__(WIDTH, HEIGHT, TITLE)

        self.set_mouse_visible(False)

        self.player_list = None
        self.pumpkin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

    def lists(self):

        self.player_list = arcade.SpriteList()
        self.pumpkin_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("images/character.png", PLAYER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.score = 0

        for i in range(PUMPKIN_COUNT):


            pumpkin = arcade.Sprite("images/pumpkin", PUMPKIN_SCALING)

            pumpkin.center_x = random.randrange(WIDTH)
            pumpkin.center_y = random.randrange(HEIGHT)

            self.pumpkin_list.append(pumpkin)

    def on_draw(self):
        arcade.start_render()
        self.pumpkin_list.draw()
        self.player_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y



    def on_update(self, delta_time):
        global draw_scare()

        self.pumpkin_list.update()
        pumpkin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.pumpkin_list)

        for pumpkin in pumpkin_hit_list:
            pumpkin.remove_from_sprite_lists()
            self.score += 1

        if self.score == 100:
            draw_scare()

    def draw_scare(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, 'images/skeleton')




def setup():
    arcade.open_window(WIDTH, HEIGHT, "BLACK")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    arcade.run()

if __name__ == '__main__':
    setup()
