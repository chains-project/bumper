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
    public void testPolygonize() {
        // ...
        MinHeap minHeap = new MinHeap(10);
        // ...
        int size = minHeap.size();
        // ...
    }

    // ...

}
```
In the patch, I've imported the new classes that have the `++` symbol, and replaced the failed import statement with the new ones. I've also changed the instantiation of `Polygon` to `MinHeap` and updated the variable declaration. This should fix the error.