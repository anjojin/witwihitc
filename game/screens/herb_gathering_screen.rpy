screen frame1_screen:
    if not frame1.empty:
        if frame1.progress == frame1.herb.turns:
            imagebutton:
                xpos frame1.xpos
                ypos frame1.ypos
                idle "herbf1_d"
                hover "herbf1_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb1_found")
        elif frame1.progress==1:
            imagebutton:
                xpos frame1.xpos
                ypos frame1.ypos
                idle "herb1f1"
                hover "herb1f1_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb1_p1_clicked")
        elif frame1.progress==2:
            imagebutton:
                xpos frame1.xpos
                ypos frame1.ypos
                idle "herb2f1"
                hover "herb2f1_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb1_p2_clicked")
        elif frame1.progress==3:
            imagebutton:
                xpos frame1.xpos
                ypos frame1.ypos
                idle "herb3f1"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                hover "herb3f1_h"
                action Jump("herb1_p3_clicked")

screen frame2_screen:
    if not frame2.empty:
        if frame2.progress == frame2.herb.turns:          
            imagebutton:
                xpos frame2.xpos
                ypos frame2.ypos
                idle "herbf2_d"
                hover "herbf2_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb2_found")
        elif frame2.progress==1:
            imagebutton:
                xpos frame2.xpos
                ypos frame2.ypos
                idle "herb1f2"
                hover "herb1f2_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb2_p1_clicked")
        elif frame2.progress==2:
            imagebutton:
                xpos frame2.xpos
                ypos frame2.ypos
                idle "herb2f2"
                hover "herb2f2_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb2_p2_clicked")
        elif frame2.progress==3:
            imagebutton:
                xpos frame2.xpos
                ypos frame2.ypos
                idle "herb3f2"
                hover "herb3f2_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb2_p3_clicked")  

screen frame3_screen:
    if not frame3.empty:
        if frame3.progress == frame3.herb.turns:
            imagebutton:
                xpos frame3.xpos
                ypos frame3.ypos
                idle "herbf3_d"
                hover "herbf3_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb3_found")
        elif frame3.progress==1:
            imagebutton:
                xpos frame3.xpos
                ypos frame3.ypos
                idle "herb1f3"
                hover "herb1f3_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb3_p1_clicked")
        elif frame3.progress==2:
            imagebutton:
                xpos frame3.xpos
                ypos frame3.ypos
                idle "herb2f3"
                hover "herb2f3_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb3_p2_clicked")
        elif frame3.progress==3:
            imagebutton:
                xpos frame3.xpos
                ypos frame3.ypos
                idle "herb3f3"
                hover "herb3f3_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb3_p3_clicked")  
        
screen frame4_screen:  
    if not frame4.empty:
        if frame4.progress == frame4.herb.turns:
            imagebutton:
                xpos frame4.xpos
                ypos frame4.ypos
                idle "herbf4_d"
                hover "herbf4_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb4_found")
        elif frame4.progress==1:
            imagebutton:
                xpos frame4.xpos
                ypos frame4.ypos
                idle "herb1f4"
                hover "herb1f4_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb4_p1_clicked")
        elif frame4.progress==2:
            imagebutton:
                xpos frame4.xpos
                ypos frame4.ypos
                idle "herb2f4"
                hover "herb2f4_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb4_p2_clicked")
        elif frame4.progress==3:
            imagebutton:
                xpos frame4.xpos
                ypos frame4.ypos
                idle "herb3f4"
                hover "herb3f4_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb4_p3_clicked")  
        
screen frame5_screen: 
    if not frame5.empty:
        if frame5.progress == frame5.herb.turns:
            imagebutton:
                xpos frame5.xpos
                ypos frame5.ypos
                idle "herbf5_d"
                hover "herbf5_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb5_found")
        elif frame5.progress==1:
            imagebutton:
                xpos frame5.xpos
                ypos frame5.ypos
                idle "herb1f5"
                hover "herb1f5_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb5_p1_clicked")
        elif frame5.progress==2:
            imagebutton:
                xpos frame5.xpos
                ypos frame5.ypos
                idle "herb2f5"
                hover "herb2f5_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb5_p2_clicked")
        elif frame5.progress==3:
            $ print("screen knows progress is 3")
            imagebutton:
                xpos frame5.xpos
                ypos frame5.ypos
                idle "herb3f5"
                hover "herb3f5_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herb5_p3_clicked")  

screen tutorial_frame_screen:
    if not tutorial_frame.empty:
        if (tutorial_frame.progress - 1) == tutorial_frame.herb.turns:
            imagebutton:
                xpos tutorial_frame.xpos
                ypos tutorial_frame.ypos
                idle "herbft_d"
                hover "herbft_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herbt_found")
        elif tutorial_frame.progress==1:
            imagebutton:
                xpos tutorial_frame.xpos
                ypos tutorial_frame.ypos
                idle "herb1ft"
                hover "herb1ft_h"
                hover_sound "audio/sfx/button_hover_3.mp3"
                activate_sound "audio/sfx/button_click_3.mp3"
                action Jump("herbt_p1_clicked")
        elif tutorial_frame.progress==2:
            add "herb2ft" xpos tutorial_frame.xpos ypos tutorial_frame.ypos
    imagebutton:
        xalign 0.5
        ypos 890
        idle "gui/button/herb_proceed.png"
        hover "gui/button/herb_proceed_hover.png"
        insensitive "gui/button/herb_proceed_unavailable.png"
        hover_sound "audio/sfx/button_hover_3.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        if not tutorial_proceeded:
            action Jump("demonstrate_proceed")
        else:
            action Jump("demonstrate_loss")

screen locked_herbs:
    if frame1.locked:
        add "herbf1_l" xpos frame1.xpos ypos frame1.ypos
    if frame2.locked:
        add "herbf2_l" xpos frame2.xpos ypos frame2.ypos
    if frame3.locked:
        add "herbf3_l" xpos frame3.xpos ypos frame3.ypos
    if frame4.locked:
        add "herbf4_l" xpos frame4.xpos ypos frame4.ypos
    if frame5.locked:
        add "herbf5_l" xpos frame5.xpos ypos frame5.ypos
    if tutorial_frame.locked:
        add "herbft_l" xpos tutorial_frame.xpos ypos tutorial_frame.ypos

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
        hover_sound "audio/sfx/button_hover_3.mp3"
        activate_sound "audio/sfx/camp_click.mp3"
        action Jump("herb_proceed")