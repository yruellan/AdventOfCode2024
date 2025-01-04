
type num =
  | N7 | N8 | N9
  | N4 | N5 | N6
  | N1 | N2 | N3
  | N0 | NA

type dir =
  | Up | Down | Left | Right | Append

let to_num s =
  s |> String.to_seq |> List.of_seq |> List.map (fun c -> match c with
    | '7' -> N7 | '8' -> N8 | '9' -> N9
    | '4' -> N4 | '5' -> N5 | '6' -> N6
    | '1' -> N1 | '2' -> N2 | '3' -> N3
    | '0' -> N0 | 'A' -> NA
    | _ -> failwith "Invalid character"
  )

let to_dir s =
  s |> String.to_seq |> List.of_seq |> List.map (fun c -> match c with
    | '^' -> Up | 'v' -> Down | '<' -> Left | '>' -> Right | 'A' -> Append
    | _ -> failwith "Invalid character"
  )


let to_char_list s =
  s |> String.to_seq |> List.of_seq

let num_coords = function
  | N7 -> (0, 0)
  | N8 -> (0, 1)
  | N9 -> (0, 2)
  | N4 -> (1, 0)
  | N5 -> (1, 1)
  | N6 -> (1, 2)
  | N1 -> (2, 0)
  | N2 -> (2, 1)
  | N3 -> (2, 2)
  | N0 -> (3, 1)
  | NA -> (3, 2)
  
let dir_coords = function
  | Up -> (0, 1)
  | Append -> (0, 2)
  | Down -> (1, 1)
  | Left -> (1, 0)
  | Right -> (1, 2)

let num_of_coords x y =
  match x,y with
  | (0, 0) -> N7
  | (0, 1) -> N8
  | (0, 2) -> N9
  | (1, 0) -> N4
  | (1, 1) -> N5
  | (1, 2) -> N6
  | (2, 0) -> N1
  | (2, 1) -> N2
  | (2, 2) -> N3
  | (3, 1) -> N0
  | (3, 2) -> NA
  | _ -> failwith "Invalid coordinates"

let is_valid_num x y =
  match x,y with
  | (0, 0) | (0, 1) | (0, 2) | (1, 0) | (1, 1) | (1, 2) | (2, 0) | (2, 1) | (2, 2) | (3, 1) | (3, 2) -> true
  | _ -> false

let dir_of_coords x y =
  match x,y with
  | (0, 1) -> Up
  | (0, 2) -> Append
  | (1, 1) -> Down
  | (1, 0) -> Left
  | (1, 2) -> Right
  | _ -> failwith "Invalid coordinates"

let is_valid_dir x y =
  match x,y with
  | (0, 1) | (0, 2) | (1, 1) | (1, 0) | (1, 2) -> true
  | _ -> false

let num_to_string s =
  s |> List.map (fun x -> match x with
    | N7 -> '7' | N8 -> '8' | N9 -> '9'
    | N4 -> '4' | N5 -> '5' | N6 -> '6'
    | N1 -> '1' | N2 -> '2' | N3 -> '3'
    | N0 -> '0' | NA -> 'A'
  ) |> List.to_seq |> String.of_seq

let dir_to_string s =
  s |> List.map (fun x -> match x with
    | Up -> '^' | Down -> 'v' | Left -> '<' | Right -> '>' | Append -> 'A'
  ) |> List.to_seq |> String.of_seq

(* Usefull function *)

let sgn = function
  | x when x > 0 -> 1
  | x when x < 0 -> -1
  | _ -> 0

(* Function executing keypad intructions, debug tools  *)

let rec exec_on_dir ?(x=0) ?(y=2) = function
  | [] -> []
  | _ when x < 0 || y < 0 || x >= 2 || y >= 3 ->
    failwith "Position out of bound"
  | _ when x=0 && y=0 ->
    failwith "Invalid position"
  | Append :: seq -> (dir_of_coords x y) :: exec_on_dir ~x ~y seq
  | Up :: seq -> exec_on_dir ~x:(x-1) ~y seq
  | Down :: seq -> exec_on_dir ~x:(x+1) ~y seq
  | Left :: seq -> exec_on_dir ~x ~y:(y-1) seq
  | Right :: seq -> exec_on_dir ~x ~y:(y+1) seq

