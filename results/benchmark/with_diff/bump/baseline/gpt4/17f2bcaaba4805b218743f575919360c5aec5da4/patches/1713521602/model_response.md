```java
import org.junit.jupiter.api.Test;
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinHeapI;
import org.tinspin.index.util.MinMaxHeap;
import org.tinspin.index.util.MinMaxHeapI;

public class PGS_MeshingTests {

    @Test
    public void testSize() {
        PointIndexMMWrapper pointIndexMMWrapper = new PointIndexMMWrapper();
        int size = pointIndexMMWrapper.size();
        PHTreeMMP phtreeMMP = new PHTreeMMP();
        size = phtreeMMP.size();
        MinHeap minHeap = new MinHeap();
        size = minHeap.size();
        MinHeapI minHeapI = new MinHeapI();
        size = minHeapI.size();
        MinMaxHeap minMaxHeap = new MinMaxHeap();
        size = minMaxHeap.size();
        MinMaxHeapI minMaxHeapI = new MinMaxHeapI();
        size = minMaxHeapI.size();
    }
}
```