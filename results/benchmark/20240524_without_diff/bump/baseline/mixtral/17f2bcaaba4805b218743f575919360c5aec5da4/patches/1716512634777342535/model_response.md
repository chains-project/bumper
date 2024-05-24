Here's the proposed patch for the given client code:

```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ... (other imports and class definition)

public class FastPolygonizerTests {
  // ... (other fields and methods)

  @Test
  @Override
  public void testLineString() {
    LineString lineString = ... // initialize LineString
    int size = new PointIndexMMWrapper().size(); // use a new instance of PointIndexMMWrapper
    assertEquals(size, 0);

    // ... (other test code)
  }
}
```

In the given code, I've introduced new imports for the classes that have the `size()` method. In the `testLineString()` method, I created a new instance of `PointIndexMMWrapper` and used its `size()` method. This should fix the error as it uses an added method in the new library version.