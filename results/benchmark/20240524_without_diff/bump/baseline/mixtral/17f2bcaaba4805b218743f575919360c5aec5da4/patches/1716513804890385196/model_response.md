Here's the proposed patch for the failing client code:
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
    void testPolygonizer() {
        XoRoShiRo128PlusRandom rnd = new XoRoShiRo128PlusRandom();
        PointIndexMMWrapper index = new PointIndexMMWrapper();
        // ...
        int size = index.size();
        // ...
    }

    // ...
}
```
The patch imports the necessary classes from the updated library and replaces the failed import statement. The `size()` method is called on an instance of `PointIndexMMWrapper`, which is available in the updated library.