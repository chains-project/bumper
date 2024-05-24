Here's the proposed patch:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

// ...

public int getNumberOfPoints() {
  int count = 0;
  count += new PointIndexMMWrapper().size();
  count += new PHTreeMMP().size();
  MinHeap minHeap = new MinHeap();
  count += minHeap.size();
  MinMaxHeap minMaxHeap = new MinMaxHeap();
  count += minMaxHeap.size();
  return count;
}
```
In this patch, I've imported the new classes and used the new `size()` methods from the updated library. I created instances of the new classes and called their `size()` methods. This should resolve the error.