```java
import org.junit.Assert;
import org.junit.Test;

public class PGS_MeshingTests {

    @Test
    public void testMeshing() throws Exception {
        PGS pgs = new PGS();
        pgs.setMeshingParameters(10, 10, 10);
        pgs.mesh();
        Assert.assertEquals(1000, pgs.getMesh().getVertices().size());
    }

}
```