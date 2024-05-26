Here':

```java
import com.twitter.finagle.thrift.FramedTransport;
import com.twitter.finagle.thrift.FramedTransportFactory;
import com.esri.core.geometry.MapGeometry;
import com.esri.core.geometry.MapGeometryFactory;
import com.esri.core.geometry.geometries.MapPoint;
import com.esri.core.geometry.Projection;
import com.esri.core.geometry.SpatialReference;
import com.esri.core.map.Graphic;
import com.esri.core.map.GraphicCollection;
import com.esri.core.map.JacksonJsonConverter;
import com.esri.core.map.Map;

@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFlushingFastFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    FramedTransportFactory factory = new FramedTransportFactory(bufferCapacity, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 102framedTransport = new FramedTransport(new org.apache.http.impl.io.HttpRequestWriter(), new org.apache.http.impl.io.HttpResponseParser(), 1024, 1024, 4096, 4096, 4096, 4096, 4096, 4096, 4096, 4096, 4096,  protocol = new org.apache.thrift.protocol.TBinaryProtocol(new org.apache.thrift.transport.TFramedTransport(framedTransport));
}
```

I replaced the class `com.pinterest.singer.client.logback.TFastFramedTransport` with the class `com.twitter.finagle.thrift.FramedTransport` and added the necessary imports.

Please note that this is just a fix for the compilation error, it doesn'

\*'t guarantee that the new class will work as the previous one.

Please also note that the new class has different parameters for the constructor, so you might need to adjust the parameters accordingly.