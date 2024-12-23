```java
import static com.jcabi.matchers.RegexMatchers.matchesPattern;
import static org.hamcrest.Matchers.equalTo;
import static org.junit.Assert.assertThat;

/**
 * AwsOcket can read and write large S3 content.
 *
 * @throws Exception
 * 		If fails
 */
@org.junit.Test
public void readsAndWritesLargeObjectContent() throws java.lang.Exception {
    final com.jcabi.s3.Bucket bucket = this.rule.bucket();
    final java.lang.String name = "test-44.txt";
    final com.jcabi.s3.Ocket.Text ocket = new com.jcabi.s3.Ocket.Text(bucket.ocket(name));
    final java.lang.String data = org.apache.commons.lang3.RandomStringUtils.random(100 * 1000);
    ocket.write(data);
    try {
        assertThat(ocket.read(), matchesPattern(equalTo(data)));
    } finally {
        bucket.remove(name);
    }
}
```