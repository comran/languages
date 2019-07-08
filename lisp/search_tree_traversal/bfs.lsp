; Perform a breadth-first traveral of the given tree, and return the list of
; elements in the order visited.

; v = number of nodes
; h = maximum tree depth
;
; Time complexity:  O(v)
; Space complexity: O(v)

(defun BFS (tree)
  (cond
    ((null tree) nil)
    ((atom tree) tree)
    ((atom (car tree)) (cons (car tree) (BFS (cdr tree))))
    (+
      (BFS
        (append
          (cdr tree)
          (car tree)
        )
      )
    )
  )
)

(print (BFS '((A (B)) C (D))))
(print (BFS '((W X) (Y Z))))
(print (BFS '(A)))
(print (BFS '(((((((((((((((((((((((((A)))))))))))))))))))))))) B)))

