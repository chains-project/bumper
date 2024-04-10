Here's a proposed patch to fix the error:
```java
import static org.junit.Assume.assumeTrue;

import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

public class PGS_MorphologyGroupShapeTests {
    // ...

    private void testSomething() {
        assumeTrue(PointIndexMMWrapper.size() > 0);
        assumeTrue(PHTreeMMP.size() > 0);
        assumeTrue(MinHeap.size() > 0);
        assumeTrue(MinMaxHeap.size() > 0);
    }
}
```
The patch imports the necessary classes and interfaces to use the `size()` methods, and also uses the `assumeTrue()` method to check that the size of the heaps is greater than zero.

Note that this patch only fixes the error in the given code snippet, and it's possible that there are other errors in the code that need to be addressed as well.