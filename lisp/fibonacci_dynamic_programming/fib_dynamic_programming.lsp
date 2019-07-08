; Calculate Nth Fibonacci number using dynamic programming.

; Time complexity: O(N)

(defun DYNAMIC_FIB_HELPER (N DP)
  (cond ((< N 2) DP)
        (+
          (DYNAMIC_FIB_HELPER (- N 1)
            (append DP
              (cons
                (+ (car (last DP)) (car (last DP 2)))
                ()
              )
            )
          )
        )
  )
)

(defun DYNAMIC_FIB (N)
  (cond ((= N 0) 0)
        (+
          (let (DP)
             (car
               (last
                 (DYNAMIC_FIB_HELPER N (cons DP `(0 1)))
               )
             )
          )
        )
  )
)

; Tests
(print (DYNAMIC_FIB 1))
(print (DYNAMIC_FIB 2))
(print (DYNAMIC_FIB 3))
(print (DYNAMIC_FIB 4))
(print (DYNAMIC_FIB 5))
(print (DYNAMIC_FIB 6))
(print (DYNAMIC_FIB 7))
(print (DYNAMIC_FIB 8))
(print (DYNAMIC_FIB 9))
(print (DYNAMIC_FIB 10))
(print (DYNAMIC_FIB 11))
(print (DYNAMIC_FIB 12))
(print (DYNAMIC_FIB 13))
(print (DYNAMIC_FIB 14))
(print (DYNAMIC_FIB 15))
(print (DYNAMIC_FIB 16))
(print (DYNAMIC_FIB 17))
(print (DYNAMIC_FIB 18))
(print (DYNAMIC_FIB 19))
(print (DYNAMIC_FIB 20))
(print (DYNAMIC_FIB 21))
(print (DYNAMIC_FIB 22))

