#This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def christmas_tree():
  for image in picture:
    for pixel in image:
      if (pixel):
        print('*', end ="")
      else:
        print(' ', end ="")
     print('')

# To print as many as you like
christmas_tree()
