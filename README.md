# <span style="color:purple"> **Game of Life** </span>

Personal implementation of the <span style="color:purple"> **John Conway's Game of Life** </span> with a combination of <span style="color:purple"> *Python* </span> and <span style="color:purple"> *C* </span>.

---

First, you need to build the <span style="color:purple"> **DLLs** </span> as follows (for Windows):

``gcc -shared -o lib/<name_file>.dll src/c/<name_file>.c``

For Linux:

``gcc -fPIC -shared -o lib/<name_file>.so src/c/<name_file>.c``

---

List of C/C++ files to build: