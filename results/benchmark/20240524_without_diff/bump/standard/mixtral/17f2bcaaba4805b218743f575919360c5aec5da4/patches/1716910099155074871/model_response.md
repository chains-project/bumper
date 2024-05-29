Here is a potential patch for the code you provided:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_chaikinCut() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.chaikinCut(GROUP_SHAPE, 0.5, 2);
    assertEquals(2, out.getChildCount());
}
```

This patch imports the `assumeTrue` method from the `org.junit.jupiter.api.Assumptions` class, which should resolve the "cannot find symbol" error.

It's worth noting that this error can also occur if the `JUnit Jupiter` library is not included in the classpath. If the error persists after applying this patch, you may need to ensure that the library is properly installed and configured.