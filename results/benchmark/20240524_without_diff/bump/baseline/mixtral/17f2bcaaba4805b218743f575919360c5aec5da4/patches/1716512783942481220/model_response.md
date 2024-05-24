Here's a possible patch for the failing client code:

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

This code creates instances of the new classes that were added in the updated library, and calls their `size()` method. Note that the `size` variable is used to accumulate the size of each index, but you can replace it with any other variable name or even remove it if it's not needed in your application.