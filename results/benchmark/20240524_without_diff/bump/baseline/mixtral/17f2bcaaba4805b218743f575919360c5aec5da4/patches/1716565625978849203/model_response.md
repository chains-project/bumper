Here is a fixed version of the failing client code:

```java
import org.junit.Assume;

// ...

assumeTrue(someCondition);
```

In this version, we remove the `static` import of `Assume.assumeTrue` and replace its usage with a regular import of `Assume` followed by a call to `Assume.assumeTrue`. This should resolve the error message you were seeing.