(ns factorial)

(defn factorial [n]
  (if (= n 1)
    1
    (* n (factorial (dec n)))))

(println "Enter Number For Factorial :")
(def user_n (read-line))
(println (factorial (Integer/parseInt user_n)))
