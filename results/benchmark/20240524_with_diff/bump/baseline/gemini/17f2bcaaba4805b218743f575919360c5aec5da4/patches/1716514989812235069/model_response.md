```java
  import org.tinspin.index.PointIndexMMWrapper;
  import org.tinspin.index.phtree.PHTreeMMP;
  import org.tinspin.index.util.MinHeap;
  import org.tinspin.index.util.MinMaxHeap;

  import static org.junit.Assume.assumeTrue;

  public class PGS_MorphologyGroupShapeTests {

    @Test
    public void test_morphology_group_shape_1() {
      assumeTrue(PointIndexMMWrapper.size() > 0);
      assumeTrue(PHTreeMMP.size() > 0);
      assumeTrue(MinHeap.size() > 0);
      assumeTrue(MinMaxHeap.size() > 0);
    }
  }
```