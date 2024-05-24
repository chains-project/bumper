Here's the proposed patch:
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
    XoRoShiRo128PlusRandom r = new XoRoShiRo128PlusRandom();
    // ...

    PointIndexMMWrapper index = new PointIndexMMWrapper();
    // ...

    PHTreeMMP tree = new PHTreeMMP();
    // ...

    MinHeap<Node> minHeap = new MinHeap<>();
    // ...

    MinMaxHeap<Node> minMaxHeap = new MinMaxHeap<>();
    // ...
  }
}
```
This patch replaces the import statement with the new library import statements and updates the class names accordingly.