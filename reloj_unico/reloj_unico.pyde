rectangle_width = 50
rectangle_widthII=50
rectangle_widthIII=50

def setup():
    size(300,300)
    noStroke()


    
def draw():   
    global rectangle_width  
    background(map(hour(), 0,24,255,0)) 
    noStroke()
    fill(250,180,230)
    rect(0,height/2-65,rectangle_width,40)
    rectangle_width += 1
    if rectangle_width > width:
        rectangle_width = 0
    else:
        rectangle_width = map(second(), 0 ,60, 0, width)
        
    global rectangle_widthII
    fill(230,100,200)
    rect(0,height/2-20,rectangle_widthII,40)
    rectangle_widthII += 1
    if rectangle_widthII > width:
        rectangle_widthII = 0
    else:
        rectangle_widthII = map(minute(), 0 , 60, 0, width)
        
    global rectangle_widthIII
    fill(200,20,240)
    rect(0,height/2+25, rectangle_widthIII, 40)
    rectangle_widthIII += 1
    if rectangle_widthIII > width:
        rectangle_widthIII = 0
    else:
        rectangle_widthIII = map(hour(), 0 , 24, 0, width)
    stroke(250,0,0)
    line(width/2,0,width/2,height)