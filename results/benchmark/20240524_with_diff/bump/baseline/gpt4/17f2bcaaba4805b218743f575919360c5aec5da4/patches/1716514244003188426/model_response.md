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
    public void test() {
        PointIndexMMWrapper pointIndexMMWrapper = new PointIndexMMWrapper();
        int sizePointIndexMMWrapper = pointIndexMMWrapper.size();

        PHTreeMMP pHTreeMMP = new PHTreeMMP();
        int sizePHTreeMMP = pHTreeMMP.size();

        MinHeap minHeap = new MinHeap();
        int sizeMinHeap = minHeap.size();

        MinHeapI minHeapI = new MinHeapI();
        int sizeMinHeapI = minHeapI.size();

        MinMaxHeap minMaxHeap = new MinMaxHeap();
        int sizeMinMaxHeap = minMaxHeap.size();

        MinMaxHeapI minMaxHeapI = new MinMaxHeapI();
        int sizeMinMaxHeapI = minMaxHeapI.size();
    }
}
```