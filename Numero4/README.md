# Concordia

# JdG2019
## Competition Académique Info - Numero 4

RSA crack.

`start.sh 7 1037` is the expected format

### Required to launch
- Python3 required
- Run the install.sh to compile
- Run the start.sh as above to run

### Explanation
Since the modulo is rather small, it is possible to brite force the p and q values that make it (n = p*q). With those numbers it is then possible to find the private exponent. This is done by finding the modular inverse of n and phi where phi is ```(p-1)*(q-1)```. 
