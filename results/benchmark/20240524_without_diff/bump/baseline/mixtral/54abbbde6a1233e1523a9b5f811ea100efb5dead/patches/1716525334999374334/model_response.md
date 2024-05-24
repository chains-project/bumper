Here's the proposed patch for the failing client code:

```java
import com.jcabi.ssh.Ssh;

@Tv({1, 2, 3})
public class SshByPassword {
  // existing code...
}
```

In this patch, I've imported the `Ssh` class directly from the `com.jcabi.ssh` package instead of importing the `Tv` class. I've also added the `@Tv` annotation to the `SshByPassword` class directly, which should resolve the error message.

Note that the `Tv` class has been removed from the library, so it's not possible to use it directly. However, the `@Tv` annotation has been retained, so it's still possible to use it as a part of the class definition.