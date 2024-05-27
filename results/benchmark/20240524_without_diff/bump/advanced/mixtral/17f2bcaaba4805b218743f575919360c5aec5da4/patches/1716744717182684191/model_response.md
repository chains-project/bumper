Here is the proposed patch:

```java
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_erosionDilation() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The failure is caused by the use of `Assume.assumeTrue` from JUnit 4, while the test is being executed with JUnit 5. I replaced it with `assertTrue` from JUnit 5.