; Calculate Nth Fibonacci number using recursion.

; Time complexity: O(2^N)

(defun FIB_RECURSIVE (N)
  (cond ((= N 0) 0)
        ((= N 1) 1)
        (+
          (+ (FIB_RECURSIVE (- N 1)) (FIB_RECURSIVE (- N 2)))
        )
  )
)

; Tests
(print (FIB_RECURSIVE 1))
(print (FIB_RECURSIVE 2))
(print (FIB_RECURSIVE 3))
(print (FIB_RECURSIVE 4))
(print (FIB_RECURSIVE 5))
(print (FIB_RECURSIVE 6))
(print (FIB_RECURSIVE 7))
(print (FIB_RECURSIVE 8))
(print (FIB_RECURSIVE 9))
(print (FIB_RECURSIVE 10))
(print (FIB_RECURSIVE 11))
(print (FIB_RECURSIVE 12))
(print (FIB_RECURSIVE 13))
(print (FIB_RECURSIVE 14))
(print (FIB_RECURSIVE 15))
(print (FIB_RECURSIVE 16))
(print (FIB_RECURSIVE 17))
(print (FIB_RECURSIVE 18))
(print (FIB_RECURSIVE 19))
(print (FIB_RECURSIVE 20))
(print (FIB_RECURSIVE 21))
(print (FIB_RECURSIVE 22))

