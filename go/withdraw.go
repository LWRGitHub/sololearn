/* Go: SoloLearn 

Withdraw 

You are working on a banking app. 

The code declares a BankAccount struct with a balance field. 
You need to add a withdraw() method for the BankAccount struct. It should take an integer argument and decrease the balance of the Bank Account by the given amount.
In case there is not enough money in the account, the method should output "Insufficient Funds".


 The code in main() takes the amount to withdraw as input, and calls the withdraw() method.


SoloLearn (2023) Withdraw: https://www.sololearn.com 

*/

package main
import "fmt"

type BankAccount struct {
  holder string
  balance int
}

func main() {
  acc := BankAccount{"James Smith", 100000}
  
  var amount int
  fmt.Scanln(&amount)
  
  acc.withdraw(amount)
  fmt.Println(acc)
}

func (ptr *BankAccount) withdraw(amount int){
	if ptr.balance < amount{
		fmt.Println("Insufficient Funds")
	}else{
		ptr.balance -= amount
	}
}





	
	
