```java
  import com.jcabi.aspects.Tv;

  import java.util.ArrayList;
  import java.util.List;

  public class AwsOcketITCase {

      private final String region;
      private final String bucket;
      private final String accessKey;
      private final String secretKey;

      public AwsOcketITCase(final String region, final String bucket, final String accessKey, final String secretKey) {
          this.region = region;
          this.bucket = bucket;
          this.accessKey = accessKey;
          this.secretKey = secretKey;
      }

      public void testOcket() {
          final List<String> list = new ArrayList<>();
          list.add("file1.txt");
          list.add("file2.txt");
          list.add("file3.txt");
          final Tv tv = new Tv(this.region, this.bucket, this.accessKey, this.secretKey);
          tv.ocket(list);
      }
  }
```