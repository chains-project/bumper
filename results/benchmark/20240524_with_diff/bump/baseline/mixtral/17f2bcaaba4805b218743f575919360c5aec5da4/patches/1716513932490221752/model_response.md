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
    public void testInsert() {
        XoRoShiRo128PlusRandom rnd = new XoRoShiRo128PlusRandom();
        PointIndexMMWrapper index = new PointIndexMMWrapper();

        for (int i = 0; i < 10000; i++) {
            index.insert(rnd.nextDouble(), rnd.nextDouble(), i);
        }

        assertEquals(10000, index.size());
    }

    // ...
}
```
The patch imports the new classes and uses the `size()` method from the new library version. The `XoRoShiRo128PlusRandom` import and usage remains unchanged.