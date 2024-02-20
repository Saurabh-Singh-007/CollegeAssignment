#include <bits/stdc++.h>
using namespace std;

void merge(int *arr, int lb, int ub, int &comparisons)
{
	int mid = lb + (ub - lb) / 2;

	int *temp = new int[ub - lb + 1];
	int i = lb, j = mid + 1, k = -1;

	while (i <= mid && j <= ub)
	{
		comparisons++;
		if (arr[i] <= arr[j]) temp[++k] = arr[i++];
		else temp[++k] = arr[j++];
	}
	while (i <= mid) temp[++k] = arr[i++];
	while (j <= ub) temp[++k] = arr[j++];

	for (i = lb, j = 0; i <= ub; ++i, ++j) arr[i] = temp[j];

	delete []temp;
}

void mergeSort(int *arr, int lb, int ub, int &comparisons)
{
	if (lb >= ub) return ;
	
	int mid = lb + (ub - lb) / 2;
	mergeSort(arr, lb, mid, comparisons); // Sorting the left half
	mergeSort(arr, mid + 1, ub, comparisons); // Sorting the right half
	merge(arr, lb, ub, comparisons); // Merging the sorted halves
}

int main()
{
	int n, comparisons = 0;
	cout << "Enter the number of elements : ";
	cin >> n;

	int *arr = new int[n];
	cout << "Enter the elements : ";
	for (int i = 0; i < n; ++i) cin >> arr[i];
	mergeSort(arr, 0, n - 1, comparisons);

	cout << "Array sorted in ascending order is : ";
	for (int i = 0; i < n; ++i) cout << arr[i] << " ";
	cout << "\nNumber of comparisons = " << comparisons << endl;

	delete []arr;	
	return 0;
}
