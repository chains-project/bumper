Here's a possible patch for the failing client code:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ...

int size = new PointIndexMMWrapper().size();
size += new PHTreeMMP().size();
size += new MinHeap().size();
size += new MinHeapI().size();
size += new MinMaxHeap().size();
size += new MinMaxHeapI().size();
```
Note that I replaced the failing import statement with several import statements for the new library version, and added a code block that creates instances of each of the new size()-providing classes and sums their sizes. This should fix the error and allow the code to compile with the new library version.