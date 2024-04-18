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
  public void testSizeMethods() {
    PointIndexMMWrapper pointIndexMMWrapper = new PointIndexMMWrapper();
    int size1 = pointIndexMMWrapper.size();

    PHTreeMMP pHTreeMMP = new PHTreeMMP();
    int size2 = pHTreeMMP.size();

    MinHeap minHeap = new MinHeap();
    int size3 = minHeap.size();

    MinHeapI minHeapI = new MinHeapI();
    int size4 = minHeapI.size();

    MinMaxHeap minMaxHeap = new MinMaxHeap();
    int size5 = minMaxHeap.size();

    MinMaxHeapI minMaxHeapI = new MinMaxHeapI();
    int size6 = minMaxHeapI.size();
  }
}
```