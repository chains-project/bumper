Here's a possible patch that you can apply to the failing client code:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

// ...

public class FastPolygonizerTests {
    // ...

    @Test
    public void testPolygonize() {
        PointIndexMMWrapper index = new PointIndexMMWrapper();
        PHTreeMMP phtree = new PHTreeMMP();
        MinHeap minHeap = new MinHeap();
        MinMaxHeap minMaxHeap = new MinMaxHeap();

        // ...

        int indexSize = index.size();
        int phtreeSize = phtree.size();
        int minHeapSize = minHeap.size();
        int minMaxHeapSize = minMaxHeap.size();

        // ...
    }

    // ...
}
```
In this patch, I have imported the new classes that have been added in the updated library version, and I have created instances of these classes. I have then called the `size()` method on these instances to get their sizes. This should fix the error that you were seeing.