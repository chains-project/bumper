Here's a possible patch that you can apply to the failing client code:
```java
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

// ...

int size = new PointIndexMMWrapper().size();
size += new PHTreeMMP().size();
size += new MinHeap().size();
size += new MinMaxHeap().size();
```
This code creates instances of the new classes that were added in the updated library, and calls their `size()` method to compute the total size. You can replace the existing failing line of code with the above code snippet to fix the error.