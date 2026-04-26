## Golang Interview questions

## Content

1. [What the below code prints](#what-the-below-code-prints)

### What the below code prints

```go
func main(){
	var x []string;
	x = append(x,"Abir");
	x = append(x,"practic")
	x = append(x,"Go")

	y := x
    z := y
	x = append(x, "expert")
	y = append(y, "beginner")
	x[0] = "Nadia"

	fmt.Println(x,len(x),cap(x))
	fmt.Println(y,len(y),cap(y))
	fmt.Println(z,len(z),cap(z))
```

This will print

```bash
["Nadia", "practice", "go", "beginner"] 4 4
["Nadia", "practice", "go", "beginner"] 4 4
["Nadia", "practice", "go"] 3 4
```

Why is that, let's debunk line by line

- First three line `x` gets `"Abir","practice", "go"` so, pointer points at ref-start, len is 3 and cap is 4
- Then `y` gets the values of `x`, so it's pointer also points ref-start, len is 3, cap is 4
- Then `z` gets the values of `y`, so it's pointer also points ref-start, len is 3, cap is 4
- Then we again append to `x`, so pointer is same, len is 4 and the `python` takes `ref-start+3`th place, cap is 4
- Then we append from `y`, The initial pointer is same, but as the len was `3` for this one it becomes `4` and `beginner` takes the `ref-start+3`th place. cap is still 4
- then `x[0]=Nadia`, the initial pointer being same it's value changed from `Abir to Nadia`, the len stays 4, cap stays 4
- Now the part's are to print,
  - according to the latest values, everyones initial position pointer is same.
  - The 4th position changed, but as the z does not know that, it has only the first 3 values

Let's analyze the below code now

```go
func main(){
	var x []string;
	x = append(x,"abir");
	x = append(x,"pratice")

	y := x
    z := y
	x = append(x, "expert")
	y = append(y, "beginner")
	x[0] = "nadia"

	fmt.Println(x,len(x),cap(x))
	fmt.Println(y,len(y),cap(y))
	fmt.Println(z,len(z),cap(z))
}
```

A change in single line completely changes the game.

```bash
[nadia pratice expert] 3 4
[abir pratice beginner] 3 4
[abir pratice] 2 2
```

- First two line `x` gets `"abir", "practice"`, the pointer points at `ref-start1`, len is 2, cap is 2
- `y` and `z` gets the values what `x` has, the pointer points at `ref-start1`, len 2, cap 2
- Now `x` appends a value.
  - But this time the `cap` limit is reached, so the whole array copies to a new location with `ref-start2`
  - Appends the value `expert` to this new location, len is 3, cap is doubled to 4
- Then `y` appends a value
  - This `cap` limit of y hits. so the whole array at `ref-start1` copies to a new location lets say `ref-start3`
  - Appends the value `"abir", "practice"` + `begginer`, len is 3 cap is doubled to 4
- Now `x[0]='nadia'` so everything assumes same, just the `ref-start2` value changed `from abir to nadia`
- Not comes the printing part
  - X is pointing at `ref-start2` so it's value is `[nadia pratice expert]` len 3, cap 4
  - Y is pointing at `ref-start3` so it's value is `[abir pratice begginer]` len 3, cap 4
  - Z is pointing at `ref-start1` so it's value is old `[abir pratice]` len 2, cap 2
