```java
  import com.jcabi.aspects.Tv;
  import org.junit.Rule;

  public class BucketRule {

    @Rule
    public final Tv tv = new Tv();

    public BucketRule() {
      System.setProperty("jcabi.s3.bucket.name", "jcabi-s3-test");
    }
  }
```