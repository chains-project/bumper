```java
  import com.jcabi.aspects.Tv;
  import java.lang.reflect.Field;

  public class RegionITCase {
    @Tv
    public void testCreate() {
      try {
        Field field = RegionITCase.class.getDeclaredField("region");
        field.setAccessible(true);
        field.set(this, new Region());
      } catch (Exception e) {
        throw new RuntimeException(e);
      }
    }
  }
```