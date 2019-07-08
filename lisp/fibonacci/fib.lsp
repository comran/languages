; Various methods for calculating the Nth Fibonacci number.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; Calculate Nth Fibonacci number using recursion.
; Time complexity: O(2^n)
(defun FIB (N)
  (cond ((= N 0) 0)
        ((= N 1) 1)
        (+
          (+ (FIB (- N 1)) (FIB (- N 2)))
        )
  )
)

; Tests
(print (FIB 10))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; Calculate Nth Fibonacci number using dynamic programming.
; Time complexity: O(n)
(defun FASTFIB_HELPER (N DP)
  (cond ((< N 2) DP)
        (+
          (FASTFIB_HELPER (- N 1)
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

(defun FASTFIB (N)
  (cond ((= N 0) 0)
        (+
          (let (DP)
             (car
               (last
                 (FASTFIB_HELPER N (cons DP `(0 1)))
               )
             )
          )
        )
  )
)

; Tests
(print (FASTFIB 10))

