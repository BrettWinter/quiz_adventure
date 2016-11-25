# An adventure game


def room1():


    print("You enter a dark old insane asylum")
    print("there are two corridors infront of you")
    print("l: Left")
    print("r: Right")

    direction = input("Direction ")
    if direction.lower() == "l":
        print("Something grabs you and snapcs your neck")
        print("GAME OVER-YOU START AGAIN AT THE START")
        room1()

    if direction.lower() == "r":
        print("as you walk down the corridor your hear singing...")





    print("as you walk towards the singing you realise its coming from little girl")
    print("and you see the room she is sitting in")
    print("e: enter her room")
    print("r: run away")

    direction = input("Direction ")
    if direction.lower() == "e":
        print("as you enter you realise the little girl is a zombie...but its too late!")
        print("she runs towards you latching onto your neck")
        print("GAME OVER-YOU START AGAIN AT THE START")
        room1()
    if direction.lower() == "r":
        print("as you run you realise she was deffinetly not human")
        print("but as you run the floorboards break beneath you and you fall into the medical ward")
        print("you notice that you could clim back up to the corridor but there is also a door u could enter")
        print("c: climb back up")
        print("d: go through the door")


    direction = input("Direction ")
    if direction.lower() == "c":
            print("as you climb back up you realise the zombie girl heard you and is waiting to kill you")
            print("she stabs you with her long sharp claws and pushed you back down the hole")
            print("you slowly bleed to death")
            print("GAME OVER-YOU START AGAIN AT THE START")
            room1()
    if direction.lower() == "d":
        print("you open the door and it creeps extremly loudly")
        print("and you notice there is blood smered all over the walls")
        print("you realise that you are in the morgue and the only way out is through the corridor at the end there is a door")
        print("but the dead wont stay dead for long")
        print("you have two choices")
        print("s: sprint down the corridor and hope they dont wake up before you reach the end")
        print("q: creep down the corridor slowly but quitely so they might not notice you")

    direction = input("Direction ")
    if direction.lower() == "s":
        print("you run as fast as you can but its too loud and the dead wake up")
        print("your spriting in and out of the way of the zombies and your almost at the door")
        print("the door is in reach but just as you go to grab it the zombies rip you back towards them and devour your flesh")
        print("GAME OVER-YOU START AGAIN AT THE START")
        room1()
    if direction.lower() == "q":
        print("you slowly but surely make your way to the door")
        print("since your so quiet the zombies dont even realise your there")
        print("you manage to get to the door")
        print("as you open it you feel the fresh air on your face")
        print("you made it to the halfway point but theres still alot to go")
        print("PART 2")
        print(".")
        print(".")
        print(".")
        print("the gate is locked so u need to make ur way to the controll tower")
        print("you enter the control tower and the elevator is still opperational")
        print("although you could still take the stairs")
        print("s: take the stairs up 20 floors")
        print("e: take the elavator straight up to 20 floors")

    direction = input("Direction ")
    if direction.lower() == "e":
        print("the elevator slowly goes up")
        print("you can hear a straining noise in the cables")
        print("you are just about to reach the top when the cable snaps and uou fall to your death")
        print("GAME OVER-YOU START AGAIN AT THE START")
        room1()
    if direction.lower() == "s":
        print("you slowly make progress to the top")
        print("before you reach the top you notice there is a door that labels SECRET")
        print("you could enter the secret room or you could keep going")
        print("e:enter the secret room")
        print("k:keep going up the staircase")

    direction = input("Direction ")
    if direction.lower() == "e":
        print("as you enter you stand on something and you hear a click")
        print("to your horror you look down and see a land mine")
        print("you say your last words then take your foor off...it explodes")
        print("GAME OVER-YOU START AGAIN AT THE START")
        room1()
    if direction.lower() == "k":
        print("as you keep going up the stairs you reach the 20th floor")
        print("you enter the top of the control tower but your not alone")
        print("you notice a mad scientist in the corner so you try and talk to him")
        print("hi there are you freindly-you")
        print("WHAT THE F*** DO U WANT-scientist")
        print("as you look down you notice there are needles and lines of cocain in front of him")
        print("hey im just here to investigate whats really going on here and ive figured it out.... you were creating a zombie army out of the insane-you")
        print("YOU F****** BET WE WERE BUT AS SOON AS WE TRIED LETTING THEM OUT THERE CAGES IT ALL TURNED TO S***-scientist")
        print("calm down man its not the end of the world-you")
        print("but dont you realise once we open the gate the alarm will wake them all up and they will go and infect the world-scientist")
        print("..... its the end of the world for us-scientist")
        print("well what other options do we have-you")
        print("we have two options-scienist")
        print("option 1- theres a nuclear warhead burried beneath the base which only has a small blast radius which would destroy all zombies which is fixing our mess-scientist")                                                             
        print("but that would incenerate both of us-you")
        print("hey man its two lives against 7 billion theres no comparrison-scientist")
        print("yeah...i know-you")
        print("option 2- we open the gate and run as fast as we can and hope we escape without being ripped apart from the zombie horde-scientist")
        print("i dont know man its a pretty risky decision-you")
        print("its all down to you man...-scientist")
        print("op1: nuke the insane asylum killing both of you but also all the zombies")
        print("op2: open the gate and run as fast as you can but this will set off the alarm sending thousands of zombies towards you")

    direction = input("Direction ")
    if direction.lower() == "op1":
        print("you decide to nuke the faccilty killing all the zombies but also yourself")
        print("you leave a message for all your family members and say your final goodbyes")
        print("thank you-scientist")
        print("you press the button and watch the countdown go from 10 to 1")
        print("you close your eyes and wait for it")
        print("the fire incinerates you and the scientist but it also kills all of the zombies too")
        print("you may have died but you just saved the wordl")
        print("you are a hero...")
        print("CONGRATULATIONS YOU SAVED THE HUMAN RACE")
    if direction.lower() == "op2":
        print("you run down the stairs as fast as you can")
        print("but there was too many of them and they could sense you")
        print("they grab on to you and devour you slowly while the scientist shouts himself to avoid the pain")
        print("its all over...humanity dosent stand a chance")
        print("GAME OVER-YOU LOST")
    if direction.lower() == "session":
        print("F*** THE HUMAN RACE GIMME SOME OF THAT COCAINNNNNN")
        print("you start doing drugs and partying for your last minutes on earth")
        print("congrats ya mad cokehead you found the secret ending ;)")
        print("""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;.   `.'@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.   `    .'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@, ` `.;+', ```'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.  ,@@@@@@@@+   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,  #@@@@@@@@@@'  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+` @@@@@@@@@@@@#``.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@` @@@@@@@@@@@@@@, `@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;``@@@@@@@@@@@@@@@` '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  #@@@@@@@@@@@@@@@# ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#  @@@@@@@@@@@@@@@@@, '@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# .@@@@@@@@@@@@@@@@@+``@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# .@@#++@@@@@@@@@@@@: `;@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ `@@   ,@@@@@@@@@@@ ` `;@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @+    @@@@@@@@@@@ ` ` .'@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@#++#@@@@@@@@@@, @# +: :@@@@@@@@@@''':`  .'@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@##;.`     `,+@@@@@@@' @@ :#``@@@@@@@@@@@@@@#',` :#@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@'.            ,@@@@@@+ @@ `,  @@@@@@@@@@@@@@@@@#`  :@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@+`  :#@:    .@; `.@@@@@; @@#`  .@@@@@@@@@@@@@@@@@@@,` .@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@' ` ;@@. `   `@@+. .@@@#` @@@#++@@@@@@@@@@@@@@@@@@@@#   #@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@# ``@@.   ,'. `.@#@` +@#. `@@@@@@@@@@@@@@@@@@@@@@@@@@#@: #@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@.  #@`` '#@#@;  ;@@'  ;.` #@@@@#@@@@@@@@@@@@@@@@@@@@@@#  @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@#  +@. `@#@##@@,``@@@ `   '@@@@;+@@@@@@@@@@@@@@@@@@@@@@: '@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@+  @' `##@'  +##` '@@    +@@#@, ,@@@@@@@@@@@@@@@@@@@@@@  +@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@, ,@' ,#@'    @@. `@# ` '@@@@: `#@@@@@@@@@#++;;:,.`..`   :#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@. +@' ,##`  . `@.  @'  ;@@@@@  +@#@@@@@@@@'  `          `  .+@@@@@@@@@@@@@@@
@@@@@@@@@@@, #@'`,@@   @  @.  +  .@@@@@, `@@@@@@@@@@@+`      ``.:+'.`  ` +@@@@@@@@@@@@@
@@@@@@@@@@@' #@'  +@, :# `@``` ``#@@@@@  +@@@@@@@@@@@;   ``:+@@+;:,::'',  '@@@@@@@@@@@@
@@@@@@@@@@@@`:@'  .@#@@:``@`` ` '@@@@@@  @@@@@@@@@@@@   .#@#'` ``     `#'` @@@@@@@@@@@@
@@@@@@@@@@@@ .@@.` :@@'  ;@`   `@@@@@@'``@@@@@@@@@@# ``+@@;``  ,;;;:   `:  @@@@@@@@@@@@
@@@@@@@@@@@@  @@@ `  ` ` @@    #@@@@@@.  @@@@@@@@@@.` +##,  `,##@@@@+   `  @@@@@@@@@@@@
@@@@@@@@@@@@. +@@'  ``  ;@+   .@@@@@@@,``@@@@@@@@#.  '@#.` ;@@@@@@@@@#.`   @@@@@@@@@@@@
@@@@@@@@@@@@: ,@@@;   `'@@,   +@@@@@@@. .@@@@@@@@.  .@#```'@@@@@#+@@@@+    @@@@@@@@@@@@
@@@@@@@@@@@@' `#@@@@'#@#@'    @@@@@@@@. .@@@@@@@;  `#@` .@@@@@@@: @@@@@.  '@@@@@@@@@@@@
@@@@@@@@@@@@@ `.@@@@@@@@,    `@@@@@@@@. ,@@@@@@#   #@;  @@@@@@@: .@@@@@``'@@@@@@@@@@@@@
@@@@@@@@@@@@@` ``:#':.`     `,@@@@@@@@. ,@@@@@@.  ;@@ `+@@@@@@@` ;@@@@@` @@@@@@@@@@@@@@
@@@@@@@@@@@@@+     `         '@@@@@@@@, :@@@@@,  '@@,`,@@@@@@@'  @@@@@@ :@@@@@@@@@@@@@@
@@@@@@@@@@@@@@;           `  ,@@@@@@@@, ;@@@@, `+@#+``@@@@@@@@, ,@@@@@: @#@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@,      .`    `@@@@@@@@. +@@@. `@@@@,`:@@@@@@@#  #@@@#@`:@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@`     @@@@@@@@. #@@, ;@@@@# `@@@@@@@@' :@@@@#: #@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@'      ;@@@@@@@. ##@@@@@@@@:`;@@@@@@@@``+@@@@@`:@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@.` '   `@@@@@@@: .@@@@@@@@@ .@@@@@@@@@ ,@@@@@: #@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@'   + `` #@@@@@@+` @@@@@@@@. #@@@@@@@@, '@@@@@ :@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@` `:'   `:@@@@@@@  @@@@@@@+`,@@@@@@@@@` @#@@@: #@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@'   @```  `@@@@@@@  #@@@@@@, @@@@@@@@@+`+@@@@# '@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@.  ,@`..```@@@@@@@  :@@@@#;`;@@@@@@@@@, @@@@@.`@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#   +@ +#`  +@@@@@@`` @@@@# `##@@@@@@@# '@@@@' +@#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@+   @# +@'  ,@@@@@@;  #@@@` ;@@@@@@@@@; @@@@@`:@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@. `:@. @#@```@@@@@@@` `@+`` @@@@@@@@@+ :@@@@,`@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@  `;@``@@@; `@@@@@@@  ```  '@@@@@@@@@,`+#@@'`+@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@   @@ ,@@@#  '@@@@@@#  `  .@@@@@@@@@+ .@@@@`:@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@  `@# ,@@@@  ,@@@@@@@'   :@@@@@@@@@@` +@#@;`+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@+  .@+ ,@@@@   #@@@@@@@@#@@@@@@@@@@@` :@@@@ ;@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@;  .@; ,@@@@`` '@@@@@@@@@@@@@@@@@@@,  +@#@,`@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@.  .@,  +@@+   `@@@@@@@@@@@@@@@@@@'  `@@@# ,@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@   .@.   `  ` ``#@@@@@@@@@@@@@@@@@`  +@@@` ;@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@`  .@;  `  ```  ;@@@@@@@@@@@@@@@@. ``@@@'  ,#@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@ ` `+#,,`,;#@#`  #@@@@@@@@@@@@@@:   '@@@:` `   ,+@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@    `#@@@@##+`  `.@@@@@@@@@@@@@#  ` @@@@'````    +@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@`     ,'``     `  ,@@@@@@@@@@@' `  `@@@@@@@@@@;. .@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@`  `         `'``  .#@@@@@@@#, `    ,@@@@@@@@#@@  @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@+        `  ;@#@,    ` ````  `    ` ` ,::;;;;::. :@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@+       `;@@@@@@@;   `` ```  `,'@@'`  `  `    `:@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#+';;;+@#@@@@@#@@@';;;:`,;'@@@@@@@@@##''';;;'#@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
        
              
        
        




    
    
    


    

    









# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()
    
