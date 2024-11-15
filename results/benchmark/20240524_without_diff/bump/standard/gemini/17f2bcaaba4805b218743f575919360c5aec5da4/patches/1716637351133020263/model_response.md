```java
import org.junit.jupiter.api.Assertions;

import java.util.Arrays;

public class PGS_MorphologyGroupShapeTests {

    @org.junit.jupiter.api.Test
    public void testGroupShape() {
        int[][] image = {
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
        };

        int[][] expected = {
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
        };

        PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape();
        int[][] result = groupShape.groupShape(image);

        Assertions.assertArrayEquals(expected, result);
    }

    @org.junit.jupiter.api.Test
    public void testGroupShapeWithHole() {
        int[][] image = {
                {1, 1, 1, 1, 1},
                {1, 0, 0, 0, 1},
                {1, 0, 1, 0, 1},
                {1, 0, 0, 0, 1},
                {1, 1, 1, 1, 1},
        };

        int[][] expected = {
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
        };

        PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape();
        int[][] result = groupShape.groupShape(image);

        Assertions.assertArrayEquals(expected, result);
    }

    @org.junit.jupiter.api.Test
    public void testGroupShapeWithMultipleHoles() {
        int[][] image = {
                {1, 1, 1, 1, 1},
                {1, 0, 0, 0, 1},
                {1, 0, 1, 0, 1},
                {1, 0, 0, 0, 1},
                {1, 1, 1, 1, 1},
        };

        int[][] expected = {
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
        };

        PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape();
        int[][] result = groupShape.groupShape(image);

        Assertions.assertArrayEquals(expected, result);
    }

    @org.junit.jupiter.api.Test
    public void testGroupShapeWithDiagonalHole() {
        int[][] image = {
                {1, 1, 1, 1, 1},
                {1, 0, 0, 0, 1},
                {1, 0, 1, 0, 1},
                {1, 0, 0, 0, 1},
                {1, 1, 1, 1, 1},
        };

        int[][] expected = {
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
        };

        PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape();
        int[][] result = groupShape.groupShape(image);

        Assertions.assertArrayEquals(expected, result);
    }

    @org.junit.jupiter.api.Test
    public void testGroupShapeWithMultipleDiagonalHoles() {
        int[][] image = {
                {1, 1, 1, 1, 1},
                {1, 0, 0, 0, 1},
                {1, 0, 1, 0, 1},
                {1, 0, 0, 0, 1},
                {1, 1, 1, 1, 1},
        };

        int[][] expected = {
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
        };

        PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape();
        int[][] result = groupShape.groupShape(image);

        Assertions.assertArrayEquals(expected, result);
    }

    @org.junit.jupiter.api.Test
    public void testGroupShapeWithComplexHole() {
        int[][] image = {
                {1, 1, 1, 1, 1},
                {1, 0, 0, 0, 1},
                {1, 0, 1, 0, 1},
                {1, 0, 0, 0, 1},
                {1, 1, 1, 1, 1},
        };

        int[][] expected = {
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
        };

        PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape();
        int[][] result = groupShape.groupShape(image);

        Assertions.assertArrayEquals(expected, result);
    }

    @org.junit.jupiter.api.Test
    public void testGroupShapeWithMultipleComplexHoles() {
        int[][] image = {
                {1, 1, 1, 1, 1},
                {1, 0, 0, 0, 1},
                {1, 0, 1, 0, 1},
                {1, 0, 0, 0, 1},
                {1, 1, 1, 1, 1},
        };

        int[][] expected = {
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
        };

        PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape();
        int[][] result = groupShape.groupShape(image);

        Assertions.assertArrayEquals(expected, result);
    }

    @org.junit.jupiter.api.Test
    public void testGroupShapeWithLargeImage() {
        int[][] image = new int[1000][1000];
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                image[i][j] = 1;
            }
        }

        int[][] expected = new int[1000][1000];
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                expected[i][j] = 1;
            }
        }

        PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape();
        int[][] result = groupShape.groupShape(image);

        Assertions.assertArrayEquals(expected, result);
    }

    @org.junit.jupiter.api.Test
    public void testGroupShapeWithEmptyImage() {
        int[][] image = new int[0][0];

        int[][] expected = new int[0][0];

        PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape();
        int[][] result = groupShape.groupShape(image);

        Assertions.assertArrayEquals(expected, result);
    }

    @org.junit.jupiter.api.Test
    public void testGroupShapeWithNullImage() {
        int[][] image = null;

        int[][] expected = new int[0][0];

        PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape();
        int[][] result = groupShape.groupShape(image);

        Assertions.assertArrayEquals(expected, result);
    }
}
```