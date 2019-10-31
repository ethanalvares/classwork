import random
import arcade

PLAYER_SCALING = 0.5
PUMPKIN_SCALING = 0.2
PUMPKIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Spooky Collection"


class MyGame(arcade.Window):

    def __init__(self):


        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

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

            pumpkin.center_x = random.randrange(SCREEN_WIDTH)
            pumpkin.center_y = random.randrange(SCREEN_HEIGHT)

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
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, 'images/skeleton')




def setup():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    setup()
