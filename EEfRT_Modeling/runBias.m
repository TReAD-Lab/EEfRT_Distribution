function fit = runBias(a)
global data SampleTrials


nTrials = length(data);
if nTrials > 50 
    nTrials = 50;   %Change this if you want to include more than 50 trials 
end 
 
trialfit = 1;
partialfit = 0;
fit=0;
SampleTrials = 0; 

for trialnum = 1:nTrials
  rt = data(trialnum,2); 
  stimchoice = data(trialnum,1);   %what they chose 
 if rt > 0   %if they made a choice 
   SampleTrials = SampleTrials + 1; 
   pr1=a;
   pr2=1-a;

   if stimchoice==0
      trialfit(trialnum) = pr1;
   elseif stimchoice==1
      trialfit(trialnum) = pr2;
   end
 
   EVMatrix(trialnum,:)=[trialnum stimchoice pr1 pr2];  
   
    partialfit=partialfit + log(trialfit(trialnum));
    fit = -1*partialfit;
    end 
   
end 
fit = -1*partialfit;
