```java
import com.jcabi.aspects.Tv;
import com.jcabi.aspects.aspects.TvImpl;

public class BucketRule {

    private final Tv tv = new TvImpl();

    @Override
    public void testUpload() throws Exception {
        tv.expect(new Exception("Test").getMessage());
    }

}
```