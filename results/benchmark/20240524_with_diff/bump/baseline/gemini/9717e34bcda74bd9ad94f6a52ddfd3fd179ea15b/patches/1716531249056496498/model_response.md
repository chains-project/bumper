```java
import com.jcabi.aspects.Tv;
import org.mockito.Mockito;

public class MkGithub {

    private final Tv tv;

    public MkGithub(Tv tv) {
        this.tv = tv;
    }

    public void mock() {
        Mockito.when(tv.isOn()).thenReturn(true);
    }
}
```