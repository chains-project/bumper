```java
import com.jcabi.aspects.Tv;
import java.util.List;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

public class RegionITCase {

  @Test
  public void test() throws Exception {
    final Tv tv = Mockito.mock(Tv.class);
    final List<String> names = List.of("first", "second", "third");
    Mockito.when(tv.names()).thenReturn(names);
    // Mockito.verify(tv).names();
  }
}
```