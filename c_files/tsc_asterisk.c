// принятие массива по концевому признаку
// упорядочить массив по возрастанию с помощью
// сортировки выбором и вывести на экран

#include <stdio.h>
#include <time.h>
#include <math.h>
#include <x86intrin.h>

#ifndef N
#error "N is not defined"
#endif

void selection_sort_asterisk(int a[], size_t size)
{
    for (size_t i = 0; i < size; i++)
    {
        size_t minind = i;
        for (size_t j = i + 1; j < size; j++)
            if (*(a + j) < *(a + minind))
                minind = j;
        int buf = *(a + i);
        *(a + i) = *(a + minind);
        *(a + minind) = buf;            
    }
}

void init_arr(int a[], size_t size)
{
    if (size == 0)
        return;
    a[0] = size % 6 + 2;
    for (size_t i = 1; i < size; i++)
        a[i] = a[i - 1] % (size - i) + 1;    
}

int main(void)
{
    int a[N];
    size_t counter = 0;
    double times[5000];
    unsigned long long start, end;
    unsigned long long answer;
    unsigned long long sum = 0;
    double avg;
    unsigned long long StdErr;
    double disp;
    double st_devi;
    double RSE = 0;
    double eps = 1e-8;

    while ((RSE > 1.0 || fabs(RSE) < eps) && counter < 5000 - 1)
    {
        init_arr(a, N); 
        start = __rdtsc();
        selection_sort_asterisk(a, N);
        end = __rdtsc();
        answer = end - start;
        printf("%llu \n", answer);  
        times[counter] = answer;
        counter++;
        sum += answer;
        avg = sum / counter;

        for (size_t i = 0; i < counter; i++)
            disp += (times[i] - avg) * (times[i] - avg);
        disp /= (counter - 1);

        st_devi = sqrt(disp);
        StdErr = st_devi / sqrt(counter);
        RSE = StdErr / avg * 100;
    }
    return 0;
}

