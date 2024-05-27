Here is a proposed patch for the failing client code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Processing_removeSmallHoles() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Processing.removeSmallHoles(GROUP_SHAPE, 10);
    assertEquals(2, out.getChildCount());
}
```

This patch replaces the `assumeTrue` method with `assertTrue`, which has the same behavior but does not throw an exception if the condition is false. This should fix the "cannot find symbol" error.