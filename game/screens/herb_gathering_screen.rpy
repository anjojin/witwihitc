screen frame1:
    if not frame1_empty:
        if frame1_progress==[herb_turns[herbf1]+1]:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herbf1_d"
                hover "herbf1_h"
                action Jump("herb1_collected")
        if frame1_progress==1:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb1f1"
                hover "herb1f1_h"
                insensitive "herb1f1_u"
                action Jump("herb1_clicked")
        elif frame1_progress==2:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb2f1"
                hover "herb2f1_h"
                insensitive "herb2f1_u"
                action Jump("herb1_clicked")
        elif frame1_progress==3:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb3f1"
                hover "herb3f1_h"
                insensitive "herb3f1_u"
                action Jump("herb1_clicked")

screen frame2:
    if not frame2_empty:
        if frame2_progress==[herb_turns[herbf2]+1]:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herbf2_d"
                hover "herbf2_h"
                action Jump("herb2_collected")
        elif frame2_progress==1:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb1f2"
                hover "herb1f2_h"
                insensitive "herb1f2_u"
                action Jump("herb2_clicked")
        elif frame2_progress==2:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb2f2"
                hover "herb2f2_h"
                insensitive "herb2f2_u"
                action Jump("herb2_clicked")
        elif frame2_progress==3:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb3f2"
                hover "herb3f2_h"
                insensitive "herb3f2_u"
                action Jump("herb2_clicked")  

screen frame3:
    if not frame3_empty:
        if frame3_progress==[herb_turns[herbf3]+1]:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herbf3_d"
                hover "herbf3_h"
                action Jump("herb3_collected")
        elif frame3_progress==1:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb1f3"
                hover "herb1f3_h"
                insensitive "herb1f3_u"
                action Jump("herb3_clicked")
        elif frame3_progress==2:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb2f3"
                hover "herb2f3_h"
                insensitive "herb2f3_u"
                action Jump("herb3_clicked")
        elif frame3_progress==3:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb3f3"
                hover "herb3f3_h"
                insensitive "herb3f3_u"
                action Jump("herb3_clicked")  
        
screen frame4:        
    if not frame4_empty:
        if frame4_progress==[herb_turns[herbf4]+1]:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herbf4_d"
                hover "herbf4_h"
                action Jump("herb4_collected")
        elif frame4_progress==1:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb1f4"
                hover "herb1f4_h"
                insensitive "herb1f4_u"
                action Jump("herb4_clicked")
        elif frame4_progress==2:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb2f4"
                hover "herb2f4_h"
                insensitive "herb2f4_u"
                action Jump("herb4_clicked")
        elif frame4_progress==3:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb3f4"
                hover "herb3f4_h"
                insensitive "herb3f4_u"
                action Jump("herb4_clicked")  
        
screen frame5:       
    if not frame5_empty:
        if frame5_progress==[herb_turns[herbf4]+1]:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herbf5_d"
                hover "herbf5_h"
                action Jump("herb5_collected")
        elif frame5_progress==1:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb1f5"
                hover "herb1f5_h"
                insensitive "herb1f5_u"
                action Jump("herb5_clicked")
        elif frame5_progress==2:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb2f5"
                hover "herb2f5_h"
                insensitive "herb2f5_u"
                action Jump("herb5_clicked")
        elif frame5_progress==3:
            imagebutton:
                xpos xpos1
                ypos ypos1
                idle "herb3f5"
                hover "herb3f5_h"
                insensitive "herb3f5_u"
                action Jump("herb5_clicked")  

screen frame1_locked:
    add "herbf1_l" xpos xpos1 ypos ypos1

screen frame2_locked:
    add "herbf2_l" xpos xpos2 ypos ypos2

screen frame3_locked:
    add "herbf3_l" xpos xpos3 ypos ypos3

screen frame4_locked:
    add "herbf4_l" xpos xpos4 ypos ypos4

screen frame5_locked:
    add "herbf5_l" xpos xpos5 ypos ypos5

screen herb_gathering_screen:
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