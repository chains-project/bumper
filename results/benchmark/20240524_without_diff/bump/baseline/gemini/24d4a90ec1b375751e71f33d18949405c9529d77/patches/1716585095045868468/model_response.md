```java
  import com.jcabi.aspects.Tv;
  import org.junit.jupiter.api.Test;

  import static org.junit.jupiter.api.Assertions.assertNotNull;

  public class BucketRule {

    @Test
    public void testBucket() {
      Tv tv = new Tv();
      assertNotNull(tv);
    }
  }
```