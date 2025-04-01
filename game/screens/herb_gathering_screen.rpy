screen frame1_screen:
    if not frame1.empty:
        if (frame1.progress - 1) == frame1.herb.turns:
            imagebutton:
                xpos frame1.xpos
                ypos frame1.ypos
                idle "herbf1_d"
                hover "herbf1_h"
                action Jump("herb1_collected")
        elif frame1.progress==1:
            imagebutton:
                xpos frame1.xpos
                ypos frame1.ypos
                idle "herb1f1"
                hover "herb1f1_h"
                insensitive "herb1f1_u"
                action Jump("herb1_clicked")
        elif frame1.progress==2:
            imagebutton:
                xpos frame1.xpos
                ypos frame1.ypos
                idle "herb2f1"
                hover "herb2f1_h"
                insensitive "herb2f1_u"
                action Jump("herb1_clicked")
        else:
            imagebutton:
                xpos frame1.xpos
                ypos frame1.ypos
                idle "herb3f1"
                hover "herb3f1_h"
                insensitive "herb3f1_u"
                action Jump("herb1_clicked")

screen frame2_screen:
    if not frame2.empty:
        if (frame2.progress - 1) == frame2.herb.turns:
            imagebutton:
                xpos frame2.xpos
                ypos frame2.ypos
                idle "herbf2_d"
                hover "herbf2_h"
                action Jump("herb2_collected")
        elif frame2.progress==1:
            imagebutton:
                xpos frame2.xpos
                ypos frame2.ypos
                idle "herb1f2"
                hover "herb1f2_h"
                insensitive "herb1f2_u"
                action Jump("herb2_clicked")
        elif frame2.progress==2:
            imagebutton:
                xpos frame2.xpos
                ypos frame2.ypos
                idle "herb2f2"
                hover "herb2f2_h"
                insensitive "herb2f2_u"
                action Jump("herb2_clicked")
        else:
            imagebutton:
                xpos frame2.xpos
                ypos frame2.ypos
                idle "herb3f2"
                hover "herb3f2_h"
                insensitive "herb3f2_u"
                action Jump("herb2_clicked")  

screen frame3_screen:
    if not frame3.empty:
        if (frame3.progress - 1) == frame3.herb.turns:
            imagebutton:
                xpos frame3.xpos
                ypos frame3.ypos
                idle "herbf3_d"
                hover "herbf3_h"
                action Jump("herb3_collected")
        elif frame3.progress==1:
            imagebutton:
                xpos frame3.xpos
                ypos frame3.ypos
                idle "herb1f3"
                hover "herb1f3_h"
                insensitive "herb1f3_u"
                action Jump("herb3_clicked")
        elif frame3.progress==2:
            imagebutton:
                xpos frame3.xpos
                ypos frame3.ypos
                idle "herb2f3"
                hover "herb2f3_h"
                insensitive "herb2f3_u"
                action Jump("herb3_clicked")
        else:
            imagebutton:
                xpos frame3.xpos
                ypos frame3.ypos
                idle "herb3f3"
                hover "herb3f3_h"
                insensitive "herb3f3_u"
                action Jump("herb3_clicked")  
        
screen frame4_screen:  
    if not frame4.empty:
        if (frame4.progress - 1) == frame4.herb.turns:
            imagebutton:
                xpos frame4.xpos
                ypos frame4.ypos
                idle "herbf4_d"
                hover "herbf4_h"
                action Jump("herb4_collected")
        elif frame4.progress==1:
            imagebutton:
                xpos frame4.xpos
                ypos frame4.ypos
                idle "herb1f4"
                hover "herb1f4_h"
                insensitive "herb1f4_u"
                action Jump("herb4_clicked")
        elif frame4.progress==2:
            imagebutton:
                xpos frame4.xpos
                ypos frame4.ypos
                idle "herb2f4"
                hover "herb2f4_h"
                insensitive "herb2f4_u"
                action Jump("herb4_clicked")
        else:
            imagebutton:
                xpos frame4.xpos
                ypos frame4.ypos
                idle "herb3f4"
                hover "herb3f4_h"
                insensitive "herb3f4_u"
                action Jump("herb4_clicked")  
        
screen frame5_screen: 
    if not frame5.empty:
        if (frame5.progress - 1) == frame5.herb.turns:
            imagebutton:
                xpos frame5.xpos
                ypos frame5.ypos
                idle "herbf5_d"
                hover "herbf5_h"
                action Jump("herb5_collected")
        elif frame5.progress==1:
            imagebutton:
                xpos frame5.xpos
                ypos frame5.ypos
                idle "herb1f5"
                hover "herb1f5_h"
                insensitive "herb1f5_u"
                action Jump("herb5_clicked")
        elif frame5.progress==2:
            imagebutton:
                xpos frame5.xpos
                ypos frame5.ypos
                idle "herb2f5"
                hover "herb2f5_h"
                insensitive "herb2f5_u"
                action Jump("herb5_clicked")
        else:
            imagebutton:
                xpos frame5.xpos
                ypos frame5.ypos
                idle "herb3f5"
                hover "herb3f5_h"
                insensitive "herb3f5_u"
                action Jump("herb5_clicked")  

screen locked_herbs:
    if frame1.locked:
        add "herbf1_l" xpos frame1.xpos ypos frame1.ypos
    elif frame2.locked:
        add "herbf2_l" xpos frame2.xpos ypos frame2.ypos
    elif frame3.locked:
        add "herbf3_l" xpos frame3.xpos ypos frame3.ypos
    elif frame4.locked:
        add "herbf4_l" xpos frame4.xpos ypos frame4.ypos
    elif frame5.locked:
        add "herbf5_l" xpos frame5.xpos ypos frame5.ypos

screen herb_gathering_screen:
    use frame1_screen
    use frame2_screen
    use frame3_screen
    use frame4_screen
    use frame5_screen
    imagebutton:
        xalign 0.5
        ypos 890
        idle "gui/button/herb_proceed.png"
        hover "gui/button/herb_proceed_hover.png"
        insensitive "gui/button/herb_proceed_unavailable.png"
        action Jump("herb_proceed")