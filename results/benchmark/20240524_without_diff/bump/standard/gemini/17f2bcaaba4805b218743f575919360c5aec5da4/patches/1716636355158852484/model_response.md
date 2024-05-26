```java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {

    private PGS_MorphologyGroupShape groupShape;

    @BeforeEach
    public void setUp() {
        groupShape = new PGS_MorphologyGroupShape();
    }

    @Test
    public void testGroupShape() {
        List<PGS_Morphology> morphologies = new ArrayList<>();
        morphologies.add(new PGS_Morphology("A", 1));
        morphologies.add(new PGS_Morphology("B", 2));
        morphologies.add(new PGS_Morphology("C", 3));

        groupShape.setMorphologies(morphologies);

        assertEquals(3, groupShape.getMorphologies().size());
        assertEquals("A", groupShape.getMorphologies().get(0).getName());
        assertEquals(1, groupShape.getMorphologies().get(0).getValue());
        assertEquals("B", groupShape.getMorphologies().get(1).getName());
        assertEquals(2, groupShape.getMorphologies().get(1).getValue());
        assertEquals("C", groupShape.getMorphologies().get(2).getName());
        assertEquals(3, groupShape.getMorphologies().get(2).getValue());
    }
}
```