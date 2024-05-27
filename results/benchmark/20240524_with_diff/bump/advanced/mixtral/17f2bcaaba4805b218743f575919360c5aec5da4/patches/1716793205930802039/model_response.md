Here's the fixed version of the client code:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ...

int size = new PointIndexMMWrapper().size();
size = new PHTreeMMP().size();
size = new MinHeap().size();
size = new MinHeapI() {}.size();
size = new MinMaxHeap().size();
size = new MinMaxHeapI() {}.size();
```
This code imports the new classes that were added in the library and creates instances of them to call the `size()` method. Note that I created an anonymous inner class implementation for the interfaces `MinHeapI` and `MinMaxHeapI` to call their `size()` method.