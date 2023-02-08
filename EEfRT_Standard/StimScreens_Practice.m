%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% STIMULI CONSTRUCTION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if form_number == 1; 
for j = 1:5
    images{j} = imread(['P' num2str(j) '.jpg'] ,'jpg');
    InstImage = imread(['Inst' subject_run '.jpg'], 'jpg');
    visual_stimulus_screen(j) = Screen(w_screen,'OpenOffscreenWindow',[],visual_stimulus_rect_presentation,[]);
    Screen(visual_stimulus_screen(j),'FillRect',background_color,visual_stimulus_rect_VisStimComb);
    Screen(visual_stimulus_screen(j),'PutImage',images{j},visual_stimulus_rect_VisStim, 'srcCopy');
    Screen(visual_stimulus_screen(j),'PutImage', InstImage, visual_stimulus_rect_VisStim2, 'srcCopy');
end
end

if form_number == 2;
for j = 51:100 
    images{j} = imread([num2str(j) '.jpg'] ,'jpg');
    InstImage = imread(['Inst' subject_run '.jpg'], 'jpg');
    visual_stimulus_screen(j) = Screen(w_screen,'OpenOffscreenWindow',[],visual_stimulus_rect_presentation,[]);
    Screen(visual_stimulus_screen(j),'FillRect',background_color,visual_stimulus_rect_VisStimComb);
    Screen(visual_stimulus_screen(j),'PutImage',images{j},visual_stimulus_rect_VisStim, 'srcCopy');
    Screen(visual_stimulus_screen(j),'PutImage', InstImage, visual_stimulus_rect_VisStim2, 'srcCopy');
end
end

% Create background colored visual stimlus screen with Fixation Square.
visual_stimulus_screen(998) = Screen(w_screen,'OpenOffscreenWindow',[],visual_stimulus_rect_VisStim,[]);
Screen(visual_stimulus_screen(998),'FillRect',background_color,[]);
Screen(visual_stimulus_screen(998),'FillRect',FixSquare_color,CenterRect(visual_stimulus_rect_FixSquare,visual_stimulus_rect_VisStim));

% Create blank screen
visual_stimulus_screen(999) = Screen(w_screen,'OpenOffscreenWindow',[],visual_stimulus_rect_VisStim,[]);
Screen(visual_stimulus_screen(999),'FillRect',background_color,[]);

% Create background colored Text stimlus screen.
visual_stimulus_screen_Textback = Screen(w_screen,'OpenOffscreenWindow',[],w_rect,[]);
Screen(visual_stimulus_screen_Textback,'FillRect',background_color,[]);