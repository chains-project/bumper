```java
import org.junit.jupiter.api.Assertions;

import java.util.List;
import java.util.Map;

public class PGS_MorphologyGroupShapeTests {

    public void test_get_group_shape_should_return_correct_shape_for_each_group() {
        // Given
        PGS pgs = new PGS();
        Map<String, List<String>> groups = Map.of(
                "group1", List.of("a", "b", "c"),
                "group2", List.of("d", "e", "f")
        );
        pgs.setGroups(groups);

        // When
        Map<String, String> groupShapes = pgs.getGroupShape();

        // Then
        Assertions.assertEquals(Map.of(
                "group1", "triangle",
                "group2", "square"
        ), groupShapes);
    }
}
```