# Implementació de l’Algorisme CKY

## Descripció
Aquest projecte implementa l’algorisme CKY (Cocke-Kasami-Younger) per determinar si una paraula pertany a un llenguatge generat per una gramàtica lliure de context (CFG) expressada en Forma Normal de Chomsky (CNF).

Inclou:
- Transformació automàtica de CFG a CNF.
- Versió probabilística amb càlcul de la probabilitat màxima de derivació.
- Versió interactiva que permet a l’usuari definir gramàtiques i paraules des de la terminal.

---

## Estructura del projecte
Els fitxers principals són:

- `CKY.py`: Implementació de l’algorisme CKY bàsic.
- `CKY_probabilistic.py`: Algorisme CKY probabilístic.
- `gramatica.py`: Classe per representar i convertir CFG a CNF.
- `gramatica_probabilistic.py`: Classe adaptada per gestionar gramàtiques probabilístiques.
- `main.py`: Script per executar CKY bàsic.
- `main_probabilistic.py`: Script per executar CKY probabilístic.
- `main_interactiu.py`: Versió interactiva del programa.

---

## Requisits
- Python 3
- No s’utilitzen llibreries externes que resolguin directament la tasca.
- Terminal amb suport per a entrada interactiva.
---

## Funcionalitats destacades
- Conversió automàtica de CFG a CNF.
- Eliminació de produccions buides i unitàries.
- Descomposició de regles llargues.
- Càlcul de probabilitats en la versió probabilística.
- Interfície interactiva i guiada.
- Comentaris explicatius en el codi.
