Here is a fixed version of the client code:
```java
import processing.core.PShape;
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

public class SomeClass {
    // existing code...

    public void someMethod() {
        // existing code...

        int size1 = new PointIndexMMWrapper().size();
        int size2 = new PHTreeMMP().size();
        int size3 = new MinHeap().size();
        int size4 = new MinHeapI().size();
        int size5 = new MinMaxHeap().size();
        int size6 = new MinMaxHeapI().size();

        // existing code...
    }
}
```
The changes I made include importing the new classes from the updated library and adding instances of those classes to call the new `size()` method. This should resolve the error you were seeing.