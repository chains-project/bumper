```java
import com.jcabi.aspects.Tv;
import com.jcabi.aspects.Loggable;

import java.util.concurrent.TimeUnit;

public class RegionITCase {

    @Loggable(Loggable.DEBUG)
    public void testUpdate() {
        Tv tv = new Tv();
        tv.update();
    }

    @Loggable(Loggable.DEBUG)
    public void testUpdateWithTimeout() {
        Tv tv = new Tv();
        tv.update(10, TimeUnit.SECONDS);
    }

    @Loggable(Loggable.DEBUG)
    public void testUpdateWithTimeoutAndUnit() {
        Tv tv = new Tv();
        tv.update(10, TimeUnit.SECONDS);
    }

}
```