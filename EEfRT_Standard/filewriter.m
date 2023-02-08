%Columns hold Choice (0 for easy, 1 for hard), reaction time, 
%number of presses, required presses, success (1 for true, 0 for non-complete), 
%win (1 for true, 0 for false), amount won.

function filewriter(inputdata, subjectID, sessionID)
dataDir ='DATA';
cd(dataDir);

[j numberOfEntries] = size(inputdata);

filename = strcat('EEfRT_Data',subjectID, '_Session', sessionID,'.xls');
outfile = fopen(filename, 'wt');
fprintf(outfile, strcat('Choice(1=Hard)   ChoiceRT   RecordedPresses    RequiredPresses  Completed(1=Yes)  WinLose    RM$Hard   Probability     CompletionTime  ButtonPressRate','\n'));

for i = 1:numberOfEntries
    outline = strcat(num2str(inputdata(1,i)), '\t',num2str(inputdata(2,i)), '\t',num2str(inputdata(3,i)), '\t', ...
        num2str(inputdata(4,i)), '\t',num2str(inputdata(5,i)), '\t',inputdata(6,i), '\t', ...
        num2str(inputdata(7,i)), '\t',num2str(inputdata(8,i)), '\t',num2str(inputdata(9,i)), '\t',num2str(inputdata(10,i)), '\n');
    fprintf(outfile, outline, '%s');
end
fclose(outfile);
cd ../
        
