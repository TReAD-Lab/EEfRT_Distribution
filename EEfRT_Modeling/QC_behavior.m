clear
clear global

%script to summarize basic behaivor in the EEfRT task. 
%note that paths have to be update to reflect paths on local machine and
%filenames need to be listed. only the first 50 trials are analyzed, but
%script can be modified if you want to do something else. practice trials
%are skipped. 
%output is one row per subject with the following column order: 
%1. mean RT when a response was made 
%2. completion proportion for effort tasks 
%3. proportion of timeout trials (i.e. trials when a response was not made) 
%4. proportion of hard effort selections in the 88% probability trials 
%5. proportion of hard effort selections in the 50% probability trials
%6. proportion of hard effort selections in the 12% probability trials
%7. porportion of hard efford selections overall 

addpath(genpath('/Users/jcrobi4/Documents/EEfRT_Modeling/EEfRT_Modeling_Share')); 
dataDir = '/Users/jcrobi4/Documents/EEfRT_Modeling/EEfRT_Modeling_Share/Data';
outputDir = '/Users/jcrobi4/Documents/EEfRT_Modeling/EEfRT_Modeling_Share/Output';

%list filenames 
%filenames_all = {'file1', 'file2', 'file3'}; 
filenames_all = {''}; 


cd(dataDir);
global data 

subdone=0;
Nsubjects = length(filenames_all); 
nHeader = 5; %number of practice and header trials (lines to skip) 
firstReward = 0; 

for s = 1:Nsubjects

%%Read in the data. I only include the choice, reward, RT, and probability. 
%%Some versions of the EEfRT do not include probability in the data file, and it is instead 
%%listed in the run script. If you use this method, verify that the
%%probabilities match up to your files. This section can be replaced with
%%other syntax to read in your data if you typically do it another way.
    fname = filenames_all{s}
    rawData = read_mixed_csv(fname,'\t'); 
    [row1, col] = size(rawData);  
    if str2double(rawData(6,7)) == 3.04 
        nHeader = 5; 
    else 
        nHeader = 1; 
    end

    data = []; 
    getLength = row1-nHeader; %4 for practice and 1 for header length 
    choiceMat = [];     
        %you only need this if you use read mixed csv to read your data
  for i = 1:getLength
    data(i,1) = str2double(rawData(i+nHeader,1)); %choice 0 or 1 
    data(i,2) = str2double(rawData(i+nHeader,2)); %RT (to exclude trials where no choice was made) 
    data(i,7) = str2double(rawData(i+nHeader,7)); %reward for difficult 
    data(i,8) = str2double(rawData(i+nHeader,8)); %probability 0 to 1 
    data(i,5) = str2double(rawData(i+nHeader,5)); %completion
  end
  
   firstreward = data(1,7);  %check to see if the first trial is 3.04 and throw and error if not 
   if firstreward == 3.04 
   else
       fname
       disp('first trial is not 3.04')
       firstreward
       keyboard
   end    
 
  
p12 = [];
p50 = []; 
p88 = []; 
RTlist = []; 
timeouts = 0;   
completes = []; 
   [row, col] = size(data);  
   if row > 50 
       row = 50 %only analyze first 50 trials 
   end 
   for t = 1:row 
       rt = data(t,2); 
       if rt > 0 %only summarize trials where they made a response 
       
       choice = data(t,1); 
       choiceMat = [choiceMat; choice]; 
       RTlist = [RTlist; rt]; 
       if data(t,8) == .12 
           p12 = [p12; choice];
       end 
       if data(t,8) == .50 
           p50 = [p50; choice];
       end 
       if data(t,8) == .88
           p88 = [p88; choice];
       end
       else
           timeouts = timeouts + 1; 
       end 
       completes = [completes; data(t,5)]; 
   end 
   firstReward = data(1,7); 
   timeoutPerc = (timeouts/row); 
   completion = mean(completes); 
   
   output(s,:) = [mean(RTlist) completion timeoutPerc mean(p88) mean(p50) mean(p12) mean(choiceMat)]; 
   cd(outputDir)
   dlmwrite('BehavioralOutput', output); 
end 

  
    
   
    