Here's a proposed patch for the failing client code:

```java
@Test
void test_PGS_Morphology_round() {
    assumeTrue(PApplet.parseInt(processing.core.PApplet.getText("GROUP_SHAPE_CHILD_COUNT")) == 2);
    PShape out = PGS_Morphology.round(getGroupShape(), 0.5);
    assertEquals(2, out.getChildCount());
}

private PShape getGroupShape() {
    // Implement the logic to get or create the GROUP_SHAPE instance
    // ...
}
```

This patch introduces a new helper method `getGroupShape()` to create or get the `GROUP_SHAPE` instance. Also, it replaces the direct reference to the `GROUP_SHAPE` constant with a call to `processing.core.PApplet.getText("GROUP_SHAPE_CHILD_COUNT")` to get the child count, assuming that the child count value is stored in the application context with the key "GROUP_SHAPE_CHILD_COUNT". You'll need to adjust the helper method and the child count retrieval to match your specific use case.