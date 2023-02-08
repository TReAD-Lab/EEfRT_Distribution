function [lik] = run_SVmodel_2parameter(a, T)

global data SampleTrials hVal

lik = 0;   % log likelihood
V1 = 0;  % initial values for the 2 stimuli
V2 = 0;
SampleTrials = 0; 
h = hVal; 

nTrials = length(data);

if nTrials > 50 
    nTrials = 50;    %We only use the first 50 trials, change this if you want to use all the trials 
end 

for t = 1:nTrials  % t = trial number
     rt = data(t,2); 
     stimchoice = data(t,1);  
   if rt > 0   %Do not fit model to data where they did not actually make a response-- check to see how this is coded in your version 
      SampleTrials = SampleTrials + 1;
     %the objective reward for each option 
        Sr2 = data(t, 7);
        e1 = .3; %if you want to change the level of effort, do so here 
        e2 = 1;
        prob = data(t, 8); %your probs 
        %prob = problist(t);  %if probability is not included in your
        %datafile, include a list of the probabilities so that you can
        %index them for each trial 
       
        V1 = (1*(prob^h))-(a*e1); %in this version the low reward was always $1 
        V2 = (Sr2*(prob^h))-(a*e2); 
    
        %calculating log likelihood, does not use logsumexp 
%      if stimchoice == 0 
%             lik = lik + log(exp(V1*T)/(exp(V1*T) + exp(V2*T)));
%      elseif stimchoice == 1 
%             lik = lik + log(exp(V2*T)/(exp(V1*T) + exp(V2*T))); 
%      end 
     

%Option 2 for calculating log liklihood, uses logsumexp.m 
    V = [V1 V2]; 
    if stimchoice == 0 
            Vc = V1; 
    elseif stimchoice == 1 
            Vc = V2; 
    end 
    lik = lik + Vc*T - logsumexp(T*V,2); 
        
   end 
end

lik = -lik;  % so we can minimize the function rather than maximize
