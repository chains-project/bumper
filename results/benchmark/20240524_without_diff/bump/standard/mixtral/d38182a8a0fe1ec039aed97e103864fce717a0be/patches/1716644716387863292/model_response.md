Here is a possible patch for the code you provided:
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
The only change I made was to import the `User` class at the beginning of the method. This class is part of the `com.artipie.http.auth` package, which is already being used in the code, so it should be available for import.

I hope this helps! Let me know if you have any other questions.