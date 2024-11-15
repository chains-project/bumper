```java
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import micycle.pgs.PGS_MorphologyGroupShape;

public class PGS_MorphologyGroupShapeTests {

	private PGS_MorphologyGroupShape groupShape;

	@Before
	public void setUp() throws Exception {
		groupShape = new PGS_MorphologyGroupShape();
	}

	@After
	public void tearDown() throws Exception {
		groupShape = null;
	}

	@Test
	public void testAddShape() {
		groupShape.addShape(1);
		groupShape.addShape(2);
		groupShape.addShape(3);
		assertEquals(3, groupShape.getShapeCount());
	}

	@Test
	public void testRemoveShape() {
		groupShape.addShape(1);
		groupShape.addShape(2);
		groupShape.addShape(3);
		groupShape.removeShape(2);
		assertEquals(2, groupShape.getShapeCount());
	}

	@Test
	public void testClearShapes() {
		groupShape.addShape(1);
		groupShape.addShape(2);
		groupShape.addShape(3);
		groupShape.clearShapes();
		assertEquals(0, groupShape.getShapeCount());
	}

	@Test
	public void testGetShapes() {
		groupShape.addShape(1);
		groupShape.addShape(2);
		groupShape.addShape(3);
		List<Integer> shapes = groupShape.getShapes();
		Collections.sort(shapes);
		assertEquals(Arrays.asList(1, 2, 3), shapes);
	}

	@Test
	public void testGetShapeCount() {
		groupShape.addShape(1);
		groupShape.addShape(2);
		groupShape.addShape(3);
		assertEquals(3, groupShape.getShapeCount());
	}

	@Test
	public void testIsShapeInGroup() {
		groupShape.addShape(1);
		groupShape.addShape(2);
		groupShape.addShape(3);
		assertTrue(groupShape.isShapeInGroup(1));
		assertTrue(groupShape.isShapeInGroup(2));
		assertTrue(groupShape.isShapeInGroup(3));
		assertFalse(groupShape.isShapeInGroup(4));
	}

	@Test
	public void testAddShapes() {
		groupShape.addShapes(Arrays.asList(1, 2, 3));
		assertEquals(3, groupShape.getShapeCount());
	}

	@Test
	public void testRemoveShapes() {
		groupShape.addShapes(Arrays.asList(1, 2, 3));
		groupShape.removeShapes(Arrays.asList(2));
		assertEquals(2, groupShape.getShapeCount());
	}

	@Test
	public void testClearAllShapes() {
		groupShape.addShapes(Arrays.asList(1, 2, 3));
		groupShape.clearAllShapes();
		assertEquals(0, groupShape.getShapeCount());
	}

	@Test
	public void testGetShapeIterator() {
		groupShape.addShapes(Arrays.asList(1, 2, 3));
		List<Integer> shapes = new ArrayList<>();
		for (int shape : groupShape.getShapeIterator()) {
			shapes.add(shape);
		}
		Collections.sort(shapes);
		assertEquals(Arrays.asList(1, 2, 3), shapes);
	}

	@Test
	public void testToString() {
		groupShape.addShapes(Arrays.asList(1, 2, 3));
		assertEquals("[1, 2, 3]", groupShape.toString());
	}

}
```