```java
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

import micycle.pgs.PGS;
import micycle.pgs.PGS_Meshing;
import micycle.pgs.PGS_Meshing.PGS_Meshing_Options;
import micycle.pgs.PGS_Options;
import micycle.pgs.meshing.Mesh;
import micycle.pgs.meshing.Mesh_Builder;
import micycle.pgs.meshing.Mesh_Options;
import micycle.pgs.meshing.Mesh_Viewer;
import micycle.pgs.meshing.Meshing_Context;
import micycle.pgs.util.PGS_Utils;

public class PGS_MeshingTests {

	@Test
	public void testMeshing() {
		PGS_Options options = new PGS_Options();
		options.setMeshing_options(new PGS_Meshing_Options());
		PGS pgs = new PGS(options);
		Meshing_Context context = new Meshing_Context(pgs);
		
		List<Mesh> meshes = new ArrayList<>();
		meshes.add(new Mesh_Builder(context, new Mesh_Options()).build());
		meshes.add(new Mesh_Builder(context, new Mesh_Options()).build());
		
		PGS_Meshing meshing = new PGS_Meshing(context, meshes);
		Mesh mesh = meshing.getMesh();
		
		assertNotNull(mesh);
	}

	@Test
	public void testMeshingWithViewer() {
		PGS_Options options = new PGS_Options();
		options.setMeshing_options(new PGS_Meshing_Options());
		PGS pgs = new PGS(options);
		Meshing_Context context = new Meshing_Context(pgs);
		
		List<Mesh> meshes = new ArrayList<>();
		meshes.add(new Mesh_Builder(context, new Mesh_Options()).build());
		meshes.add(new Mesh_Builder(context, new Mesh_Options()).build());
		
		PGS_Meshing meshing = new PGS_Meshing(context, meshes);
		Mesh mesh = meshing.getMesh();
		
		Mesh_Viewer viewer = new Mesh_Viewer(mesh);
		viewer.show();
		
		assertNotNull(mesh);
	}

	@Test
	public void testMeshingWithPGSUtils() {
		PGS_Options options = new PGS_Options();
		options.setMeshing_options(new PGS_Meshing_Options());
		PGS pgs = new PGS(options);
		Meshing_Context context = new Meshing_Context(pgs);
		
		List<Mesh> meshes = new ArrayList<>();
		meshes.add(new Mesh_Builder(context, new Mesh_Options()).build());
		meshes.add(new Mesh_Builder(context, new Mesh_Options()).build());
		
		PGS_Meshing meshing = new PGS_Meshing(context, meshes);
		Mesh mesh = meshing.getMesh();
		
		PGS_Utils.writeMeshToPLY(mesh, "mesh.ply");
		
		assertNotNull(mesh);
	}

}
```