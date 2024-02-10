from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0 
left_turns_made = 0 
right_turns_made = 0

while True:
    print(state, )
    if state == 0:
        mycontroller.drive_forwards()
        if mycontroller.left_odom.get_count() >= 2000 and mycontroller.right_odom.get_count() >= 2000 and right_turns_made == 0 and left_turns_made == 0:
            state = 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()
        if mycontroller.left_odom.get_count() >= 1000 and mycontroller.right_odom.get_count() >= 1000 and right_turns_made == 1 and left_turns_made == 0:
            state = 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()
        if mycontroller.left_odom.get_count() >= 1000 and mycontroller.right_odom.get_count() >= 1000 and right_turns_made == 2 and left_turns_made == 0:
            state = 2
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()
        if mycontroller.left_odom.get_count() >= 1000 and mycontroller.right_odom.get_count() >= 1000 and right_turns_made == 2 and left_turns_made == 1:
            state = 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()
        if mycontroller.left_odom.get_count() >= 1000 and mycontroller.right_odom.get_count() >= 1000 and right_turns_made == 3 and left_turns_made == 1:
            state = 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()
        if mycontroller.left_odom.get_count() >= 2000 and mycontroller.right_odom.get_count() >= 2000 and right_turns_made == 4 and left_turns_made == 1:
            state = 3
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()


  

    #turning state
    elif state == 1:
        mycontroller.raft.led_on()
        mycontroller.right_turn()
        turns_made += 1
        state = 0

    elif state == 2:
        mycontroller.left_turn()
        mycontroller.raft.led_on()
        turns_made += 1
        state = 0
        
    elif state == 3:
        mycontroller.stop()
    




