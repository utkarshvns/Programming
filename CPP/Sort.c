#include<stdio.h>
#include<stdlib.h>


//O(n2)
void SelectionSort(int A[], int n)
{
    for (int i = 0; i < n-1; i++)
    {
        int imin = i;
        for (int j = i+1; j < n; j++)
        {
            if(A[j] < A[imin])
            {
                imin = j;
            }              
        }
        int temp = A[i];
        A[i] = A[imin];
        A[imin] = temp;        
    }    
}

void descSelectionSort(int A[], int n)
{
    for (int i = 0; i < n-1; i++)
    {
        int imax = i;
        for (int j = i+1; j < n; j++)
        {
            if(A[j] > A[imax])
            {
                imax = j;
            }              
        }
        int temp = A[i];
        A[i] = A[imax];
        A[imax] = temp;        
    }    
}
//O (n2)
void BubbleSort(int A[], int n)
{
    for (int k = 1; k <= n-1; k++)
    {
        int flag = 0;
        for (int i = 0; i <= n-1-k; i++)
        {
            if (A[i]>A[i+1])
            {
                int temp = A[i+1];
                A[i+1] = A[i];
                A[i] = temp;
                flag = 1;
            }            
        }
        if (flag == 0) break;       
    }    
}

// O(n2) for worse case reverse sorted array and O(n) for best case full sorted array   
// considered better than bubble and selection sort as number of comparison and shift is usually less then the other two
void InsertionSort(int A[],int n)
{
    for (int i = 1; i < n; i++)
    {
        int value = A[i];
        int vaccant =i;
        while ( (vaccant > 0) && (A[vaccant-1] > value) )
        {
            A[vaccant] = A[vaccant-1];
            vaccant = vaccant - 1;
        }
        A[vaccant]= value;
    }    
}




void Merge(int L[], int R[], int A[],int nL, int nR)
{
    int i,j,k;
    i=j=k=0;
    while ((i<nL) && (j < nR))
    {
        if (L[i]<=R[j])
        {
            A[k] = L[i];
            i = i+1;
        }
        else
        {
            A[k] = R[j];
            j = j+1;
        }
        k=k+1;        
    }
    // After any one of the list is exhausted first, fill the rest of the element from other list
    while (i<nL)
    {
        A[k] = L[i];
        i=i+1;
        k= k+1;
    }
    while (j<nR)
    {
        A[k] = R[j];
        j=j+1;
        k= k+1;
    }    
}


void MergeSort(int A[], int n)
{
    if(n<2) return;
    int mid = n/2;
    int left[mid];
    int right[n-mid];
    for (int i = 0; i < mid; i++)
    {
        left[i] = A[i];
    }
    for (int i = mid; i < n; i++)
    {
        right[i-mid] = A[i];
    }
    MergeSort(left,mid);
    MergeSort(right,n-mid);
    int nL = sizeof(left)/sizeof(left[0]);
    int nR = sizeof(right)/sizeof(right[0]);
    Merge(left,right,A,nL,nR);
}


int Partition(int A[], int start, int end)
{
    int pivot = A[end]; // instead picking last pick element randomly
    int pIndex = start;// set partition index as start intially
    for (int i = start; i < end; i++)
    {
        if (A[i]<= pivot)
        {
            int temp = A[i]; // swap if  element is lesser than pivot
            A[i] = A[pIndex];
            A[pIndex] = temp;
            pIndex = pIndex+1;
        }   
    }
    int temp = A[pIndex]; // swap pivot with element at partition index
    A[pIndex] = A[end];
    A[end] = temp;
    return pIndex;     
}

void QuickSort(int A[],int start,int end)
{
    if(start<end)
    {
        int pIndex = Partition(A,start,end);
        QuickSort(A,start,pIndex-1);
        QuickSort(A,pIndex+1,end);
    }
}


void foobar(int arr[], int n)
{

   int i, j;

   for (i = 0; i < 4; i++)   {

         for (j = n-1; j >i; j--) 

           if (arr[j] < arr[j-1])

            //   swap(&arr[j], &arr[j-1]);

            {int temp = arr[j]; // swap if  element is lesser than pivot
            arr[j]= arr[j-1];
            arr[j-1] = temp;}

   }   

}

int main()
{
    int A[] = {2,7,4,1,5,3};
    int length = sizeof(A)/sizeof(A[0]);
    
    // int A[] = {5, 2, 7, 3, 9, 1, 8, 4};

    // foobar(A,8);



    // SelectionSort(A,length);
    // BubbleSort(A,length);
    // InsertionSort(A,length);
    // MergeSort(A, length);
    // QuickSort(A,0,length-1);

    descSelectionSort(A,length);

    
    for (int i = 0; i < length; i++)
    {
        printf("%d", A[i]);
    }
    
}