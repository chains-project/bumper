```java
import com.jcabi.aspects.Tv;

import java.util.List;

public class RegionITCase {

    private final Tv tv;

    public RegionITCase(Tv tv) {
        this.tv = tv;
    }

    public void testList() throws Exception {
        List<String> regions = tv.list();
        // ...
    }

    public void testCreate() throws Exception {
        String region = tv.create("us-east-1");
        // ...
    }

    public void testDelete() throws Exception {
        tv.delete("us-east-1");
        // ...
    }

    public void testExists() throws Exception {
        boolean exists = tv.exists("us-east-1");
        // ...
    }
}
```