```java
import com.jcabi.aspects.Tv;
import com.jcabi.aspects.TvPlus;

public class RegionITCase {

  @Tv
  public void testRegion() throws Exception {
    TvPlus tv = new TvPlus();
    tv.testRegion();
  }
}
```