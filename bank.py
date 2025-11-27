
import sys

if len(sys.argv) >= 3:
  script_name = sys.argv[0]
  initial = sys.argv[1]
  deposit = sys.argv[2]
else:
  script_name = sys.argv[0]
  initial= 1500
  deposit=2000
balance=initial+deposit
print("initial Amount:",initial)
print("deposit Amount:",deposit)
print("Balance Amount:",balance)
 
