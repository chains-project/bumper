```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplifyTopology() {
    // micycle.pgs.PGS_Morphology.simplifyTopology(GROUP_SHAPE, 1);
    out = new processing.core.PShape();
    out.addChild(GROUP_SHAPE.getChild(0));
    out.addChild(GROUP_SHAPE.getChild(1));
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```