```java
import com.jcabi.aspects.Tv;
import com.jcabi.aspects.TvImpl;

public class RegionITCase {

    public void testRegion() throws Exception {
        Tv tv = new TvImpl();
        tv.play("Hello, world!");
    }
}
```