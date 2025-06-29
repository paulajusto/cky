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

## Ús

### Execució CKY bàsic
\`\`\`bash
python main.py
\`\`\`
**Format del fitxer d’entrada:**
\`\`\`
S 3
AB BC ε
A 2
BA a
B 2
CC b
C 2
AB a
paraules 3 ab a ε
\`\`\`
El programa comprovarà si cada paraula pertany a la gramàtica.

---

### Execució CKY probabilístic
\`\`\`bash
python main_probabilistic.py
\`\`\`
**Format del fitxer d’entrada:**
\`\`\`
S 1
ε 0.2
S 2
B A 0.8
A 1
a 1
B 1
b 1
paraules 3 ba a ε
\`\`\`
El programa mostrarà si la paraula pertany i la probabilitat de derivació més probable.

---

### Execució interactiva
\`\`\`bash
python main_interactiu.py
\`\`\`
Permet:
1. Crear una gramàtica manualment.
2. Escollir entre CKY bàsic (amb conversió automàtica a CNF si cal) o CKY probabilístic.
3. Introduir paraules i verificar si pertanyen a la gramàtica.

---

## Funcionalitats destacades
- Conversió automàtica de CFG a CNF.
- Eliminació de produccions buides i unitàries.
- Descomposició de regles llargues.
- Càlcul de probabilitats en la versió probabilística.
- Interfície interactiva i guiada.
- Comentaris explicatius en el codi.
