Here is the proposed patch:

```java
import org.junit.Assume;
```

And then replace all occurrences of `assumeTrue` with `Assume.assumeTrue` in the client code.