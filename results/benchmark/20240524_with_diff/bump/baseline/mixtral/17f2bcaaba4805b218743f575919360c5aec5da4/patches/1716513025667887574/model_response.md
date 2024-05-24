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
        Polygonizer polygonizer = new Polygonizer();

        // ...

        int size = new PointIndexMMWrapper().size();
        System.out.println("PointIndexMMWrapper size: " + size);

        size = new PHTreeMMP().size();
        System.out.println("PHTreeMMP size: " + size);

        size = new MinHeap().size();
        System.out.println("MinHeap size: " + size);

        size = new MinMaxHeap().size();
        System.out.println("MinMaxHeap size: " + size);
    }
}
```
In this patch, I've imported the new classes that have the `size()` method and added print statements to display the size of different objects. This should resolve the error and provide you with the size of the objects.