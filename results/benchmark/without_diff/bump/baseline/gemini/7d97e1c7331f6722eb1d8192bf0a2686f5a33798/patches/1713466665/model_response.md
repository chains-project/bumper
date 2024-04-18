```java
  import com.jcabi.aspects.Tv;

  import java.util.List;

  public class RegionITCase {

      private final Tv tv = new Tv();

      public void testRegions() {
          final List<String> regions = tv.regions();
          regions.forEach(System.out::println);
      }
  }
```