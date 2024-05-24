Here's a possible patch for the failing client code:

```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

// ...

public class FastPolygonizerTests {

  // ...

  @Test
  public void testGetEnvelope() {
    // ...
    int size = new PointIndexMMWrapper().size(); // use PointIndexMMWrapper.size()
    assertTrue(size > 0);
    size = new PHTreeMMP().size(); // use PHTreeMMP.size()
    assertTrue(size > 0);
    size = new MinHeap(10).size(); // use MinHeap.size()
    assertTrue(size == 10);
    size = new MinMaxHeap(10).size(); // use MinMaxHeap.size()
    assertTrue(size == 10);
    // ...
  }

  // ...

}
```

This patch replaces the failing import statement with the necessary imports to use the new library methods. It also adds instances of the classes with the new `size()` method and calls the method on those instances. Note that the `@Override` decorator has been removed from the `testGetEnvelope()` method since it's not overriding any method in the new version.