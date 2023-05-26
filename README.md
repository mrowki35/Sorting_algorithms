# Sorting_algorithms
This repo contains a few implentations of sortig algorythms written in Thomas H. Cormen Introduction to Algorithms as pseudocode.
The long time goal is to implement almost every pseudocode written in this textbook.

---
#Table of Contents
1. [Bucketsort]()
2. [Bubblesort]()
3. [Insertion Sort]()
4. [Merge Sort]()
5. [Quicksort]()

---
##Bucketsort
###Description
Bucketsort is a distribution sorting algorithm that works by dividing the input into discrete buckets and then sorting each bucket individually using another sorting algorithm or recursively applying the bucketsort algorithm.


###Example
```python
Copy code
A = [5, 2, 4, 7, 1, 3, 2, 6]
Bucketsort(A)
print(A)
```
---

##Bubblesort
###Description
Bubblesort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

###Example
```python
A = [5, 2, 4, 6, 1, 3, 24, 13, 10, 11, 31, 145, 14]
bubblesort(A)
print(A)
```

---
##Insertion Sort
###Description
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It iterates through the input elements, growing the sorted array at each iteration by inserting the current element into the correct position.

###Example
```python
A = [5, 2, 4, 6, 1, 3, 24, 13, 10, 11, 31, 145, 14]
insertion_sort(A)
print(A)
```
---
##Merge Sort
###Description
Merge sort is a divide-and-conquer algorithm that divides the unsorted list into smaller sublists, sorts them recursively, and then merges the sorted sublists to produce a sorted list.

###Example
```python
A = [5, 2, 4, 7, 1, 3, 2, 6]
Merge_Sort(A, 0, len(A)-1)
print(A)
```
---
##Quicksort
###Description
Quicksort is a divide-and-conquer algorithm that selects a pivot element and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. It then recursively sorts the sub-arrays.

###Example
```python
A = [5, 2, 4, 6, 1, 3, 24, 13, 10, 11, 31, 145, 14, 6]
quicksort(A, 0, len(A)-1)
print(A)
```
---
