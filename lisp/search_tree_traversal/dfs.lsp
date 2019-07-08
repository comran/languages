; Perform a depth-first traveral of the given tree, and return the list of
; elements in the order visited.

; v = number of nodes
; h = maximum tree depth
;
; Time complexity:  O(v)
; Space complexity: O(h)

(defun DFS (tree)
  (cond ((null tree) nil)
        ((atom tree) (cons tree nil))
        ((null (car tree)) (DFS (cdr tree)))
        ((null (cdr tree)) (DFS (car tree)))
        (+
          (append
            (DFS (car tree))
            (DFS (cdr tree))
          )
        )
  )
)

; Tests
(print (DFS 'A))
(print (DFS '(A)))
(print (DFS '((W X) (Y Z))))
(print (DFS '((A (B)) C (D))))
(print (DFS '((A) D (C A))))

