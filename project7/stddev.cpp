//
//	Michael Cooper
//	Ohio University CS3560
//	Variadic Function Project
//

#include "stddev.h"
#include <cstdarg>
#include <cmath>

double stddev(int n, ... )
{

	va_list va;

	va_start(va, n);

	double sum = 0;
	for(int i = 0; i < n; i++)
	{
		sum += va_arg(va, int);		//cast arg to int and add to sum
	}

	double mean = sum/n;

	double stddev = 0;

	va_start(va, n);

	int arg = 0;

	for(int i = 0; i < n; i++)
	{
		arg = va_arg(va, int);
		stddev += (arg - mean) * (arg - mean);
	}

	stddev /= n;

	return sqrt(stddev);

}