Here's a fixed version of the client code:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ...

XoRoShiRo128PlusRandom rnd = new XoRoShiRo128PlusRandom();

// ...

int size = new PointIndexMMWrapper().size();
size += new PHTreeMMP().size();
size += new MinHeap().size();
size += new MinHeapI().size();
size += new MinMaxHeap().size();
size += new MinMaxHeapI().size();
```
The code imports the new classes from the updated library and uses the new `size()` methods in the new classes.