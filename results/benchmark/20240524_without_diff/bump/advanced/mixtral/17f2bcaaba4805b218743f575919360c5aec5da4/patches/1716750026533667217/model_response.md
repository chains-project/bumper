Here is the proposed patch:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

@Test
void test_PGS_Morphology_round() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```

The issue is caused by the use of `org.junit.Assume.assumeTrue` which is not present in JUnit 5. The method has been replaced by `org.junit.jupiter.api.Assertions.assertTrue` in JUnit 5.