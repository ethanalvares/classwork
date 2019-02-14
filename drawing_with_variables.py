import arcade


WIDTH = 1360
HEIGHT = 720

#measure by pixels. Right, left, size
right = 50
left = 50
size = 30

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(right, left, size, arcade.color.BLUE_GREEN)
arcade.draw_rectangle_filled(190, 190, 190, 190, arcade.color.AIR_FORCE_BLUE)

# End drawing
arcade.finish_render()
arcade.run()