It seems like the code is trying to use the `JoinedText` class from the `org.cactoos.text` package, but the classpath cannot find it. This could be due to a version mismatch or a missing dependency in the project's build configuration.

To fix the issue, you can add the following Maven dependency to the project's `pom.xml` file:
```xml
<dependency>
    <groupId>org.cactoos</groupId>
    <artifactId>cactoos-text</artifactId>
    <version>0.32</version>
</dependency>
```
If adding the dependency doesn't fix the issue, you can modify the failing code to use a different class from the same package, such as `TextJoined`, which has a similar functionality:
```java
import org.cactoos.text.TextJoined;

// ...

public InputStream inputOf(String id) throws IOException {
    TextJoined joined = new TextJoined(",",
        new TextOf(id),
        new TextOf(System.lineSeparator()),
        new TextOf(new JsonOf(new WalletOf(id).value()))
    );
    return new ByteArrayInputStream(joined.asString().getBytes());
}
```
This modification replaces the `JoinedText` class with `TextJoined`, which has the same method signature and functionality. The `TextJoined` class is available in the same package as `JoinedText`, so no further changes are needed.