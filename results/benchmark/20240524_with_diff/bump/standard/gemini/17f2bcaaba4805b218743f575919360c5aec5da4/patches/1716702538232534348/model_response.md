```java
import static org.junit.Assert.assertEquals;

import java.util.Arrays;

import org.junit.Test;
import org.tinspin.index.PointIndexMMWrapper;
import org.tinspin.index.phtree.PHTreeMMP;
import org.tinspin.index.util.MinHeap;
import org.tinspin.index.util.MinMaxHeap;

import micycle.pgs.PGS_Meshing;

public class PGS_MeshingTests {

	@Test
	public void testMeshing() {
		PGS_Meshing meshing = new PGS_Meshing(new PointIndexMMWrapper(new PHTreeMMP()), new MinHeap(), new MinMaxHeap());
		double[][] points = new double[][] { { 0.0, 0.0 }, { 1.0, 0.0 }, { 0.0, 1.0 }, { 1.0, 1.0 } };
		int[][] triangles = new int[][] { { 0, 1, 2 }, { 1, 3, 2 } };
		meshing.mesh(points, triangles);
		assertEquals(4, meshing.getPoints().size());
		assertEquals(2, meshing.getTriangles().size());
	}

}
```