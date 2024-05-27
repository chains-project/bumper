Here's a potential patch for the given client code:

```java
import com.artipie.http.auth.Authentication.User;

@Override
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
                java.util.stream.Stream.of(
                    TestAuthentication.ALICE,
                    TestAuthentication.BOB
                ).filter(
                    (user) -> token.equals(token(user))
                ).map(
                    (user) -> new User(user.name())
                ).findFirst()
            ),
            ""
        )
    );
}
```

The change made here is simply importing the `User` class from the `com.artipie.http.auth.Authentication` interface at the beginning of the file. This should resolve the "cannot find symbol" error.