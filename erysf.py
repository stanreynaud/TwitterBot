from PIL import Image
import io
import random
import time




def littleenv(pixel,width,height):
    m = set()

    x=pixel[0]
    y=pixel[1]

    if (x >= 0):
        if(y-1 >= 0):
            m.add((x,y-1))
    if (x-1 >= 0):
        if(y >= 0):
            m.add((x-1,y))
    if (x < width):
        if(y+1 < height):
            m.add((x,y+1))
    if (x+1 < width):
        if(y < height):
            m.add((x+1,y))
    return m


#-------------------------------------------------------------------------------------------------------

def env(pixel,width,height):
    m = set()

    x=pixel[0]
    y=pixel[1]

    if (x-1 >= 0):
        if(y-1 >= 0):
            m.add((x-1,y-1))
    if (x >= 0):
        if(y-1 >= 0):
            m.add((x,y-1))
    if (x-1 >= 0):
        if(y >= 0):
            m.add((x-1,y))
    if (x+1 < width):
        if(y+1 < height):
            m.add((x+1,y+1))
    if (x < width):
        if(y+1 < height):
            m.add((x,y+1))
    if (x+1 < width):
        if(y < height):
            m.add((x+1,y))
    if (x-1 >= 0):
        if(y+1 < height):
            m.add((x-1,y+1))
    if (x+1 < width):
        if(y-1 >= 0):
            m.add((x+1,y-1))
    return m

#-------------------------------------------------------------------------------------------------------

def diagenv(pixel,width,height):
    m = set()

    x=pixel[0]
    y=pixel[1]

    if (x-1 >= 0):
        if(y-1 >= 0):
            m.add((x-1,y-1))
    if (x+1 < width):
        if(y+1 < height):
            m.add((x+1,y+1))
    if (x-1 >= 0):
        if(y+1 < height):
            m.add((x-1,y+1))
    if (x+1 < width):
        if(y-1 >= 0):
            m.add((x+1,y-1))
    return m

#-------------------------------------------------------------------------------------------------------

def maker(image,canvas):
    start=time.time()
    
    width, height = image.size
    stock = random.randint(1,width*height)
    fullx,fully = canvas.size
    print("stock ",stock)
    startx = random.randint(0,width-1)
    starty = random.randint(0,height-1)
    print("starting ",startx," ",starty)
    color = f(0,width,height,fullx,fully)
    colorlist= list(color)
    colorlist[3]=255
    color=tuple(colorlist)

    colored = set()
    colored.add((startx,starty))

    coloredaround=set()
    
    chosen = (startx,starty)
    count = 0
    tmpcount =0

    image.putpixel(chosen,color)
    
    
    for i in range(1,8000):
        if random.randint(1,100)<= 40:
            count=8
            for source in colored-coloredaround:
                if env(source,width,height).issubset(colored):
                    coloredaround.add(source)
                    break
                
                for near in env(source,width,height)-colored:
                    for nearnear in env(near, width,height):
                        if nearnear in colored:
                            tmpcount+=1
                    if  tmpcount < count:
                        count = tmpcount
                        chosen = near
                    elif tmpcount == count:
                        #print("1/2")
                        if random.randint(1,10) > 5:
                            count = tmpcount
                            chosen = near
                    tmpcount=0
            image.putpixel(chosen,color)
            colored.add(chosen)
            #print(chosen,"count ",count,colored,i)
        else:
            count=0
            for source in colored-coloredaround:
                if env(source,width,height).issubset(colored):
                    coloredaround.add(source)
                    break

                
                for near in env(source,width,height)-colored:
                    for nearnear in env(near, width,height):
                        if nearnear in colored:
                            tmpcount+=1
                    if  tmpcount > count:
                        count = tmpcount
                        chosen = near
                    elif tmpcount == count:
                        #print("1/2")
                        if random.randint(1,10) > 5:
                            count = tmpcount
                            chosen = near
                    tmpcount=0
            image.putpixel(chosen,color)
            colored.add(chosen)
            #print(chosen,"count ",count,colored,i)

            
        if i%500 == 0:
            print(i,"%.6s" %(time.time()-start),len(coloredaround))
    return


