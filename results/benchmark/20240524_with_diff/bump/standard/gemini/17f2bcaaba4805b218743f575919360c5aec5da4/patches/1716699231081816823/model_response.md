```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.Test;

import micycle.pgs.PGS;
import micycle.pgs.PGS_ProcessingGroupShape;
import micycle.pgs.PGS_ProcessingGroupShape.PGS_ProcessingGroupShapeBuilder;

public class PGS_ProcessingGroupShapeTests {

    @Test
    public void testSimpleShape() {
        PGS_ProcessingGroupShape shape = new PGS_ProcessingGroupShapeBuilder()
                .setName("test")
                .setProcessingGroup(new ArrayList<>())
                .build();
        PGS pgs = new PGS(shape);
        List<Integer> result = pgs.getProcessingGroupShape("test").getProcessingGroup();
        assertTrue(result.isEmpty());
    }

    @Test
    public void testShapeWithOneElement() {
        List<Integer> processingGroup = new ArrayList<>();
        processingGroup.add(1);
        PGS_ProcessingGroupShape shape = new PGS_ProcessingGroupShapeBuilder()
                .setName("test")
                .setProcessingGroup(processingGroup)
                .build();
        PGS pgs = new PGS(shape);
        List<Integer> result = pgs.getProcessingGroupShape("test").getProcessingGroup();
        assertEquals(1, result.size());
        assertEquals(1, result.get(0));
    }

    @Test
    public void testShapeWithMultipleElements() {
        List<Integer> processingGroup = new ArrayList<>();
        processingGroup.add(1);
        processingGroup.add(2);
        processingGroup.add(3);
        PGS_ProcessingGroupShape shape = new PGS_ProcessingGroupShapeBuilder()
                .setName("test")
                .setProcessingGroup(processingGroup)
                .build();
        PGS pgs = new PGS(shape);
        List<Integer> result = pgs.getProcessingGroupShape("test").getProcessingGroup();
        assertEquals(3, result.size());
        assertEquals(1, result.get(0));
        assertEquals(2, result.get(1));
        assertEquals(3, result.get(2));
    }

}
```