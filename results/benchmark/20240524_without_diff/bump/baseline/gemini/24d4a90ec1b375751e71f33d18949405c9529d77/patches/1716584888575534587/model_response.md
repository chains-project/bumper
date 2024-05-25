```java
  import com.jcabi.aspects.Tv;
import com.jcabi.log.Logger;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.TimeUnit;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.condition.DisabledIfEnvironmentVariable;
import org.junit.jupiter.api.condition.EnabledIfEnvironmentVariable;

class BucketRuleTest {

  private static final Logger LOG = new Logger(BucketRuleTest.class);
  private static final String BUCKET = "jcabi-s3-rule-test";
  private static final String TMP = System.getProperty("java.io.tmpdir");
  private static final String KEY = "tmp/bucket.rule.test";
  private static final String FILE = TMP + "/" + KEY;
  private static final Path PATH = Paths.get(FILE);
  private static final int TIMEOUT = 5;
  private Tv tv;

  @BeforeEach
  void setUp() throws IOException {
    this.tv = new Tv();
    this.tv.start();
    if (Files.exists(PATH)) {
      Files.delete(PATH);
    }
  }

  @AfterEach
  void tearDown() throws IOException {
    this.tv.stop();
    if (Files.exists(PATH)) {
      Files.delete(PATH);
    }
  }

  @Test
  @DisabledIfEnvironmentVariable(named = "CI", matches = "true")
  void testRule() throws IOException {
    BucketRuleTest.LOG.info("Starting testRule(String)...");
    BucketRuleTest.LOG.info("Creating bucket...");
    new Bucket(BUCKET).create();
    BucketRuleTest.LOG.info("Creating file...");
    Files.createFile(PATH);
    BucketRuleTest.LOG.info("Rule...");
    new BucketRule(BUCKET, KEY).run();
    BucketRuleTest.LOG.info("Waiting for file...");
    this.tv.waitFor(
      () -> Files.exists(PATH),
      TIMEOUT,
      TimeUnit.SECONDS
    );
    BucketRuleTest.LOG.info("Checking file...");
    assert Files.exists(PATH);
  }

  @Test
  @EnabledIfEnvironmentVariable(named = "CI", matches = "true")
  void testRuleWithExistingFile() throws IOException {
    BucketRuleTest.LOG.info("Starting testRuleWithExistingFile(String)...");
    BucketRuleTest.LOG.info("Creating bucket...");
    new Bucket(BUCKET).create();
    BucketRuleTest.LOG.info("Creating file...");
    Files.createFile(PATH);
    BucketRuleTest.LOG.info("Rule...");
    new BucketRule(BUCKET, KEY).run();
    BucketRuleTest.LOG.info("Waiting for file...");
    this.tv.waitFor(
      () -> Files.exists(PATH),
      TIMEOUT,
      TimeUnit.SECONDS
    );
    BucketRuleTest.LOG.info("Checking file...");
    assert Files.exists(PATH);
  }

  @Test
  @EnabledIfEnvironmentVariable(named = "CI", matches = "true")
  void testRuleWithExistingFileAndExistingBucket() throws IOException {
    BucketRuleTest.LOG.info("Starting testRuleWithExistingFileAndExistingBucket(String)...");
    BucketRuleTest.LOG.info("Creating bucket...");
    new Bucket(BUCKET).create();
    BucketRuleTest.LOG.info("Creating file...");
    Files.createFile(PATH);
    BucketRuleTest.LOG.info("Rule...");
    new BucketRule(BUCKET, KEY).run();
    BucketRuleTest.LOG.info("Waiting for file...");
    this.tv.waitFor(
      () -> Files.exists(PATH),
      TIMEOUT,
      TimeUnit.SECONDS
    );
    BucketRuleTest.LOG.info("Checking file...");
    assert Files.exists(PATH);
  }

}
```