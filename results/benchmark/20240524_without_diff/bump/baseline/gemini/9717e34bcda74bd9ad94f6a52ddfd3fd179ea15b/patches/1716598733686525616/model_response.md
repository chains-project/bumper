```java
import com.jcabi.aspects.Tv;

import java.util.concurrent.TimeUnit;

public class MkGithub {

    private final Tv tv;

    public MkGithub(Tv tv) {
        this.tv = tv;
    }

    public void init() throws Exception {
        tv.play(TimeUnit.SECONDS.toMillis(1));
    }

    public void close() throws Exception {
        tv.stop();
    }
}
```