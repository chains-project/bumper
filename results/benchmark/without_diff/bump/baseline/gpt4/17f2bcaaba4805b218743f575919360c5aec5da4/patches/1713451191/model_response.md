```java
@Test
void testRobustnessRandomly() {
	Random r = new XoRoShiRo128PlusRandom(0);
	for (int k = 0; k < 100; k++) {
		List<SegmentString> segmentStrings = new ArrayList<>(111 + k);
		for (int i = 0; i < 111 + k; i++) {
			segmentStrings.add(new NodedSegmentString(new Coordinate[] { new Coordinate(r.nextDouble() * 10000, r.nextDouble() * 10000),
					new Coordinate(r.nextDouble() * 10000, r.nextDouble() * 13337) }, null));
		}
		Collection<SegmentString> nodedSS = PGS.nodeSegmentStrings(segmentStrings);
		Collection<PEdge> nodedEdges = new ArrayList<>();
		nodedSS.forEach(ss -> nodedEdges.add(new PEdge(PGS.toPVector(ss.getCoordinate(0)), PGS.toPVector(ss.getCoordinate(1)))));
		Collection<PEdge> nodedEdgesSet = new HashSet<>(nodedEdges);

		final Polygonizer polygonizerJTS = new Polygonizer();
		polygonizerJTS.setCheckRingsValid(false);
		nodedEdgesSet.forEach(e -> {
			final LineString l = PGS.GEOM_FACTORY
					.createLineString(new Coordinate[] { PGS.coordFromPVector(e.a), PGS.coordFromPVector(e.b) });
			polygonizerJTS.add(l);
		});

		long t1 = System.currentTimeMillis();
		Collection<Polygon> JTS = polygonizerJTS.getPolygons();
		long t2 = System.currentTimeMillis();
		long timeJTS = t2 - t1;

		t1 = System.currentTimeMillis();
		PShape FP = polygonize(nodedEdgesSet);
		t2 = System.currentTimeMillis();
		long timeFP = t2 - t1;
		assertEquals(JTS.size(), FP.getChildCount());
	}
}
```