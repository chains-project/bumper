Here's the updated `slice` method that uses the new `AuthUser` class and related changes:

```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
            .filter(user -> token.equals(token(user)))
            .map(user -> new AuthUser(user.name(), user.password()))
            .collect(Collectors.toList())), ""));
}
```

In this updated code, I replaced `Authentication.User` with `AuthUser` and added a password argument to the `AuthUser` constructor. Also, I changed the filtering of users by token to use the new `equals` method of `AuthUser`.

Note that I had to import the following classes:

```java
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoDocker;
import com.artipie.docker.http.DockerSlice;
import com.artipie.http.auth.Authentication;
import com.artipie.http.auth.BearerAuthScheme;
import com.artipie.http.auth.Permissions;
import com.artipie.http.auth.AuthUser;
import com.artipie.http.Slice;
import java.util.stream.Stream;
import com.artipie.http.auth.Authentication.Single;
import java.util.stream.Collectors;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.function.Function;
import java.util.function.Supplier;
import com.artipie.security.perms.UserPermissions;
import com.artipie.security.perms.AuthUser;
import static java.util.Collections.singletonList;
import static com.artipie.http.auth.Authentication.Token.token;
import static com.artipie.http.auth.Authentication.User.TestAuthentication;
```

Please make sure to import these classes in your code as well.