let insertion_sort int_list = 
    let rec pour a_list container =
        match a_list with 
        | head :: tail -> pour tail (head :: container)
        | [] -> container in
    let rec insert a_list key =
        match a_list with
        | head :: tail -> 
            if head <= key then key :: a_list
            else head :: (insert tail key)
        | [] -> key :: [] in
    let rec iterate (loop_invariant, todo) =
        match todo with
        | head :: tail ->
            let inserted = insert loop_invariant head in
            iterate (inserted, tail)
        | [] -> loop_invariant in
    match int_list with
    | head :: tail -> pour (iterate (head :: [], tail)) []
    | [] -> []

let rec print_list a_list =
    match a_list with
    | head :: tail ->
        print_int head;
        print_endline "";
        print_list tail
    | [] -> ()

let my_list = [14; 34; 234; 5; 67; 23; 12; 67; 465; 12; 13; 56; 512; 12; 23; 4; 5; 768; 2]

let _ = print_list (insertion_sort my_list)

