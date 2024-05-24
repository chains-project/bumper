Here is a possible patch for the failing client code:
```java
import processing.core.PShape;
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

// ...

public class FastPolygonizerTests {

  // ...

  @Test
  public void testSomething() {
    // ...

    int size = new PointIndexMMWrapper().size();
    System.out.println("PointIndexMMWrapper size: " + size);

    size = new PHTreeMMP().size();
    System.out.println("PHTreeMMP size: " + size);

    size = new MinHeap().size();
    System.out.println("MinHeap size: " + size);

    size = new MinMaxHeap().size();
    System.out.println("MinMaxHeap size: " + size);

    // ...
  }

  // ...

}
```
In this patch, I have added imports for the new classes that have a `size()` method, and I have created instances of those classes to call the `size()` method. This should fix the error by using the new methods added in the updated dependency version.