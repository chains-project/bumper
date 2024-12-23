```java
import com.jcabi.aspects.Tv;

public class AwsOcketITCase {

    private static final String BUCKET = "test-bucket";
    private static final String KEY = "test-key";
    private static final String VALUE = "test-value";

    @Test
    public void testPutGet() throws Exception {
        // Create a TV object
        Tv tv = new Tv();

        // Create an S3 bucket
        tv.bucket(BUCKET).create();

        // Put a key-value pair
        tv.bucket(BUCKET).put(KEY, VALUE);

        // Get the value of the key
        String value = tv.bucket(BUCKET).get(KEY);

        // Assert that the value is correct
        assertEquals(VALUE, value);

        // Delete the key-value pair
        tv.bucket(BUCKET).delete(KEY);

        // Delete the S3 bucket
        tv.bucket(BUCKET).delete();
    }
}
```