Here's the proposed patch to fix the error:

```java
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplifyTopology() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.simplifyTopology(GROUP_SHAPE, 1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The fix involves importing the `assertTrue` method from `org.junit.jupiter.api.Assertions` to replace the `assumeTrue` method, since the latter is not available in JUnit 5. The `assumeTrue` method has been replaced by the `assertTrue` method in JUnit 5.