#-------------------------------------------------------------------------------------------------------


def randmaker(image,canvas):
    start=time.time()
    
    width, height = image.size
    stock = random.randint(1,int((width*height)))%10000#STOCK ADJUSTEMENT
    fullx,fully = canvas.size
    startx = random.randint(0,width-1)
    starty = random.randint(0,height-1)
    print("\n\n\npixel stock ",stock)
    print("starting point",(startx,starty))
    color = f(0,width,height,fullx,fully)
    colorlist= list(color)
    colorlist[3]=255
    color=tuple(colorlist)

    colored = set()
    colored.add((startx,starty))

    coloredaround=set()
    
    chosen = (startx,starty)
    tmpcount =0

    image.putpixel(chosen,color)
    transparency=255

    minimumtransparency = random.randint(0,255)
    print("minimum transparency: ",minimumtransparency,"/255")
    friends = random.randint(1,8)
    for i in range(1,stock):
        #TRANSPARENCY MODE   int(255-(i*255)/stock) != transparency
        if int(255-(i*minimumtransparency)/stock) != transparency and (transparency >= minimumtransparency):
            colorlist= list(color)
            transparency=int(255-(i*255)/stock)
            colorlist[3]=transparency
            color=tuple(colorlist)


        
        if True:
            if True:
                for source in colored-coloredaround:
                    if env(source,width,height).issubset(colored):
                        coloredaround.add(source)
                        break
                    
                    for near in env(source,width,height)-colored:
                        for nearnear in env(near, width,height):
                            if nearnear in colored:
                                tmpcount+=1
                        #print(tmpcount)
                        if tmpcount == friends or tmpcount ==friends+1 or tmpcount == friends+2:
                            if random.randint(1,10) > 5:
                                chosen = near
                                break
                        tmpcount=0
                image.putpixel(chosen,color)
                colored.add(chosen)
        if i%500 == 0:
            print(i,"%.6s" %(time.time()-start),"full",len(coloredaround))
    return


