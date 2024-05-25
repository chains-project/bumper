```java
import com.jcabi.aspects.Tv;
import com.jcabi.log.Logger;

public class AwsOcketITCase {

    private static final Logger LOG = new Logger(AwsOcketITCase.class);

    @Tv
    public void testPutGetDelete() throws Exception {
        LOG.info("Testing put, get, delete ...");
        final String bucket = "jcabi-" + System.currentTimeMillis();
        try (S3 s3 = new S3(new Aws(new Properties()))) {
            LOG.info("Creating bucket '{}' ...", bucket);
            s3.bucket(bucket).create();
            LOG.info("Bucket '{}' created", bucket);
            s3.bucket(bucket).put("file.txt", new byte[0]);
            s3.bucket(bucket).put("file.txt", "Hello World!");
            final String text = s3.bucket(bucket).get("file.txt");
            assertThat(text, is("Hello World!"));
            s3.bucket(bucket).delete();
        }
    }

}
```