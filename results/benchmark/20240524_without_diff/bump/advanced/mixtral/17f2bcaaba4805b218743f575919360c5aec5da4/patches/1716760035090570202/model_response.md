Here is the proposed patch for the failing client code:

```java
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Processing_removeSmallHoles() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Processing.removeSmallHoles(GROUP_SHAPE, 10);
    assertTrue(out.getChildCount() == 2);
}
```
In this patch, I replaced the `assumeTrue` method with `assertTrue` method from `org.junit.jupiter.api.Assertions` package. This change should fix the "cannot find symbol" error.