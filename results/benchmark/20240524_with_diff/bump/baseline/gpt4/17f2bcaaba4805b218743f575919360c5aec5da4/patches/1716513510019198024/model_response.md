```java
import org.junit.jupiter.api.Test;

public class PGS_MeshingTests {
    @Test
    public void testSize() {
        org.tinspin.index.PointIndexMMWrapper pointIndexMMWrapper = new org.tinspin.index.PointIndexMMWrapper();
        int size = pointIndexMMWrapper.size();

        org.tinspin.index.phtree.PHTreeMMP phtreeMMP = new org.tinspin.index.phtree.PHTreeMMP();
        size = phtreeMMP.size();

        org.tinspin.index.util.MinHeap minHeap = new org.tinspin.index.util.MinHeap();
        size = minHeap.size();

        org.tinspin.index.util.MinMaxHeap minMaxHeap = new org.tinspin.index.util.MinMaxHeap();
        size = minMaxHeap.size();
    }
}
```