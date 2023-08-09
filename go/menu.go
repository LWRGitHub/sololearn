/* Go: SoloLearn 

Menu

You are making a digital Menu App. 
The menu choices are stored in an array called menu.

You need to take a number as input, which indicates the choice index, and output the corresponding item from the menu.
In case the index is not valid, your app should output "Invalid choice".
The input indicates the index of the array, meaning 0 corresponds to the first item.

Sample Input:
2

Sample Output:
Cake


The menu array is already defined in the code.


SoloLearn (2023) Menu: https://www.sololearn.com 

*/

package main
import "fmt"

func main() {

  menu := [6]string{"Water", "Burger", "Cake", "Soup", "Soda", "Fries"}
  var itemNum int
  fmt.Scanln(&itemNum)
  
  if itemNum > 5 || itemNum < 0{
  	fmt.Println("Invalid choice")
  }else{
  	fmt.Println(menu[itemNum])
  }
}








	
	
