function [payment] = paymentCalc(allData)

count = 1;

if length(allData(:,1)) > 6
    for x = 6:length(allData)
        %if trial was a win trial
        if allData(x,6) ~= 'l'
            %if trial was completed
            if allData(x,5) == 1 
                %if subject chose harder task
                if allData(x,1) == 1
                    payMatrix(count) = allData(x,7);
                    count = count+1;
                %if subject chose easier task
                else 
                    payMatrix(count) = 1;
                    count = count+1;
                end
            end
        end
    end
else
    reward = 0;
end


if count > 1
    payMatrix = payMatrix';
    reward = 0;
    count2 = 0;
    while count2 < 2
        t = round(rand(1)*10);
        if t ~= 0
            if t < length(payMatrix)
                reward = reward + payMatrix(t);
                count2 = count2+1;
            end
        end
    end
else
    reward = 0;
end
payment = reward;

                