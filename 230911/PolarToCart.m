function [x, y] = PolarToCart(r, theta)
    x = r * cos(theta);
    y = r * sin(theta);
end