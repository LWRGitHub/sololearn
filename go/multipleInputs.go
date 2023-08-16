/* Go: SoloLearn 

Multiple Inputs 

The make() function allows you to make dynamically sized arrays, which can use the append() function to add new elements to it.
This is useful when, for example, you need to take multiple inputs and store them in an array.

Your program needs to take a number, indicating the number of inputs, followed by those inputs. The input numbers should be stored in an array and be outputted as the result of the program.

Sample Input:
3
42
88
11
 
Sample Output:
[42 88 11]


The first number indicates that there are going to be 3 numbers as input.


SoloLearn (2023) Multiple Inputs: https://www.sololearn.com 

*/

package main
import "fmt"

func main() {
  var n int
  fmt.Scanln(&n)
  
  //your code goes here
  arr := make([]int, n)
  
  var num int
  for i:=0; i<n; i++{
  	fmt.Scanln(&num)
  	arr[i] = num
  }
  
  fmt.Println(arr)
  
}


	
	
