#include <bits/stdc++.h>
using namespace std;

void insertionSort(int *arr, int &n, int &comparisons, int &shifts)
{
	for (int i = 1; i < n; ++i)
	{
		int j, temp = arr[i];
		for (j = i - 1; j >= 0; --j)
		{
			comparisons++;
			if (temp <= arr[j])
			{
				shifts++;
				arr[j + 1] = arr[j];
			}
			else break;
		}
		arr[j + 1] = temp;
	}
}

int main()
{
	int n, comparisons = 0, shifts = 0;
	cout << "Enter the number of elements : ";
	cin >> n;
	int *arr = new int[n];
	cout << "Enter the numbers : ";
	for (int i = 0; i < n; ++i) cin >> arr[i];

	insertionSort(arr, n, comparisons, shifts);
	
	cout << "Array sorted in increasing order : ";
	for (int i = 0; i < n; ++i) cout << arr[i] << " ";
	cout << "\nNumber of comparisons = " << comparisons << endl;
	cout << "Number of shifts = " << shifts << endl;

	delete []arr;
	return 0;
}
