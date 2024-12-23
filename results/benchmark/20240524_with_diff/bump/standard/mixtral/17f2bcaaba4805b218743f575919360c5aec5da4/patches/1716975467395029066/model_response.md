Here's the fixed version of the client code:
```java
import processing.core.PShape;
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ...

public void testSize() {
    PointIndexMMWrapper pi = new PointIndexMMWrapper();
    PHTreeMMP phtree = new PHTreeMMP();
    MinHeap minHeap = new MinHeap();
    MinHeapI minHeapI = new MinHeap();
    MinMaxHeap minMaxHeap = new MinMaxHeap();
    MinMaxHeapI minMaxHeapI = new MinMaxHeap();

    int piSize = pi.size();
    int phtreeSize = phtree.size();
    int minHeapSize = minHeap.size();
    int minHeapISize = minHeapI.size();
    int minMaxHeapSize = minMaxHeap.size();
    int minMaxHeapISize = minMaxHeapI.size();

    System.out.println("PointIndexMMWrapper size: " + piSize);
    System.out.println("PHTreeMMP size: " + phtreeSize);
    System.out.println("MinHeap size: " + minHeapSize);
    System.out.println("MinHeapI size: " + minHeapISize);
    System.out.println("MinMaxHeap size: " + minMaxHeapSize);
    System.out.println("MinMaxHeapI size: " + minMaxHeapISize);
}
```
The code above now imports all the necessary classes that include the `size()` method. This should resolve the "class, interface, or enum expected" error.