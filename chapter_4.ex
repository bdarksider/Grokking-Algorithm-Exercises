defmodule ChapterFour do
 
    def sum_list([]) do
        0
    end

    def sum_list([h|t]) do
        h + sum_list(t)
    end

    def count_items([]) do
        0
    end

    def count_items([_|t]) do
        1 + count_items(t)
    end

    def find_max(arr) do
        if length(arr) == 2 do
            [a,b] = arr
            if a > b, do: a, else: b
        end
        sub_max = find_max(tl(arr))
        if hd(arr) > sub_max, do: hd(arr), else: sub_max
    end

end

IO.puts ChapterFour.find_max([1,2,3])