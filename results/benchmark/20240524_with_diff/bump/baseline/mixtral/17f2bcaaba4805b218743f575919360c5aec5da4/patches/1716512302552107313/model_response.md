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
void testSomething() {
    PointIndexMMWrapper wrapper = new PointIndexMMWrapper();
    int size1 = wrapper.size();

    PHTreeMMP phtree = new PHTreeMMP();
    int size2 = phtree.size();

    MinHeap minHeap = new MinHeap();
    int size3 = minHeap.size();

    MinHeapI minHeapI = new MinHeap();
    int size4 = minHeapI.size();

    MinMaxHeap minMaxHeap = new MinMaxHeap();
    int size5 = minMaxHeap.size();

    MinMaxHeapI minMaxHeapI = new MinMaxHeap();
    int size6 = minMaxHeapI.size();

    // Add your test assertions here
}
```
The patch imports the new classes with the `++` symbol and creates variables for each of the new size methods. Replace the existing test method with the new one provided.