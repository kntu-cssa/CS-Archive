function roots = quadraticRoots(a, b, c)
discriminant = b^2 - 4*a*c;

if discriminant > 0
    root1 = (-b + sqrt(discriminant)) / (2*a);
    root2 = (-b - sqrt(discriminant)) / (2*a);
    roots = [root1, root2];
elseif discriminant == 0
    root = -b / (2*a);
    roots = root;
else
    real_part = -b / (2*a);
    imaginary_part = sqrt(abs(discriminant)) / (2*a);
    root1 = complex(real_part, imaginary_part);
    root2 = complex(real_part, -imaginary_part);
    roots = [root1, root2];
end

end