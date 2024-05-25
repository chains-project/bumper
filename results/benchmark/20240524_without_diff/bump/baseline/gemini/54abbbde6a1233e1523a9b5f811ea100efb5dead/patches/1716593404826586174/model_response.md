```java
import com.jcabi.aspects.Tv;

public class Ssh {
    public static Tv connect(String host) {
        return new Tv(host);
    }
}
```