#-------------------------------------------------------------------------------------------------------
def mixmaker(image,canvas):
    start=time.time()
    
    width, height = image.size
    stock = 3000#random.randint(1,int((width*height)))%5000#STOCK ADJUSTEMENT
    fullx,fully = canvas.size
    startx = random.randint(0,width-1)
    starty = random.randint(0,height-1)
    print("\npixel stock ",stock)
    print("starting point",(startx,starty))
    color = f(0,width,height,fullx,fully)
    colorlist= list(color)
    colorlist[3]=255
    color=tuple(colorlist)

    colored = set()
    colored.add((startx,starty))

    coloredaround=set()
    coloredarounddiag=set()
    coloredaroundlittle=set()
    
    chosen = (startx,starty)
    count = 0
    tmpcount =0

    image.putpixel(chosen,color)
    transparency=255

    awaychance = random.randint(1,100)
    littleenvchance = random.randint(1,100)
    diagenvchance = random.randint(1,100-littleenvchance)
    minimumtransparency = random.randint(0,180)
    print("little environement : ",littleenvchance,"%")
    print("diag environement : ",diagenvchance,"%")
    print("full environement   : ",100-littleenvchance-diagenvchance,"%")
    print("away (both env)     : ",awaychance,"%")
    print("close (both env)    : ",(100-awaychance),"%")
    print("minimum transparency: ",minimumtransparency,"/255")

    t_end = time.time() + random.randint(60,60*2)
    i=0
    while time.time() < t_end and i<10000:
        i+=1
    #for i in range(1,stock):
        #TRANSPARENCY MODE   int(255-(i*255)/stock) != transparency
        if int(255-(i*minimumtransparency)/stock) != transparency and (transparency >= minimumtransparency):
            colorlist= list(color)
            transparency=int(255-(i*255)/stock)
            colorlist[3]=transparency
            color=tuple(colorlist)

        #LITTLEENV
        if random.randint(1,100)<= littleenvchance:
            if random.randint(1,100)<= awaychance:
                count=8
                for source in colored-coloredaroundlittle-coloredaround:
                    if littleenv(source,width,height).issubset(colored):
                        coloredaroundlittle.add(source)
                        break
                    
                    for near in littleenv(source,width,height)-colored:
                        for nearnear in env(near, width,height):
                            if nearnear in colored:
                                tmpcount+=1
                        if  tmpcount < count:
                            count = tmpcount
                            chosen = near
                        elif tmpcount == count:
                            #print("1/2")
                            if random.randint(1,10) > 5:
                                count = tmpcount
                                chosen = near
                        tmpcount=0
                image.putpixel(chosen,color)
                colored.add(chosen)
                #print(chosen,"count ",count,colored,i)
            else:
                count=0
                for source in colored-coloredaroundlittle-coloredaround:
                    if littleenv(source,width,height).issubset(colored):
                        coloredaroundlittle.add(source)
                        break

                    
                    for near in littleenv(source,width,height)-colored:
                        for nearnear in env(near, width,height):
                            if nearnear in colored:
                                tmpcount+=1
                        if  tmpcount > count:
                            count = tmpcount
                            chosen = near
                        elif tmpcount == count:
                            #print("1/2")
                            if random.randint(1,10) > 5:
                                count = tmpcount
                                chosen = near
                        tmpcount=0
                image.putpixel(chosen,color)
                colored.add(chosen)
                #print(chosen,"count ",count,colored,i)

        

        #DIAGENV
        if random.randint(1,100)<= diagenvchance:
            if random.randint(1,100)<= awaychance:
                count=8
                for source in colored-coloredarounddiag-coloredaround:
                    if diagenv(source,width,height).issubset(colored):
                        coloredarounddiag.add(source)
                        break
                    
                    for near in diagenv(source,width,height)-colored:
                        for nearnear in env(near, width,height):
                            if nearnear in colored:
                                tmpcount+=1
                        if  tmpcount < count:
                            count = tmpcount
                            chosen = near
                        elif tmpcount == count:
                            #print("1/2")
                            if random.randint(1,10) > 5:
                                count = tmpcount
                                chosen = near
                        tmpcount=0
                image.putpixel(chosen,color)
                colored.add(chosen)
                #print(chosen,"count ",count,colored,i)
            else:
                count=0
                for source in colored-coloredarounddiag-coloredaround:
                    if littleenv(source,width,height).issubset(colored):
                        coloredarounddiag.add(source)
                        break

                    
                    for near in littleenv(source,width,height)-colored:
                        for nearnear in env(near, width,height):
                            if nearnear in colored:
                                tmpcount+=1
                        if  tmpcount > count:
                            count = tmpcount
                            chosen = near
                        elif tmpcount == count:
                            #print("1/2")
                            if random.randint(1,10) > 5:
                                count = tmpcount
                                chosen = near
                        tmpcount=0
                image.putpixel(chosen,color)
                colored.add(chosen)
                #print(chosen,"count ",count,colored,i)

        #ENV        
        else:
            if random.randint(1,100)<= awaychance:
                count=8
                for source in colored-coloredaround:
                    if env(source,width,height).issubset(colored):
                        coloredaround.add(source)
                        break
                    
                    for near in env(source,width,height)-colored:
                        for nearnear in env(near, width,height):
                            if nearnear in colored:
                                tmpcount+=1
                        if  tmpcount < count:
                            count = tmpcount
                            chosen = near
                        elif tmpcount == count:
                            #print("1/2")
                            if random.randint(1,10) > 5:
                                count = tmpcount
                                chosen = near
                        tmpcount=0
                image.putpixel(chosen,color)
                colored.add(chosen)
                #print(chosen,"count ",count,colored,i)
            else:
                count=0
                for source in colored-coloredaround:
                    if env(source,width,height).issubset(colored):
                        coloredaround.add(source)
                        break

                    
                    for near in env(source,width,height)-colored:
                        for nearnear in env(near, width,height):
                            if nearnear in colored:
                                tmpcount+=1
                        if  tmpcount > count:
                            count = tmpcount
                            chosen = near
                        elif tmpcount == count:
                            #print("1/2")
                            if random.randint(1,10) > 5:
                                count = tmpcount
                                chosen = near
                        tmpcount=0
                image.putpixel(chosen,color)
                colored.add(chosen)
                #print(chosen,"count ",count,colored,i)


            
        if i%500 == 0:
            print(i,"%.6s" %(time.time()-start),"full",len(coloredaround)," little",len(coloredaroundlittle)," diag",len(coloredarounddiag))
    
    return



