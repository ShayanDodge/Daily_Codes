function [y] = blended(x,pow)
% UNTITLED Summary of this function goes here
% Detailed explanation goes here
y = zeros(1,length(x));
for i=1:length(x)
    if (x(i) <= 0)
        y(i) = (x(i)).^pow;
    elseif (x(i) > 0 && x(i) <= 1)
        y(i) = x(i);
    else
        y(i) = exp((x(i) .^ pow) -1);
    end
end