b = [1, 2, 3, 4, 5, 6, 7, 8]

mid xs = last $ take (succ $ div (length xs) 2) xs

-- same result
[ x | x <- [1..1000], mod x 6 == 2]
filter (\x -> mod x 6 == 2) [1..1000]

[if even x then "even!" else "odd!" | x <- [1..100], x `mod` 3 == 0]

[ x + y | x <- [1, 2, 3], y <- [4, 5, 6], x * y > 4 ]

triangles = [ (a, b, c) | c <- [1..10], b <- [1..c], a <- [1..b], a + b + c == 24, a^2 + b^2 == c^2 ]
