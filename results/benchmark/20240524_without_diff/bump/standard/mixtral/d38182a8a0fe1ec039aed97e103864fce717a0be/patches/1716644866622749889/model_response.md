Here's a possible patch for the given client code:

```java
import com.artipie.http.auth.Authentication.User;
import java.util.stream.Stream;
import static java.util.stream.Stream.of;
import static java.util.stream.Collectors.toList;

@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    return new com.artipie.docker.http.DockerSlice(
        new com.artipie.docker.asto.AstoDocker(
            new com.artipie.asto.memory.InMemoryStorage()
        ),
        new com.artipie.http.auth.Permissions.Single(
            TestAuthentication.ALICE.name(),
            action
        ),
        new com.artipie.http.auth.BearerAuthScheme(
            (token) -> java.util.concurrent.CompletableFuture.completedFuture(
                of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter((user) -> token.equals(token(user)))
                    .map((user) -> new User(user.name()))
                    .collect(toList())
            ),
            ""
        )
    );
}
```

The patch imports the missing `User` class from the `com.artipie.http.auth` package, and uses it to create a list of `User` objects instead of a `Stream` of `User` objects. This should fix the compilation error.