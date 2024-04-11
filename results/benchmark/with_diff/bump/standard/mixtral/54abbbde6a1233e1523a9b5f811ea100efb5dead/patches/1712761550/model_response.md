Here is a proposed patch for the failing method:

```java
import static java.time.Duration.ofMinutes;
import static java.time.temporal.ChronoUnit.MINUTES;

// ...

@Override
@com.jcabi.aspects.RetryOnFailure(attempts = 7, delay = ofMinutes(1), unit = MINUTES, verbose = false, types = java.io.IOException.class)
protected com.jcraft.jsch.Session session() throws java.io.IOException {
    // ...
}
```

This patch replaces the usage of the removed `Tv` class with the new `java.time` classes to specify the retry attempts and delay, which should resolve the "cannot find symbol" error.