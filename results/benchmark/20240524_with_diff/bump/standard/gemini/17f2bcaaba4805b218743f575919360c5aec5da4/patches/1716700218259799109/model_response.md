```java
import org.junit.Assume;

public class PGS_ProcessingGroupShapeTests {

    public void testPointIndexMM() {
        assumeTrue(org.tinspin.index.PointIndexMMWrapper.size() > 0);
    }

    public void testPHTreeMMP() {
        assumeTrue(org.tinspin.index.phtree.PHTreeMMP.size() > 0);
    }

    public void testMinHeap() {
        assumeTrue(org.tinspin.index.util.MinHeap.size() > 0);
    }

    public void testMinHeapI() {
        assumeTrue(org.tinspin.index.util.MinHeapI.size() > 0);
    }

    public void testMinMaxHeap() {
        assumeTrue(org.tinspin.index.util.MinMaxHeap.size() > 0);
    }

    public void testMinMaxHeapI() {
        assumeTrue(org.tinspin.index.util.MinMaxHeapI.size() > 0);
    }
}
```