let rec exec_on_num ?(x=3) ?(y=2) = function
  | [] -> []
  | _ when x < 0 || y < 0 || x >= 4 || y >= 3 ->
    failwith "Position out of bound"
  | _ when x=3 && y=0 ->
    failwith "Invalid position"
  | Append :: seq -> (num_of_coords x y) :: exec_on_num ~x ~y seq
  | Up :: seq -> exec_on_num ~x:(x-1) ~y seq
  | Down :: seq -> exec_on_num ~x:(x+1) ~y seq
  | Left :: seq -> exec_on_num ~x ~y:(y-1) seq
  | Right :: seq -> exec_on_num ~x ~y:(y+1) seq

(* Encoding for dir keypad *)

let rec get_move_dir x y obj_x obj_y =
  if x=obj_x && y=obj_y then [[Append]] else 
  if not (is_valid_dir x y) then [] else

    let dx = obj_x - x in
    let dy = obj_y - y in
    let cx = if dx > 0 then Down else Up in
    let cy = if dy > 0 then Right else Left in
    let res_x = if dx=0
      then []
      else get_move_dir (x+sgn dx) y obj_x obj_y in
    let res_y = if dy=0
      then [] 
      else get_move_dir x (y+sgn dy) obj_x obj_y in
  
    List.map (fun x -> cx :: x) res_x
    @ List.map (fun x -> cy :: x) res_y

let rec encode_dir ?(last=Append)= function
| [] -> []
| a :: seq ->
  let lastx, lasty = dir_coords last in
  let ax, ay = dir_coords a in 
  get_move_dir lastx lasty ax ay :: encode_dir ~last:a seq

(* Encoding num keypad *)

let rec get_move_num x y obj_x obj_y =
  if x=obj_x && y=obj_y then [[Append]] else 
  if not (is_valid_num x y) then [] else

    let dx = obj_x - x in
    let dy = obj_y - y in
    let cx = if dx > 0 then Down else Up in
    let cy = if dy > 0 then Right else Left in
    let res_x = if dx=0
      then []
      else get_move_num (x+sgn dx) y obj_x obj_y in
    let res_y = if dy=0
      then [] 
      else get_move_num x (y+sgn dy) obj_x obj_y in
  
    List.map (fun x -> cx :: x) res_x
    @ List.map (fun x -> cy :: x) res_y

let rec encode_num ?(last=NA)= function
  | [] -> []
  | a :: seq ->
    let lastx, lasty = num_coords last in
    let ax, ay = num_coords a in 
    get_move_num lastx lasty ax ay :: encode_num ~last:a seq
    

(* New encode methode *)

type sequence = dir list

let cache = Hashtbl.create 1_000 

let rec encode n seq =
  if n = 0 then List.length seq else

  match Hashtbl.find_opt cache (n,seq) with
  | Some x -> x
  | None ->
  
    (* Encode each sub-sequence *)
    (* Apply recursivly *)
    (* Find the smallest subseq encoding size*)
    (* Call the sum of all subseq encoding size *)
    let res = 
      encode_dir seq
      |> List.map (fun l -> List.map (encode (n-1)) l)
      |> List.map (fun l -> List.fold_left min Int.max_int l)
      |> List.fold_left (+) 0 in
    let _ = Hashtbl.add cache (n,seq) res in
    res
  
(* Utils *)

let cartesian_product l1 l2 =
  List.concat_map (
    fun e1 -> List.map (fun e2 -> e1 @ e2) l2
  ) l1

let rec list_product = function
  | [] -> []
  | [x] -> x
  | a :: b :: l -> 
  list_product ((cartesian_product a b) :: l)

(* Run the code *)

let nb_of_dir_keypads = 2
let inputs = ["341A" ; "083A" ; "802A" ; "973A" ; "780A"]
let nums = [341 ; 83 ; 802 ; 973 ; 780]
let lengths = inputs
  |> List.map to_num 
  (* Encoding the num keypad *)
  |> List.map encode_num 
  |> List.map list_product
  (* Encoding the dir keypads *)
  |> List.map (List.map (fun s -> encode nb_of_dir_keypads s))
  (* Find the min lenght *)
  |> List.map (List.fold_left min Int.max_int)
let sum = lengths
  |> List.map2 ( * ) nums
  |> List.fold_left ( + ) 0

