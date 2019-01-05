#include <thread>
#include <atomic>
#include <string>
#include <iostream>
#include <cmath>

int modInverse(int a, int m) 
{ 
    a = a%m; 
    for (int x=1; x<m; x++) 
       if ((a*x) % m == 1) 
          return x; 
} 

int main(int argc, char**argv)
{
    const unsigned int numThreads = 8;
    std::atomic<bool> isFound(false);
   
    if (argc != 3)
    {
        std::cout << "Please run the program as described int he challenge" << std::endl;
        return -1;
    }

    unsigned int public_e = std::stoul(argv[1]);
    unsigned int public_n = std::stoul(argv[2]);

    unsigned int bot = (unsigned int)floor(sqrt(public_n));
    //If even add 1
    if ((bot % 2) == 0)
    {
        ++bot;
    }

    //Find p and q, since its a small exponent, can relatively easilt brute force it, TODO: Parallelize this search.
    unsigned int p = 0;
    unsigned int q = 0;
    for (unsigned int i = bot; i < public_n ; i +=2)
    {
        if (public_n % i == 0)
        {
            p = i;
            q = public_n / i;
            break;
        }
    }
    
    //We have p, q, and e, find d (private exponent)
    unsigned int d = modInverse(public_e, (p-1)*(q-1));
    std::cout << "PRIVATE EXPONENT: " << d << std::endl;

    return 0;
}
