Here's the proposed patch:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_round() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```

The error is caused by the use of `org.junit.Assume.assumeTrue`, which is not available in JUnit 5. I replaced it with `org.junit.jupiter.api.Assertions.assertTrue`.

Additionally, I added the necessary import statements for the static imports used in the fixed code.