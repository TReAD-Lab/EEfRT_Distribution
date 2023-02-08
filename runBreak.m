function runBreak(window, resX, resY)
Screen(window,'FillRect',0);
Screen(window, 'Flip');
Screen('DrawText', window, 'Practice trials are complete. ',floor(resX/2)-70,floor(resY/2), 255); %Show reminder.
Screen('DrawText', window, 'Press space bar to begin actual trials', floor(resX/2)-70,floor(resY/2)+100, 255);
Screen(window, 'Flip');
KbWait;