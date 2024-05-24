```java
import static org.junit.Assume.assumeTrue;
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

public class PGS_MorphologyGroupShapeTests {

  public void test_2D_disk_1() {
    assumeTrue(PointIndexMMWrapper.size() == 0);
    assumeTrue(PHTreeMMP.size() == 0);
    assumeTrue(MinHeap.size() == 0);
    assumeTrue(MinMaxHeap.size() == 0);
  }
}
```