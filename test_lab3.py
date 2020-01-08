import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):

    
    def test_1_pq_insert(self):
        print("\n")
        print("insert into the priority queue")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [3,1,2])
        print("\n")

    
    def test_2_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

    
    def test_3_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(10)
        pq.insert(10)
        pq.insert(24)
        pq.insert(3)
        pq.insert(57)
        pq.insert(4)
        pq.insert(67)
        pq.insert(37)
        pq.insert(87)
        pq.insert(7)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [87,67,57,24,4,3,37,10,7])
        print("\n")

class T1_pqueue_peek(unittest.TestCase):

    
    def test_1_pq_peek(self):
        print("Just return the first element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")

    def test_3_pq_peek(self):
        print("\n")
        pq = pqueue.pqueue(10)
        pq.insert(10)
        pq.insert(24)
        pq.insert(3)
        pq.insert(57)
        pq.insert(4)
        pq.insert(67)
        pq.insert(37)
        pq.insert(87)
        pq.insert(7)
        self.assertEqual(pq.peek(), 87)
        print("\n")

class T2_pqueue_extract_max(unittest.TestCase):

    
    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")

    def test_2_pq_extract_max(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.extract_max()
        pq.insert(4)
        pq.insert(5)
        self.assertEqual(pq.extract_max(), 5)
        self.assertEqual(pq.extract_max(), 4)
        print("\n")

    
    def test_3_pq_extract_max(self):
        print("\n")
        pq = pqueue.pqueue(10)
        pq.insert(10)
        pq.insert(24)
        pq.insert(3)
        pq.insert(57)
        pq.insert(4)
        pq.insert(67)
        pq.insert(37)
        pq.insert(87)
        pq.insert(7)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [87,67,57,24,4,3,37,10,7])
        pq.extract_max()
        pq.extract_max()
        pq.extract_max()
        pq.extract_max()
        pq.extract_max()
        pq.extract_max()
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [7,4,3])
        print("\n")

class T3_pqueue_overflow(unittest.TestCase):

    
    def test_1_pq_overflow(self):
        print("inserting when the queue is full")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        with self.assertRaises(IndexError):
            pq.insert(6)
        print("\n")

    
    def test_2_pq_overflow(self):
        print("extracting when the queue is empty")
        print("\n")
        pq = pqueue.pqueue(5)
        with self.assertRaises(KeyError):
            pq.extract_max()
        print("\n")

class T4_heap_build_heap(unittest.TestCase):

    
    def test_heap_sort_1(self):
        print("\n")
        to_build_heap_list = [10,24,3,57,4,67,37,87,7]
        sort_heap = mheap.max_heap(len(to_build_heap_list), to_build_heap_list)
        sort_heap.build_heap()
        # print(sort_heap.get_heap())
        

        self.assertEqual(sort_heap.get_heap(), [87, 57, 67, 24, 4, 3, 37, 10, 7])
        print("\n")

class T5_heap_sort(unittest.TestCase):

    
    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")

    
    def test_heap_sort_3(self):
        print("\n")
        to_sort_list = [85, 34, 35, 17, 33, 31, 14, 42, 41, 19, 77, 
                        23, 78, 60, 13, 71, 2, 43, 57, 4]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [2, 4, 13, 14, 17, 19, 23, 31, 
                                        33, 34, 35, 41, 42, 43, 57, 60, 71, 77, 78, 85])
        print("\n")


class T6_pqueue_insert(unittest.TestCase):

    
    def test_1_pq_insert(self):
        print("inserting 20 elements")
        print("\n")
        pq = pqueue.pqueue(20)
        pq.insert(85)
        pq.insert(34)
        pq.insert(35)
        pq.insert(17)
        pq.insert(33)
        pq.insert(31)
        pq.insert(14)
        pq.insert(42)
        pq.insert(41)
        pq.insert(19)
        pq.insert(77)
        pq.insert(23)
        pq.insert(78)
        pq.insert(60)
        pq.insert(13)
        pq.insert(71)
        pq.insert(2)
        pq.insert(43)
        pq.insert(57)
        pq.insert(4)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [85,77,78,71,42,35,60,41,57,19,33,23,31,14,13,17,2,34,43,4])
        print("\n")

    
    def test_3_pq_extract_max(self):
        print("inserting and extracting from a priority queue of 20 elements")
        print("\n")
        pq = pqueue.pqueue(20)
        pq.insert(85)
        pq.insert(34)
        pq.insert(35)
        pq.extract_max()
        pq.insert(17)
        pq.insert(33)
        pq.extract_max()
        pq.insert(31)
        pq.insert(14)
        pq.insert(42)
        pq.extract_max()
        pq.insert(41)
        pq.insert(19)
        pq.extract_max()
        pq.insert(77)
        pq.insert(23)
        pq.insert(78)
        pq.extract_max()
        pq.insert(60)
        pq.insert(13)
        pq.insert(71)
        pq.insert(2)
        pq.insert(43)
        pq.insert(57)
        pq.insert(4)
        pq_list = [element for element in pq]
        # print(pq_list)
        self.assertEqual(pq_list, [77,71,57,33,60,34,43,23,31,13,14,2,17,19,4])
        print("\n")


    
    
if __name__ == '__main__':
    unittest.main()