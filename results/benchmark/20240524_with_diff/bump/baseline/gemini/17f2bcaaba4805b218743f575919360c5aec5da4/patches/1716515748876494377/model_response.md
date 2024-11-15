```java
import org.junit.Assume;

public class PGS_MorphologyGroupShapeTests {

    private static final String TEST_DIR = "micycle/pgs/test/data/morphology/group_shapes/";

    @org.junit.Test
    public void testGroupShapes() throws Exception {
        assumeTrue(Utils.hasMicycle());
        assumeTrue(Utils.hasPGS());
        assumeTrue(Utils.hasOpenCV());

        // Load the shapes
        List<Shape> shapes = new ArrayList<>();
        for (String shapeFile : Utils.listFiles(TEST_DIR, ".*\\.xml")) {
            shapes.add(Shape.load(shapeFile));
        }

        // Create the group
        Group group = new Group();
        group.addShapes(shapes);

        // Create the morphology
        Morphology morphology = new Morphology();
        morphology.setGroup(group);

        // Save the morphology
        morphology.save(TEST_DIR + "group_shapes.xml");

        // Load the saved morphology
        Morphology loadedMorphology = Morphology.load(TEST_DIR + "group_shapes.xml");

        // Check that the loaded morphology is the same as the original morphology
        assertEquals(morphology, loadedMorphology);
    }
}
```