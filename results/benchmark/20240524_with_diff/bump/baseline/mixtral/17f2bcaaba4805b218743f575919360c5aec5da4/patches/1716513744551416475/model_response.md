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
  public void testGetNearestNeighbors() {
    XoRoShiRo128PlusRandom r = new XoRoShiRo128PlusRandom();
    PointIndexMMWrapper index = new PointIndexMMWrapper(100, 2);
    // ...
    int size = index.size(); // use the new size() method
    // ...
  }

  // ...
}
```
The patch replaces the import statement with the new library import statements. It also uses the new `size()` method from the new library classes.