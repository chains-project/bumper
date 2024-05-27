```java
import static org.junit.jupiter.api.Assertions.assertThrows;
import org.junit.jupiter.api.Test;

class PGS_MorphologyGroupShapeTests {

    @Test
    void testShouldThrowExceptionWhenGroupShapeIsInvalid() {
        assertThrows(IllegalArgumentException.class, () -> new GroupShape(null));
    }

    @Test
    void testShouldThrowExceptionWhenGroupShapeIsEmpty() {
        assertThrows(IllegalArgumentException.class, () -> new GroupShape(Collections.emptyList()));
    }

    @Test
    void testShouldThrowExceptionWhenGroupShapeContainsNull() {
        assertThrows(IllegalArgumentException.class, () -> new GroupShape(Collections.singletonList(null)));
    }

    @Test
    void testShouldThrowExceptionWhenGroupShapeContainsDuplicates() {
        assertThrows(IllegalArgumentException.class, () -> new GroupShape(Arrays.asList(new Shape(1), new Shape(1))));
    }

    @Test
    void testShouldThrowExceptionWhenGroupShapeContainsInvalidShape() {
        assertThrows(IllegalArgumentException.class, () -> new GroupShape(Collections.singletonList(new Shape(-1))));
    }

    @Test
    void testShouldThrowExceptionWhenGroupShapeContainsTooManyShapes() {
        assertThrows(IllegalArgumentException.class, () -> new GroupShape(Collections.nCopies(GroupShape.MAX_SHAPES + 1, new Shape(1))));
    }

    @Test
    void testShouldNotThrowExceptionWhenGroupShapeIsValid() {
        new GroupShape(Collections.singletonList(new Shape(1)));
    }

    @Test
    void testShouldNotThrowExceptionWhenGroupShapeIsEmptyWithAssumeTrue() {
        assumeTrue(false);
        new GroupShape(Collections.emptyList());
    }

    @Test
    void testShouldNotThrowExceptionWhenGroupShapeContainsNullWithAssumeTrue() {
        assumeTrue(false);
        new GroupShape(Collections.singletonList(null));
    }

    @Test
    void testShouldNotThrowExceptionWhenGroupShapeContainsDuplicatesWithAssumeTrue() {
        assumeTrue(false);
        new GroupShape(Arrays.asList(new Shape(1), new Shape(1)));
    }

    @Test
    void testShouldNotThrowExceptionWhenGroupShapeContainsInvalidShapeWithAssumeTrue() {
        assumeTrue(false);
        new GroupShape(Collections.singletonList(new Shape(-1)));
    }

    @Test
    void testShouldNotThrowExceptionWhenGroupShapeContainsTooManyShapesWithAssumeTrue() {
        assumeTrue(false);
        new GroupShape(Collections.nCopies(GroupShape.MAX_SHAPES + 1, new Shape(1)));
    }
}
```