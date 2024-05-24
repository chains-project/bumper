Here's the proposed patch:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ...

public int getNumberOfPoints() {
  int size = 0;
  size += new PointIndexMMWrapper().size();
  size += new PHTreeMMP().size();
  size += new MinHeap().size();
  size += new MinHeapI().size();
  size += new MinMaxHeap().size();
  size += new MinMaxHeapI().size();
  return size;
}
```
This code imports the new libraries and creates instances of the classes that have the `size()` method. It then calculates the size of each instance and sums them up to return the total size. This should resolve the error.