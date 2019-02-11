#include <iostream>
#include <vector>
#include <cmath>

/**
*
*	\brief Finds the standard deviation of a given array
*	\param pointer to an array of integers
*	\param size of the array
*	\return double
*
*/
double deviation(int* a, int n)
{
	int sum = 0;
	for(size_t i = 0; i < n; i++)
	{
		sum += a[i];
	} 
	double mean = sum;
	mean /= n;
	double stddev = 0;
	for(size_t i = 0; i < n; i++)
	{
		stddev += (a[i] - mean) * (a[i] - mean); 
	}
	stddev /= n;
	if(stddev == 0)
		std::cout << "Sigma is zero." << std::endl;

	return sqrt(stddev);
}
