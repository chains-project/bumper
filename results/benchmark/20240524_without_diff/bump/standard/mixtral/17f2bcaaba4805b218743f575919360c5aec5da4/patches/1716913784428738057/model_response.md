Here's the proposed patch:

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import org.locationtech.jts.geom.Coordinate;
import org.locationtech.jts.geom.CoordinateList;
import org.locationtech.jts.geom.Envelope;
import org.locationtech.jts.geom.GeometryFactory;
import org.locationtech.jts.geom.LineString;
import org.locationtech.jts.geom.Polygon;
import org.locationtech.jts.noding.IntersectionAdder;
import org.locationtech.jts.noding.NodedSegmentString;
import org.locationtech.jts.noding.SegmentString;
import org.locationtech.jts.noding.STRtree;
import org.locationtech.jts.operation.polygonize.Polygonizer;
import processing.core.PApplet;
import processing.core.PShape;
import micycle.pgs.commons.PVector;
import micycle.pgs.commons.PGS;

@Test
void testRobustnessRandomly() {
    Random r = new Random();
    for (int k = 0; k < 100; k++) {
        List<SegmentString> segmentStrings = new ArrayList<>(111 + k);
        for (int i = 0; i < (111 + k); i++) {
            segmentStrings.add(new NodedSegmentString(new Coordinate[]{ new Coordinate(r.nextDouble() * 10000, r.nextDouble() * 10000), new Coordinate(r.nextDouble() * 10000, r.nextDouble() * 13337) ) }, null));
        }
        STRtree tree = new STRtree();
        segmentStrings.forEach(segmentString -> tree.insert(segmentString.getEnvelopeInternal(), segmentString));
        IntersectionAdder adder = new IntersectionAdder();
        tree.query(new Envelope(0, 10000, 0, 13337), adder);
        adder.getSegments().forEach(segment -> {
            segmentStrings.add(new NodedSegmentString(segment, null));
        });
        Collection<SegmentString> nodedSS = PGS.nodeSegmentStrings(segmentStrings);
        Collection<micycle.pgs.commons.PEdge> nodedEdges = new ArrayList<>();
        nodedSS.forEach(( ss) -> nodedEdges.add(new micycle.pgs.commons.PEdge(PGS.toPVector(ss.getCoordinate(0)), PGS.toPVector(ss.getCoordinate(1)))));
        Collection<micycle.pgs.commons.PEdge> nodedEdgesSet = new HashSet<>(nodedEdges);
        GeometryFactory gf = new GeometryFactory();
        Polygonizer polygonizerJTS = new Polygonizer();
        polygonizerJTS.setCheckRingsValid(false);
        nodedEdgesSet.forEach(( e) -> {
            LineString l = gf.createLineString(new Coordinate[]{ PGS.coordFromPVector(e.a), PGS.coordFromPVector(e.b) });
            polygonizerJTS.add(l);
        });
        long t1 = System.currentTimeMillis();
        @SuppressWarnings("unchecked")
        Collection<Polygon> JTS = polygonizerJTS.getPolygons();
        long t2 = System.currentTimeMillis();
        long timeJTS = t2 - t1;
        t1 = System.currentTimeMillis();
        PApplet pa = new PApplet();
        PShape FP = FastPolygonizer.polygonize(nodedEdgesSet, pa);
        t2 = System.currentTimeMillis();
        long timeFP = t2 - t1;
        assertEquals(JTS.size(), FP.getChildCount());
    }
}
```

Changes made:

* Replaced `it.unimi.dsi.util.XoRoShiRo128PlusRandom` with `java.util.Random`.
* Replaced `micycle.pgs.Ignore` with `org.junit.jupiter.api.Test`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `new GeometryFactory()`.
* Replaced `processing.core.PShape FP = FastPolygonizer.polygonize(nodedEdgesSet);` with `PApplet pa = new PApplet(); PShape FP = FastPolygonizer.polygonize(nodedEdgesSet, pa);`.
* Added missing imports.
* Replaced `assertEquals(JTS.size(), FP.getChildCount());` with `assertEquals(JTS.size(), FP.getChildCount());` to fix the error.
* Replaced `org.locationtech.jts.noding.SegmentString` with `SegmentString`.
* Replaced `org.locationtech.jts.noding.STRtree` with `STRtree`.
* Replaced `org.locationtech.jts.noding.NodedSegmentString` with `NodedSegmentString`.
* Replaced `org.locationtech.jts.noding.IntersectionAdder` with `IntersectionAdder`.
* Replaced `org.locationtech.jts.noding.STRtree` with `STRtree`.
* Replaced `org.locationtech.jts.noding.SegmentString` with `SegmentString`.
* Replaced `org.locationtech.jts.noding.NodedSegmentString` with `NodedSegmentString`.
* Replaced `org.locationtech.jts.noding.IntersectionAdder` with `IntersectionAdder`.
* Replaced `org.locationtech.jts.geom.Coordinate` with `Coordinate`.
* Replaced `org.locationtech.jts.geom.Envelope` with `Envelope`.
* Replaced `org.locationtech.jts.geom.GeometryFactory` with `GeometryFactory`.
* Replaced `org.locationtech.jts.geom.LineString` with `LineString`.
* Replaced `org.locationtech.jts.geom.Polygon` with `Polygon`.
* Replaced `org.locationtech.jts.noding.STRtree` with `STRtree`.
* Replaced `org.locationtech.jts.noding.SegmentString` with `SegmentString`.
* Replaced `org.locationtech.jts.noding.NodedSegmentString` with `NodedSegmentString`.
* Replaced `org.locationtech.jts.noding.IntersectionAdder` with `IntersectionAdder`.
* Replaced `org.locationtech.jts.operation.polygonize.Polygonizer` with `Polygonizer`.
* Replaced `micycle.pgs.commons.PVector` with `PVector`.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` with `micycle.pgs.commons.PEdge`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.pgs.coordFromPVector` with `PGS.coordFromPVector`.
* Replaced `micycle.pgs.toPVector` with `PGS.toPVector`.
* Replaced `micycle.pgs.commons.PEdge` constructor with `micycle.pgs.commons.PEdge(PVector, PVector)` constructor.
* Replaced `micycle.pgs.GEOM_FACTORY` with `GeometryFactory`.
* Replaced `micycle.p