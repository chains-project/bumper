Here's the patched code:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_smooth() {
    org.junit.jupiter.api.Assertions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smooth(GROUP_SHAPE, 0.5);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

In this case, I replaced `org.junit.Assume.assumeTrue` with `org.junit.jupiter.api.Assertions.assumeTrue` since `org.junit.Assume` is not available in Jupiter (which seems to be the version of JUnit used here).