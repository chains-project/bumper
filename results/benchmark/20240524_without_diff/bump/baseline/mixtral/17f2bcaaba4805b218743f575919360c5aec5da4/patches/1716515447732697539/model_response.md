Here's a possible patch for the failing client code:

```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

// ...

int sizeOfIndexWrapper = new PointIndexMMWrapper().size();
int sizeOfPHTreeMMP = new PHTreeMMP().size();
int sizeOfMinHeap = new MinHeap().size();
int sizeOfMinMaxHeap = new MinMaxHeap().size();
```

This code creates instances of the new classes that were added in the updated library version, and calls their `size()` method. This should fix the error by using the new methods that were added in the updated library version.