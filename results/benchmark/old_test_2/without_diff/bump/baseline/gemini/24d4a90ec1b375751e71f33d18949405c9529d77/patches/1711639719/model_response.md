```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.log.Logger;

  public class AwsOcketITCase {
    private static final Logger LOG = Logger.of(AwsOcketITCase.class);

    @Override
    public void testPutGetDelete() throws Exception {
      final String bucket = "jcabi-s3-test";
      LOG.info("Testing bucket '%s'", bucket);
      try (Tv timer = new Tv()) {
        final Bucket bucket1 = new Bucket(bucket);
        final String key = "file.txt";
        final String content = "Hello, world!";
        bucket1.put(key, content);
        assertEquals(content, bucket1.get(key));
        bucket1.delete(key);
        timer.stop();
        LOG.info("Bucket '%s' tested in %s", bucket, timer);
      }
    }
  }
```