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

The failure is caused by the fact that the `assumeTrue` method is not available in JUnit 5, which is used by the client code. The `assertTrue` method can be used instead.