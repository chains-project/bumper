Here's the fixed version of the code:

```java
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Processing_densify() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Processing.densify(GROUP_SHAPE, 1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

In this case, the method `assumeTrue` is not found, so I replaced it with `assertTrue`, which has the same behavior.