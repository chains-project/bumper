Here's a possible patch for the failing code:

```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ...

XoRoShiRo128PlusRandom rnd = new XoRoShiRo128PlusRandom();

// ...

public int getRandomPointsCount() {
    int count = 0;
    count += new PointIndexMMWrapper().size();
    count += new PHTreeMMP().size();
    MinHeap<Double> minHeap = new MinHeap<>();
    count += minHeap.size();
    MinHeapI<Double> minHeapI = new MinHeap<>();
    count += minHeapI.size();
    MinMaxHeap<Double> minMaxHeap = new MinMaxHeap<>();
    count += minMaxHeap.size();
    MinMaxHeapI<Double> minMaxHeapI = new MinMaxHeap<>();
    count += minMaxHeapI.size();
    return count;
}
```

This patch imports the new classes from the updated library and uses the new `size()` methods to calculate the random points count. It creates instances of the new classes and calls the `size()` method on each of them. The `Override` decorator has been removed from the `getRandomPointsCount()` method since it's not overriding any method in the new version.