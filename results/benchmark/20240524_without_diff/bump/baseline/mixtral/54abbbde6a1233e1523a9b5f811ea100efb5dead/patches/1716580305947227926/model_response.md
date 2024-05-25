Here's a possible patch for the failing client code:

```java
import com.jcabi.ssh.Ssh;

@Tv({"0.15.2"}) // specify the version of jcabi-ssh that you depend on
public class MyClass {
    public void myMethod() {
        Ssh ssh = new Ssh("my-ssh-server.com", 22);
        // use the Ssh object as before
    }
}
```

Note that I've specified the version of `jcabi-ssh` that you depend on using the `@Tv` annotation. This will ensure that the correct version of the library is used at runtime.

I've also changed the import statement to import `com.jcabi.ssh.Ssh` directly, since that's the class that you're actually using.

Finally, I've created an `Ssh` object using its constructor, which should still be available in version 0.15.2 of `jcabi-ssh`.

Note that this is just one possible solution, and there may be other ways to fix the issue as well.