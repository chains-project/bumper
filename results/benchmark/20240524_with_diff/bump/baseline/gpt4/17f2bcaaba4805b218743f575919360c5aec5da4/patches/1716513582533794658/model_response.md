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
    public void sizeTest() {
        PointIndexMMWrapper pointIndexMMWrapper = new PointIndexMMWrapper();
        int pointIndexMMWrapperSize = pointIndexMMWrapper.size();

        PHTreeMMP phtreeMMP = new PHTreeMMP();
        int phtreeMMPSize = phtreeMMP.size();

        MinHeap minHeap = new MinHeap();
        int minHeapSize = minHeap.size();

        MinHeapI minHeapI = new MinHeapI();
        int minHeapISize = minHeapI.size();

        MinMaxHeap minMaxHeap = new MinMaxHeap();
        int minMaxHeapSize = minMaxHeap.size();

        MinMaxHeapI minMaxHeapI = new MinMaxHeapI();
        int minMaxHeapISize = minMaxHeapI.size();
    }
}
```