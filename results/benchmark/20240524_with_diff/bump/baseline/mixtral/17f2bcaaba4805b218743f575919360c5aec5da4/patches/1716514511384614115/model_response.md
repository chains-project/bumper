Here's a possible patch for the given client code:

```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

// ...

public class FastPolygonizerTests {

    // ...

    @Test
    public void testFastPolygonizer() {
        PointIndexMMWrapper index = new PointIndexMMWrapper();
        PHTreeMMP phtree = new PHTreeMMP();
        MinHeap minHeap = new MinHeap();
        MinMaxHeap minMaxHeap = new MinMaxHeap();

        // ...

        assertEquals(index.size(), 10);
        assertEquals(phtree.size(), 5);
        assertEquals(minHeap.size(), 3);
        assertEquals(minMaxHeap.size(), 7);
    }
}
```

In this patch, I've imported the new classes that were added in the updated library version. I've then created instances of these classes and used them in the `testFastPolygonizer()` method. Finally, I've added assertions to check the size of these objects using their `size()` methods. This should fix the error and allow the code to compile and run successfully.