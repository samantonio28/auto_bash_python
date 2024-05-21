// принятие массива по концевому признаку
// упорядочить массив по возрастанию с помощью
// сортировки выбором и вывести на экран

#include <stdio.h>
#include <time.h>

#ifndef N
#error "N is not defined"
#endif

void selection_sort_pointers(int a[], size_t size)
{
    for (int *pi = a; pi < a + size; pi++)
    {
        int *pmin = pi;
        for (int *pj = pi + 1; pj < a + size; pj++)
            if (*pj < *pmin)
                pmin = pj;
        int buf = *pi;
        *pi = *pmin;
        *pmin = buf;            
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
    struct timespec start, end;
    unsigned long long answer;

    init_arr(a, N); 
    clock_gettime(CLOCK_MONOTONIC_RAW, &start);
    selection_sort_pointers(a, N);
    clock_gettime(CLOCK_MONOTONIC_RAW, &end);
    answer = 1000000000 * (end.tv_sec - start.tv_sec) + end.tv_nsec - start.tv_nsec;
    printf("%llu \n", answer);  
    return 0;
}