#-------------------------------------------------------------------------------------------------------


def littlemaker(image,canvas):
    start=time.time()
    fullx,fully = canvas.size
    width, height = image.size
    stock = random.randint(200,12000)
    print("stock ",stock)
    startx = random.randint(0,width-1)
    starty = random.randint(0,height-1)
    print("starting ",startx," ",starty)
    color = f(0,width,height,fullx,fully)
    colorlist= list(color)
    colorlist[3]=255
    color=tuple(colorlist)

    colored = set()
    colored.add((startx,starty))

    coloredaround=set()
    
    chosen = (startx,starty)
    count = 0
    tmpcount =0

    image.putpixel(chosen,color)
    minimumtransparency = random.randint(1,180)
    transparency = 255
    for i in range(1,stock):
        #TRANSPARENCY MODE   int(255-(i*255)/stock) != transparency
        if int(255-(i*255)/stock) != transparency:#int(255-(i*minimumtransparency)/stock) != transparency and (transparency >= minimumtransparency):
            colorlist= list(color)
            transparency=int(255-(i*255)/stock)
            colorlist[3]=transparency
            color=tuple(colorlist)
        if True:
            if True:
                for source in colored-coloredaround:
                    if env(source,width,height).issubset(colored):
                        coloredaround.add(source)
                        break
                    if random.randint(1,100) <= 10:
                        chosen=list(env(source,width,height)-colored)[random.randint(0,len(list(env(source,width,height)-colored))-1)]
                        image.putpixel(chosen,color)
                        colored.add(chosen)
                    #print(chosen)
        if i%500 == 0:
            print(i,"%.6s" %(time.time()-start),len(coloredaround))
    return



#-------------------------------------------------------------------------------------------------------

def f(n,x,y,fullx,fully):
    A = int((x*y*255)/(int(3*fullx/4)*int(3*fully/4)))
    B = random.randint(0,255)
    G = random.randint(0,255)
    R = random.randint(0,255)

    return (R,G,B,A)

def rectangles(canvas):
    fullx,fully = canvas.size
    for n in range(300):
        sizew = random.randint(1,int(3*fullx/4))
        sizeh = random.randint(1,int(3*fully/4))
        l = list(f(n,sizew,sizeh,fullx,fully))
        l[3] = random.randint(0,40)
        
        
        pix = Image.new("RGBA", (sizew,sizeh), tuple(l))
        width, height = pix.size
        littlemaker(pix,canvas)
        canvas.paste(pix,(random.randint(0,fullx-int(sizew/2)),random.randint(0,fully-int(sizeh/2))),pix)
        #canvas.show()
        canvas.save("image.png", format="png")
    return

def rectanglesclean(canvas):
    fullx,fully = canvas.size
    for n in range(300):
        l = list(f(n,fullx,fully,fullx,fully))
        l[3] = 0
        
        
        pix = Image.new("RGBA", (fullx,fully), tuple(l))
        width, height = pix.size
        mixmaker(pix,canvas)
        canvas.paste(pix,(0,0),pix)
        #canvas.show()
        canvas.save("image.png", format="png")
    return


def rectanglesclean(canvas):
    fullx,fully = canvas.size
    for n in range(1):
        l = list(f(n,fullx,fully,fullx,fully))
        l[3] = 0
        
        
        pix = Image.new("RGBA", (fullx,fully), tuple(l))
        width, height = pix.size
        mixmaker(pix,canvas)
        canvas.paste(pix,(0,0),pix)
        #canvas.show()
        canvas.save("image.png", format="png")
    return
