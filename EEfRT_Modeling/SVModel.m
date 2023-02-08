clear
clear global

addpath(genpath('/Users/jcrobi4/Documents/EEfRT_Modeling/EEfRT_Modeling_Share')); 
dataDir = '/Users/jcrobi4/Documents/EEfRT_Modeling/EEfRT_Modeling_Share/Data';
outputDir = '/Users/jcrobi4/Documents/EEfRT_Modeling/EEfRT_Modeling_Share/Output';

%list filenames 
%filenames_all = {'file1', 'file2', 'file3'}; 
filenames_all = {''}; 
cd(dataDir);


global data SampleTrials

subdone=0;
Nsubjects = length(filenames_all); 
nIt = 100; 
nHeader = 5; %number of practice and header trials (lines to skip) 


for s = 1:Nsubjects

%%Read in the data. I only include the choice, reward, RT, and probability. 
%%Some versions of the EEfRT do not include probability in the data file, and it is instead 
%%listed in the run script. If you use this method, verify that the
%%probabilities match up to your files. This section can be replaced with
%%other syntax to read in your data if you typically do it another way.
    fname = filenames_all{s};
    rawData = read_mixed_csv(fname,'\t'); 
    if str2double(rawData(6,7)) == 3.04 
        nHeader = 5; 
    else 
        nHeader = 1; 
    end
    data = []; 
    [row1, col] = size(rawData);  
    getLength = row1-nHeader; %4 for practice and 1 for header length 
        
        
        %you only need this if you use read mixed csv to read your data
  for i = 1:getLength
    data(i,1) = str2double(rawData(i+nHeader,1)); %choice 0 or 1 
    data(i,2) = str2double(rawData(i+nHeader,2)); %RT (to exclude trials where no choice was made) 
    data(i,7) = str2double(rawData(i+nHeader,7)); %reward for difficult 
    data(i,8) = str2double(rawData(i+nHeader,8)); %probability 0 to 1 
    %data(i,5) = str2double(rawData(i+nHeader,5)); %completion
  end
  
   firstreward = data(1,7);
   if firstreward == 3.04 
   else
       fname
       disp('first trial is not 3.04')
       firstreward
       keyboard
   end    
    
    
clear Fit
Fit.Nparms = 3;
Fit.LB = [0 0 0];   %parameter bounds - minimum 
Fit.UB = [10 10 100];    %parameter bounds - maximum 
SampleTrials = 0; 
fprintf('Fitting subject %d out of %d...\n',s,Nsubjects)
   
    for iter = 1:nIt   % run 50 times from random initial conditions, to get best fit
        fprintf('Iteration %d...\n',iter)
        
        Fit.init(s,iter,:) = rand(1,length(Fit.LB)).*(Fit.UB-Fit.LB)+Fit.LB; % random initialization
       
        [res,lik] = ... 
            fmincon(@(x) run_SVmodel(x(1),x(2),x(3)),...
            squeeze(Fit.init(s,iter,:)),[],[],[],[],Fit.LB,Fit.UB,[],...
            optimset('maxfunevals',10000,'maxiter',4000,'GradObj','off','DerivativeCheck','off','LargeScale','on','Algorithm','active-set'));
        Fit.Result.a(s,iter) = res(1); 
        Fit.Result.h(s,iter) = res(2); 
        Fit.Result.T(s,iter) = res(3); 
        Fit.Result.Lik(s,iter) = lik;
        Fit.Result.Lik;  

    end
    
% find the best fit results for each subject
[a,b] = min(Fit.Result.Lik,[],2);
    Fit.Result.BestFit(s,:) = [s,...
    Fit.Result.a(s,b(s)),... 
    Fit.Result.h(s,b(s)),...
    Fit.Result.T(s,b(s)),...
    Fit.Result.Lik(s,b(s))];
Fit.Result.BestFit;

thisLik =  Fit.Result.Lik(s,b(s));
%calculate BIC. BIC =ln(n)*k-2*ln(L)
%fit value returned from fmincon is negative log likelihood (-ln(L)) 
%n is number of trials, k is number of parameters (3) 
thisBIC = (2*thisLik)+Fit.Nparms*(log(SampleTrials)); 
xlsOutGLCSO = [Fit.Result.BestFit(s,:) SampleTrials thisBIC];
 subdone=subdone+1
 outputMatrix = []; 
 outputMatrix = [xlsOutGLCSO];     
 
 allOutputMatrix(subdone,:) = outputMatrix;
 cd(outputDir); 
 eval(['save ' 'SVOutput_1.txt allOutputMatrix -ascii']);
 %output is s (subnum starting at 1), k, h, t, fit (negative LL), number of
 %trials included, BIC 
end 

  
    
   
    