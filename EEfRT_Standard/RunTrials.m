%Effort Expenditure for Rewards Task (EEfRT)   
    % Designed, Michael T. Treadway, Ph.D. 
    % Licensed by Emory University
    % Requires PTB 3.0.9 or later and Matlab 2007b or later
    %Provided to non-commercial partners under a GNU public license.
    %This code is provided in the hopes it will be useful. No guarantees or warranties, implied or otherwise. 
     
 
%% environment
% clean up
clear all
fclose('all'); 
sca
clc

% PTB basics
AddPsychJavaPath;
%LoadPsychHID;
PsychJavaTrouble;

%Begin setup here
resX = 1280;
resY = 1024;
Black = [0 0 0];
White = [255 255 255];


%Quit key, ends test during cue card selection.
 prompt = {'Subject number: ','Handedness (l/r):', 'Instructions & Practice Trials (y/n:)', 'Session:'};
 defaults = {'','','',''};
 dlgout = inputdlg(prompt,'',1,defaults);
 subjectID  = dlgout{1};
 dexterity = dlgout{2};
 pracTrial = dlgout{3};
 sessionID = (dlgout{4});

 maxTime = 20; %Specify time to complete the task
 maxTime = maxTime*60;

%Create background rectangle
background = zeros(1000, 700, 3);

%Create a structure for holding experimental results.
resultLog = zeros(10,1); 
resultLogCount = 1; %Maintains the count to index the result log.
[cueCard winSelect rewardLarge] = textread('run1.dat','%c %c %f', 'delimiter', '\n');
rewardSmall = 1.00; 

%Optional code to remove sync tests. Generally not recommended. 
%Screen('Preference','SkipSynctests',1); 

%Specify the window pointer
whichScreen = 0;
window = Screen(whichScreen, 'OpenWindow');

%set fonts
oldTextSize = Screen('TextSize', window, 24);

if pracTrial == 'y'
    for instruct = 1:10 
             Screen('FillRect',window,Black);
             Screen('Flip',window);   
             InstructName = ['Instructions' num2str(instruct) dexterity '.tif'];
             instructScreen = imread(['STIM/' InstructName], 'tif');
             Screen('Flip',window);
             Screen(window,'PutImage',instructScreen);
             Screen('Flip',window);
             pause(1);
             KbWait(-3); 
             %Flushevents; 
    end
    Screen('FillRect',window,Black);
    Screen('Flip',window);   
    DrawFormattedText(window,'Wait for the experimenter.','center','center',255);
    Screen('Flip',window);
    KbWait(-3);
    
    
else
    % makes sure the subject is ready
    Screen('FillRect',window,Black);
    Screen('Flip',window);   
    DrawFormattedText(window,'Press any button when ready to begin.','center','center',255);
    Screen('Flip',window);
    KbWait(-3);
end


%Run task selection here...
numberOfRuns = size(cueCard);
numberOfRuns = numberOfRuns(1);

%call TaskMain



% waits for a second 
DrawFormattedText(window,'The task will begin momentarily.','center','center',255);
Screen('Flip',window);
WaitSecs(1);

%Actual run here:
resultLogMain = taskMain(window, numberOfRuns, cueCard, winSelect, rewardSmall, rewardLarge, ...
    dexterity, resX, resY, resultLogCount, resultLog, maxTime, pracTrial, subjectID, sessionID);

%Write logfile.
filewriter(resultLogMain,subjectID,sessionID);


%Specify Payment
allData = resultLogMain';
earnings = paymentCalc(allData);
fileNameEarnings = ['Earnings_' subjectID '_session' sessionID '.xls'];
dataDir ='DATA';
cd(dataDir);
xlswrite(fileNameEarnings,earnings);
cd ../
Screen(window,'FillRect',0);
Screen(window, 'Flip');
Screen('DrawText', window, 'Task complete. Please get the experimenter.', floor(resX/2)-70,floor(resY/2)+100, 255);
Screen(window, 'Flip');
pause(1)
KbWait;


%Cleanup workspace and window...
cd ../
Screen('CloseAll');
ListenChar(0);
