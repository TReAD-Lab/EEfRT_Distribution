function resultLog = taskMain(window, numberOfRuns, cueCard, winSelect, rewardSmall, rewardLarge, ... 
    dexterity, resX, resY, resultLogCount, resultLog, maxTime,pracTrial,subjectID,sessionID)
if pracTrial == 'y'
    i = 1;
else
    i = 7; 
end
currentTime = 0;
tic;
while i<numberOfRuns && currentTime<maxTime %For the size of the number of cue cards...
        if cueCard(i) ~= '0' %If a break is not signified, run the task.
        calibrationImage = imread('STIM/fixation.bmp','bmp');
        Screen(window,'FillRect',0);
        Screen(window, 'Flip');
        Screen(window,'PutImage',calibrationImage); %Display fixation
        Screen(window, 'Flip');
        pause(1); %Calibration screen finishes after displaying for 1.5 seconds
        Screen(window,'FillRect',0);
        Screen(window, 'Flip');            

        disp(strcat('Pair: ',cueCard(i),' ',winSelect(i)));
        
        %Write win/lose to log structure...
        resultLog(6,resultLogCount) = winSelect(i);
        resultLog(7,resultLogCount) = rewardLarge(i);
        
        [selection yes reactionTime] = taskSelect(window, dexterity, rewardLarge(i), cueCard(i), winSelect(i), rewardSmall);%Cue card selection; Determines here if reward will be given or not.
        
        %Prompt for READY
        Screen(window,'FillRect',0);
        Screen(window, 'Flip');
        readyScreen = imread('STIM/readyscreen.bmp', 'bmp');
        Screen(window, 'Flip');
        Screen(window, 'PutImage', readyScreen);
        Screen(window, 'Flip');
        pause(1); %Delay
        
        %Recode probability level
        switch cueCard(i)
            case 'b'  
                resultLog(8,resultLogCount) = .12;
            case 'y'
                resultLog(8,resultLogCount) = .50;
            case 'r' 
                resultLog(8,resultLogCount) = .88;
        end
        
       
        [completionStatus numberOfPresses goalReachedCount completionTime] = taskRun(window, dexterity, selection, resX, resY); %Task performance here.
    
        if completionStatus == 1 %If task completed successfully, compute reward. 
            switch (selection)
                case 'e'
                    resultLog(1,resultLogCount) = 0;%easy vs hard
                case 'h'
                    resultLog(1,resultLogCount) = 1;%easy vs hard
            end
        else %If task did not complete successfully, set the log parameters accordingly. Do not update score.
            switch (selection)
                case 'e'
                    resultLog(1,resultLogCount) = 0;%easy vs hard
                case 'h'
                    resultLog(1,resultLogCount) = 1;%easy vs hard                    
            end
        end

        %Write other info to result log received.
        resultLog(2,resultLogCount) = reactionTime;
        resultLog(4,resultLogCount) = numberOfPresses;
        resultLog(5,resultLogCount) = completionStatus; 
        resultLog(3,resultLogCount) = goalReachedCount; 
        resultLog(9,resultLogCount) = completionTime;
        resultLog(10,resultLogCount) = goalReachedCount/completionTime; 
        
        %Increment the log structure index.
        resultLogCount = resultLogCount + 1;
        
        %"Anticipatory delay screen."
        Screen(window,'FillRect',0);
        Screen(window, 'Flip');
        pause(2.0); %Delay 2 seconds...
        
        %Display winnings
       
        if completionStatus == 1
            Screen(window,'FillRect',0);
            Screen(window, 'Flip');
            Screen(window, 'DrawText', 'You completed the task!', ceil(resX/2)-60, ceil(resY/2), 255);
            Screen(window, 'Flip');
            pause(1.0);
            if selection == 'e'
                displayAmount = num2str(rewardSmall * yes); %multiply winnings times win/lose
                t = num2str(3 * yes);
            else
                displayAmount = num2str(rewardLarge(i)*yes);%multiply winnings by win/lose
                t = num2str(7 * yes);
            end
            Screen(window,'FillRect',0);
            Screen(window, 'Flip');
                    
            if t ~= '0'
                Screen(window, 'DrawText', strcat('You won: $',displayAmount), ceil(resX/2)-60, ceil(resY/2)+40, 255);
            else
                Screen(window, 'DrawText', 'No money this trial.', ceil(resX/2)-60, ceil(resY/2)+40, 255);
            end
            Screen(window, 'Flip');
            pause(2.0);
        else
            Screen(window,'FillRect',0);
            Screen(window, 'Flip');
            Screen(window, 'DrawText', 'You failed to complete the task.', ceil(resX/2)-60, ceil(resY/2), 255);
            Screen(window, 'Flip');
            pause(2.0);
        end
        currentTime = toc;
    else
        Screen(window,'FillRect',0);
        Screen(window, 'Flip');
        if i == 1
            Screen(window, 'Flip');
            Screen(window, 'DrawText', 'Loading Task...', ceil(resX/2)-60, ceil(resY/2), 255);
            Screen(window, 'Flip');
            currentTime = 0;
            tic;
            pause(1.0);
        else
            runBreak(window, resX, resY);
            Screen(window, 'Flip');
            KbWait;
            tic;
        end
        end
        i=i+1;
        
        %Write to logfile.
        filewriter(resultLog,subjectID,sessionID);
 end
resultLog;