# Is it a heap or is it a pile?

Complete the following tasks:

1. Show each step of turning list `[42, 35, 71, 34, 76, 39, 77, 47, 6, 20]` into a _min_ heap.

   - The following is an example of heapifying `[55, 73, 17, 41, 83, 89, 7, 28, 10, 69]`.

   | Step | List                                  |
   | ---- | ------------------------------------- |
   | 0    | 55, 73, 17, 41, 83, 89, 7, 28, 10, 69 |
   | 1    | 55, 73, 17, 41, 69, 89, 7, 28, 10, 83 |
   | 2    | 55, 73, 17, 10, 69, 89, 7, 28, 41, 83 |
   | 3    | 55, 73, 7, 10, 69, 89, 17, 28, 41, 83 |
   | 4    | 55, 10, 7, 28, 69, 89, 17, 73, 41, 83 |
   | 5    | 7, 10, 17, 28, 69, 89, 55, 73, 41, 83 |

   - The following is the solution.

   | Step | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
   | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | 0    | 42  | 35  | 71  | 34  | 76  | 39  | 77  | 47  | 6   | 20  |
   | 1    | 42  | 35  | 71  | 34  | 20  | 39  | 77  | 47  | 6   | 76  |
   | 2    | 42  | 35  | 71  | 6   | 20  | 39  | 77  | 47  | 34  | 76  |
   | 3    | 42  | 35  | 39  | 6   | 20  | 71  | 77  | 47  | 34  | 76  |
   | 4    | 42  | 6   | 39  | 34  | 20  | 71  | 77  | 47  | 35  | 76  |
   | 5    | 6   | 20  | 39  | 34  | 42  | 71  | 77  | 47  | 35  | 76  |

2. Show each step of turning list `[42, 35, 71, 34, 76, 39, 77, 47, 6, 20]` into a _max_ heap.

   - The following is an example of heapifying `[69, 10, 28, 7, 89, 83, 41, 17, 73, 55]`.

   | Step | List                                  |
   | ---- | ------------------------------------- |
   | 0    | 69, 10, 28, 7, 89, 83, 41, 17, 73, 55 |
   | 1    | 69, 10, 28, 73, 89, 83, 41, 17, 7, 55 |
   | 2    | 69, 10, 83, 73, 89, 28, 41, 17, 7, 55 |
   | 3    | 69, 89, 83, 73, 55, 28, 41, 17, 7, 10 |
   | 4    | 89, 69, 83, 73, 55, 28, 41, 17, 7, 10 |
   | 5    | 89, 73, 83, 69, 55, 28, 41, 17, 7, 10 |

   - The following is the solution.

   | Step | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
   | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | 0    | 42  | 35  | 71  | 34  | 76  | 39  | 77  | 47  | 6   | 20  |
   | 1    | 42  | 35  | 71  | 47  | 76  | 39  | 77  | 34  | 6   | 20  |
   | 2    | 42  | 35  | 77  | 47  | 76  | 39  | 71  | 34  | 6   | 20  |
   | 3    | 42  | 76  | 77  | 47  | 35  | 39  | 71  | 34  | 6   | 20  |
   | 4    | 77  | 76  | 71  | 47  | 35  | 39  | 42  | 34  | 6   | 20  |

3. Show each intermediate step of adding 1 to the following heap: `[20, 27, 30, 41, 42, 83, 66, 91, 74, 63]`.

4. Show each intermediate step of removing an item (20) from the following heap: `[20, 27, 30, 41, 42, 83, 66, 91, 74, 63]`.

5. Show each intermediate step of sorting `[594, 850, 281, 952, 129, 348, 264, 972, 598, 758]` using HeapSort. The following is an example of sorting `[15, 16, 73, 65, 38, 10, 22, 79, 87, 64]`:

| Step | List                                   |
| ---- | -------------------------------------- |
| 0    | 15, 16, 73, 65, 38, 10, 22, 79, 87, 64 |
| 1    | 10, 16, 15, 65, 38, 73, 22, 79, 87, 64 |
| 2    | 10, 15, 16, 22, 38, 73, 65, 79, 87, 64 |
| 3    | 10, 15, 16, 22, 38, 64, 65, 79, 87, 73 |
| 4    | 10, 15, 16, 22, 38, 64, 65, 79, 87, 73 |
| 5    | 10, 15, 16, 22, 38, 64, 65, 79, 87, 73 |
| 6    | 10, 15, 16, 22, 38, 64, 65, 79, 87, 73 |
| 7    | 10, 15, 16, 22, 38, 64, 65, 73, 87, 79 |
| 8    | 10, 15, 16, 22, 38, 64, 65, 73, 87, 79 |
| 9    | 10, 15, 16, 22, 38, 64, 65, 73, 79, 87 |
| 10   | 10, 15, 16, 22, 38, 64, 65, 73, 79, 87 |
| 11   | 10, 15, 16, 22, 38, 64, 65, 73, 79, 87 |