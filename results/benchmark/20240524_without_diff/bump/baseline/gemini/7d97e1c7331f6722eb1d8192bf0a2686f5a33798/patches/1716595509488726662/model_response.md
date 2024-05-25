```java
import com.jcabi.aspects.Tv;
import com.jcabi.aspects.Tv.Result;

public class RegionITCase {

    @Tv
    public void testRegion(Result<String> result) throws Exception {
        result.expect("us-east-1");
    }
}
```