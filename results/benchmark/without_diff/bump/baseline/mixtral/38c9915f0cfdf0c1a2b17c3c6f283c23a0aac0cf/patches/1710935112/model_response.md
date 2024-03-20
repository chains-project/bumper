I see that the issue is caused by the use of a class from the `org.cactoos.text` package, which is causing a compilation error. To fix this issue, we can replace the usage of the `Joined` class from the `org.cactoos.text` package with a similar class from the Java Standard Library.

Here's a patch that you can apply to the code to fix the error:
```java
-import org.cactoos.text.Joined;