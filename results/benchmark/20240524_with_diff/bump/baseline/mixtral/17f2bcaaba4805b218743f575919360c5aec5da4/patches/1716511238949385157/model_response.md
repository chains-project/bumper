Here's the fixed version of the failing client code:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

// ...

XoRoShiRo128PlusRandom rnd = new XoRoShiRo128PlusRandom();

// ...

public int getSize() {
    int size = PointIndexMMWrapper.size();
    size += PHTreeMMP.size();
    MinHeap minHeap = new MinHeap(10);
    size += minHeap.size();
    MinMaxHeap minMaxHeap = new MinMaxHeap(10);
    size += minMaxHeap.size();
    return size;
}
```
In this fixed version, I replaced the failed import statement with the new ones, and added the necessary imports for the new library. I also created a new method `getSize()` that calculates the size by using the new `size()` methods from the updated library.