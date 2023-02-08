function [selection yes reactionTime] = taskSelect(window, dexterity, rewardLarge, cueCardColor, winSelect, rewardSmall)




cueCardMatrix = zeros(200,400,3); %Contains the cuecard matrix information

switch(winSelect) %Based on 'w' or 'l' in the run data file, we return whether or not the win will be given or not
    case 'w'
        yes = 1;
    otherwise
        yes = 0;
end



switch(cueCardColor) %Based on 'r', 'y' or 'b' we select the matrix color for the cue card
    case 'r' %Red...
        Prob = ' 88%';
    case 'y' %Yellow
        Prob = ' 50%';
    otherwise %Blue...
        Prob = ' 12%';
end
        
% button setup
KbName('UnifyKeyNames');

if dexterity == 'r'  
    HARD  = KbName('s');
    EASY = KbName('l');
    showKey = 's';
elseif dexterity == 'l'
    HARD  = KbName('l');
    EASY = KbName('s');
    showKey = 'l';
end


if dexterity == 'r' 
    Screen(window,'Flip');
    Screen('DrawText', window, strcat('The Easy Task is worth: $', num2str(rewardSmall)),350,200); 
    Screen('DrawText', window, strcat('The Hard task is worth: $', num2str(rewardLarge)),350,300);
    Screen('DrawText', window, strcat('The Probability of winning is:', Prob),350,400);
    Screen(window,'Flip');
else
    Screen(window,'Flip');
    Screen('DrawText', window, strcat('The Easy Task is worth: $', num2str(rewardSmall)),350,200);
    Screen('DrawText', window, strcat('The Hard task is worth: $', num2str(rewardLarge)),350,300); 
    Screen('DrawText', window, strcat('The Probability of winning: is', Prob),350,400);
    Screen(window,'Flip');
end
reactionTime = 0;
j = [1 2];
j = Shuffle(j);
if j(1) == 1
    selection = 'e';
else
    selection = 'h';
end
if dexterity == 'r'
    timeDelta1 = 5;
    startTime1 = GetSecs;
    currentTime1 = GetSecs;
    while currentTime1 < (startTime1+timeDelta1)%While the time has not yet expired...
         [pressed, secs, kbData] = KbCheck;
         if (pressed == 1) 
             if find(kbData) == HARD
                 selection = 'h';
                 reactionTime = GetSecs - startTime1; %Output the reaction time if pressed
                 break;
             else
                 if find(kbData) == EASY
                     selection = 'e';
                     reactionTime = GetSecs - startTime1; %Output the reaction time if pressed
                      break;
                 end 
             end
         end
         currentTime1 = GetSecs;
    end
else
    timeDelta1 = 5;
    startTime1 = GetSecs;
    currentTime1 = GetSecs;
    while currentTime1 < (startTime1+timeDelta1)%While the time has not yet expired...
         [pressed, secs, kbData] = KbCheck;
        if (pressed == 1) 
             if find(kbData) == HARD
                 selection = 'h';
                 reactionTime = GetSecs - startTime1; %Output the reaction time if pressed
                 break
             else
                 if find(kbData) == EASY
                     selection = 'e';
                     reactionTime = GetSecs - startTime1; %Output the reaction time if pressed
                     break
                 end 
             end
             
         end
         currentTime1 = GetSecs;
    end     
end
Screen(window,'Flip');
