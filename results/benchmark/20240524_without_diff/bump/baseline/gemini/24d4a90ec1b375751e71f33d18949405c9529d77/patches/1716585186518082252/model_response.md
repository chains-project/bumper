```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.s3.Bucket;
  import com.jcabi.s3.Storage;
  import org.junit.jupiter.api.Test;

  import java.io.IOException;

  import static org.junit.jupiter.api.Assertions.assertEquals;

  public class BucketRuleTest {

    @Test
    public void testCreate() throws IOException {
      final Bucket bucket = new Storage().bucket("bucket");
      bucket.create();
      assertEquals("bucket", bucket.name());
      bucket.remove();
    }

    @Test
    public void testCreateWithRegion() throws IOException {
      final Bucket bucket = new Storage("US").bucket("bucket");
      bucket.create();
      assertEquals("bucket", bucket.name());
      assertEquals("US", bucket.region());
      bucket.remove();
    }

    @Test
    public void testCreateWithAcl() throws IOException {
      final Bucket bucket = new Storage().bucket("bucket").acl("public-read");
      bucket.create();
      assertEquals("bucket", bucket.name());
      assertEquals("public-read", bucket.acl());
      bucket.remove();
    }

    @Test
    public void testCreateWithRegionAndAcl() throws IOException {
      final Bucket bucket = new Storage("US").bucket("bucket").acl("public-read");
      bucket.create();
      assertEquals("bucket", bucket.name());
      assertEquals("US", bucket.region());
      assertEquals("public-read", bucket.acl());
      bucket.remove();
    }

    @Test
    public void testCreateWithTv() throws IOException {
      final Bucket bucket = new Storage().bucket("bucket").tv(Tv.ON);
      bucket.create();
      assertEquals("bucket", bucket.name());
      assertEquals(Tv.ON, bucket.tv());
      bucket.remove();
    }

    @Test
    public void testCreateWithRegionAndTv() throws IOException {
      final Bucket bucket = new Storage("US").bucket("bucket").tv(Tv.ON);
      bucket.create();
      assertEquals("bucket", bucket.name());
      assertEquals("US", bucket.region());
      assertEquals(Tv.ON, bucket.tv());
      bucket.remove();
    }

    @Test
    public void testCreateWithAclAndTv() throws IOException {
      final Bucket bucket = new Storage().bucket("bucket").acl("public-read").tv(Tv.ON);
      bucket.create();
      assertEquals("bucket", bucket.name());
      assertEquals("public-read", bucket.acl());
      assertEquals(Tv.ON, bucket.tv());
      bucket.remove();
    }

    @Test
    public void testCreateWithRegionAclAndTv() throws IOException {
      final Bucket bucket = new Storage("US").bucket("bucket").acl("public-read").tv(Tv.ON);
      bucket.create();
      assertEquals("bucket", bucket.name());
      assertEquals("US", bucket.region());
      assertEquals("public-read", bucket.acl());
      assertEquals(Tv.ON, bucket.tv());
      bucket.remove();
    }

  }
```