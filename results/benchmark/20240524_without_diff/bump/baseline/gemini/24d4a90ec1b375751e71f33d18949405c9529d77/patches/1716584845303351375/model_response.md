```java
  import com.jcabi.aspects.Tv;
  import org.junit.jupiter.api.Test;

  public class BucketRule {

    @Test
    public void test() {
      Tv tv = new Tv();
      tv.play("Breaking Bad");
    }
  }
```