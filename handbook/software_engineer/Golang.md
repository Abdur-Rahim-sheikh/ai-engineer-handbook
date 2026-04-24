# Interview preperations for Golang

### Resources

- [Go with habib (beginner)](https://www.youtube.com/playlist?list=PLpCqPSEm2Xe8sEY2haMDUVgwbkIs5NCJI)

## Content

1. [Internal Memory](#internal-memory)
2. [Closure](#closure)
3. [Receiver](#receiver)

#### Internal Memory

There are 4 basic types of memory

- **Code segment**
  - Functions, constant are kept here as binary
- **Data segment**
  - All global veriables are kept here
- **Stack**
  - During runtime the running blocks (actually only reference of the code segment) and scoped variables are kept here
  - as soon as the function is done that part is removed from stack
- **Heap**
  - It keeps the value **escaped** during execution of closure, more later
  - Managed by gorutine garbage collector.

#### Closure

If a function's inner function needs a variable from that function, then it keeps the
varialbe outside of scope, called closure.

```go
int a=3;
const PI=3.1416;

func outer(){
    int b=8;
    int result = 0;

    func inner(){
        result:=result+a+b;
        return result;
    }
    return inner;
}

func main(){
    x:=outer()
    x()
    x()
    y:=outer()
    y()
}
```

Here during compilation,

- Code Block has: Const PI, outer function, main function
- Data block has: variable a

Then during execution,
in Stack:

- finds init -> not found no isue
- find main -> found
  - finds outer -> execute returns inner, escapes `b and result to heap`
  - executes inner taking data b and result from heap (by the way currently outer function is not present in stack just those escapped values)
  - executes inner second time
  - finds outer again -> escapes the b and result to heap again
  - gets another inner
  - executes that another inner again
  - exits main

### Receiver

In Go, receiver is what turns a normal function into a method `attached` to a type.
in below code `Citizen` and `isChild` are receriver.

There are two types of receiver:

1. Value Receiver
   - works on a copy
   - original struct does not change
   - `Citizen` is the example
2. Pointer receiver
   - works on the original value
   - Can modify struct fields

```go
type User struct{
    name string
    age int
}
// we can use any variable instead of `this` but its usually named as `this`
func (this User) Citizen(){
    return this.name>17
}

func (this *User) isChild(){
    return this.age<5
}
```

**Note**: If any method on a type uses a pointer receiver, it's common practice to use pointer receivers for all methods of that type.
