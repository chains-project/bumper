```java
import com.jcabi.aoc.annotations.Loggable;
import com.jcabi.log.Logger;

Logger logger = Logger.getLogger(this.getClass());

@Loggable(Loggable.DEBUG)
public void method() {
    logger.debug("Using Logger instead of Tv");
}
```