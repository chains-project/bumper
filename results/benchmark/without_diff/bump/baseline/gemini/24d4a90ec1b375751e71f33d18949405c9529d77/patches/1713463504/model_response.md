```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.log.Logger;
  import com.jcabi.aspects.Loggable;
  import org.junit.jupiter.api.Test;
  import static org.junit.jupiter.api.Assertions.assertEquals;

  @Loggable(value = Loggable.DEBUG, limit = 1)
  public abstract class AwsOcketITCase {

    @Test
    void test() throws Exception {
      final Tv tv = new Tv(new AwsOcket());
      assertEquals("http://test.s3.amazonaws.com", tv.url());
    }

  }
```