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
        int size = new PointIndexMMWrapper().size(); // use new added method
        // ...
        size = new PHTreeMMP().size(); // use new added method
        // ...
        size = new MinHeap().size(); // use new added method
        // ...
        size = new MinHeapI().size(); // use new added method
        // ...
        size = new MinMaxHeap().size(); // use new added method
        // ...
        size = new MinMaxHeapI().size(); // use new added method
        // ...
    }

    // ...

}
```
The patch replaces the failing import statement and modifies the `testPolygonize` method to use the newly added `size()` methods from the updated library.