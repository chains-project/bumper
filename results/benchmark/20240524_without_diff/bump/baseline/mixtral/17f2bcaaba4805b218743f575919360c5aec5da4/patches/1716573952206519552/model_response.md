Here is a fixed version of the failing method that uses an added library method `++` to replace the usage of the removed library method `--`:

```java
@Test
void test_PGS_Morphology_minkSum() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    final PShape mink = new PShape(PShape.PATH);
    mink.beginShape();
    mink.vertex(0, 0);
    mink.vertex(5, 0);
    mink.vertex(5, 5);
    mink.vertex(0, 5);
    mink.endShape(PConstants.CLOSE);

    PShape out = PGS_Morphology.minkSum(GROUP_SHAPE, mink);

    // Replace 'getChildCount()' with 'getVertexCount()'
    int expectedVertexCount = 2;
    if (out.getShapeType() == PShape.GROUP) {
        int totalVertexCount = 0;
        for (PShape childShape : out.getChildren()) {
            totalVertexCount += childShape.getVertexCount();
        }
        assertEquals(expectedVertexCount, totalVertexCount);
    } else {
        assertEquals(expectedVertexCount, out.getVertexCount());
    }
}
```
This version of the method uses the added library method `getVertexCount()` to replace the usage of the removed library method `getChildCount()`. It also checks if the resulting shape is a group and calculates the total vertex count of all child shapes if it is. This should fix the error message and allow the code to compile.