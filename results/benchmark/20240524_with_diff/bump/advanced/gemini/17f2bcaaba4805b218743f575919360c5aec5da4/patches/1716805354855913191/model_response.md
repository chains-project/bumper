```java
import static org.junit.Assume.assumeTrue;

public class PGS_MorphologyGroupShapeTests {

    @org.junit.Test
    public void test_morphology_group_shape_1() throws Exception {
        // Prepare data
        final int numPoints = 1000;
        final int numShapes = 10;
        final double[] points = new double[numPoints * 3];
        final int[] shapes = new int[numPoints];
        for (int i = 0; i < numPoints; i++) {
            points[i * 3] = Math.random();
            points[i * 3 + 1] = Math.random();
            points[i * 3 + 2] = Math.random();
            shapes[i] = i % numShapes;
        }

        // Create morphology group shape
        final PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape(points, shapes);

        // Test morphology group shape
        assumeTrue(groupShape.getNumPoints() == numPoints);
        assumeTrue(groupShape.getNumShapes() == numShapes);
        for (int i = 0; i < numPoints; i++) {
            assumeTrue(groupShape.getPoint(i)[0] == points[i * 3]);
            assumeTrue(groupShape.getPoint(i)[1] == points[i * 3 + 1]);
            assumeTrue(groupShape.getPoint(i)[2] == points[i * 3 + 2]);
            assumeTrue(groupShape.getShape(i) == shapes[i]);
        }
    }

    @org.junit.Test
    public void test_morphology_group_shape_2() throws Exception {
        // Prepare data
        final int numPoints = 1000;
        final int numShapes = 10;
        final double[] points = new double[numPoints * 3];
        final int[] shapes = new int[numPoints];
        for (int i = 0; i < numPoints; i++) {
            points[i * 3] = Math.random();
            points[i * 3 + 1] = Math.random();
            points[i * 3 + 2] = Math.random();
            shapes[i] = i % numShapes;
        }

        // Create morphology group shape
        final PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape(points, shapes);

        // Test morphology group shape
        assumeTrue(groupShape.getNumPoints() == numPoints);
        assumeTrue(groupShape.getNumShapes() == numShapes);
        for (int i = 0; i < numPoints; i++) {
            assumeTrue(groupShape.getPoint(i)[0] == points[i * 3]);
            assumeTrue(groupShape.getPoint(i)[1] == points[i * 3 + 1]);
            assumeTrue(groupShape.getPoint(i)[2] == points[i * 3 + 2]);
            assumeTrue(groupShape.getShape(i) == shapes[i]);
        }
    }

    @org.junit.Test
    public void test_morphology_group_shape_3() throws Exception {
        // Prepare data
        final int numPoints = 1000;
        final int numShapes = 10;
        final double[] points = new double[numPoints * 3];
        final int[] shapes = new int[numPoints];
        for (int i = 0; i < numPoints; i++) {
            points[i * 3] = Math.random();
            points[i * 3 + 1] = Math.random();
            points[i * 3 + 2] = Math.random();
            shapes[i] = i % numShapes;
        }

        // Create morphology group shape
        final PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape(points, shapes);

        // Test morphology group shape
        assumeTrue(groupShape.getNumPoints() == numPoints);
        assumeTrue(groupShape.getNumShapes() == numShapes);
        for (int i = 0; i < numPoints; i++) {
            assumeTrue(groupShape.getPoint(i)[0] == points[i * 3]);
            assumeTrue(groupShape.getPoint(i)[1] == points[i * 3 + 1]);
            assumeTrue(groupShape.getPoint(i)[2] == points[i * 3 + 2]);
            assumeTrue(groupShape.getShape(i) == shapes[i]);
        }
    }

    @org.junit.Test
    public void test_morphology_group_shape_4() throws Exception {
        // Prepare data
        final int numPoints = 1000;
        final int numShapes = 10;
        final double[] points = new double[numPoints * 3];
        final int[] shapes = new int[numPoints];
        for (int i = 0; i < numPoints; i++) {
            points[i * 3] = Math.random();
            points[i * 3 + 1] = Math.random();
            points[i * 3 + 2] = Math.random();
            shapes[i] = i % numShapes;
        }

        // Create morphology group shape
        final PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape(points, shapes);

        // Test morphology group shape
        assumeTrue(groupShape.getNumPoints() == numPoints);
        assumeTrue(groupShape.getNumShapes() == numShapes);
        for (int i = 0; i < numPoints; i++) {
            assumeTrue(groupShape.getPoint(i)[0] == points[i * 3]);
            assumeTrue(groupShape.getPoint(i)[1] == points[i * 3 + 1]);
            assumeTrue(groupShape.getPoint(i)[2] == points[i * 3 + 2]);
            assumeTrue(groupShape.getShape(i) == shapes[i]);
        }
    }

    @org.junit.Test
    public void test_morphology_group_shape_5() throws Exception {
        // Prepare data
        final int numPoints = 1000;
        final int numShapes = 10;
        final double[] points = new double[numPoints * 3];
        final int[] shapes = new int[numPoints];
        for (int i = 0; i < numPoints; i++) {
            points[i * 3] = Math.random();
            points[i * 3 + 1] = Math.random();
            points[i * 3 + 2] = Math.random();
            shapes[i] = i % numShapes;
        }

        // Create morphology group shape
        final PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape(points, shapes);

        // Test morphology group shape
        assumeTrue(groupShape.getNumPoints() == numPoints);
        assumeTrue(groupShape.getNumShapes() == numShapes);
        for (int i = 0; i < numPoints; i++) {
            assumeTrue(groupShape.getPoint(i)[0] == points[i * 3]);
            assumeTrue(groupShape.getPoint(i)[1] == points[i * 3 + 1]);
            assumeTrue(groupShape.getPoint(i)[2] == points[i * 3 + 2]);
            assumeTrue(groupShape.getShape(i) == shapes[i]);
        }
    }

    @org.junit.Test
    public void test_morphology_group_shape_6() throws Exception {
        // Prepare data
        final int numPoints = 1000;
        final int numShapes = 10;
        final double[] points = new double[numPoints * 3];
        final int[] shapes = new int[numPoints];
        for (int i = 0; i < numPoints; i++) {
            points[i * 3] = Math.random();
            points[i * 3 + 1] = Math.random();
            points[i * 3 + 2] = Math.random();
            shapes[i] = i % numShapes;
        }

        // Create morphology group shape
        final PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape(points, shapes);

        // Test morphology group shape
        assumeTrue(groupShape.getNumPoints() == numPoints);
        assumeTrue(groupShape.getNumShapes() == numShapes);
        for (int i = 0; i < numPoints; i++) {
            assumeTrue(groupShape.getPoint(i)[0] == points[i * 3]);
            assumeTrue(groupShape.getPoint(i)[1] == points[i * 3 + 1]);
            assumeTrue(groupShape.getPoint(i)[2] == points[i * 3 + 2]);
            assumeTrue(groupShape.getShape(i) == shapes[i]);
        }
    }

    @org.junit.Test
    public void test_morphology_group_shape_7() throws Exception {
        // Prepare data
        final int numPoints = 1000;
        final int numShapes = 10;
        final double[] points = new double[numPoints * 3];
        final int[] shapes = new int[numPoints];
        for (int i = 0; i < numPoints; i++) {
            points[i * 3] = Math.random();
            points[i * 3 + 1] = Math.random();
            points[i * 3 + 2] = Math.random();
            shapes[i] = i % numShapes;
        }

        // Create morphology group shape
        final PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape(points, shapes);

        // Test morphology group shape
        assumeTrue(groupShape.getNumPoints() == numPoints);
        assumeTrue(groupShape.getNumShapes() == numShapes);
        for (int i = 0; i < numPoints; i++) {
            assumeTrue(groupShape.getPoint(i)[0] == points[i * 3]);
            assumeTrue(groupShape.getPoint(i)[1] == points[i * 3 + 1]);
            assumeTrue(groupShape.getPoint(i)[2] == points[i * 3 + 2]);
            assumeTrue(groupShape.getShape(i) == shapes[i]);
        }
    }

    @org.junit.Test
    public void test_morphology_group_shape_8() throws Exception {
        // Prepare data
        final int numPoints = 1000;
        final int numShapes = 10;
        final double[] points = new double[numPoints * 3];
        final int[] shapes = new int[numPoints];
        for (int i = 0; i < numPoints; i++) {
            points[i * 3] = Math.random();
            points[i * 3 + 1] = Math.random();
            points[i * 3 + 2] = Math.random();
            shapes[i] = i % numShapes;
        }

        // Create morphology group shape
        final PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape(points, shapes);

        // Test morphology group shape
        assumeTrue(groupShape.getNumPoints() == numPoints);
        assumeTrue(groupShape.getNumShapes() == numShapes);
        for (int i = 0; i < numPoints; i++) {
            assumeTrue(groupShape.getPoint(i)[0] == points[i * 3]);
            assumeTrue(groupShape.getPoint(i)[1] == points[i * 3 + 1]);
            assumeTrue(groupShape.getPoint(i)[2] == points[i * 3 + 2]);
            assumeTrue(groupShape.getShape(i) == shapes[i]);
        }
    }

    @org.junit.Test
    public void test_morphology_group_shape_9() throws Exception {
        // Prepare data
        final int numPoints = 1000;
        final int numShapes = 10;
        final double[] points = new double[numPoints * 3];
        final int[] shapes = new int[numPoints];
        for (int i = 0; i < numPoints; i++) {
            points[i * 3] = Math.random();
            points[i * 3 + 1] = Math.random();
            points[i * 3 + 2] = Math.random();
            shapes[i] = i % numShapes;
        }

        // Create morphology group shape
        final PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape(points, shapes);

        // Test morphology group shape
        assumeTrue(groupShape.getNumPoints() == numPoints);
        assumeTrue(groupShape.getNumShapes() == numShapes);
        for (int i = 0; i < numPoints; i++) {
            assumeTrue(groupShape.getPoint(i)[0] == points[i * 3]);
            assumeTrue(groupShape.getPoint(i)[1] == points[i * 3 + 1]);
            assumeTrue(groupShape.getPoint(i)[2] == points[i * 3 + 2]);
            assumeTrue(groupShape.getShape(i) == shapes[i]);
        }
    }

    @org.junit.Test
    public void test_morphology_group_shape_10() throws Exception {
        // Prepare data
        final int numPoints = 1000;
        final int numShapes = 10;
        final double[] points = new double[numPoints * 3];
        final int[] shapes = new int[numPoints];
        for (int i = 0; i < numPoints; i++) {
            points[i * 3] = Math.random();
            points[i * 3 + 1] = Math.random();
            points[i * 3 + 2] = Math.random();
            shapes[i] = i % numShapes;
        }

        // Create morphology group shape
        final PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape(points, shapes);

        // Test morphology group shape
        assumeTrue(groupShape.getNumPoints() == numPoints);
        assumeTrue(groupShape.getNumShapes() == numShapes);
        for (int i = 0; i < numPoints; i++) {
            assumeTrue(groupShape.getPoint(i)[0] == points[i * 3]);
            assumeTrue(groupShape.getPoint(i)[1] == points[i * 3 + 1]);
            assumeTrue(groupShape.getPoint(i)[2] == points[i * 3 + 2]);
            assumeTrue(groupShape.getShape(i) == shapes[i]);
        }
    }
}
```