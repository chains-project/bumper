Here is a possible patch for the failing client code:
```java
import com.artipie.http.auth.Authentication.User;

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
                java.util.stream.Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter((user) -> token.equals(token(user)))
                    .map((user) -> new User(user.name()))
                    .findFirst()
            ),
            ""
        )
    );
}
```
The change I made is to import the `User` class from `com.artipie.http.auth.Authentication` at the beginning of the method. This is because the `User` class is not in the default package, so it needs to be imported in order to be used. I also added a blank line at the end of the method for readability.