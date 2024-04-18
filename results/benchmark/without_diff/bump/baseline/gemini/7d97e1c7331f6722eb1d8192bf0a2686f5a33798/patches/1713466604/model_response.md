```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.aspects.TvImpl;

  public class RegionITCase {

    private final Tv tv = new TvImpl();

    @Test
    public void testRegion() throws Exception {
      String region = this.tv.region("1234567890");
      assertEquals("US", region);
    }
  }
```