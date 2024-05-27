Here's the proposed patch for the failing client code:
```java
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

public class PGS_MorphologyGroupShapeTests {
    // existing code...

    @Test
    public void testSize() {
        PointIndexMMWrapper wrapper = new PointIndexMMWrapper();
        // ... use wrapper
        assertEquals(10, wrapper.size());

        PHTreeMMP phtree = new PHTreeMMP();
        // ... use phtree
        assertEquals(5, phtree.size());

        MinHeap<Double> minHeap = new MinHeap<>(10);
        // ... use minHeap
        assertEquals(3, minHeap.size());

        MinHeapI<Double> minHeapI = new MinHeapI<Double>() {
            @Override
            public int size() {
                // implementation
            }

            // override other methods as needed
        };
        // ... use minHeapI
        assertEquals(7, minHeapI.size());

        MinMaxHeap<Double> minMaxHeap = new MinMaxHeap<>(10);
        // ... use minMaxHeap
        assertEquals(4, minMaxHeap.size());

        MinMaxHeapI<Double> minMaxHeapI = new MinMaxHeapI<Double>() {
            @Override
            public int size() {
                // implementation
            }

            // override other methods as needed
        };
        // ... use minMaxHeapI
        assertEquals(6, minMaxHeapI.size());
    }
}
```
This patch adds imports for the new classes and interfaces, creates instances of them, and uses the `size()` method for each instance. The `assertEquals()` method is used to check the size of each instance. The `MinHeapI` and `MinMaxHeapI` interfaces require an implementation for the `size()` method.