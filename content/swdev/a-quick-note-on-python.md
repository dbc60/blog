---
title: A Quick Note on Python
date: 2016-01-04
2016: ["01"]
---

I saw an amusing Python tutorial.
<!--more-->

I have been meaning to learn Python for a while now. While searching for other things, I came across an amusingly titled video on YouTube, [Python Programming: Learn Python in One Video](https://www.youtube.com/watch?v=N4mEzFDjqtA&list=PLGLfVvz_LVvSX7fVd4OUFp_ODd86H0ZIY&index=2), by [Derek Banas](https://www.youtube.com/user/derekbanas).

I had no illusions it was going to cover the language in any depth. Still, it is only about 45 minutes long, so I decided to take a look. It actually hit a lot of highlights and was a nice overview of the language.

For example, it introduces the built-in operators and data types. It goes over the `for` and `while` loops. It also covers several other programming concepts. If you've never seen Python before, this video is worth a look.

I recently picked up a copy of Steven Skiena's "Programming Challenges" and started going through the problems. To see if I learned anything from the video, I tried coding the first puzzle, the [`3n+1` problem](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=36). The link is to the puzzle on the [UVa Online Judge](https://uva.onlinejudge.org/), where one can submit code in C, C++, Java or Pascal. Sadly, they don't support Python. Nevertheless, here's my version in Python:

```python
import sys

# Execute: "python p100.py < data" where 'data' is the input file, two integers per line.
def cycle_length(n):
    result = 1

    while (n != 1):
        if (n % 2):
            # n is odd, so multiply by 3 and add 1
            n = 3 * n + 1
        else:
            # n is even, so divide by 2
            n /= 2

        result += 1

    return result

# Each line of input consists of two integers
def main():
    for line in sys.stdin:
        input_list = line.split()
        input_list = list(map(int, input_list))

        # reset the max cycle length for each line of input
        max_cycle_length = 0

        # Make a copy of the original list for output
        original_list = list(input_list)
        if input_list[0] > input_list[1]:
            x = input_list[0]
            input_list[0] = input_list[1]
            input_list[1] = x

        for n in range(input_list[0], input_list[1]+1):
            length = cycle_length(n)
            if length > max_cycle_length:
                max_cycle_length = length

        print("%d %d %d" % (original_list[0], original_list[1], max_cycle_length))

if __name__ == "__main__":
    main()
```

I think the only thing here that wasn't covered in the video is reading from stdin.
