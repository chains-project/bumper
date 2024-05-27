```java
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

@RunWith(JUnit4.class)
public class PGS_MeshingTests {

  @Test
  public void test_PHTreeMMP_size() {
    PHTreeMMP phtree = new PHTreeMMP(10, 20, 30);
    assertEquals(0, phtree.size());
    phtree.add(new int[]{1, 2, 3});
    assertEquals(1, phtree.size());
  }

  @Test
  public void test_PointIndexMMWrapper_size() {
    PointIndexMMWrapper pointIndex = new PointIndexMMWrapper(10, 20, 30);
    assertEquals(0, pointIndex.size());
    pointIndex.add(new int[]{1, 2, 3});
    assertEquals(1, pointIndex.size());
  }

  @Test
  public void test_MinHeap_size() {
    MinHeap heap = new MinHeap(10);
    assertEquals(0, heap.size());
    heap.add(1);
    assertEquals(1, heap.size());
  }

  @Test
  public void test_MinMaxHeap_size() {
    MinMaxHeap heap = new MinMaxHeap(10);
    assertEquals(0, heap.size());
    heap.add(1);
    assertEquals(1, heap.size());
  }
}
```