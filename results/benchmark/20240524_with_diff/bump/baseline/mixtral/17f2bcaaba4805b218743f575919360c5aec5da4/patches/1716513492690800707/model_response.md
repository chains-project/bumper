Here's the proposed patch:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ...

int sizeOfPointIndexMMWrapper = new PointIndexMMWrapper().size();
int sizeOfPHTreeMMP = new PHTreeMMP().size();
int sizeOfMinHeap = new MinHeap().size();
int sizeOfMinHeapI = new MinHeapI().size();
int sizeOfMinMaxHeap = new MinMaxHeap().size();
int sizeOfMinMaxHeapI = new MinMaxHeapI().size();
```
Replace the original import statement and add the above code snippet to fix the error. The code snippet creates instances of the new classes and calls their `size()` method to ensure the code compiles with the updated library.