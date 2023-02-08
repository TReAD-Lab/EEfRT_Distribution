start = GetSecs;
timeSecs = KbWait;
[keyDown, secs, keyCode] = KbCheck;
stop = GetSecs;
rt_catch(nbtrial_catch) = stop - start;
         
success = 0;
while success == 0
    pressed = 0;
    while pressed == 0
        [pressed, secs, kbData] = KbCheck;
    end
    for i = 1:length(keysWanted)
        if kbData(keysWanted(i)) == 1
            success = 1;
            keyPressed = keysWanted(i);
            break;
        end
    end
end