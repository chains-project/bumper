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
The code above imports the new classes that were added in the library version. By doing this, the error message should disappear. Note that the `PConstants` class from the `processing.core` package was removed from the import statement, as it was causing the error.