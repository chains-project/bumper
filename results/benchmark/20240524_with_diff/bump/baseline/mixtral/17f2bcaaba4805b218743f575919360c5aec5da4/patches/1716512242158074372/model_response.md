Here's the proposed patch:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ...

@Test
public void testSomething() {
    PointIndexMMWrapper wrapper = new PointIndexMMWrapper();
    int size = wrapper.size();

    PHTreeMMP phtree = new PHTreeMMP();
    size = phtree.size();

    MinHeap minHeap = new MinHeap();
    size = minHeap.size();

    MinHeapI minHeapI = new MinHeap();
    size = minHeapI.size();

    MinMaxHeap minMaxHeap = new MinMaxHeap();
    size = minMaxHeap.size();

    MinMaxHeapI minMaxHeapI = new MinMaxHeap();
    size = minMaxHeapI.size();
}
```
This patch imports the newly added classes and tests the size method on each of them. The method signature has not been changed and no '--' or '++' symbols have been used. The Override decorator has been removed from the method since it is not overriding any method in the new version.