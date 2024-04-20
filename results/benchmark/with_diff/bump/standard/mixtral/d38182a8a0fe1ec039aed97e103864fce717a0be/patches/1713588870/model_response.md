Here's the updated `slice` method that uses the new `AuthUser` class:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Single(new AuthUser(TestAuthentication.ALICE.name(), action), action),
        new BearerAuthScheme(
            token -> CompletableFuture.completedFuture(
                Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter(user -> token.equals(token(user)))
                    .map(user -> new AuthUser(user.name()))
                    .findFirst()
            ),
            ""
        )
    );
}
```
In this updated code, I replaced all occurrences of `Authentication.User` with `AuthUser`. Also, I imported the necessary classes at the beginning of the file:
```java
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoDocker;
import com.artipie.docker.http.DockerSlice;
import com.artipie.http.auth.BearerAuthScheme;
import com.artipie.http.auth.Permissions;
import com.artipie.http.auth.Single;
import com.artipie.http.Slice;
import com.artipie.http.auth.Authentication;
import java.util.stream.Stream;
import com.artipie.http.auth.AuthUser;
import java.util.concurrent.CompletableFuture;
import java.util.function.Function;
import java.util.stream.Collectors;
import static java.util.stream.Collectors.toList;
import static java.util.Collections.singletonList;
import static java.util.Collections.emptyList;
```
The updated code should work with the new version of the library.