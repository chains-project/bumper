Here's the fixed version of the client code:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

// ...
```
This code imports the new classes that were added in the library update. Note that the `PConstants` class from the `processing.core` package was removed, so it's no longer needed in the client code.