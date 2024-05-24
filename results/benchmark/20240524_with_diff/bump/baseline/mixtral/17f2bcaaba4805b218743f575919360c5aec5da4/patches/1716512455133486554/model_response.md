Here's a proposed patch for the failing client code:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

// ...

public class FastPolygonizerTests {

    // ...

    @Test
    public void testLineString() {
        PointIndexMMWrapper index = new PointIndexMMWrapper();
        // ...
        int size = index.size(); // use the new size() method from PointIndexMMWrapper

        PHTreeMMP phtree = new PHTreeMMP();
        // ...
        size = phtree.size(); // use the new size() method from PHTreeMMP

        MinHeap minHeap = new MinHeap();
        // ...
        size = minHeap.size(); // use the new size() method from MinHeap

        MinMaxHeap minMaxHeap = new MinMaxHeap();
        // ...
        size = minMaxHeap.size(); // use the new size() method from MinMaxHeap
    }

    // ...

}
```
The changes made include importing the new classes that have a `size()` method and using those methods in the test method. This should fix the error caused by the dependency update.