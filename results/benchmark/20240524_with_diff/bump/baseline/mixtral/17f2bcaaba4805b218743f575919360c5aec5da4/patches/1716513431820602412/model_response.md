Here's the proposed patch:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ...

int size = new PointIndexMMWrapper().size();
size = new PHTreeMMP().size();
size = new MinHeap().size();
size = new MinHeapI().size();
size = new MinMaxHeap().size();
size = new MinMaxHeapI().size();
```
This patch imports the new classes from the updated library and uses their `size()` methods. Note that the original import statement is replaced with the new imports.