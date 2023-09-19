function digitName(digit)

% if digit == 0
%     disp('zero')
% elseif digit == 1
%     disp("one")
% elseif digit == 2
%     disp("two")
% elseif digit == 3
%     disp("three")
% elseif digit == 4
%     disp("four")
% elseif digit == 5
%     disp("five")
% elseif digit == 6
%     disp("six")
% elseif digit == 7
%     disp("seven")
% elseif digit == 8
%     disp("eight")
% elseif digit == 9
%     disp("nine")
% else
%     disp("out of range")
% end

switch digit
    case 1
        disp("one")
    case 2
        disp("two")
    case 3
        disp("three")
    case 4
        disp("four")
    case 5
        disp("five")
    case 6
        disp("six")
    case 7
        disp("seven")
    case 8
        disp("eight")
    case 9
        disp("nine")
    otherwise
        disp("out of range")
end