```java
import com.jcabi.aspects.Tv;

public class MkGithub {

    // ...

    private Tv tv() {
        return new Tv() {
            @Override
            public void show() {
                // ...
            }
        };
    }

    // ...
}
```