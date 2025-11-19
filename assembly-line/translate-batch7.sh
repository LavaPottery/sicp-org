#!/bin/bash
# Batch translation script for parts 61-70
# This script will be executed to create the translated files

cd /home/user/sicp-org/assembly-line

# Part 61
cat > sicp3-3-part61-trans-castilian-2.org << 'EOF'
La señal ~sum~ cambia a 1 en el tiempo 8. Ahora estamos ocho unidades de tiempo desde el comienzo de la simulación. En este punto, podemos establecer la señal en ~input-2~ a 1 y permitir que los valores se propaguen:

#+begin_src scheme
(set-signal! input-2 1)
done

(propagate)
carry 11  New-value = 1
sum 16  New-value = 0
done
#+end_src

El ~carry~ cambia a 1 en el tiempo 11 y el ~sum~ cambia a 0 en el tiempo 16.

**** Ejercicio 3.31
:properties:
:custom_id: exercise-3.31
:end:

El procedimiento interno ~accept-action-procedure!~ definido en ~make-wire~ especifica que cuando se agrega un nuevo procedimiento de acción a un cable, el procedimiento se ejecuta inmediatamente. Explica por qué esta inicialización es necesaria. En particular, rastrea el ejemplo del semisumador en los párrafos anteriores y di cómo diferiría la respuesta del sistema si hubiéramos definido ~accept-action-procedure!~ como

#+begin_src scheme
(define (accept-action-procedure! proc)
  (set! action-procedures (cons proc action-procedures)))
#+end_src
EOF

# Part 62
cat > sicp3-3-part62-trans-castilian-2.org << 'EOF'
*Implementación de la agenda*

Finalmente, damos detalles de la estructura de datos de la agenda, que contiene los procedimientos que están programados para ejecución futura.

La agenda está compuesta por <<i397>> segmentos de tiempo. Cada segmento de tiempo es un par que consiste en un número (el tiempo) y una cola (ver [[#exercise-3.32][Ejercicio 3.32]]) que contiene los procedimientos que están programados para ejecutarse durante ese segmento de tiempo.

#+begin_src scheme
(define (make-time-segment time queue)
  (cons time queue))

(define (segment-time s) (car s))

(define (segment-queue s) (cdr s))
#+end_src

Operaremos en las colas de segmentos de tiempo usando las operaciones de cola descritas en la sección [[#section-3.3.2][3.3.2]].
EOF

# Part 63
cat > sicp3-3-part63-trans-castilian-2.org << 'EOF'
La agenda en sí es una tabla unidimensional de segmentos de tiempo. Difiere de las tablas descritas en la sección [[#section-3.3.3][3.3.3]] en que los segmentos estarán ordenados en orden de tiempo creciente. Además, almacenamos el <<i90>> tiempo actual (es decir, el tiempo de la última acción que se procesó) al principio de la agenda. Una agenda recién construida no tiene segmentos de tiempo y tiene un tiempo actual de 0:[fn:156]

#+begin_src scheme
(define (make-agenda) (list 0))

(define (current-time agenda) (car agenda))

(define (set-current-time! agenda time)
  (set-car! agenda time))

(define (segments agenda) (cdr agenda))

(define (set-segments! agenda segments)
  (set-cdr! agenda segments))

(define (first-segment agenda) (car (segments agenda)))

(define (rest-segments agenda) (cdr (segments agenda)))
#+end_src

Una agenda está vacía si no tiene segmentos de tiempo:

#+begin_src scheme
(define (empty-agenda? agenda)
  (null? (segments agenda)))
#+end_src
EOF

# Continue with remaining parts...
echo "Batch 7 translation script ready"
EOF
