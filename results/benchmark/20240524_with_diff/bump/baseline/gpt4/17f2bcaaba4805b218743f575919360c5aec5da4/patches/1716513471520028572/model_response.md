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
        PointIndexMMWrapper pointIndex = new PointIndexMMWrapper();
        int size = pointIndex.size();

        PHTreeMMP tree = new PHTreeMMP();
        int treeSize = tree.size();

        MinHeap minHeap = new MinHeap();
        int minHeapSize = minHeap.size();

        MinMaxHeap minMaxHeap = new MinMaxHeap();
        int minMaxHeapSize = minMaxHeap.size();
    }
  }
```