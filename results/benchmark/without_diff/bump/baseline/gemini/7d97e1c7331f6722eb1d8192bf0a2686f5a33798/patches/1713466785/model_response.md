```java
import com.jcabi.aspects.Tv;

public class RegionITCase {

    private final Tv tv = new Tv();

    @Test
    public void testRegion() throws Exception {
        // ...
        tv.region(region);
    }
}
```