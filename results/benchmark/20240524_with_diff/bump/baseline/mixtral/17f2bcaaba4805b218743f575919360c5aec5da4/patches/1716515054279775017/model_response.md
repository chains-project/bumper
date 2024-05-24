Here's a possible patch for the client code:

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
  public void testGetNumberOfPoints() {
    PointIndexMMWrapper index = new PointIndexMMWrapper();
    // ...
    int size = index.size(); // use new size() method
    // ...
  }

  // ...

  @Test
  public void testGetNumberOfPoints2() {
    PHTreeMMP index = new PHTreeMMP();
    // ...
    int size = index.size(); // use new size() method
    // ...
  }

  // ...

  @Test
  public void testGetNumberOfPoints3() {
    MinHeap<Node> index = new MinHeap<>();
    // ...
    int size = index.size(); // use new size() method
    // ...
  }

  // ...

  @Test
  public void testGetNumberOfPoints4() {
    MinHeapI<Node> index = new MinHeap<>();
    // ...
    int size = index.size(); // use new size() method
    // ...
  }

  // ...

  @Test
  public void testGetNumberOfPoints5() {
    MinMaxHeap<Node> index = new MinMaxHeap<>();
    // ...
    int size = index.size(); // use new size() method
    // ...
  }

  // ...

  @Test
  public void testGetNumberOfPoints6() {
    MinMaxHeapI<Node> index = new MinMaxHeap<>();
    // ...
    int size = index.size(); // use new size() method
    // ...
  }

  // ...

}
```

In this patch, I've added imports for the new classes that have a `size()` method. Then, I've replaced the calls to `getNumberOfPoints()` with calls to `size()` for each test method. This should fix the error by using the new `size()` method provided by the updated library.