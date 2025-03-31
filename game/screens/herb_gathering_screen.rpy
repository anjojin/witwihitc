screen herb_gathering_screen:
    $ print("I am now in screen herb_gathering_screen")
    use frame1
    use frame2
    use frame3
    use frame4
    use frame5
    imagebutton:
        xalign 0.5
        ypos 890
        idle "gui/button/herb_proceed.png"
        hover "gui/button/herb_proceed_hover.png"
        insensitive "gui/button/herb_proceed_unavailable.png"
        action Jump("herb_proceed")

screen frame1:
    $ print("I am now in screen frame1")
    $ print(frame1_empty)
    $ print(frame1_progress)
    if frame1_empty==False:
        $ print(frame1_empty)
        $ print("I think frame1 is not empty")
        if turn_max1 == herb_max1:
            $ print("I am incorrectly accessing this statement")
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herbf1_d"
                hover "herbf1_h"
                action Jump("herb1_collected")
        elif frame1_progress==1:
            $ print("I think frame1's progress is 1")
            $ print(frame1_progress)
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb1f1"
                hover "herb1f1_h"
                insensitive "herb1f1_u"
                action Jump("herb1_clicked")
        elif frame1_progress==2:
            $ print("I think frame1's progress is 2")
            $ print(frame1_progress)
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb2f1"
                hover "herb2f1_h"
                insensitive "herb2f1_u"
                action Jump("herb1_clicked")
        else:
            $ print("I think frame1's progress is 3")
            $ print(frame1_progress)
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb3f1"
                hover "herb3f1_h"
                insensitive "herb3f1_u"
                action Jump("herb1_clicked")

screen frame2:
    $ print("I am now in screen frame2")
    if not frame2_empty:
        if turn_max2==herb_max2:
            imagebutton:
                xpos xpos2
                ypos ypos2
                idle "herbf2_d"
                hover "herbf2_h"
                action Jump("herb2_collected")
        elif frame2_progress==1:
            imagebutton:
                xpos xpos2
                ypos ypos2
                idle "herb1f2"
                hover "herb1f2_h"
                insensitive "herb1f2_u"
                action Jump("herb2_clicked")
        elif frame2_progress==2:
            imagebutton:
                xpos xpos2
                ypos ypos2
                idle "herb2f2"
                hover "herb2f2_h"
                insensitive "herb2f2_u"
                action Jump("herb2_clicked")
        else:
            imagebutton:
                xpos xpos2
                ypos ypos2
                idle "herb3f2"
                hover "herb3f2_h"
                insensitive "herb3f2_u"
                action Jump("herb2_clicked")  

screen frame3:
    $ print("I am now in screen frame3")
    if not frame3_empty:
        if turn_max3==herb_max3:
            imagebutton:
                xpos xpos3
                ypos ypos3
                idle "herbf3_d"
                hover "herbf3_h"
                action Jump("herb3_collected")
        elif frame3_progress==1:
            imagebutton:
                xpos xpos3
                ypos ypos3
                idle "herb1f3"
                hover "herb1f3_h"
                insensitive "herb1f3_u"
                action Jump("herb3_clicked")
        elif frame3_progress==2:
            imagebutton:
                xpos xpos3
                ypos ypos3
                idle "herb2f3"
                hover "herb2f3_h"
                insensitive "herb2f3_u"
                action Jump("herb3_clicked")
        else:
            imagebutton:
                xpos xpos3
                ypos ypos3
                idle "herb3f3"
                hover "herb3f3_h"
                insensitive "herb3f3_u"
                action Jump("herb3_clicked")  
        
screen frame4:  
    $ print("I am now in screen frame4")
    if not frame4_empty:
        if turn_max4==herb_max4:
            imagebutton:
                xpos xpos4
                ypos ypos4
                idle "herbf4_d"
                hover "herbf4_h"
                action Jump("herb4_collected")
        elif frame4_progress==1:
            imagebutton:
                xpos xpos4
                ypos ypos4
                idle "herb1f4"
                hover "herb1f4_h"
                insensitive "herb1f4_u"
                action Jump("herb4_clicked")
        elif frame4_progress==2:
            imagebutton:
                xpos xpos4
                ypos ypos4
                idle "herb2f4"
                hover "herb2f4_h"
                insensitive "herb2f4_u"
                action Jump("herb4_clicked")
        else:
            imagebutton:
                xpos xpos4
                ypos ypos4
                idle "herb3f4"
                hover "herb3f4_h"
                insensitive "herb3f4_u"
                action Jump("herb4_clicked")  
        
screen frame5: 
    $ print("I am now in screen frame5")
    if not frame5_empty:
        if turn_max5==herb_max5:
            imagebutton:
                xpos xpos5
                ypos ypos5
                idle "herbf5_d"
                hover "herbf5_h"
                action Jump("herb5_collected")
        elif frame5_progress==1:
            imagebutton:
                xpos xpos5
                ypos ypos5
                idle "herb1f5"
                hover "herb1f5_h"
                insensitive "herb1f5_u"
                action Jump("herb5_clicked")
        elif frame5_progress==2:
            imagebutton:
                xpos xpos5
                ypos ypos5
                idle "herb2f5"
                hover "herb2f5_h"
                insensitive "herb2f5_u"
                action Jump("herb5_clicked")
        else:
            imagebutton:
                xpos xpos5
                ypos ypos5
                idle "herb3f5"
                hover "herb3f5_h"
                insensitive "herb3f5_u"
                action Jump("herb5_clicked")  

screen locked_herbs:
    if f1_locked:
        add "herbf1_l" xpos xpos1 ypos ypos1
    if f2_locked:
        add "herbf2_l" xpos xpos2 ypos ypos2
    if f3_locked:
        add "herbf3_l" xpos xpos3 ypos ypos3
    if f4_locked:
        add "herbf4_l" xpos xpos4 ypos ypos4
    if f5_locked:
        add "herbf5_l" xpos xpos5 ypos ypos5