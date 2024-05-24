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
    public void testGetPolygons() {
        PointIndexMMWrapper index = new PointIndexMMWrapper();
        // ...
        int size = index.size(); // use the new size() method
        // ...
    }

    // ...

    @Test
    public void testGetPolygons2() {
        PHTreeMMP index = new PHTreeMMP();
        // ...
        int size = index.size(); // use the new size() method
        // ...
    }

    // ...

    @Test
    public void testGetPolygons3() {
        MinHeap<Point> index = new MinHeap<>(10);
        // ...
        int size = index.size(); // use the new size() method
        // ...
    }

    // ...

    @Test
    public void testGetPolygons4() {
        MinMaxHeap<Point> index = new MinMaxHeap<>(10);
        // ...
        int size = index.size(); // use the new size() method
        // ...
    }

    // ...
}
```
In this patch, I added import statements for the new classes that have a `size()` method. Then, in each of the failing tests, I replaced the call to the removed `size()` method with a call to the new `size()` method of the corresponding class. This should fix the error and make the code compile again.