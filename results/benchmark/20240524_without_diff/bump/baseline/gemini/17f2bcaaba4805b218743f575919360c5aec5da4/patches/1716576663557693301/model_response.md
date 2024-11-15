```java
@Test
void test_PGS_Morphology_minkDifference() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    final PShape mink = new PShape(PShape.PATH);
    mink.beginShape();
    mink.vertex(0, 0);
    mink.vertex(5, 0);
    mink.vertex(5, 5);
    mink.vertex(0, 5);
    mink.endShape(PConstants.CLOSE);

    PShape out = PGS_Morphology.minkDifference(GROUP_SHAPE, mink);

    // Check if the output shape has two children.
    assertEquals(2, out.getChildCount());

    // Check if the first child of the output shape has the expected coordinates.
    PShape child1 = (PShape) out.getChildren().get(0);
    assertEquals(new PVector(0, 0), child1.getVertex(0));
    assertEquals(new PVector(5, 0), child1.getVertex(1));
    assertEquals(new PVector(5, 5), child1.getVertex(2));
    assertEquals(new PVector(0, 5), child1.getVertex(3));

    // Check if the second child of the output shape has the expected coordinates.
    PShape child2 = (PShape) out.getChildren().get(1);
    assertEquals(new PVector(0, 0), child2.getVertex(0));
    assertEquals(new PVector(0, 5), child2.getVertex(1));
    assertEquals(new PVector(5, 5), child2.getVertex(2));
    assertEquals(new PVector(5, 0), child2.getVertex(3));
}
```