Here's the proposed patch:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ...

public class FastPolygonizerTests {
    // ...

    @Test
    @Override
    public void testSize() {
        PointIndexMMWrapper index = new PointIndexMMWrapper();
        PHTreeMMP phtree = new PHTreeMMP();
        MinHeap minHeap = new MinHeap();
        MinHeapI minHeapI = new MinHeap();
        MinMaxHeap minMaxHeap = new MinMaxHeap();
        MinMaxHeapI minMaxHeapI = new MinMaxHeap();

        int indexSize = index.size();
        int phtreeSize = phtree.size();
        int minHeapSize = minHeap.size();
        int minHeapISize = minHeapI.size();
        int minMaxHeapSize = minMaxHeap.size();
        int minMaxHeapISize = minMaxHeapI.size();

        // ...
    }

    // ...
}
```
In the proposed patch, the import statement for the `XoRoShiRo128PlusRandom` class has been replaced with import statements for the new classes added in the updated library version. The `testSize()` method has been updated to use the new classes.