```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.aspects.Loggable;

  @Loggable
  public class AwsOcketITCase extends AbstractAwsITCase {

      @Test
      public void testWithAwsOcket() throws Exception {
          final String bucket = "jcab1-s3-aws-test";
          final String key = "test.txt";
          final String content = "Hello, world!";

          // Create a bucket
          final S3 s3 = new S3(this.aws());
          s3.bucket(bucket).create();

          // Upload an object
          s3.bucket(bucket).object(key).set(content);

          // Download an object
          final String downloaded = s3.bucket(bucket).object(key).get();

          // Assert
          assertThat(downloaded, is(content));

          // Delete an object
          s3.bucket(bucket).object(key).remove();

          // Delete a bucket
          s3.bucket(bucket).remove();
      }

      @Test
      public void testWithAwsOcketAndProxy() throws Exception {
          final String bucket = "jcab1-s3-aws-test";
          final String key = "test.txt";
          final String content = "Hello, world!";

          // Create a bucket
          final S3 s3 = new S3(this.aws());
          s3.bucket(bucket).create();

          // Upload an object
          s3.bucket(bucket).object(key).set(content);

          // Download an object
          final String downloaded = s3.bucket(bucket).object(key).get();

          // Assert
          assertThat(downloaded, is(content));

          // Delete an object
          s3.bucket(bucket).object(key).remove();

          // Delete a bucket
          s3.bucket(bucket).remove();
      }

  }
```