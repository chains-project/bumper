```java
import com.jcabi.aspects.Tv;
import com.jcabi.aspects.Cacheable;

@Cacheable(cache = "http://localhost:6379/0", key = "bucket:{$name}")
public class BucketRule implements CloseableRule {
  private final String name;
  private final S3 s3;

  public BucketRule(String name, S3 s3) {
    this.name = name;
    this.s3 = s3;
  }

  @Override
  public void before() throws Exception {
    final Bucket bucket = s3.bucket(name);
    bucket.remove();
    bucket.create();
  }

  @Override
  public void after() {
    final Bucket bucket = s3.bucket(name);
    bucket.remove();
  }

  @Override
  public void close() {
  }
}
```