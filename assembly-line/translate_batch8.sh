#!/bin/bash

# Part 71
cat > sicp3-3-part71-trans-castilian-2.org << 'END71'
La sonda en ~C~ despierta e informa el valor. ~C~ también propaga su valor a través de la red como se describió anteriormente. Esto establece ~F~ a 77, que es informado por la sonda en ~F~.

Ahora podemos intentar establecer ~F~ a un nuevo valor, digamos 212:

#+begin_src scheme
(set-value! F 212 'user)
Error! Contradiction (77 212)
#+end_src

El conector se queja de que ha detectado una contradicción: Su valor es 77, y alguien está tratando de establecerlo a 212. Si realmente queremos reutilizar la red con nuevos valores, podemos decirle a ~C~ que olvide su valor antiguo:

#+begin_src scheme
(forget-value! C 'user)
Probe: Celsius temp = ?
Probe: Fahrenheit temp = ?
done
#+end_src

~C~ encuentra que el ~user~, quien estableció su valor originalmente, ahora está retractando ese valor, por lo que ~C~ acepta perder su valor, como muestra la sonda, e informa al resto de la red de este hecho. Esta información finalmente se propaga a ~F~, que ahora encuentra que no tiene razón para continuar creyendo que su propio valor es 77. Por lo tanto, ~F~ también renuncia a su valor, como muestra la sonda.
END71

# Part 72
cat > sicp3-3-part72-trans-castilian-2.org << 'END72'
Ahora que ~F~ no tiene valor, somos libres de establecerlo a 212:

#+begin_src scheme
(set-value! F 212 'user)
Probe: Fahrenheit temp = 212
Probe: Celsius temp = 100
done
#+end_src

Este nuevo valor, cuando se propaga a través de la red, fuerza a ~C~ a tener un valor de 100, y esto es registrado por la sonda en ~C~. Nota que la misma red se está usando para calcular ~C~ dado ~F~ y para calcular ~F~ dado ~C~. Esta no direccionalidad del cálculo es la característica distintiva de los sistemas basados en restricciones.

*Implementación del sistema de restricciones*

El sistema de restricciones se implementa mediante objetos procedimentales con estado local, de una manera muy similar al simulador de circuitos digitales de la sección [[#section-3.3.4][3.3.4]]. Aunque los objetos primitivos del sistema de restricciones son algo más complejos, el sistema general es más simple, ya que no hay preocupación por las agendas y los retrasos lógicos.
END72

# Part 73
cat > sicp3-3-part73-trans-castilian-2.org << 'END73'
Las operaciones básicas en conectores son las siguientes:

- ~(has-value? <CONNECTOR>)~ indica si el conector tiene un valor.

- ~(get-value <CONNECTOR>)~ devuelve el valor actual del conector.

- ~(set-value! <CONNECTOR> <NEW-VALUE> <INFORMANT>)~ indica que el informante está solicitando al conector que establezca su valor al nuevo valor.

- ~(forget-value! <CONNECTOR> <RETRACTOR>)~ le dice al conector que el retractor le está solicitando que olvide su valor.

- ~(connect <CONNECTOR> <NEW-CONSTRAINT>)~ le dice al conector que participe en la nueva restricción.

Los conectores se comunican con las restricciones por medio de los procedimientos ~inform-about-value~, que le dice a la restricción dada que el conector tiene un valor, e ~inform-about-no-value~, que le dice a la restricción que el conector ha perdido su valor.
END73

