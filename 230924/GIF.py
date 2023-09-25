from PIL import Image

# Open the first image
with Image.open('python1.png') as im:
    # Create a list of images
    images = [im]
    # Open and append the rest of the frames
    frame_filename = 'python2.png'
    with Image.open(frame_filename) as frame:
        images.append(frame)

        # Save the animated GIF
        images[0].save('animation.gif', 
                       save_all=True, 
                       append_images=[images[1]], 
                       duration=200, loop=0)