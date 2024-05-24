Here's a possible patch for the failing client code:

```java
import org.cactoos.Scalar;
import org.cactoos.io.IoCheckedBytes;
import org.cactoos.text.TextOfScalar;

//...

Scalar<String> content = // your scalar here
IoCheckedBytes bytes = new IoCheckedBytes(new TextOfScalar(content));
```

This code creates a `Scalar` object from your content, then converts it to an `IoCheckedBytes` object, which should be compatible with the original code. Note that you need to replace the `// your scalar here` comment with the actual code that creates the `Scalar` object.