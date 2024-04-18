```java
import com.jcabi.aspects.Tv;
import org.mockito.Mockito;

public class MkGithub {

    private final Tv tv;

    public MkGithub() {
        this.tv = Mockito.mock(Tv.class);
    }

    public MkGithub(Tv tv) {
        this.tv = tv;
    }

    public Tv tv() {
        return tv;
    }
}
```